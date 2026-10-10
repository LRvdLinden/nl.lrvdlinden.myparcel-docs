# DHL Express

![DHL Express](../../media/drivers/dhl-express/assets/images/large.png)

Follow international DHL Express shipments with their air waybill number (10 digits) – no account needed. Optionally combine that with your MyDHL+ account to also see the shipments in that account.

## At a glance

| | |
|---|---|
| Countries | 🌍 Worldwide |
| Connect with | Tracking number · Account |
| Device ID | `dhl-express` |
| Flow cards | 10 triggers · 8 conditions · 4 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **DHL Express**.
2. Enter the **air waybill numbers** (one per line, e.g. `1234567890`; add `out` for a shipment you send yourself) and tap **Track shipments**.
3. Optional: open **Use a MyDHL+ account** and sign in with e-mail address and password (plus a verification code when DHLPass asks for one).
4. If DHLPass blocks the direct login, use the **DHL Express Homey Login Helper** and paste the `DHLEXPRESS1` session code via **Connect with helper code**.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| DHL Express Track & Trace | **Tracking numbers** | One 10-digit air waybill per line – no account needed. Add “out” for a shipment you sent yourself. DHL Express allows about one lookup per 40 minutes, so with several numbers each one is refreshed in turn. |
| DHL Express Track & Trace | **Show delivered parcels for (days)** | (default: 7) |
| MyDHL+ account (optional) | **MyDHL+ web session** | (stored hidden) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `dhl_express_parcel_count` | number | Actieve pakketten | Active parcels |
| `dhl_express_total_count` | number | Totaal pakketten | Total parcels |
| `dhl_express_status` | text | Status | Status |
| `dhl_express_tracking` | text | Trackingnummer | Tracking number |
| `dhl_express_sender` | text | Afzender | Sender |
| `dhl_express_receiver` | text | Ontvanger | Receiver |
| `dhl_express_delivery_date` | text | Bezorgdatum | Delivery date |
| `dhl_express_delivery_window` | text | Bezorgvenster | Delivery window |
| `dhl_express_next_delivery` | text | Volgende bezorging | Next delivery |
| `dhl_express_service` | text | Service | Service |
| `dhl_express_origin` | text | Herkomst | Origin |
| `dhl_express_destination` | text | Bestemming | Destination |
| `dhl_express_pieces` | number | Colli | Pieces |
| `dhl_express_last_event` | text | Laatste gebeurtenis | Last event |
| `dhl_express_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `dhl_express_delivered_count` | number | Recent bezorgd | Recently delivered |
| `dhl_express_delivered` | yes/no | Bezorgd | Delivered |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `dhl_express_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

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
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `dhl_express_packages_underway` | Er zijn DHL Express-pakketten onderweg | DHL Express parcels are underway | — |
| `dhl_express_is_connected` | DHL Express is/is niet verbonden | DHL Express is/isn't connected | — |
| `dhl_express_delivery_window_known` | DHL Express-bezorgvenster is/is niet bekend | DHL Express delivery window is/isn't known | — |
| `dhl_express_out_for_delivery_now` | Er is een/geen DHL Express-pakket onderweg voor bezorging | A DHL Express parcel is/is not out for delivery | — |
| `dhl_express_any_status_is` | Een DHL Express-pakket heeft/heeft niet status… | A DHL Express parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at DHL Express) |
| `dhl_express_parcel_is_delivered` | DHL Express-pakket… is/is niet bezorgd | DHL Express parcel… is/is not delivered | Tracking number |
| `dhl_express_is_tracking` | DHL Express-pakket… wordt wel/niet gevolgd | DHL Express parcel… is/is not being tracked | Tracking number |
| `dhl_express_outgoing_underway` | Er zijn/zijn geen verzonden DHL Express-pakketten onderweg | Sent DHL Express parcels are/are not underway | — |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `dhl_express_refresh` | Vernieuw DHL Express | Refresh DHL Express | — |
| `dhl_express_track_parcel` | Volg DHL Express-pakket… | Track DHL Express parcel… | Tracking number; Direction (Incoming, Outgoing (sent by me)) |
| `dhl_express_untrack_parcel` | Stop met volgen van DHL Express-pakket… | Stop tracking DHL Express parcel… | Tracking number |
| `dhl_express_remove_delivered` | Verwijder bezorgde DHL Express-pakketten | Remove delivered DHL Express parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 30 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `carrier` | text | Vervoerder | Carrier |
| `tracking` | text | Trackingnummer | Tracking number |
| `sender` | text | Afzender | Sender |
| `receiver` | text | Ontvanger | Receiver |
| `status` | text | Status | Status |
| `delivery_date` | text | Bezorgdatum | Delivery date |
| `delivery_window` | text | Bezorgvenster | Delivery window |
| `service` | text | Service | Service |
| `origin` | text | Herkomst | Origin |
| `destination` | text | Bestemming | Destination |
| `last_event` | text | Laatste gebeurtenis | Last event |
| `delivered` | yes/no | Bezorgd | Delivered |
| `active_count` | number | Actieve pakketten | Active parcels |
| `total_count` | number | Totaal pakketten | Total parcels |
| `last_update` | text | Laatste update | Last update |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | DHL Express-statustekst | DHL Express status text |
| `window_start` | text | Begin venster | Window start |
| `window_end` | text | Einde venster | Window end |
| `pickup_point` | text | Afhaalpunt | Pickup point |
| `last_event_time` | text | Tijd laatste gebeurtenis | Last event time |
| `delivered_at` | text | Bezorgd op | Delivered at |
| `direction` | text | Richting | Direction |
| `history` | text | Statusgeschiedenis | Status history |
| `url` | text | Trackinglink | Tracking link |
| `pieces` | number | Colli | Pieces |
| `proof_of_delivery` | text | Afleverbewijs | Proof of delivery |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige DHL Express-statustekst | Previous DHL Express status text |

</details>

## Limitations and tips

* **Rate limit:** DHL Express allows about one lookup per 40 minutes. Several numbers are refreshed in turn (shipments with the courier first) and MyParcel backs off when DHL asks to slow down.
* Not every shipment has a delivery window; that depends on what DHL Express returns.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
