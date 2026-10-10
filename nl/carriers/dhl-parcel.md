# DHL

![DHL](../../media/drivers/dhl-parcel/assets/images/large.png)

DHL Parcel (eCommerce) in Homey: je My DHL-pakketten met DHL's eigen statuscodes (onderweg, klaar bij een ServicePoint/ParcelStation, bezorgd bij de buren of in de brievenbus, retouren), het bezorgvenster en de statusgeschiedenis. Een account is optioneel: losse trackingnummers werken ook.

## In één oogopslag

| | |
|---|---|
| Landen | 🇳🇱 Nederland (My DHL-account en DHL Parcel-trackingnummers) |
| Koppelen met | Account · Trackingnummer |
| Apparaat-ID | `dhl-parcel` |
| Flow-kaarten | 11 triggers · 9 condities · 4 acties |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **DHL**.
2. Vul je **My DHL-account** (e-mailadres en wachtwoord) in om al je pakketten automatisch te zien, **of** vul alleen **trackingnummers** in (één per regel, bijv. `JJD…` of `3S…`). Allebei kan ook.
3. Voeg optioneel een postcode toe voor de trackinglink en `out` voor een pakket dat je zelf verstuurt.
4. Tik op **DHL toevoegen**. Nummers toevoegen kan later via de apparaatinstellingen of met een Flow.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| DHL Track & Trace | **Trackingnummers** | Eén per regel. Werkt zonder My DHL-account voor DHL Parcel-nummers (bijv. JJD…, 3S…). Voeg eventueel een postcode toe voor de trackinglink, en “uit” voor een pakket dat je zelf verstuurt, bijv. 3SABC1234567890 1234AB uit. |
| DHL Track & Trace | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `dhl_parcel_count` | getal | Actieve pakketten | Active parcels |
| `dhl_status` | tekst | Status | Status |
| `dhl_tracking_number` | tekst | Trackingnummer | Tracking number |
| `dhl_sender` | tekst | Afzender | Sender |
| `dhl_receiver` | tekst | Ontvanger | Receiver |
| `dhl_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `dhl_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `dhl_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `dhl_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `dhl_en_route_pickup_count` | getal | Onderweg naar afhaalpunt | En route to pickup point |
| `dhl_pickup_count` | getal | Klaar om op te halen | Ready for pickup |
| `dhl_pickup_point` | tekst | Afhaalpunt | Pickup point |
| `dhl_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `dhl_outgoing_count` | getal | Verzonden pakketten onderweg | Sent parcels underway |
| `dhl_last_event` | tekst | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | tekst | Verbindingsstatus | Connection status |
| `dhl_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `dhl_new_package` | Nieuw DHL-pakket | New DHL parcel |
| `status_changed` | Zendingstatus is gewijzigd | Shipment status changed |
| `dhl_package_event_changed` | Nieuwe DHL-trackinggebeurtenis | New DHL tracking event |
| `dhl_out_for_delivery` | DHL-pakket onderweg voor bezorging | DHL parcel out for delivery |
| `dhl_ready_for_pickup` | DHL-pakket klaar om op te halen | DHL parcel ready for pickup |
| `shipment_delivered` | Zending is bezorgd | Shipment delivered |
| `dhl_package_problem` | Probleem of retour bij DHL-pakket | DHL parcel has a problem or is returning |
| `dhl_outgoing_status_changed` | Status van verzonden DHL-pakket gewijzigd | Status of sent DHL parcel changed |
| `dhl_outgoing_delivered` | Verzonden DHL-pakket bezorgd | Sent DHL parcel delivered |
| `dhl_delivery_window_changed` | Bezorgvenster bekend of gewijzigd | Delivery window available or changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `is_delivered` | Zending is bezorgd | Shipment is delivered | — |
| `dhl_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |
| `dhl_packages_underway` | Er zijn/zijn geen DHL-pakketten onderweg | DHL parcels are/are not underway | — |
| `dhl_out_for_delivery_now` | Er is een/geen DHL-pakket onderweg voor bezorging | A DHL parcel is/is not out for delivery | — |
| `dhl_ready_for_pickup_now` | Er ligt een/geen DHL-pakket klaar om op te halen | A DHL parcel is/is not ready for pickup | — |
| `dhl_any_status_is` | Een DHL-pakket heeft/heeft niet status… | A DHL parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij DHL) |
| `dhl_parcel_is_delivered` | DHL-pakket… is/is niet bezorgd | DHL parcel… is/is not delivered | Trackingnummer |
| `dhl_is_tracking` | DHL-pakket… wordt wel/niet gevolgd | DHL parcel… is/is not being tracked | Trackingnummer |
| `dhl_outgoing_underway` | Er zijn/zijn geen verzonden DHL-pakketten onderweg | Sent DHL parcels are/are not underway | — |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `refresh_shipment` | Zending vernieuwen | Refresh shipment | — |
| `dhl_track_parcel` | Volg DHL-pakket… | Track DHL parcel… | Trackingnummer; Richting (Inkomend, Uitgaand (door mij verzonden)) |
| `dhl_untrack_parcel` | Stop met volgen van DHL-pakket… | Stop tracking DHL parcel… | Trackingnummer |
| `dhl_remove_delivered` | Verwijder bezorgde DHL-pakketten | Remove delivered DHL parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 25 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | tekst | Trackingnummer | Tracking number |
| `status` | tekst | Status | Status |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | DHL-statustekst | DHL status text |
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
| `service` | tekst | DHL-dienst | DHL service |
| `previous_status` | tekst | Vorige status | Previous status |
| `last_update` | tekst | Laatste update | Last update |
| `delivered` | ja/nee | Bezorgd | Delivered |
| `active_parcels` | getal | Actieve pakketten | Active parcels |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige DHL-statustekst | Previous DHL status text |
| `carrier` | tekst | Vervoerder | Carrier |

</details>

## Beperkingen en tips

* De statusgeschiedenis wordt alleen opgehaald als een status verandert.
* Zonder account worden trackingnummers via DHL's openbare tracking gelezen; afzender en ontvanger zijn dan niet altijd bekend.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
