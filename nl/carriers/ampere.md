# Ampère

![Ampère](../../media/drivers/ampere/assets/images/large.png)

Ampère bezorgt pakketten voor bol.com. MyParcel leest de status van Ampère's eigen pakketpagina via de link in de bol.com-mail, met bezorgvenster en statusgeschiedenis. Met de helper vindt MyParcel Ampère-pakketten automatisch in je bol.com-account.

## In één oogopslag

| | |
|---|---|
| Landen | 🇳🇱 Nederland |
| Koppelen met | Trackingnummer · Account |
| Apparaat-ID | `ampere` |
| Flow-kaarten | 9 triggers · 8 condities · 4 acties |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **Ampère**.
2. Gebruik de **Bol.com Homey Login Helper**, log één keer in via login.bol.com en plak de gegenereerde **bol.com-sessiecode**. MyParcel controleert daarna automatisch je bol.com-bestellingen op Ampère-bezorgingen.
3. **Of handmatig:** plak de **trackinglink uit de bol.com-mail** (bijv. `https://link.bol.com/t/…`).
4. Tik op **Koppelen**.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| Ampère Track & Trace | **Trackinglinks uit de bol.com-mail** | Eén link per regel, bijv. https://link.bol.com/t/… – pakketten uit je bol.com-account worden automatisch gevonden als de helpercode is ingesteld. |
| Ampère Track & Trace | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |
| bol.com-account (helper) | **bol.com-sessiecode** | (wordt verborgen opgeslagen) |
| bol.com-account (helper) | **Ampère Track & Trace-URL (fallback)** | — |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `ampere_parcel_count` | getal | Actieve pakketten | Active parcels |
| `ampere_total_count` | getal | Totaal pakketten | Total parcels |
| `ampere_status` | tekst | Status | Status |
| `ampere_tracking` | tekst | Trackingnummer | Tracking number |
| `ampere_sender` | tekst | Afzender | Sender |
| `ampere_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `ampere_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `ampere_window_start` | tekst | Start bezorgvenster | Delivery window start |
| `ampere_window_end` | tekst | Einde bezorgvenster | Delivery window end |
| `ampere_delivered` | ja/nee | Bezorgd | Delivered |
| `ampere_details_url` | tekst | Track & Trace-URL | Track & Trace URL |
| `ampere_receiver` | tekst | Ontvanger | Receiver |
| `ampere_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `ampere_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `ampere_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `ampere_last_event` | tekst | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | tekst | Verbindingsstatus | Connection status |
| `ampere_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `ampere_new_package` | Nieuw Ampère-pakket gevonden | New Ampère parcel found |
| `ampere_status_changed` | Status van Ampère-pakket gewijzigd | Ampère parcel status changed |
| `ampere_package_event_changed` | Nieuwe Ampère-trackinggebeurtenis | New Ampère tracking event |
| `ampere_out_for_delivery` | Ampère-pakket onderweg voor bezorging | Ampère parcel out for delivery |
| `ampere_delivered` | Ampère-pakket bezorgd | Ampère parcel delivered |
| `ampere_package_problem` | Probleem of retour bij Ampère-pakket | Ampère parcel has a problem or is returning |
| `ampere_delivery_updated` | Ampère-bezorginformatie bijgewerkt | Ampère delivery information updated |
| `ampere_delivery_window_changed` | Ampère-bezorgvenster bekend of gewijzigd | Ampère delivery window available or changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `ampere_packages_underway` | Er zijn Ampère-pakketten onderweg | Ampère parcels are underway | — |
| `ampere_delivery_window_known` | Ampère-bezorgvenster is/is niet bekend | Ampère delivery window is/isn't known | — |
| `ampere_is_delivered` | Laatste Ampère-pakket is/is niet bezorgd | Latest Ampère parcel is/isn't delivered | — |
| `ampere_is_connected` | Ampère is/is niet verbonden | Ampère is/isn't connected | — |
| `ampere_out_for_delivery_now` | Er is een/geen Ampère-pakket onderweg voor bezorging | A Ampère parcel is/is not out for delivery | — |
| `ampere_any_status_is` | Een Ampère-pakket heeft/heeft niet status… | A Ampère parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij Ampère) |
| `ampere_parcel_is_delivered` | Ampère-pakket… is/is niet bezorgd | Ampère parcel… is/is not delivered | Trackingnummer |
| `ampere_is_tracking` | Ampère-pakket… wordt wel/niet gevolgd | Ampère parcel… is/is not being tracked | Trackingnummer |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `ampere_refresh` | Vernieuw Ampère | Refresh Ampère | — |
| `ampere_track_parcel` | Volg Ampère-pakket via bol.com-link… | Track Ampère parcel from bol.com link… | Trackingnummer |
| `ampere_untrack_parcel` | Stop met volgen van Ampère-pakket… | Stop tracking Ampère parcel… | Trackingnummer |
| `ampere_remove_delivered` | Verwijder bezorgde Ampère-pakketten | Remove delivered Ampère parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 27 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `carrier` | tekst | Vervoerder | Carrier |
| `tracking` | tekst | Trackingnummer | Tracking number |
| `sender` | tekst | Afzender | Sender |
| `status` | tekst | Status | Status |
| `delivery_date` | tekst | Bezorgdatum | Delivery date |
| `delivery_window` | tekst | Bezorgvenster | Delivery window |
| `window_start` | tekst | Start bezorgvenster | Delivery window start |
| `window_end` | tekst | Einde bezorgvenster | Delivery window end |
| `delivered` | ja/nee | Bezorgd | Delivered |
| `track_url` | tekst | Track & Trace-URL | Track & Trace URL |
| `active_count` | getal | Actieve pakketten | Active parcels |
| `total_count` | getal | Totaal pakketten | Total parcels |
| `last_update` | tekst | Laatste update | Last update |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | Ampère-statustekst | Ampère status text |
| `receiver` | tekst | Ontvanger | Recipient |
| `pickup_point` | tekst | Afhaalpunt | Pickup point |
| `last_event` | tekst | Laatste gebeurtenis | Last event |
| `last_event_time` | tekst | Tijd laatste gebeurtenis | Last event time |
| `delivered_at` | tekst | Bezorgd op | Delivered at |
| `direction` | tekst | Richting | Direction |
| `history` | tekst | Statusgeschiedenis | Status history |
| `url` | tekst | Trackinglink | Tracking link |
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige Ampère-statustekst | Previous Ampère status text |
| `old_delivery_window` | tekst | Vorig bezorgvenster | Previous delivery window |

</details>

## Beperkingen en tips

* Alleen Ampère-zendingen worden getoond; PostNL-3S-zendingen en niet-bevestigde kandidaten worden gefilterd.
* Verloopt de Ampère-sessie, dan start MyParcel stil een nieuwe sessie.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
