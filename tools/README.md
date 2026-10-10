# Docs tools

Scripts to regenerate the MyParcel docs from the app repository. They are not part of the GitBook site (GitBook only reads `nl/` and `en/`).

| Script | What it does |
|---|---|
| `gen_docs.py` | Reads `app.json` (and the global token definitions in `app.js` / `drivers/postnl/driver.js`) and writes `carriers/<id>.md`, `flows.md`, `tokens.md` and `device.md` in `nl/` and `en/`, and copies each `drivers/<id>/assets/images/large.png` to `media/drivers/<id>/assets/images/`. |
| `carrier_meta.py` | Hand-written text per carrier (name, flags, countries, intro, connect steps, limitations) in NL and EN, plus the carrier order used in the pages. |
| `check_links.py` | Checks every relative link and anchor in the `.md` and `.html` files, that every page in `SUMMARY.md` exists and that every carrier page is listed. |

## Regenerate

Run from the docs repo root, with the app repo checked out next to it and its `app.json` composed (`homey app build` or Homey Compose):

```bash
python3 tools/gen_docs.py ../nl.lrvdlinden.myparcel .
python3 tools/check_links.py .
```

`gen_docs.py` overwrites only the generated pages listed above. Hand-written pages (`README.md`, `installation.md`, `widgets.md`, `examples.md`, `troubleshooting.md`, `changelog.md`, `SUMMARY.md` and `carriers/README.md`) and `carriers/index.html` are not touched.

## New carrier

1. Add an entry to `ORDER` and `M` in `carrier_meta.py` (the script stops if a driver in `app.json` has no entry).
2. Run `gen_docs.py`.
3. Add the page to `nl/SUMMARY.md` and `en/SUMMARY.md`, and update the card in `nl/carriers/README.md`, `en/carriers/README.md` and `carriers/index.html` (✅ Homey, link, image).
4. Run `check_links.py`.
