# Dynalogic

![Dynalogic](../../media/drivers/dynalogic/assets/images/large.png)

> **New in v0.3.6**

Dynalogic delivers large and valuable shipments (e.g. electronics). Follow deliveries with the order number and postcode – no account needed. Statuses come from Dynalogic's own scenario/step/result codes (delivered, out for delivery, problem, returning), with sender, receiver and history.

## At a glance

| | |
|---|---|
| Countries | 🇳🇱 🇧🇪 Netherlands and Belgium |
| Connect with | Tracking number |
| Device ID | `dynalogic` |
| Flow cards | 7 triggers · 5 conditions · 4 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **Dynalogic**.
2. Choose the **country** (Netherlands or Belgium) and enter the **delivery postcode** (required; NL `1234AB`, BE `1000`).
3. Optionally enter the **order numbers**, one per line; add a different postcode after the number.
4. Tap **Add Dynalogic**. You can add order numbers later in the device settings or with a Flow.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| Dynalogic Track & Trace | **Country** | (choices: Netherlands, Belgium) |
| Dynalogic Track & Trace | **Delivery postal code** | Postal code of the delivery address (Netherlands 1234AB, Belgium 1000). Dynalogic needs it to show the order. |
| Dynalogic Track & Trace | **Tracking numbers** | One tracking number per line. Add a postal code after a number when it differs from the one above (e.g. "1234567890 1234AB"). |
| Dynalogic Track & Trace | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `dynalogic_parcel_count` | number | Actieve pakketten | Active parcels |
| `dynalogic_status` | text | Status | Status |
| `dynalogic_tracking` | text | Trackingnummer | Tracking number |
| `dynalogic_sender` | text | Afzender | Sender |
| `dynalogic_receiver` | text | Ontvanger | Receiver |
| `dynalogic_delivery_date` | text | Bezorgdatum | Delivery date |
| `dynalogic_delivery_window` | text | Bezorgvenster | Delivery window |
| `dynalogic_next_delivery` | text | Volgende bezorging | Next delivery |
| `dynalogic_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `dynalogic_delivered_count` | number | Recent bezorgd | Recently delivered |
| `dynalogic_last_event` | text | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `dynalogic_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `dynalogic_new_package` | Nieuw Dynalogic-pakket | New Dynalogic parcel |
| `dynalogic_status_changed` | Status Dynalogic-pakket gewijzigd | Dynalogic parcel status changed |
| `dynalogic_package_event_changed` | Nieuwe Dynalogic-trackinggebeurtenis | New Dynalogic tracking event |
| `dynalogic_out_for_delivery` | Dynalogic-pakket onderweg voor bezorging | Dynalogic parcel out for delivery |
| `dynalogic_delivered` | Dynalogic-pakket bezorgd | Dynalogic parcel delivered |
| `dynalogic_package_problem` | Probleem of retour bij Dynalogic-pakket | Dynalogic parcel has a problem or is returning |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `dynalogic_packages_underway` | Er zijn/zijn geen Dynalogic-pakketten onderweg | Dynalogic parcels are/are not underway | — |
| `dynalogic_out_for_delivery_now` | Er is een/geen Dynalogic-pakket onderweg voor bezorging | A Dynalogic parcel is/is not out for delivery | — |
| `dynalogic_any_status_is` | Een Dynalogic-pakket heeft/heeft niet status… | A Dynalogic parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at Dynalogic) |
| `dynalogic_parcel_is_delivered` | Dynalogic-pakket… is/is niet bezorgd | Dynalogic parcel… is/is not delivered | Tracking number |
| `dynalogic_is_tracking` | Dynalogic-pakket… wordt wel/niet gevolgd | Dynalogic parcel… is/is not being tracked | Tracking number |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `dynalogic_refresh` | Vernieuw Dynalogic | Refresh Dynalogic | — |
| `dynalogic_track_parcel` | Volg Dynalogic-pakket… | Track Dynalogic parcel… | Tracking number |
| `dynalogic_untrack_parcel` | Stop met volgen van Dynalogic-pakket… | Stop tracking Dynalogic parcel… | Tracking number |
| `dynalogic_remove_delivered` | Verwijder bezorgde Dynalogic-pakketten | Remove delivered Dynalogic parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 21 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | Dynalogic-statustekst | Dynalogic status text |
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
| `destination` | text | Bestemming | Destination |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige Dynalogic-statustekst | Previous Dynalogic status text |

</details>

## Limitations and tips

* **No delivery window:** Dynalogic does not provide a structured delivery window (yet). The *Delivery window* capability stays empty and there is no *delivery time changed* card.
* Dynalogic only shows a delivery together with the delivery postcode.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
