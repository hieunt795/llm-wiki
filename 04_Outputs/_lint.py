import os, re
from pathlib import Path

wiki_root = Path(r'e:\Wiki Link\03_Wiki')
all_nodes = {}
all_wikilinks_out = {}
all_wikilinks_in = {}

for md in wiki_root.rglob('*.md'):
    if md.name == '.gitkeep': continue
    content = md.read_text(encoding='utf-8')
    name = md.stem
    folder = md.parent.name
    
    fm_type = ''
    fm_match = re.search(r'type:\s*(\w+)', content)
    if fm_match: fm_type = fm_match.group(1)
    
    all_nodes[name] = {'folder': folder, 'type': fm_type}
    links = [l for l in re.findall(r'\[\[([^\]#|]+)', content) if not l.endswith('.pdf')]
    all_wikilinks_out[name] = set(links)
    for l in links:
        all_wikilinks_in.setdefault(l, set()).add(name)

type_to_folder = {
    'definition':'concepts', 'mechanism':'mechanisms',
    'relationship':'relationships', 'evidence':'evidence',
    'perspective':'perspectives'
}

orphans, broken, wrong_type = [], [], []

for name in all_nodes:
    out_wiki = all_wikilinks_out.get(name, set()) & set(all_nodes.keys())
    inc_wiki = all_wikilinks_in.get(name, set()) & set(all_nodes.keys())
    if not out_wiki and not inc_wiki:
        orphans.append(name)

for name, links in all_wikilinks_out.items():
    for l in links:
        if l not in all_nodes:
            broken.append(f'{name} -> [[{l}]]')

for name, info in all_nodes.items():
    expected = type_to_folder.get(info['type'], '')
    actual = info['folder']
    if expected and actual != expected:
        wrong_type.append(f'{name}: type={info["type"]} in {actual}/ (expected {expected}/)')

print(f'Total nodes: {len(all_nodes)}')
print(f'\nOrphans ({len(orphans)}):')
for o in orphans: print(f'  - {o}')
print(f'\nBroken links ({len(broken)}):')
for b in broken: print(f'  - {b}')
print(f'\nWrong type ({len(wrong_type)}):')
for w in wrong_type: print(f'  - {w}')
