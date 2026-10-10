# Dynalogic

![Dynalogic](../../media/drivers/dynalogic/assets/images/large.png)

> **Nieuw in v0.3.6**

Dynalogic bezorgt grote en waardevolle zendingen (bijv. elektronica). Volg bezorgingen met het ordernummer en de postcode – geen account nodig. Statussen komen uit Dynalogic's eigen scenario-/stap-/resultaatcodes (bezorgd, wordt bezorgd, probleem, retour), met afzender, ontvanger en geschiedenis.

## In één oogopslag

| | |
|---|---|
| Landen | 🇳🇱 🇧🇪 Nederland en België |
| Koppelen met | Trackingnummer |
| Apparaat-ID | `dynalogic` |
| Flow-kaarten | 7 triggers · 5 condities · 4 acties |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **Dynalogic**.
2. Kies het **land** (Nederland of België) en vul de **postcode van het bezorgadres** in (verplicht; NL `1234AB`, BE `1000`).
3. Vul optioneel de **ordernummers** in, één per regel; zet een afwijkende postcode achter het nummer.
4. Tik op **Dynalogic toevoegen**. Ordernummers toevoegen kan later via de apparaatinstellingen of met een Flow.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| Dynalogic Track & Trace | **Land** | (keuzes: Nederland, België) |
| Dynalogic Track & Trace | **Bezorgpostcode** | Postcode van het bezorgadres (Nederland 1234AB, België 1000). Dynalogic heeft die nodig om de order te tonen. |
| Dynalogic Track & Trace | **Trackingnummers** | Eén trackingnummer per regel. Zet een postcode achter een nummer als die afwijkt van de postcode hierboven (bijv. "1234567890 1234AB"). |
| Dynalogic Track & Trace | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `dynalogic_parcel_count` | getal | Actieve pakketten | Active parcels |
| `dynalogic_status` | tekst | Status | Status |
| `dynalogic_tracking` | tekst | Trackingnummer | Tracking number |
| `dynalogic_sender` | tekst | Afzender | Sender |
| `dynalogic_receiver` | tekst | Ontvanger | Receiver |
| `dynalogic_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `dynalogic_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `dynalogic_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `dynalogic_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `dynalogic_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `dynalogic_last_event` | tekst | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | tekst | Verbindingsstatus | Connection status |
| `dynalogic_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `dynalogic_new_package` | Nieuw Dynalogic-pakket | New Dynalogic parcel |
| `dynalogic_status_changed` | Status Dynalogic-pakket gewijzigd | Dynalogic parcel status changed |
| `dynalogic_package_event_changed` | Nieuwe Dynalogic-trackinggebeurtenis | New Dynalogic tracking event |
| `dynalogic_out_for_delivery` | Dynalogic-pakket onderweg voor bezorging | Dynalogic parcel out for delivery |
| `dynalogic_delivered` | Dynalogic-pakket bezorgd | Dynalogic parcel delivered |
| `dynalogic_package_problem` | Probleem of retour bij Dynalogic-pakket | Dynalogic parcel has a problem or is returning |
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `dynalogic_packages_underway` | Er zijn/zijn geen Dynalogic-pakketten onderweg | Dynalogic parcels are/are not underway | — |
| `dynalogic_out_for_delivery_now` | Er is een/geen Dynalogic-pakket onderweg voor bezorging | A Dynalogic parcel is/is not out for delivery | — |
| `dynalogic_any_status_is` | Een Dynalogic-pakket heeft/heeft niet status… | A Dynalogic parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij Dynalogic) |
| `dynalogic_parcel_is_delivered` | Dynalogic-pakket… is/is niet bezorgd | Dynalogic parcel… is/is not delivered | Trackingnummer |
| `dynalogic_is_tracking` | Dynalogic-pakket… wordt wel/niet gevolgd | Dynalogic parcel… is/is not being tracked | Trackingnummer |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `dynalogic_refresh` | Vernieuw Dynalogic | Refresh Dynalogic | — |
| `dynalogic_track_parcel` | Volg Dynalogic-pakket… | Track Dynalogic parcel… | Trackingnummer |
| `dynalogic_untrack_parcel` | Stop met volgen van Dynalogic-pakket… | Stop tracking Dynalogic parcel… | Trackingnummer |
| `dynalogic_remove_delivered` | Verwijder bezorgde Dynalogic-pakketten | Remove delivered Dynalogic parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 21 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | tekst | Trackingnummer | Tracking number |
| `status` | tekst | Status | Status |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | Dynalogic-statustekst | Dynalogic status text |
| `sender` | tekst | Afzender | Sender |
| `receiver` | tekst | Ontvanger | Recipient |
| `delivery_date` | tekst | Bezorgdatum | Delivery date |
| `delivery_window` | tekst | Bezorgvenster | Delivery window |
| `window_start` | tekst | Begin venster | Window start |
| `window_end` | tekst | Einde venster | Window end |
| `pickup_point` | tekst | Afhaalpunt | Pickup point |
| `last_event` | tekst | Laatste gebeurtenis | Last event |
| `last_event_time` | tekst | Tijd laatste gebeurtenis | Last event time |
| `delivered_at` | tekst | Bezorgd op | Delivered at |
| `direction` | tekst | Richting | Direction |
| `history` | tekst | Statusgeschiedenis | Status history |
| `url` | tekst | Trackinglink | Tracking link |
| `destination` | tekst | Bestemming | Destination |
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige Dynalogic-statustekst | Previous Dynalogic status text |

</details>

## Beperkingen en tips

* **Geen bezorgvenster:** Dynalogic levert (nog) geen gestructureerd bezorgvenster. De capability *Bezorgvenster* blijft leeg en er is geen kaart *bezorgtijd gewijzigd*.
* Dynalogic toont een bezorging alleen samen met de postcode van het bezorgadres.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
