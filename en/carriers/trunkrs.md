# Trunkrs

![Trunkrs](../../media/drivers/trunkrs/assets/images/large.png)

> **New in v0.3.6**

Trunkrs delivers same-day and in the evening. Follow Trunkrs parcels with their number and the delivery postal code – no account needed. With the Trunkrs delivery window, out for delivery, delivered, history and event texts in your own language.

## At a glance

| | |
|---|---|
| Countries | 🇳🇱 Netherlands |
| Connect with | Tracking number |
| Device ID | `trunkrs` |
| Flow cards | 8 triggers · 5 conditions · 4 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **Trunkrs**.
2. Enter the **delivery postcode** (required, e.g. `1234AB`).
3. Optionally enter the **Trunkrs numbers**, one per line. For a parcel delivered to another address, add its postcode after the number: `419719666 1234AB`.
4. Tap **Add Trunkrs**. You can add numbers later in the device settings or with a Flow.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| Trunkrs Track & Trace | **Delivery postal code** | Dutch postal code of the delivery address (e.g. 1234AB). Trunkrs needs it to show the parcel. |
| Trunkrs Track & Trace | **Tracking numbers** | One tracking number per line. Add a postal code after a number when it differs from the one above (e.g. "419719666 1234AB"). |
| Trunkrs Track & Trace | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `trunkrs_parcel_count` | number | Actieve pakketten | Active parcels |
| `trunkrs_status` | text | Status | Status |
| `trunkrs_tracking` | text | Trackingnummer | Tracking number |
| `trunkrs_sender` | text | Afzender | Sender |
| `trunkrs_receiver` | text | Ontvanger | Receiver |
| `trunkrs_delivery_date` | text | Bezorgdatum | Delivery date |
| `trunkrs_delivery_window` | text | Bezorgvenster | Delivery window |
| `trunkrs_next_delivery` | text | Volgende bezorging | Next delivery |
| `trunkrs_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `trunkrs_delivered_count` | number | Recent bezorgd | Recently delivered |
| `trunkrs_last_event` | text | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `trunkrs_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `trunkrs_new_package` | Nieuw Trunkrs-pakket | New Trunkrs parcel |
| `trunkrs_status_changed` | Status Trunkrs-pakket gewijzigd | Trunkrs parcel status changed |
| `trunkrs_package_event_changed` | Nieuwe Trunkrs-trackinggebeurtenis | New Trunkrs tracking event |
| `trunkrs_out_for_delivery` | Trunkrs-pakket onderweg voor bezorging | Trunkrs parcel out for delivery |
| `trunkrs_delivered` | Trunkrs-pakket bezorgd | Trunkrs parcel delivered |
| `trunkrs_package_problem` | Probleem of retour bij Trunkrs-pakket | Trunkrs parcel has a problem or is returning |
| `trunkrs_delivery_window_changed` | Trunkrs-bezorgtijd gewijzigd | Trunkrs delivery time changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `trunkrs_packages_underway` | Er zijn/zijn geen Trunkrs-pakketten onderweg | Trunkrs parcels are/are not underway | — |
| `trunkrs_out_for_delivery_now` | Er is een/geen Trunkrs-pakket onderweg voor bezorging | A Trunkrs parcel is/is not out for delivery | — |
| `trunkrs_any_status_is` | Een Trunkrs-pakket heeft/heeft niet status… | A Trunkrs parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at Trunkrs) |
| `trunkrs_parcel_is_delivered` | Trunkrs-pakket… is/is niet bezorgd | Trunkrs parcel… is/is not delivered | Tracking number |
| `trunkrs_is_tracking` | Trunkrs-pakket… wordt wel/niet gevolgd | Trunkrs parcel… is/is not being tracked | Tracking number |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `trunkrs_refresh` | Vernieuw Trunkrs | Refresh Trunkrs | — |
| `trunkrs_track_parcel` | Volg Trunkrs-pakket… | Track Trunkrs parcel… | Tracking number |
| `trunkrs_untrack_parcel` | Stop met volgen van Trunkrs-pakket… | Stop tracking Trunkrs parcel… | Tracking number |
| `trunkrs_remove_delivered` | Verwijder bezorgde Trunkrs-pakketten | Remove delivered Trunkrs parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 22 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | Trunkrs-statustekst | Trunkrs status text |
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
| `service` | text | Dienst | Service |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige Trunkrs-statustekst | Previous Trunkrs status text |
| `old_delivery_window` | text | Vorig bezorgvenster | Previous delivery window |

</details>

## Limitations and tips

* Trunkrs only shows a parcel together with the Dutch delivery postcode.
* No account link: only numbers you add are followed.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
