# Widgets

MyParcel heeft acht Homey Dashboard-widgets. Voeg ze toe via het Dashboard → **Widget toevoegen** → **MyParcel** en kies het apparaat (of de apparaten) dat de widget moet tonen.

## Voor alle vervoerders

### MyParcel Pakketten

Widget-ID: `myparcel-pakketten` · hoogte 360

Lijst met de pakketten van al je MyParcel-vervoerders, met logo, vertaalde status, afzender, datum en bezorgvenster of laatste update. Tik op een pakket voor een popup met alle details die de vervoerder levert (trackingnummer, laatste gebeurtenis, gewicht, afmetingen, afhaalpunt …).

**Instelling:** **Toon alle vervoerders (ook nieuw toegevoegde)** – standaard aan: elk MyParcel-apparaat wordt getoond, ook apparaten die je later toevoegt. Zet dit uit om alleen de apparaten te tonen die je voor deze widget selecteert.

### MyParcel Bezorging

Widget-ID: `myparcel-bezorging` · hoogte 420

De actieve bezorgingen van alle geselecteerde vervoerders samen, met vervoerderbranding, afzender, status, bezorgdatum/-venster en een tijdlijn die de eigen status van elke vervoerder volgt.

**Instelling:** **Toon alle vervoerders (ook nieuw toegevoegde)** – zoals hierboven.

## PostNL

| Widget | ID | Wat je ziet |
|---|---|---|
| **Mijn Post** | `poststukken` | Aangekondigde post met scans (live; ververst elke minuut zolang de widget open is). |
| **Mijn Pakketten** | `postnl-mijn-pakketten` | Je PostNL-pakketten met status en bezorgmoment. |
| **Mijn Bezorging** | `postnl-pakketdetails` | Het actieve pakket met de geanimeerde PostNL-bus, live bezorgvenster en voortgang. |
| **Reis van je pakket** | `postnl-pakket-reis` | De tijdlijn van een PostNL-pakket, stap voor stap. |

Deze widgets tonen één PostNL-apparaat.

## Post & DHL Duitsland

| Widget | ID | Wat je ziet |
|---|---|---|
| **DHL-pakketten (Duitsland)** (*DHL Pakete*) | `dhl-de-pakete` | Je DHL-pakketten in Duitsland met status, Packstation en verzonden pakketten. |
| **Deutsche Post Poststukken** | `deutsche-post-poststukken` | Aangekondigde Deutsche Post-brieven. |

## Goed om te weten

* Widgets verversen een apparaat hooguit eens per 5 minuten; ze starten geen volledige synchronisatie per open scherm.
* Datums en tijden volgen je taal; widgets tonen relatieve tijden („2 uur geleden"). Arabisch wordt rechts-naar-links getoond.
* De beschikbaarheid van gegevens verschilt per vervoerder en pakket.

[Apparaatgegevens](device.md) · [Vervoerders](carriers/README.md)
