# Dragonfly / Intelcom

![Dragonfly / Intelcom](../../media/drivers/dragonfly/assets/images/large.png)

> **Nieuw in v0.3.6**

Volg pakketten van Dragonfly (Nederland, Australië) en Intelcom (Canada) met hun trackingnummer – geen account nodig. Met bezorgvenster (ETA), onderweg, bezorgd, geschiedenis in je eigen taal (als Dragonfly die heeft) en pakketten die je zelf verstuurt. Voor Canada heet het apparaat Intelcom.

## In één oogopslag

| | |
|---|---|
| Landen | 🇳🇱 🇦🇺 🇨🇦 Nederland en Australië (Dragonfly), Canada (Intelcom) |
| Koppelen met | Trackingnummer |
| Apparaat-ID | `dragonfly` |
| Flow-kaarten | 10 triggers · 6 condities · 4 acties |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **Dragonfly / Intelcom**.
2. Kies het **land**: Nederland (Dragonfly), Australië (Dragonfly) of Canada (Intelcom).
3. Vul optioneel **trackingnummers** in, één per regel (bijv. `INTLCMB2C000999999`). Zet ` out` achter een code voor een pakket dat je zelf verstuurt.
4. Tik op **Apparaat toevoegen**. Codes toevoegen kan later via de apparaatinstellingen of met een Flow.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| Dragonfly / Intelcom Track & Trace | **Land** | (keuzes: Nederland (Dragonfly), Australië (Dragonfly), Canada (Intelcom)) |
| Dragonfly / Intelcom Track & Trace | **Trackingnummers** | Eén trackingnummer per regel. Zet " uit" achter een nummer voor een pakket dat je zelf verstuurt. |
| Dragonfly / Intelcom Track & Trace | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `dragonfly_parcel_count` | getal | Actieve pakketten | Active parcels |
| `dragonfly_status` | tekst | Status | Status |
| `dragonfly_tracking` | tekst | Trackingnummer | Tracking number |
| `dragonfly_sender` | tekst | Afzender | Sender |
| `dragonfly_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `dragonfly_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `dragonfly_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `dragonfly_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `dragonfly_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `dragonfly_outgoing_count` | getal | Verzonden pakketten onderweg | Sent parcels underway |
| `dragonfly_last_event` | tekst | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | tekst | Verbindingsstatus | Connection status |
| `dragonfly_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `dragonfly_new_package` | Nieuw Dragonfly-pakket | New Dragonfly parcel |
| `dragonfly_status_changed` | Status Dragonfly-pakket gewijzigd | Dragonfly parcel status changed |
| `dragonfly_package_event_changed` | Nieuwe Dragonfly-trackinggebeurtenis | New Dragonfly tracking event |
| `dragonfly_out_for_delivery` | Dragonfly-pakket onderweg voor bezorging | Dragonfly parcel out for delivery |
| `dragonfly_delivered` | Dragonfly-pakket bezorgd | Dragonfly parcel delivered |
| `dragonfly_package_problem` | Probleem of retour bij Dragonfly-pakket | Dragonfly parcel has a problem or is returning |
| `dragonfly_outgoing_status_changed` | Status van verzonden Dragonfly-pakket gewijzigd | Status of sent Dragonfly parcel changed |
| `dragonfly_outgoing_delivered` | Verzonden Dragonfly-pakket bezorgd | Sent Dragonfly parcel delivered |
| `dragonfly_delivery_window_changed` | Dragonfly-bezorgtijd gewijzigd | Dragonfly delivery time changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `dragonfly_packages_underway` | Er zijn/zijn geen Dragonfly-pakketten onderweg | Dragonfly parcels are/are not underway | — |
| `dragonfly_out_for_delivery_now` | Er is een/geen Dragonfly-pakket onderweg voor bezorging | A Dragonfly parcel is/is not out for delivery | — |
| `dragonfly_any_status_is` | Een Dragonfly-pakket heeft/heeft niet status… | A Dragonfly parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij Dragonfly / Intelcom) |
| `dragonfly_parcel_is_delivered` | Dragonfly-pakket… is/is niet bezorgd | Dragonfly parcel… is/is not delivered | Trackingnummer |
| `dragonfly_is_tracking` | Dragonfly-pakket… wordt wel/niet gevolgd | Dragonfly parcel… is/is not being tracked | Trackingnummer |
| `dragonfly_outgoing_underway` | Er zijn/zijn geen verzonden Dragonfly-pakketten onderweg | Sent Dragonfly parcels are/are not underway | — |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `dragonfly_refresh` | Vernieuw Dragonfly | Refresh Dragonfly | — |
| `dragonfly_track_parcel` | Volg Dragonfly-pakket… | Track Dragonfly parcel… | Trackingnummer; Richting (Inkomend, Uitgaand (door mij verzonden)) |
| `dragonfly_untrack_parcel` | Stop met volgen van Dragonfly-pakket… | Stop tracking Dragonfly parcel… | Trackingnummer |
| `dragonfly_remove_delivered` | Verwijder bezorgde Dragonfly-pakketten | Remove delivered Dragonfly parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 24 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | tekst | Trackingnummer | Tracking number |
| `status` | tekst | Status | Status |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | Dragonfly / Intelcom-statustekst | Dragonfly / Intelcom status text |
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
| `service` | tekst | Dienst | Service |
| `country` | tekst | Land | Country |
| `carrier` | tekst | Vervoerder | Carrier |
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige Dragonfly / Intelcom-statustekst | Previous Dragonfly / Intelcom status text |
| `old_delivery_window` | tekst | Vorig bezorgvenster | Previous delivery window |

</details>

## Beperkingen en tips

* Geen account-koppeling: alleen nummers die je toevoegt (en ophaaltaken voor verzonden pakketten) worden gevolgd.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
