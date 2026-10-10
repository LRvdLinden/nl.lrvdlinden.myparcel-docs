# DHL

![DHL](../../media/drivers/dhl-parcel/assets/images/large.png)

DHL Parcel (eCommerce) in Homey: your My DHL parcels with DHL's own status codes (out for delivery, ready at a ServicePoint/ParcelStation, delivered at neighbours or in the mailbox, returns), the delivery window and status history. An account is optional: plain tracking numbers work too.

## At a glance

| | |
|---|---|
| Countries | 🇳🇱 Netherlands (My DHL account and DHL Parcel tracking numbers) |
| Connect with | Account · Tracking number |
| Device ID | `dhl-parcel` |
| Flow cards | 11 triggers · 9 conditions · 4 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **DHL**.
2. Enter your **My DHL account** (e-mail address and password) to see all your parcels automatically, **or** only enter **tracking numbers** (one per line, e.g. `JJD…` or `3S…`). You can also do both.
3. Optionally add a postal code for the tracking link and `out` for a parcel you send yourself.
4. Tap **Add DHL**. You can add numbers later in the device settings or with a Flow.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| DHL Track & Trace | **Tracking numbers** | One per line. Works without a My DHL account for DHL Parcel numbers (e.g. JJD…, 3S…). Optionally add a postcode for the tracking link, and “out” for a parcel you sent yourself, e.g. 3SABC1234567890 1234AB out. |
| DHL Track & Trace | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `dhl_parcel_count` | number | Actieve pakketten | Active parcels |
| `dhl_status` | text | Status | Status |
| `dhl_tracking_number` | text | Trackingnummer | Tracking number |
| `dhl_sender` | text | Afzender | Sender |
| `dhl_receiver` | text | Ontvanger | Receiver |
| `dhl_delivery_date` | text | Bezorgdatum | Delivery date |
| `dhl_delivery_window` | text | Bezorgvenster | Delivery window |
| `dhl_next_delivery` | text | Volgende bezorging | Next delivery |
| `dhl_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `dhl_en_route_pickup_count` | number | Onderweg naar afhaalpunt | En route to pickup point |
| `dhl_pickup_count` | number | Klaar om op te halen | Ready for pickup |
| `dhl_pickup_point` | text | Afhaalpunt | Pickup point |
| `dhl_delivered_count` | number | Recent bezorgd | Recently delivered |
| `dhl_outgoing_count` | number | Verzonden pakketten onderweg | Sent parcels underway |
| `dhl_last_event` | text | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `dhl_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

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
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `is_delivered` | Zending is bezorgd | Shipment is delivered | — |
| `dhl_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |
| `dhl_packages_underway` | Er zijn/zijn geen DHL-pakketten onderweg | DHL parcels are/are not underway | — |
| `dhl_out_for_delivery_now` | Er is een/geen DHL-pakket onderweg voor bezorging | A DHL parcel is/is not out for delivery | — |
| `dhl_ready_for_pickup_now` | Er ligt een/geen DHL-pakket klaar om op te halen | A DHL parcel is/is not ready for pickup | — |
| `dhl_any_status_is` | Een DHL-pakket heeft/heeft niet status… | A DHL parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at DHL) |
| `dhl_parcel_is_delivered` | DHL-pakket… is/is niet bezorgd | DHL parcel… is/is not delivered | Tracking number |
| `dhl_is_tracking` | DHL-pakket… wordt wel/niet gevolgd | DHL parcel… is/is not being tracked | Tracking number |
| `dhl_outgoing_underway` | Er zijn/zijn geen verzonden DHL-pakketten onderweg | Sent DHL parcels are/are not underway | — |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `refresh_shipment` | Zending vernieuwen | Refresh shipment | — |
| `dhl_track_parcel` | Volg DHL-pakket… | Track DHL parcel… | Tracking number; Direction (Incoming, Outgoing (sent by me)) |
| `dhl_untrack_parcel` | Stop met volgen van DHL-pakket… | Stop tracking DHL parcel… | Tracking number |
| `dhl_remove_delivered` | Verwijder bezorgde DHL-pakketten | Remove delivered DHL parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 25 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | DHL-statustekst | DHL status text |
| `sender` | text | Afzender | Sender |
| `receiver` | text | Ontvanger | Recipient |
| `delivery_date` | text | Bezorgdatum | Delivery date |
| `delivery_window` | text | Bezorgvenster | Delivery window |
| `window_start` | text | Begin venster | Window start |
| `window_end` | text | Einde venster | Window end |
| `pickup_point` | text | Afhaalpunt | Pickup point |
| `last_event` | text | Laatste gebeurtenis | Last event |
| `last_event_time` | text | Tijd laatste gebeurtenis | Last event time |
| `delivered_at` | text | Bezorgd op | Delivered at |
| `direction` | text | Richting | Direction |
| `history` | text | Statusgeschiedenis | Status history |
| `url` | text | Trackinglink | Tracking link |
| `service` | text | DHL-dienst | DHL service |
| `previous_status` | text | Vorige status | Previous status |
| `last_update` | text | Laatste update | Last update |
| `delivered` | yes/no | Bezorgd | Delivered |
| `active_parcels` | number | Actieve pakketten | Active parcels |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige DHL-statustekst | Previous DHL status text |
| `carrier` | text | Vervoerder | Carrier |

</details>

## Limitations and tips

* Status history is only fetched when a status changes.
* Without an account, tracking numbers are read through DHL's public tracking; sender and receiver are not always known then.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
