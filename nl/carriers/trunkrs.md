# Trunkrs

![Trunkrs](../../media/drivers/trunkrs/assets/images/large.png)

> **Nieuw in v0.3.6**

Trunkrs bezorgt same-day en in de avond. Volg Trunkrs-pakketten met hun nummer en de postcode van het bezorgadres – geen account nodig. Met het bezorgvenster van Trunkrs, onderweg, bezorgd, geschiedenis en gebeurtenisteksten in je eigen taal.

## In één oogopslag

| | |
|---|---|
| Landen | 🇳🇱 Nederland |
| Koppelen met | Trackingnummer |
| Apparaat-ID | `trunkrs` |
| Flow-kaarten | 8 triggers · 5 condities · 4 acties |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **Trunkrs**.
2. Vul de **postcode van het bezorgadres** in (verplicht, bijv. `1234AB`).
3. Vul optioneel de **Trunkrs-nummers** in, één per regel. Voor een pakket naar een ander adres zet je de postcode achter het nummer: `419719666 1234AB`.
4. Tik op **Trunkrs toevoegen**. Nummers toevoegen kan later via de apparaatinstellingen of met een Flow.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| Trunkrs Track & Trace | **Bezorgpostcode** | Postcode van het bezorgadres (bijv. 1234AB). Trunkrs heeft die nodig om het pakket te tonen. |
| Trunkrs Track & Trace | **Trackingnummers** | Eén trackingnummer per regel. Zet een postcode achter een nummer als die afwijkt van de postcode hierboven (bijv. "419719666 1234AB"). |
| Trunkrs Track & Trace | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `trunkrs_parcel_count` | getal | Actieve pakketten | Active parcels |
| `trunkrs_status` | tekst | Status | Status |
| `trunkrs_tracking` | tekst | Trackingnummer | Tracking number |
| `trunkrs_sender` | tekst | Afzender | Sender |
| `trunkrs_receiver` | tekst | Ontvanger | Receiver |
| `trunkrs_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `trunkrs_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `trunkrs_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `trunkrs_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `trunkrs_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `trunkrs_last_event` | tekst | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | tekst | Verbindingsstatus | Connection status |
| `trunkrs_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `trunkrs_new_package` | Nieuw Trunkrs-pakket | New Trunkrs parcel |
| `trunkrs_status_changed` | Status Trunkrs-pakket gewijzigd | Trunkrs parcel status changed |
| `trunkrs_package_event_changed` | Nieuwe Trunkrs-trackinggebeurtenis | New Trunkrs tracking event |
| `trunkrs_out_for_delivery` | Trunkrs-pakket onderweg voor bezorging | Trunkrs parcel out for delivery |
| `trunkrs_delivered` | Trunkrs-pakket bezorgd | Trunkrs parcel delivered |
| `trunkrs_package_problem` | Probleem of retour bij Trunkrs-pakket | Trunkrs parcel has a problem or is returning |
| `trunkrs_delivery_window_changed` | Trunkrs-bezorgtijd gewijzigd | Trunkrs delivery time changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `trunkrs_packages_underway` | Er zijn/zijn geen Trunkrs-pakketten onderweg | Trunkrs parcels are/are not underway | — |
| `trunkrs_out_for_delivery_now` | Er is een/geen Trunkrs-pakket onderweg voor bezorging | A Trunkrs parcel is/is not out for delivery | — |
| `trunkrs_any_status_is` | Een Trunkrs-pakket heeft/heeft niet status… | A Trunkrs parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij Trunkrs) |
| `trunkrs_parcel_is_delivered` | Trunkrs-pakket… is/is niet bezorgd | Trunkrs parcel… is/is not delivered | Trackingnummer |
| `trunkrs_is_tracking` | Trunkrs-pakket… wordt wel/niet gevolgd | Trunkrs parcel… is/is not being tracked | Trackingnummer |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `trunkrs_refresh` | Vernieuw Trunkrs | Refresh Trunkrs | — |
| `trunkrs_track_parcel` | Volg Trunkrs-pakket… | Track Trunkrs parcel… | Trackingnummer |
| `trunkrs_untrack_parcel` | Stop met volgen van Trunkrs-pakket… | Stop tracking Trunkrs parcel… | Trackingnummer |
| `trunkrs_remove_delivered` | Verwijder bezorgde Trunkrs-pakketten | Remove delivered Trunkrs parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 22 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | tekst | Trackingnummer | Tracking number |
| `status` | tekst | Status | Status |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | Trunkrs-statustekst | Trunkrs status text |
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
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige Trunkrs-statustekst | Previous Trunkrs status text |
| `old_delivery_window` | tekst | Vorig bezorgvenster | Previous delivery window |

</details>

## Beperkingen en tips

* Trunkrs toont een pakket alleen samen met de Nederlandse postcode van het bezorgadres.
* Geen account-koppeling: alleen nummers die je toevoegt worden gevolgd.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
