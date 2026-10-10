#!/usr/bin/env python3
"""Generate MyParcel GitBook carrier/flow/token/device pages from the app manifest.

usage: python3 tools/gen_docs.py <app_dir> <docs_dir>
"""
import json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrier_meta import ORDER, M, NEW_IN_036

APP, DOCS = sys.argv[1], sys.argv[2]
A = json.load(open(os.path.join(APP, 'app.json'), encoding='utf-8'))
VERSION = A['version']
CAPS = A['capabilities']
DRIVERS = {d['id']: d for d in A['drivers']}
assert set(DRIVERS) == set(ORDER), set(DRIVERS) ^ set(ORDER)

STORE = 'https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/'
COMMUNITY = 'https://community.homey.app/t/app-pro-myparcel/159800'

L = {
    'nl': dict(glance='In één oogopslag', countries='Landen', connectwith='Koppelen met', driver='Apparaat-ID',
               cards='Flow-kaarten', connect='Koppelen', settings='Instellingen', caps='Apparaatwaarden (capabilities)',
               flows='Flow-kaarten', when='Wanneer… (triggers)', andc='En… (condities)', then='Dan… (acties)',
               tokens='Belangrijke tokens', limits='Beperkingen en tips', group='Groep', setting='Instelling',
               expl='Uitleg', id='ID', type='Type', token='Token', nl='Nederlands', en='English', args='Argumenten',
               all_devices='geldt voor alle MyParcel-apparaten', default='standaard', choices='keuzes',
               hidden='wordt verborgen opgeslagen', back='← Alle vervoerders', none='—',
               tokens_intro='Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).',
               show_tokens='Toon alle {n} tokens', new='Nieuw in v{v}', exp='Experimenteel',
               caps_intro='Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.',
               counts='{t} triggers · {c} condities · {a} acties', dev='Apparaatgegevens', flowsp='Flow-kaarten', tokp='Flow-tokens'),
    'en': dict(glance='At a glance', countries='Countries', connectwith='Connect with', driver='Device ID',
               cards='Flow cards', connect='Connect', settings='Settings', caps='Device values (capabilities)',
               flows='Flow cards', when='When… (triggers)', andc='And… (conditions)', then='Then… (actions)',
               tokens='Notable tokens', limits='Limitations and tips', group='Group', setting='Setting',
               expl='Explanation', id='ID', type='Type', token='Token', nl='Nederlands', en='English', args='Arguments',
               all_devices='applies to all MyParcel devices', default='default', choices='choices',
               hidden='stored hidden', back='← All carriers', none='—',
               tokens_intro='Tokens passed by this carrier\'s When cards (not every card has every token).',
               show_tokens='Show all {n} tokens', new='New in v{v}', exp='Experimental',
               caps_intro='Every value appears on the device in Homey. Not every field is filled for every parcel.',
               counts='{t} triggers · {c} conditions · {a} actions', dev='Device data', flowsp='Flow cards', tokp='Flow tokens'),
}
METHOD = {'nl': {'Account': 'Account', 'Tracking': 'Trackingnummer', 'API': 'API-sleutel'},
          'en': {'Account': 'Account', 'Tracking': 'Tracking number', 'API': 'API key'}}
TYPE = {'nl': {'string': 'tekst', 'number': 'getal', 'boolean': 'ja/nee', 'image': 'afbeelding', 'enum': 'keuze'},
        'en': {'string': 'text', 'number': 'number', 'boolean': 'yes/no', 'image': 'image', 'enum': 'choice'}}


def tx(obj, lang):
    if obj is None:
        return ''
    if isinstance(obj, str):
        return obj
    return obj.get(lang) or obj.get('en') or ''


def ftitle(s):
    """Render Homey's !{{positive|negative}} syntax readably and make it table-safe."""
    s = re.sub(r'!\{\{([^|}]*)\|([^}]*)\}\}', lambda m: f'{m.group(1)}/{m.group(2)}'.strip('/'), s)
    return cell(s)


def cell(s):
    return str(s).replace('|', '\\|').replace('\n', ' ').strip()


def card_driver(c):
    for a in c.get('args', []):
        if a.get('type') == 'device':
            f = a.get('filter')
            return f.replace('driver_id=', '') if f else '*'
    return None


FLOW = {k: A['flow'].get(k, []) for k in ('triggers', 'conditions', 'actions')}


def cards_for(did, kind, include_global=True):
    out = [c for c in FLOW[kind] if card_driver(c) == did]
    if include_global:
        out += [c for c in FLOW[kind] if card_driver(c) == '*']
    return out


def token_union(did):
    seen = {}
    for c in cards_for(did, 'triggers', include_global=False):
        for t in c.get('tokens', []):
            seen.setdefault(t['name'], t)
    return list(seen.values())


def args_text(c, lang):
    parts = []
    for a in c.get('args', []):
        if a.get('type') == 'device':
            continue
        name = tx(a.get('title') or a.get('placeholder') or {'en': a['name']}, lang)
        if a.get('type') == 'dropdown':
            vals = ', '.join(tx(v.get('label'), lang) for v in a.get('values', []))
            parts.append(f'{name} ({vals})')
        else:
            parts.append(name)
    return cell('; '.join(parts)) or L[lang]['none']


def settings_rows(did, lang):
    rows = []

    def walk(s, group):
        if s.get('type') == 'group':
            for ch in s.get('children', []):
                walk(ch, tx(s.get('label'), lang))
            return
        label = tx(s.get('label'), lang)
        hint = tx(s.get('hint'), lang)
        extra = []
        if s.get('type') == 'dropdown':
            extra.append(f"{L[lang]['choices']}: " + ', '.join(tx(v.get('label'), lang) for v in s.get('values', [])))
        if s.get('type') == 'number' and s.get('value') is not None:
            extra.append(f"{L[lang]['default']}: {s['value']}")
        if s.get('type') == 'password':
            extra.append(L[lang]['hidden'])
        text = ' '.join(x for x in [hint] + [f'({e})' for e in extra] if x)
        rows.append((group or L[lang]['none'], label, text or L[lang]['none'], s.get('id')))

    for s in DRIVERS[did].get('settings', []):
        walk(s, '')
    return rows


def name(did, lang):
    return M[did]['name'][lang]


def img(did, depth):
    return '../' * depth + f'media/drivers/{did}/assets/images/large.png'


def carrier_page(did, lang):
    T, m, d = L[lang], M[did], DRIVERS[did]
    o = []
    o.append(f'# {name(did, lang)}\n')
    o.append(f'![{name(did, lang)}]({img(did, 2)})\n')
    badges = []
    if did in NEW_IN_036:
        badges.append(T['new'].format(v='0.3.6'))
    if m.get('experimental'):
        badges.append(T['exp'])
    if badges:
        o.append('> ' + ' · '.join(f'**{b}**' for b in badges) + '\n')
    o.append(m['intro'][lang] + '\n')
    trig, cond, act = (cards_for(did, k) for k in ('triggers', 'conditions', 'actions'))
    o.append(f"## {T['glance']}\n")
    o.append(f"| | |\n|---|---|")
    o.append(f"| {T['countries']} | {m['flags']} {m['countries'][lang]} |")
    o.append(f"| {T['connectwith']} | {' · '.join(METHOD[lang][x] for x in m['methods'])} |")
    o.append(f"| {T['driver']} | `{did}` |")
    cnt = T['counts'].format(t=len(trig), c=len(cond), a=len(act))
    if len(act) == 1:
        cnt = cnt.replace('1 acties', '1 actie').replace('1 actions', '1 action')
    if len(cond) == 1:
        cnt = cnt.replace('1 condities', '1 conditie').replace('1 conditions', '1 condition')
    o.append(f"| {T['cards']} | {cnt} |\n")
    o.append(f"## {T['connect']}\n")
    for i, step in enumerate(m['connect'][lang], 1):
        o.append(f'{i}. {step}')
    o.append('')
    rows = settings_rows(did, lang)
    if rows:
        o.append(f"## {T['settings']}\n")
        o.append(f"| {T['group']} | {T['setting']} | {T['expl']} |\n|---|---|---|")
        for g, lab, text, sid in rows:
            o.append(f'| {cell(g)} | **{cell(lab)}** | {cell(text)} |')
        o.append('')
    o.append(f"## {T['caps']}\n")
    o.append(T['caps_intro'] + '\n')
    o.append(f"| {T['id']} | {T['type']} | {T['nl']} | {T['en']} |\n|---|---|---|---|")
    for cap in d['capabilities']:
        c = CAPS.get(cap, {})
        o.append(f"| `{cap}` | {TYPE[lang].get(c.get('type'), c.get('type', ''))} | {cell(tx(c.get('title'), 'nl'))} | {cell(tx(c.get('title'), 'en'))} |")
    o.append('')
    o.append(f"## {T['flows']}\n")
    for head, cards, show_args in ((T['when'], trig, False), (T['andc'], cond, True), (T['then'], act, True)):
        o.append(f'### {head}\n')
        if show_args:
            o.append(f"| {T['id']} | {T['nl']} | {T['en']} | {T['args']} |\n|---|---|---|---|")
        else:
            o.append(f"| {T['id']} | {T['nl']} | {T['en']} |\n|---|---|---|")
        for c in cards:
            note = f" *({T['all_devices']})*" if card_driver(c) == '*' else ''
            row = f"| `{c['id']}` | {ftitle(tx(c['title'], 'nl'))}{note if lang == 'nl' else ''} | {ftitle(tx(c['title'], 'en'))}{note if lang == 'en' else ''} |"
            if show_args:
                row += f" {args_text(c, lang)} |"
            o.append(row)
        o.append('')
    toks = token_union(did)
    if toks:
        o.append(f"## {T['tokens']}\n")
        o.append(T['tokens_intro'] + '\n')
        o.append(f"<details>\n<summary>{T['show_tokens'].format(n=len(toks))}</summary>\n")
        o.append(f"| {T['token']} | {T['type']} | {T['nl']} | {T['en']} |\n|---|---|---|---|")
        for t in toks:
            o.append(f"| `{t['name']}` | {TYPE[lang].get(t.get('type'), t.get('type'))} | {cell(tx(t.get('title'), 'nl'))} | {cell(tx(t.get('title'), 'en'))} |")
        o.append('\n</details>\n')
    o.append(f"## {T['limits']}\n")
    for x in m['limits'][lang]:
        o.append(f'* {x}')
    o.append('')
    links = {'nl': ('Flow-kaarten', 'Flow-tokens', 'Problemen oplossen'), 'en': ('Flow cards', 'Flow tokens', 'Troubleshooting')}[lang]
    o.append(f"[{T['back']}](README.md) · [{links[0]}](../flows.md) · [{links[1]}](../tokens.md) · [{links[2]}](../troubleshooting.md) · [Homey App Store]({STORE}) · [Homey Community]({COMMUNITY})\n")
    return '\n'.join(o)


# ---------- flows.md ----------
def flows_page(lang):
    T = L[lang]
    o = []
    if lang == 'nl':
        o.append('# Flow-kaarten\n')
        o.append(f'Overzicht van alle Flow-kaarten in MyParcel v{VERSION}, per vervoerder. Elke kaart hoort bij het apparaat van die vervoerder; je kiest het apparaat in de kaart. In totaal: **{len(FLOW["triggers"])} triggers, {len(FLOW["conditions"])} condities en {len(FLOW["actions"])} acties**.\n')
        o.append('* **Wanneer**-kaarten gaan één keer per wijziging af, ook na een herstart van de app (bestaande pakketten worden bij de eerste synchronisatie na een update stil vastgelegd).')
        o.append('* Condities met *is/is niet* kun je in Homey omkeren.')
        o.append('* Acties **Volg pakket…**, **Stop met volgen…** en **Verwijder bezorgde pakketten** beheren de lijst met trackingnummers zonder de apparaatinstellingen te openen.')
        o.append('* De volledige NL/EN-titels, argumenten en tokens per kaart staan op de pagina van elke [vervoerder](carriers/README.md); de tokens op [Flow-tokens](tokens.md).\n')
        o.append('## Alle vervoerders\n')
        o.append('* **Verbindingsstatus is gewijzigd** (`connection_status_changed`) – voor elk MyParcel-apparaat, met tokens *Verbonden*, *Verbindingsstatus* en *Vervoerder*.\n')
    else:
        o.append('# Flow cards\n')
        o.append(f'Overview of all Flow cards in MyParcel v{VERSION}, per carrier. Every card belongs to that carrier\'s device; you pick the device in the card. In total: **{len(FLOW["triggers"])} triggers, {len(FLOW["conditions"])} conditions and {len(FLOW["actions"])} actions**.\n')
        o.append('* **When** cards fire once per change, also after an app restart (existing parcels are recorded silently on the first sync after an update).')
        o.append('* Conditions with *is/is not* can be inverted in Homey.')
        o.append('* The actions **Track parcel…**, **Stop tracking parcel…** and **Remove delivered parcels** manage the tracking-number list without opening the device settings.')
        o.append('* The full NL/EN titles, arguments and tokens per card are on each [carrier](carriers/README.md) page; the tokens on [Flow tokens](tokens.md).\n')
        o.append('## All carriers\n')
        o.append('* **Connection status changed** (`connection_status_changed`) – for every MyParcel device, with tokens *Connected*, *Connection status* and *Carrier*.\n')
    for did in ORDER:
        o.append(f'## {name(did, lang)}\n')
        o.append(f"[{('Vervoerderspagina' if lang == 'nl' else 'Carrier page')} →](carriers/{did}.md)\n")
        for head, kind in ((T['when'], 'triggers'), (T['andc'], 'conditions'), (T['then'], 'actions')):
            cards = cards_for(did, kind, include_global=False)
            o.append(f'**{head}**\n')
            for c in cards:
                o.append(f"* {ftitle(tx(c['title'], lang))} (`{c['id']}`)")
            if not cards:
                o.append(f"* {T['none']}")
            o.append('')
    return '\n'.join(o)


# ---------- tokens.md ----------
def postnl_global_defs():
    src = open(os.path.join(APP, 'drivers/postnl/driver.js'), encoding='utf-8').read()
    start = src.index('_globalTokenDefinitions()')
    end = src.index('_globalTokenDeviceKey', start)
    block = src[start:end]
    out = []
    for m in re.finditer(r"^\s*(\w+): \{ type: '(\w+)', title: \{ en: \"([^\"]*)\", nl: \"([^\"]*)\"", block, re.M):
        out.append(dict(name=m.group(1), type=m.group(2), en=m.group(3), nl=m.group(4)))
    assert any(x['name'] == 'package_image' for x in out) and any(x['name'] == 'mail_image' for x in out)
    return out


def delivery_token_defs():
    src = open(os.path.join(APP, 'app.js'), encoding='utf-8').read()
    def grab(lang):
        m = re.search(r"^\s*" + lang + r": \{ (image: .*?) \},?$", src, re.M)
        return dict(re.findall(r"(\w+): '([^']*)'", m.group(1)))
    en, nl = grab('en'), grab('nl')
    ids = dict(re.findall(r"(\w+): \{ id: '(myparcel_delivery_\w+)', type: '(?:\w+)' \}", src))
    types = dict(re.findall(r"\w+: \{ id: '(myparcel_delivery_\w+)', type: '(\w+)' \}", src))
    return [dict(key=k, id=ids[k], type=types[ids[k]], en=en[k], nl=nl[k]) for k in ids]


def tokens_page(lang):
    T = L[lang]
    o = []
    if lang == 'nl':
        o.append('# Flow-tokens\n')
        o.append('MyParcel kent drie soorten tokens:\n')
        o.append('1. **Kaart-tokens** – meegegeven door een *Wanneer*-kaart (bijv. *Status*, *Afzender*, *Bezorgvenster*). Ze bestaan alleen in de Flow die door díe kaart is gestart.')
        o.append('2. **Globale PostNL-tokens** – per PostNL-apparaat, beschikbaar in élke Flow (ook de afbeeldingen **Pakketafbeelding** en **Scan laatste poststuk**).')
        o.append('3. **Globale MyParcel-bezorgtokens** – de eerstvolgende actieve bezorging over alle vervoerders heen.\n')
        o.append('> **Tip:** gebruik je in een Advanced Flow een token van kaart A in een blok dat ook door kaart B gestart kan worden, dan meldt Homey *Missing token value*. Gebruik één trigger-kaart per actieketen, of een globaal token. Zie [Problemen oplossen](troubleshooting.md#missing-token-value).\n')
    else:
        o.append('# Flow tokens\n')
        o.append('MyParcel has three kinds of tokens:\n')
        o.append('1. **Card tokens** – passed by a *When* card (e.g. *Status*, *Sender*, *Delivery window*). They only exist in the Flow started by *that* card.')
        o.append('2. **Global PostNL tokens** – per PostNL device, available in *every* Flow (including the images **Parcel image** and **Latest mail scan**).')
        o.append('3. **Global MyParcel delivery tokens** – the next active delivery across all carriers.\n')
        o.append('> **Tip:** if an Advanced Flow uses a token of card A in a block that can also be started by card B, Homey reports *Missing token value*. Use one trigger card per action chain, or a global token. See [Troubleshooting](troubleshooting.md#missing-token-value).\n')
    o.append('## ' + ('Globale PostNL-tokens' if lang == 'nl' else 'Global PostNL tokens') + '\n')
    o.append(('Elk PostNL-apparaat maakt deze tokens aan als *&lt;apparaatnaam&gt; · &lt;titel&gt;*. De afbeeldingstokens werken in elke Flow, welke kaart de Flow ook startte.'
              if lang == 'nl' else
              'Every PostNL device creates these tokens as *&lt;device name&gt; · &lt;title&gt;*. The image tokens work in every Flow, whichever card started it.') + '\n')
    o.append(f"| {T['token']} | {T['type']} | {T['nl']} | {T['en']} |\n|---|---|---|---|")
    for t in postnl_global_defs():
        bold = '**' if t['type'] == 'image' else ''
        o.append(f"| `{t['name']}` | {TYPE[lang].get(t['type'], t['type'])} | {bold}{cell(t['nl'])}{bold} | {bold}{cell(t['en'])}{bold} |")
    o.append('')
    o.append('## ' + ('Globale MyParcel-bezorgtokens' if lang == 'nl' else 'Global MyParcel delivery tokens') + '\n')
    o.append(('Deze tokens tonen de eerstvolgende actieve bezorging van alle MyParcel-vervoerders samen. De titel volgt de taal van Homey.'
              if lang == 'nl' else
              'These tokens show the next active delivery across all MyParcel carriers. The title follows Homey\'s language.') + '\n')
    o.append(f"| {T['token']} | {T['type']} | {T['nl']} | {T['en']} |\n|---|---|---|---|")
    for t in delivery_token_defs():
        o.append(f"| `{t['id']}` | {TYPE[lang].get(t['type'], t['type'])} | {cell(t['nl'])} | {cell(t['en'])} |")
    o.append('')
    o.append('## ' + ('Kaart-tokens per vervoerder' if lang == 'nl' else 'Card tokens per carrier') + '\n')
    o.append(T['tokens_intro'] + '\n')
    for did in ORDER:
        toks = token_union(did)
        o.append(f'### {name(did, lang)}\n')
        o.append(f"<details>\n<summary>{T['show_tokens'].format(n=len(toks))}</summary>\n")
        o.append(f"| {T['token']} | {T['type']} | {('Titel' if lang == 'nl' else 'Title')} |\n|---|---|---|")
        for t in toks:
            o.append(f"| `{t['name']}` | {TYPE[lang].get(t.get('type'), t.get('type'))} | {cell(tx(t.get('title'), lang))} |")
        o.append('\n</details>\n')
    o.append(('[Flow-kaarten](flows.md) · [Apparaatgegevens](device.md) · [Flow-voorbeelden](examples.md)' if lang == 'nl'
              else '[Flow cards](flows.md) · [Device data](device.md) · [Flow examples](examples.md)') + '\n')
    return '\n'.join(o)


# ---------- device.md ----------
def device_page(lang):
    T = L[lang]
    o = [f"# {T['dev']}\n"]
    if lang == 'nl':
        o.append(f'Elke vervoerder is een eigen apparaat in Homey. Hieronder de apparaatwaarden (capabilities) per vervoerder in v{VERSION}. De beschikbaarheid van gegevens verschilt per vervoerder en pakket; niet elk veld is altijd gevuld en MyParcel verzint nooit gegevens die de vervoerder niet levert.\n')
        o.append('Gemeenschappelijk:\n')
        o.append('* **Verbindingsstatus** (`myparcel_connection_status`) – op (bijna) elk apparaat; wordt het apparaat *Niet verbonden*, dan verschijnt er een melding in de Tijdlijn.')
        o.append('* Een netwerkstoring toont een waarschuwing met de laatst bekende gegevens in plaats van het apparaat onbeschikbaar te maken.')
        o.append('* Bezorgde pakketten blijven het ingestelde aantal dagen zichtbaar (instelling *Bezorgde pakketten tonen (dagen)*).')
        o.append('* Slim pollen: elke 15 minuten als een bezorging dichtbij is, anders elke 45 minuten, rustig in de nacht.\n')
    else:
        o.append(f'Every carrier is its own device in Homey. Below are the device values (capabilities) per carrier in v{VERSION}. Available data depends on the carrier and parcel; not every field is always filled and MyParcel never makes up data the carrier does not provide.\n')
        o.append('Common to all:\n')
        o.append('* **Connection status** (`myparcel_connection_status`) – on (almost) every device; when a device becomes *Not connected*, a Timeline notification appears.')
        o.append('* A network hiccup shows a warning with the last known data instead of making the device unavailable.')
        o.append('* Delivered parcels stay visible for the configured number of days (setting *Show delivered parcels for (days)*).')
        o.append('* Smart polling: every 15 minutes when a delivery is near, every 45 minutes otherwise, quiet at night.\n')
    for did in ORDER:
        o.append(f'## {name(did, lang)}\n')
        o.append(f"| {T['id']} | {('Naam' if lang == 'nl' else 'Name')} | {T['type']} |\n|---|---|---|")
        for cap in DRIVERS[did]['capabilities']:
            c = CAPS.get(cap, {})
            o.append(f"| `{cap}` | {cell(tx(c.get('title'), lang))} | {TYPE[lang].get(c.get('type'), c.get('type', ''))} |")
        o.append(f"\n[{name(did, lang)} →](carriers/{did}.md)\n")
    return '\n'.join(o)


def write(path, text):
    full = os.path.join(DOCS, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(text.rstrip() + '\n')


for lang in ('nl', 'en'):
    for did in ORDER:
        write(f'{lang}/carriers/{did}.md', carrier_page(did, lang))
    write(f'{lang}/flows.md', flows_page(lang))
    write(f'{lang}/tokens.md', tokens_page(lang))
    write(f'{lang}/device.md', device_page(lang))

for did in ORDER:
    src = os.path.join(APP, f'drivers/{did}/assets/images/large.png')
    dst = os.path.join(DOCS, f'media/drivers/{did}/assets/images/large.png')
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)

print('ok', VERSION, len(FLOW['triggers']), len(FLOW['conditions']), len(FLOW['actions']))
