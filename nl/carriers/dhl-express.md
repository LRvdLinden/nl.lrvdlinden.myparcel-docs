# DHL Express

![DHL Express](../../media/drivers/dhl-express/assets/images/large.png)

Internationale DHL Express-zendingen volgen met hun luchtvrachtbriefnummer (10 cijfers) – zonder account. Optioneel combineer je dat met je MyDHL+-account om ook de zendingen uit dat account te zien.

## In één oogopslag

| | |
|---|---|
| Landen | 🌍 Wereldwijd |
| Koppelen met | Trackingnummer · Account |
| Apparaat-ID | `dhl-express` |
| Flow-kaarten | 10 triggers · 8 condities · 4 acties |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **DHL Express**.
2. Vul de **luchtvrachtbriefnummers** in (één per regel, bijv. `1234567890`; voeg `out` toe voor een zending die je zelf verstuurt) en tik op **Zendingen volgen**.
3. Optioneel: open **MyDHL+-account gebruiken** en log in met e-mailadres en wachtwoord (plus verificatiecode als DHLPass erom vraagt).
4. Blokkeert DHLPass de directe login, gebruik dan de **DHL Express Homey Login Helper** en plak de `DHLEXPRESS1`-sessiecode via **Koppelen met helpercode**.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| DHL Express Track & Trace | **Trackingnummers** | Eén luchtvrachtbriefnummer van 10 cijfers per regel – geen account nodig. Voeg “uit” toe voor een zending die je zelf verstuurt. DHL Express staat ongeveer één opvraging per 40 minuten toe; met meerdere nummers wordt elk nummer om de beurt bijgewerkt. |
| DHL Express Track & Trace | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |
| MyDHL+-account (optioneel) | **MyDHL+ websessie** | (wordt verborgen opgeslagen) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `dhl_express_parcel_count` | getal | Actieve pakketten | Active parcels |
| `dhl_express_total_count` | getal | Totaal pakketten | Total parcels |
| `dhl_express_status` | tekst | Status | Status |
| `dhl_express_tracking` | tekst | Trackingnummer | Tracking number |
| `dhl_express_sender` | tekst | Afzender | Sender |
| `dhl_express_receiver` | tekst | Ontvanger | Receiver |
| `dhl_express_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `dhl_express_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `dhl_express_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `dhl_express_service` | tekst | Service | Service |
| `dhl_express_origin` | tekst | Herkomst | Origin |
| `dhl_express_destination` | tekst | Bestemming | Destination |
| `dhl_express_pieces` | getal | Colli | Pieces |
| `dhl_express_last_event` | tekst | Laatste gebeurtenis | Last event |
| `dhl_express_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `dhl_express_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `dhl_express_delivered` | ja/nee | Bezorgd | Delivered |
| `myparcel_connection_status` | tekst | Verbindingsstatus | Connection status |
| `dhl_express_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `dhl_express_new_package` | Nieuw DHL Express-pakket gevonden | New DHL Express parcel found |
| `dhl_express_status_changed` | Status DHL Express-pakket gewijzigd | DHL Express parcel status changed |
| `dhl_express_package_event_changed` | Nieuwe DHL Express-trackinggebeurtenis | New DHL Express tracking event |
| `dhl_express_out_for_delivery` | DHL Express-pakket onderweg voor bezorging | DHL Express parcel out for delivery |
| `dhl_express_delivered` | DHL Express-pakket bezorgd | DHL Express parcel delivered |
| `dhl_express_package_problem` | Probleem of retour bij DHL Express-pakket | DHL Express parcel has a problem or is returning |
| `dhl_express_outgoing_status_changed` | Status van verzonden DHL Express-pakket gewijzigd | Status of sent DHL Express parcel changed |
| `dhl_express_outgoing_delivered` | Verzonden DHL Express-pakket bezorgd | Sent DHL Express parcel delivered |
| `dhl_express_delivery_updated` | DHL Express-bezorginformatie bijgewerkt | DHL Express delivery information updated |
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `dhl_express_packages_underway` | Er zijn DHL Express-pakketten onderweg | DHL Express parcels are underway | — |
| `dhl_express_is_connected` | DHL Express is/is niet verbonden | DHL Express is/isn't connected | — |
| `dhl_express_delivery_window_known` | DHL Express-bezorgvenster is/is niet bekend | DHL Express delivery window is/isn't known | — |
| `dhl_express_out_for_delivery_now` | Er is een/geen DHL Express-pakket onderweg voor bezorging | A DHL Express parcel is/is not out for delivery | — |
| `dhl_express_any_status_is` | Een DHL Express-pakket heeft/heeft niet status… | A DHL Express parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij DHL Express) |
| `dhl_express_parcel_is_delivered` | DHL Express-pakket… is/is niet bezorgd | DHL Express parcel… is/is not delivered | Trackingnummer |
| `dhl_express_is_tracking` | DHL Express-pakket… wordt wel/niet gevolgd | DHL Express parcel… is/is not being tracked | Trackingnummer |
| `dhl_express_outgoing_underway` | Er zijn/zijn geen verzonden DHL Express-pakketten onderweg | Sent DHL Express parcels are/are not underway | — |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `dhl_express_refresh` | Vernieuw DHL Express | Refresh DHL Express | — |
| `dhl_express_track_parcel` | Volg DHL Express-pakket… | Track DHL Express parcel… | Trackingnummer; Richting (Inkomend, Uitgaand (door mij verzonden)) |
| `dhl_express_untrack_parcel` | Stop met volgen van DHL Express-pakket… | Stop tracking DHL Express parcel… | Trackingnummer |
| `dhl_express_remove_delivered` | Verwijder bezorgde DHL Express-pakketten | Remove delivered DHL Express parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 30 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `carrier` | tekst | Vervoerder | Carrier |
| `tracking` | tekst | Trackingnummer | Tracking number |
| `sender` | tekst | Afzender | Sender |
| `receiver` | tekst | Ontvanger | Receiver |
| `status` | tekst | Status | Status |
| `delivery_date` | tekst | Bezorgdatum | Delivery date |
| `delivery_window` | tekst | Bezorgvenster | Delivery window |
| `service` | tekst | Service | Service |
| `origin` | tekst | Herkomst | Origin |
| `destination` | tekst | Bestemming | Destination |
| `last_event` | tekst | Laatste gebeurtenis | Last event |
| `delivered` | ja/nee | Bezorgd | Delivered |
| `active_count` | getal | Actieve pakketten | Active parcels |
| `total_count` | getal | Totaal pakketten | Total parcels |
| `last_update` | tekst | Laatste update | Last update |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | DHL Express-statustekst | DHL Express status text |
| `window_start` | tekst | Begin venster | Window start |
| `window_end` | tekst | Einde venster | Window end |
| `pickup_point` | tekst | Afhaalpunt | Pickup point |
| `last_event_time` | tekst | Tijd laatste gebeurtenis | Last event time |
| `delivered_at` | tekst | Bezorgd op | Delivered at |
| `direction` | tekst | Richting | Direction |
| `history` | tekst | Statusgeschiedenis | Status history |
| `url` | tekst | Trackinglink | Tracking link |
| `pieces` | getal | Colli | Pieces |
| `proof_of_delivery` | tekst | Afleverbewijs | Proof of delivery |
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige DHL Express-statustekst | Previous DHL Express status text |

</details>

## Beperkingen en tips

* **Aanvraaglimiet:** DHL Express staat ongeveer één opvraging per 40 minuten toe. Meerdere nummers worden om de beurt bijgewerkt (zendingen bij de koerier eerst) en MyParcel wacht langer als DHL vraagt om te vertragen.
* Er is geen apart bezorgvenster bij alle zendingen; dat hangt af van wat DHL Express teruggeeft.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
