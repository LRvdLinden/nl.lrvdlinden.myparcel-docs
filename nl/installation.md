# Installeren en koppelen

## 1. App installeren

Installeer **MyParcel** uit de [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/). De app werkt op Homey Pro (lokaal platform) met Homey-versie 12.3.0 of nieuwer.

## 2. Een vervoerder toevoegen

1. Open Homey → **Apparaten** → **+** → **MyParcel**.
2. Kies je vervoerder. Elke vervoerder is een **eigen apparaat**; voeg er één toe per vervoerder (of per account) die je gebruikt.
3. Volg het koppelscherm. Afhankelijk van de vervoerder:
   * **Account** – log in met je vervoerdersaccount (PostNL, DPD, bpost, Vinted Go, Post & DHL Duitsland, Mondial Relay, Amazon; optioneel bij DHL, DHL Express en InPost). Bij sommige vervoerders open je een inlogpagina en plak je daarna het adres waarop je uitkwam terug in Homey.
   * **Trackingnummer** – vul trackingnummers in, soms met postcode (GLS, Trunkrs, Dynalogic, Dragonfly / Intelcom, Budbee, InPost, DHL, DHL Express, bpost).
   * **API-sleutel** – FedEx (Track API) en Royal Mail (Click & Drop).
4. Wacht tot de eerste synchronisatie klaar is. Bestaande pakketten worden dan stil vastgelegd, zodat er geen stroom aan *nieuw pakket*-meldingen komt.

De exacte stappen staan op de pagina van elke [vervoerder](carriers/README.md).

## 3. Trackingnummers later toevoegen

Bij vervoerders die met trackingnummers werken kun je nummers toevoegen of verwijderen via:

* de **apparaatinstellingen** (één nummer per regel, soms met postcode erachter), of
* de Flow-acties **Volg pakket…**, **Stop met volgen van pakket…** en **Verwijder bezorgde pakketten**.

Voeg `out` (of ` out`) achter een nummer toe voor een pakket dat je zelf verstuurt, waar de vervoerder dat ondersteunt (DHL, DHL Express, Post & DHL Duitsland, Dragonfly).

## 4. Widgets en Flows

* Zet de [widgets](widgets.md) op je Homey Dashboard. **MyParcel Pakketten** en **MyParcel Bezorging** tonen standaard alle vervoerders, ook apparaten die je later toevoegt.
* Bouw [Flows](flows.md) met de kaarten van je vervoerder; zie de [voorbeelden](examples.md).

## Goed om te weten

* **Slim pollen:** elke 15 minuten als een bezorging dichtbij is, anders elke 45 minuten en rustig in de nacht. Bezorgde pakketten worden niet meer opgevraagd.
* **Wachtwoorden:** waar mogelijk bewaart MyParcel alleen tokens, niet je wachtwoord.
* **Herstellen:** is een aanmelding verlopen, gebruik dan **Herstellen** op het apparaat – je hoeft het apparaat niet te verwijderen. Zie [Problemen oplossen](troubleshooting.md).
* Niet elke vervoerder levert dezelfde gegevens; lege velden betekenen dat de vervoerder die waarde niet geeft.

[Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
