# Problemen oplossen

## Apparaat zegt „Niet verbonden" of aanmelding verlopen

1. Open het apparaat → **⚙ Instellingen** → **Herstellen** (Repair) en log opnieuw in of plak een nieuwe code. Je hoeft het apparaat niet te verwijderen: Flows en widgets blijven werken.
2. Controleer of je pakketten ook zichtbaar zijn in de app of op de website van de vervoerder.
3. Land of winkel gewijzigd (DPD, Amazon)? Gebruik **Herstellen** om voor dat land of die winkel opnieuw in te loggen.

Bij een tijdelijke netwerkstoring blijft het apparaat beschikbaar met een waarschuwing en de laatst bekende gegevens; MyParcel probeert het later opnieuw.

## Inloglinks werken maar één keer

Bij **Amazon**, **Mondial Relay**, **InPost** en **Post & DHL Duitsland** open je een inlogpagina en plak je daarna het adres waarop je uitkwam terug in Homey. Elke inloglink is eenmalig:

* Mislukt het koppelen, open dan de inlogpagina **opnieuw** vanuit het koppelscherm – je krijgt een nieuwe link.
* Kopieer het **volledige** adres uit de adresbalk. Een pagina die niet laadt of een fout toont (bijv. `https://account.inpost-group.com/callback?code=…`) is normaal.
* Plak het adres snel; een oude code wordt door de vervoerder geweigerd.

## Een pakket verschijnt niet

* **Trackingnummer-vervoerders** (GLS, Trunkrs, Dynalogic, Dragonfly, Budbee, InPost, DHL, DHL Express, FedEx): controleer het nummer en – waar nodig – de **postcode**. GLS, Trunkrs, Dynalogic en bpost (zonder account) tonen een pakket alleen met de juiste bezorgpostcode; zet een afwijkende postcode achter het nummer.
* **Accountvervoerders:** het pakket moet aan je account gekoppeld zijn bij de vervoerder.
* **Amazon** leest maximaal 10 zendingen per pollronde; meer zendingen verschijnen in volgende rondes.
* Bezorgde pakketten verdwijnen na het ingestelde aantal dagen (*Bezorgde pakketten tonen (dagen)*).

## Updates komen traag binnen (limieten)

* MyParcel pollt slim: elke 15 minuten als een bezorging dichtbij is, anders elke 45 minuten, rustig in de nacht.
* **DHL Express** staat ongeveer één opvraging per 40 minuten toe; meerdere luchtvrachtbrieven worden om de beurt bijgewerkt en MyParcel wacht langer als DHL vraagt om te vertragen.
* Widgets verversen een apparaat hooguit eens per 5 minuten.
* Gebruik de actie **Vernieuw …** / **Synchroniseer PostNL** als je direct wilt verversen.

## Missing token value

Homey toont *Missing token value: …* (bijv. `package_image`) als een Flow een token gebruikt dat de startende kaart niet heeft meegegeven. Dat gebeurt vooral in **Advanced Flow**, wanneer twee trigger-kaarten aan hetzelfde actieblok hangen en het blok een token van één van beide gebruikt.

Oplossingen:

* Gebruik **één trigger-kaart per actieketen**, of
* gebruik een **globaal token** dat in elke Flow werkt: **&lt;apparaatnaam&gt; · Pakketafbeelding**, **&lt;apparaatnaam&gt; · Scan laatste poststuk** of de MyParcel-bezorgtokens. Zie [Flow-tokens](tokens.md).

Sinds v0.3.5 is de PostNL-afbeelding in pakket-Flows nooit leeg: bezorgde pakketten houden de huidige Mijn Bezorging-afbeelding.

## Een kaart gaat niet af

* Kaarten gaan **één keer per wijziging** af. Na een update of herstart worden bestaande pakketten stil vastgelegd, dus er komen geen meldingen voor pakketten die al bekend waren.
* **Mondial Relay** geeft nog geen betrouwbare status: alleen *nieuw pakket* en *trackinggebeurtenis* gaan af.
* **Dynalogic** levert geen bezorgvenster, dus er is geen kaart *bezorgtijd gewijzigd*.

## Nog steeds problemen?

Stuur een diagnoserapport via Homey → **Instellingen** → **Apps** → **MyParcel** → **Diagnoserapport versturen** en meld het nummer in het [Homey Community-topic](https://community.homey.app/t/app-pro-myparcel/159800).
