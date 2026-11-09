from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
required=['liushui-ip','liushui-persona','liushui-content-loop']
for name in required:
    p=root/'skills'/name/'SKILL.md'
    assert p.exists(), f'missing {p}'
    text=p.read_text(encoding='utf-8')
    assert text.startswith('---\n'),f'bad YAML {p}'
    assert f'name: {name}' in text.split('---',2)[1],f'wrong name in {p}'
    assert 'description:' in text.split('---',2)[1],f'no description {p}'
    for ref in re.findall(r'\]\((references/[^)]+)\)',text):
        assert (p.parent/ref).is_file(),f'bad link: {name}: {ref}'
    assert (p.parent/'references').is_dir()
for md in root.rglob('*.md'):
    text=md.read_text(encoding='utf-8')
    for link in re.findall(r'\]\(([^)#]+)(?:#[^)]+)?\)',text):
        if '://' not in link and not link.startswith('mailto:'):
            assert (md.parent/link).is_file(),f'bad markdown link: {md}: {link}'
print('PASS: metadata, local markdown links, paths, references, self-contained directories')
print('Total package files:',sum(p.is_file() for p in root.rglob('*') if '.git' not in p.parts))
