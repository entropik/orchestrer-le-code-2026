"""Transpositions graphiques contrôlées des 17 schémas ASCII du corpus.

Les sélections sont figées sur les blocs identifiés par leur empreinte.
Les libellés proviennent du texte original, jamais d'une réécriture.
"""
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDS = ['harnais', 'profondeur', 'hexagonal', 'validation', 'worktrees', 'stacked-pr',
       'pyramide', 'asynchrone', 'outbox', 'expand-contract', 'livraison', 'kiss',
       'observabilite', 'circuit-breaker', 'dlq', 'reprise', 'routage']
HASHES = [
    '9c34761a873c95fe19ae2bb85b94e51c2c907974577f963e9afc0b5b53600c0b',
    '69e51917fb91e4abe8a8d0f82ccc9fb47747decdccae0876ad1598fda25f221d',
    '15255bfae710363a1c023b9caa221355b98386f07ee31163121c9a15089b2582',
    '0d10109827f984274c22928ab174e7cb1c3876d0c44e825849c8107e1ba5c25f',
    '66d4e66b7ce695c364882075fa4e448343e8514c13d780b2710f5dab08bd7f97',
    'f2ac29aa99e4e1ad322220bcacae33ac1a988a91714b20e009acc7aa6ff883ed',
    '682980f9958acc7cdf5cb438afc7e1c5da6527dbcab26a9f4dcd0a8b8c64f397',
    '3bb6837916c9f18d57103ba558e18d5c49e26b550d3961daf101963da3f8ce71',
    'b89b6ce97d8ad68e3c31aa91c98e3d33ff2542f133538356d7329b426cdc6b8e',
    '02ca5eacd31f36d9a7ba8c48272f02613a0af78be45451288c47cce8c8dc6f5d',
    '0ab2e6eaf3d357c44fcf0f11a5ac249a92b43ee96e0db5af7088064540acda69',
    'bb214ee97f133517f3c0aa9433548ee3681cd233934d324429ca7da9a9007fe8',
    'a5298b082325a1a45fdc4cda00ab9f78aca6f74b89872daa70bd05bf832e5ff5',
    '2890f98a7f21904747d4c8d28fcc8b2b91e21eef7dc36ef9d4134a5a2895221d',
    '9b24c108ce18bf3b5671286744e180ddaeeb61127e28bb14a599cf76ba7e5563',
    '647d2f5aa0ef2ce8873f8d929f82c33ea1b7dbac79750e17ae5b05e886bdc394',
    'f8ac5930ea4d81f526088c867b7de9187593060fc9f94f61281b3f9ae3255882'
]


def clean(line):
    line = line.strip().strip('|│').strip()
    line = re.sub(r'^[├└]──\s*', '', line).strip()
    return line.removeprefix('• ').strip()


def bracket(line):
    return re.search(r'\[\s*(.*?)\s*\]', line)[1]


def node(title, lines=(), **extra):
    return dict(kind='node', title=title, lines=list(lines), **extra)


def arrow(label='', direction='down'):
    return dict(kind='arrow', label=label, direction=direction)


def grid(items, **extra):
    return dict(kind='grid', items=items, **extra)


def sequence(nodes):
    result = []
    for n in nodes:
        if result:
            result.append(arrow())
        result.append(n)
    return result


def boxes(lines):
    result, current = [], None
    for line in lines:
        if line.lstrip().startswith('┌'):
            current = []
        elif line.lstrip().startswith('└') and current:
            result.append(node(current[0], current[1:]))
            current = None
        elif current is not None and line.lstrip().startswith('│'):
            value = clean(line)
            if value:
                current.append(value)
    return result


def phases(lines, pattern):
    result = []
    for line in lines:
        if re.match(pattern, line):
            result.append(node(clean(line).strip('[] ')))
        elif result and re.search(r'\w', line):
            result[-1]['lines'].append(clean(line))
    return result


def texts(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in ('title', 'label', 'badge'):
                yield item
            elif key == 'lines':
                yield from item
            elif key in ('parts', 'items', 'transitions'):
                yield from texts(item)
    elif isinstance(value, list):
        for item in value:
            yield from texts(item)


def build():
    original = (ROOT / 'sources/originaux/MANUEL_INGENIERIE_LOGICIELLE_2026_COMPLET.md').read_text(encoding='utf-8-sig')
    blocks = [m[2] for m in re.finditer(r'^```([^\n]*)\n(.*?)^```\s*$', original, re.M | re.S) if m[1] == 'text']
    if len(blocks) != 17:
        raise ValueError('Le corpus de schémas a changé : revoir les sélections.')
    registry = {}
    for i, body in enumerate(blocks):
        digest = hashlib.sha256(body.encode()).hexdigest()
        if digest != HASHES[i]:
            raise ValueError(f'Bloc {IDS[i]} modifié : {digest}')
        ls = body.splitlines()
        d = dict(id=IDS[i], title=ls[0].strip(), source_sha256=digest)
        parts = []
        if i == 0:
            d.update(kind='harnais', title='ANATOMIE DU HARNAIS AGENTIQUE')
            registry[digest] = d
            continue
        elif i == 1:
            titles = re.split(r' {2,}', ls[2].strip())
            columns = [[clean(line[a:b]) for line in ls[4:] if '|' in line[a:b]] for a,b in [(0,48),(48,None)]]
            columns = [[l for l in col if l] for col in columns]
            left, right = columns
            parts = [grid([
                dict(kind='module',title=titles[0],parts=[node(left[0],[left[1]]),node(left[2],left[3:])]),
                dict(kind='module',title=titles[1],parts=[node(right[0],[' '.join(right[1:3])]),node(right[3],[' '.join(right[4:])])])
            ], style='comparison')]
        elif i == 2:
            parts = [grid([node(t.strip()) for t in re.findall(r'\[([^]]+)\]', ls[2])]), arrow()] + sequence(boxes(ls))
        elif i == 3:
            parts = sequence([node(bracket(ls[2])), node(bracket(ls[5]))])
            outcomes = re.findall(r'\[\s*(.*?)\s*\]', ls[9])
            parts += [arrow(), grid([
                dict(kind='branch', parts=sequence([node(outcomes[0]), node('Rejet 400 Immédiat', ['(Zéro propagation)'])])),
                dict(kind='branch', parts=sequence([node(outcomes[1]), node('Type Statique Garanti Invariant'), node('Domaine Métier Pur')]))
            ])]
        elif i == 4:
            columns = [re.split(r' {2,}', line.strip()) for line in ls[7:12]]
            parts = [node(ls[2].strip(), [bracket(ls[3])]), arrow(), grid([
                node(columns[0][j], [l[j].strip('[]') for l in columns[1:]]) for j in range(3)
            ])]
        elif i == 5:
            parts = [node(bracket(ls[2]), [ls[2].split(']')[1].strip()])]
            for k in [5,8,11,14]:
                parts += [arrow(ls[k-1].strip().strip('│ '), 'up'), node(bracket(ls[k]), [ls[k].split('──>')[1].strip()])]
        elif i == 6:
            levels = []
            for k,badge in [(2,'E2E'),(5,'INTEG'),(8,'UNITAIRES'),(11,'ANALYSE STATIQUE')]:
                levels.append(node(ls[k].split('<--')[1].strip(), ['Couverture' + ls[k+1].split('Couverture')[1], ls[k+2].split('\\')[-1].strip()], badge=badge))
            parts = [dict(kind='pyramid', items=levels)]
        elif i == 7:
            api = node(bracket(ls[7]), [clean(l[:61]) for l in ls[8:11]])
            reply = node(re.findall(r'\[\s*(.*?)\s*\]',ls[7])[1], [ls[8][61:].strip(), ' '.join(l[61:].strip() for l in ls[9:11])])
            api_flow = sequence([api,node(bracket(ls[13]),[clean(l) for l in ls[14:16]]),node(bracket(ls[18]),[clean(l) for l in ls[19:]])])
            api_flow[3]['label'] = ls[17].strip().removeprefix('▼ ').strip()
            parts = [node(bracket(ls[2])),arrow(clean(ls[4]).split('─')[0].strip()),grid([dict(kind='branch',parts=api_flow),reply], style='async')]
        elif i == 8:
            parts = boxes(ls)
            parts[0]['lines'] = [parts[0]['lines'][0], ' '.join(parts[0]['lines'][1:])]
            parts.insert(1, arrow(next(l.strip() for l in ls if 'COMMIT LOCAL' in l)))
            parts[0]['style'] = 'sql'
        elif i in (9,15):
            parts = sequence(phases(ls[1:], r'^\s*PHASE \d'))
        elif i == 10:
            parts = sequence(phases(ls[1:], r'^\s*\[ '))
        elif i == 11:
            parts = sequence(boxes(ls))
        elif i == 12:
            cells = [[v.strip() for v in line.split('│')[1::2]] for line in [ls[3],ls[4],*ls[6:10]]]
            parts = [grid([node(cells[0][j],[cells[1][j], ' '.join(row[j] for row in cells[2:])]) for j in range(3)],style='pillars')]
        elif i == 13:
            states = [node('FERMÉ',['(Nominal)'],key='closed'),node('OUVERT',['(Protection)'],key='open'),node('SEMI-OUVERT',['(Sondage)'],key='half')]
            parts = [dict(kind='states',items=states,transitions=[
                dict(source='closed',target='open',label="Taux d'échec > 50%"),
                dict(source='open',target='half',label='(Délai de cooldown expiré)'),
                dict(source='open',target='closed',label='(Succès du test)'),
                dict(source='half',target='closed',label='(Échec du test)')])]
            d['note'] = "Les retours des tests suivent le tracé ASCII fourni, dont les flèches sont ambiguës ; cette transposition ne corrige pas le modèle technique."
        elif i == 14:
            parts = [node(bracket(ls[2])),arrow()]
            attempts = []
            for line in ls[4:7]:
                left,right = re.split(r'─+>', clean(line),maxsplit=1)
                attempts.append(node(left.strip(),[bracket(right)]))
            parts += sequence(attempts) + [arrow(),node(bracket(ls[9]),[clean(l) for l in ls[10:]])]
        elif i == 16:
            headers = re.findall(r'\[\s*(.*?)\s*\]',ls[12])
            row1 = [s.removeprefix('• ').strip() for s in re.split(r' {2,}',ls[13].strip())]
            # La dernière ligne colle deux colonnes : leurs puces sont la frontière.
            row2 = [s.strip() for s in ls[14].split('•')[1:]]
            parts = [node(bracket(ls[2]),[ls[3].strip()]),arrow(ls[5].strip().removeprefix('▼ ')),node(clean(ls[7])),arrow(),grid([node(headers[j],[row1[j],row2[j]]) for j in range(3)])]
        d['parts'] = parts
        before, after = Counter(re.findall(r'\w+',body)), Counter(re.findall(r'\w+',' '.join(texts(d))))
        if before != after:
            raise ValueError(f'{IDS[i]} : manque {before-after} ; ajout {after-before}')
        registry[digest] = d
    return registry


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.dumps(build(), ensure_ascii=False, indent=2) + '\n'
    dest = ROOT / 'data/diagrams/registry.json'
    if args.check:
        if not dest.exists() or dest.read_text(encoding='utf-8') != data:
            raise SystemExit('Registre des schémas non synchronisé.')
    else:
        with open(dest, 'w', encoding='utf-8', newline='\n') as f:
            f.write(data)
    print('OK : 17 schémas, libellés intégraux et empreintes vérifiés.')


if __name__ == '__main__':
    main()
