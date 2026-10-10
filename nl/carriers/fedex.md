# FedEx

![FedEx](../../media/drivers/fedex/assets/images/large.png)

FedEx-zendingen via de officiële **FedEx Track API** met je eigen API-sleutel: FedEx-statuscodes inclusief retouren, klaar om op te halen bij een FedEx-locatie, bezorgvenster, service, gewicht, afmetingen en statusgeschiedenis.

## In één oogopslag

| | |
|---|---|
| Landen | 🌍 Wereldwijd |
| Koppelen met | API-sleutel |
| Apparaat-ID | `fedex` |
| Flow-kaarten | 9 triggers · 6 condities · 4 acties |

## Koppelen

1. Maak op het FedEx Developer Portal een project aan met toegang tot de **Track API** en noteer de **Client ID** en **Client Secret**.
2. Open Homey → **Apparaten** → **+** → **MyParcel** → **FedEx**.
3. Vul Client ID, Client Secret en de **trackingnummers** (één per regel) in en tik op **FedEx koppelen**.
4. Het OAuth-token wordt door MyParcel zelf bewaard en vernieuwd.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| FedEx API | **Client-ID** | — |
| FedEx API | **Clientgeheim** | (wordt verborgen opgeslagen) |
| FedEx Track & Trace | **Trackingnummers** | Eén trackingnummer per regel. |
| FedEx Track & Trace | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `fedex_parcel_count` | getal | Pakketten onderweg | Parcels underway |
| `fedex_status` | tekst | Status | Status |
| `fedex_tracking` | tekst | Trackingnummer | Tracking number |
| `fedex_sender` | tekst | Afzender | Sender |
| `fedex_receiver` | tekst | Ontvanger | Receiver |
| `fedex_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `fedex_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `fedex_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `fedex_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `fedex_pickup_count` | getal | Klaar om op te halen | Ready for pickup |
| `fedex_pickup_point` | tekst | Afhaalpunt | Pickup point |
| `fedex_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `fedex_last_event` | tekst | Laatste gebeurtenis | Last event |
| `fedex_service` | tekst | Dienst | Service |
| `fedex_weight` | tekst | Gewicht | Weight |
| `fedex_dimensions` | tekst | Afmetingen | Dimensions |
| `myparcel_connection_status` | tekst | Verbindingsstatus | Connection status |
| `fedex_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `fedex_new_package` | Nieuw FedEx-pakket | New FedEx package |
| `fedex_status_changed` | FedEx-pakketstatus gewijzigd | FedEx package status changed |
| `fedex_package_event_changed` | Nieuwe FedEx-trackinggebeurtenis | New FedEx tracking event |
| `fedex_out_for_delivery` | FedEx-pakket onderweg voor bezorging | FedEx parcel out for delivery |
| `fedex_ready_for_pickup` | FedEx-pakket klaar om op te halen | FedEx parcel ready for pickup |
| `fedex_delivered` | FedEx-pakket bezorgd | FedEx parcel delivered |
| `fedex_package_problem` | Probleem of retour bij FedEx-pakket | FedEx parcel has a problem or is returning |
| `fedex_delivery_updated` | FedEx-bezorgtijd gewijzigd | FedEx delivery time changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `fedex_packages_underway` | Er zijn FedEx-pakketten onderweg | FedEx packages are underway | — |
| `fedex_out_for_delivery_now` | Er is een/geen FedEx-pakket onderweg voor bezorging | A FedEx parcel is/is not out for delivery | — |
| `fedex_ready_for_pickup_now` | Er ligt een/geen FedEx-pakket klaar om op te halen | A FedEx parcel is/is not ready for pickup | — |
| `fedex_any_status_is` | Een FedEx-pakket heeft/heeft niet status… | A FedEx parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij FedEx) |
| `fedex_parcel_is_delivered` | FedEx-pakket… is/is niet bezorgd | FedEx parcel… is/is not delivered | Trackingnummer |
| `fedex_is_tracking` | FedEx-pakket… wordt wel/niet gevolgd | FedEx parcel… is/is not being tracked | Trackingnummer |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `fedex_refresh` | Vernieuw FedEx | Refresh FedEx | — |
| `fedex_track_parcel` | Volg FedEx-pakket… | Track FedEx parcel… | Trackingnummer |
| `fedex_untrack_parcel` | Stop met volgen van FedEx-pakket… | Stop tracking FedEx parcel… | Trackingnummer |
| `fedex_remove_delivered` | Verwijder bezorgde FedEx-pakketten | Remove delivered FedEx parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 26 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | tekst | Trackingnummer | Tracking number |
| `status` | tekst | Status | Status |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | FedEx-statustekst | FedEx status text |
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
| `weight` | tekst | Gewicht | Weight |
| `dimensions` | tekst | Afmetingen | Dimensions |
| `origin` | tekst | Herkomst | Origin |
| `destination` | tekst | Bestemming | Destination |
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige FedEx-statustekst | Previous FedEx status text |
| `old_delivery_window` | tekst | Vorig bezorgvenster | Previous delivery window |

</details>

## Beperkingen en tips

* Zonder eigen FedEx API-gegevens werkt dit apparaat niet; FedEx heeft geen accountlogin voor externe koppelingen.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
