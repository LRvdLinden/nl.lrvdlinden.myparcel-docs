#!/usr/bin/env python3
"""Check relative links in md/html files and SUMMARY entries. usage: check_links.py <docs_dir>"""
import os, re, sys, glob
from urllib.parse import unquote

ROOT = sys.argv[1]
errors, checked = [], 0


def slug(h):
    h = re.sub(r'[*_`]', '', h.strip().lower())
    h = re.sub(r'[^\w\- ]', '', h)
    return re.sub(r'\s+', '-', h).strip('-')


def anchors(path):
    if not path.endswith('.md'):
        return None
    return {slug(m.group(1)) for m in re.finditer(r'^#+\s+(.*)$', open(path, encoding='utf-8').read(), re.M)}


files = [f for f in glob.glob(os.path.join(ROOT, '**/*'), recursive=True)
         if f.endswith(('.md', '.html')) and '/.git/' not in f]
for f in files:
    text = open(f, encoding='utf-8').read()
    targets = re.findall(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)', text)
    targets += re.findall(r'(?:href|src)="([^"]+)"', text)
    if f.endswith('index.html'):
        # dynamic links built in JS
        ids = set(re.findall(r'"id":"([a-z0-9-]+)"', text))
        targets += [f'../media/drivers/{i}/assets/images/large.png' for i in ids]
        targets += [f'../en/carriers/{i}.md' for i in ids]
    for t in targets:
        if re.match(r'^(https?:|mailto:|data:|#$)', t) or '{' in t or "'" in t:
            continue
        checked += 1
        path, _, frag = t.partition('#')
        dest = os.path.normpath(os.path.join(os.path.dirname(f), unquote(path))) if path else f
        if not os.path.exists(dest):
            errors.append(f'{os.path.relpath(f, ROOT)}: missing {t}')
        elif frag:
            a = anchors(dest)
            if a is not None and frag not in a:
                errors.append(f'{os.path.relpath(f, ROOT)}: missing anchor {t}')

for lang in ('nl', 'en'):
    s = open(os.path.join(ROOT, lang, 'SUMMARY.md'), encoding='utf-8').read()
    for t in re.findall(r'\]\(([^)]+)\)', s):
        checked += 1
        if not os.path.exists(os.path.join(ROOT, lang, t)):
            errors.append(f'{lang}/SUMMARY.md: missing {t}')
    listed = set(re.findall(r'\]\(([^)]+)\)', s))
    for p in sorted(glob.glob(os.path.join(ROOT, lang, 'carriers', '*.md'))):
        rel = os.path.relpath(p, os.path.join(ROOT, lang))
        if rel not in listed:
            errors.append(f'{lang}: carrier page not in SUMMARY: {rel}')

print(f'files={len(files)} links_checked={checked} errors={len(errors)}')
for e in errors:
    print(' ', e)
sys.exit(1 if errors else 0)
