# Budbee

![Budbee](../../media/drivers/budbee/assets/images/large.png)

Budbee home deliveries and Budbee Boxes. A parcel *delivered in the Box* is ready for pickup, *picked up* means delivered. With ETA as delivery window, pickup deadline, returns/sent parcels and event texts in your own language.

## At a glance

| | |
|---|---|
| Countries | 🇳🇱 🇧🇪 🇸🇪 🇩🇰 🇫🇮 Netherlands, Belgium and the other Budbee countries (tracking through Budbee) |
| Connect with | Tracking number |
| Device ID | `budbee` |
| Flow cards | 11 triggers · 8 conditions · 4 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **Budbee**.
2. Enter your **tracking/order numbers** (one per line, from the shop e-mail or the Budbee link). No account is needed.
3. Tap **Add Budbee device**. You can add numbers later in the device settings or with a Flow.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| Budbee Track & Trace | **Tracking numbers** | One Budbee tracking code per line (from the shop e-mail or the Budbee link). |
| Budbee Track & Trace | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `budbee_parcel_count` | number | Actieve pakketten | Active parcels |
| `budbee_status` | text | Status | Status |
| `budbee_tracking` | text | Trackingnummer | Tracking number |
| `budbee_sender` | text | Afzender | Sender |
| `budbee_delivery_date` | text | Bezorgdatum | Delivery date |
| `budbee_delivery_window` | text | Bezorgvenster | Delivery window |
| `budbee_next_delivery` | text | Volgende bezorging | Next delivery |
| `budbee_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `budbee_en_route_pickup_count` | number | Onderweg naar afhaalpunt | En route to pickup point |
| `budbee_pickup_count` | number | Klaar om op te halen | Ready for pickup |
| `budbee_pickup_point` | text | Afhaalpunt | Pickup point |
| `budbee_delivered_count` | number | Recent bezorgd | Recently delivered |
| `budbee_outgoing_count` | number | Verzonden pakketten onderweg | Sent parcels underway |
| `budbee_last_event` | text | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `budbee_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `budbee_new_package` | Nieuw Budbee-pakket | New Budbee package |
| `budbee_status_changed` | Budbee-pakketstatus gewijzigd | Budbee package status changed |
| `budbee_package_event_changed` | Nieuwe Budbee-trackinggebeurtenis | New Budbee tracking event |
| `budbee_out_for_delivery` | Budbee-pakket onderweg voor bezorging | Budbee parcel out for delivery |
| `budbee_ready_for_pickup` | Budbee-pakket klaar om op te halen | Budbee parcel ready for pickup |
| `budbee_delivered` | Budbee-pakket bezorgd | Budbee parcel delivered |
| `budbee_package_problem` | Probleem of retour bij Budbee-pakket | Budbee parcel has a problem or is returning |
| `budbee_outgoing_status_changed` | Status van verzonden Budbee-pakket gewijzigd | Status of sent Budbee parcel changed |
| `budbee_outgoing_delivered` | Verzonden Budbee-pakket bezorgd | Sent Budbee parcel delivered |
| `budbee_delivery_window_changed` | Bezorgvenster bekend of gewijzigd | Delivery window available or changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `budbee_packages_underway` | Er zijn Budbee-pakketten onderweg | Budbee packages are underway | — |
| `budbee_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |
| `budbee_out_for_delivery_now` | Er is een/geen Budbee-pakket onderweg voor bezorging | A Budbee parcel is/is not out for delivery | — |
| `budbee_ready_for_pickup_now` | Er ligt een/geen Budbee-pakket klaar om op te halen | A Budbee parcel is/is not ready for pickup | — |
| `budbee_any_status_is` | Een Budbee-pakket heeft/heeft niet status… | A Budbee parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at Budbee) |
| `budbee_parcel_is_delivered` | Budbee-pakket… is/is niet bezorgd | Budbee parcel… is/is not delivered | Tracking number |
| `budbee_is_tracking` | Budbee-pakket… wordt wel/niet gevolgd | Budbee parcel… is/is not being tracked | Tracking number |
| `budbee_outgoing_underway` | Er zijn/zijn geen verzonden Budbee-pakketten onderweg | Sent Budbee parcels are/are not underway | — |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `budbee_refresh` | Vernieuw Budbee | Refresh Budbee | — |
| `budbee_track_parcel` | Volg Budbee-pakket… | Track Budbee parcel… | Tracking number |
| `budbee_untrack_parcel` | Stop met volgen van Budbee-pakket… | Stop tracking Budbee parcel… | Tracking number |
| `budbee_remove_delivered` | Verwijder bezorgde Budbee-pakketten | Remove delivered Budbee parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 22 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | Budbee-statustekst | Budbee status text |
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
| `pickup_deadline` | text | Ophalen vóór | Pick up before |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige Budbee-statustekst | Previous Budbee status text |
| `carrier` | text | Vervoerder | Carrier |

</details>

## Limitations and tips

* Budbee has no account link: only numbers you add are followed.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
