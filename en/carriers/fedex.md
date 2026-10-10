# FedEx

![FedEx](../../media/drivers/fedex/assets/images/large.png)

FedEx shipments through the official **FedEx Track API** with your own API key: FedEx status codes incl. returns, ready for pickup at a FedEx location, delivery window, service, weight, dimensions and status history.

## At a glance

| | |
|---|---|
| Countries | 🌍 Worldwide |
| Connect with | API key |
| Device ID | `fedex` |
| Flow cards | 9 triggers · 6 conditions · 4 actions |

## Connect

1. Create a project on the FedEx Developer Portal with access to the **Track API** and note the **Client ID** and **Client Secret**.
2. Open Homey → **Devices** → **+** → **MyParcel** → **FedEx**.
3. Enter Client ID, Client Secret and the **tracking numbers** (one per line) and tap **Connect FedEx**.
4. MyParcel keeps and renews the OAuth token on its own.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| FedEx API | **Client ID** | — |
| FedEx API | **Client Secret** | (stored hidden) |
| FedEx Track & Trace | **Tracking numbers** | One tracking number per line. |
| FedEx Track & Trace | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `fedex_parcel_count` | number | Pakketten onderweg | Parcels underway |
| `fedex_status` | text | Status | Status |
| `fedex_tracking` | text | Trackingnummer | Tracking number |
| `fedex_sender` | text | Afzender | Sender |
| `fedex_receiver` | text | Ontvanger | Receiver |
| `fedex_delivery_date` | text | Bezorgdatum | Delivery date |
| `fedex_delivery_window` | text | Bezorgvenster | Delivery window |
| `fedex_next_delivery` | text | Volgende bezorging | Next delivery |
| `fedex_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `fedex_pickup_count` | number | Klaar om op te halen | Ready for pickup |
| `fedex_pickup_point` | text | Afhaalpunt | Pickup point |
| `fedex_delivered_count` | number | Recent bezorgd | Recently delivered |
| `fedex_last_event` | text | Laatste gebeurtenis | Last event |
| `fedex_service` | text | Dienst | Service |
| `fedex_weight` | text | Gewicht | Weight |
| `fedex_dimensions` | text | Afmetingen | Dimensions |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `fedex_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

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
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `fedex_packages_underway` | Er zijn FedEx-pakketten onderweg | FedEx packages are underway | — |
| `fedex_out_for_delivery_now` | Er is een/geen FedEx-pakket onderweg voor bezorging | A FedEx parcel is/is not out for delivery | — |
| `fedex_ready_for_pickup_now` | Er ligt een/geen FedEx-pakket klaar om op te halen | A FedEx parcel is/is not ready for pickup | — |
| `fedex_any_status_is` | Een FedEx-pakket heeft/heeft niet status… | A FedEx parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at FedEx) |
| `fedex_parcel_is_delivered` | FedEx-pakket… is/is niet bezorgd | FedEx parcel… is/is not delivered | Tracking number |
| `fedex_is_tracking` | FedEx-pakket… wordt wel/niet gevolgd | FedEx parcel… is/is not being tracked | Tracking number |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `fedex_refresh` | Vernieuw FedEx | Refresh FedEx | — |
| `fedex_track_parcel` | Volg FedEx-pakket… | Track FedEx parcel… | Tracking number |
| `fedex_untrack_parcel` | Stop met volgen van FedEx-pakket… | Stop tracking FedEx parcel… | Tracking number |
| `fedex_remove_delivered` | Verwijder bezorgde FedEx-pakketten | Remove delivered FedEx parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 26 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | FedEx-statustekst | FedEx status text |
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
| `weight` | text | Gewicht | Weight |
| `dimensions` | text | Afmetingen | Dimensions |
| `origin` | text | Herkomst | Origin |
| `destination` | text | Bestemming | Destination |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige FedEx-statustekst | Previous FedEx status text |
| `old_delivery_window` | text | Vorig bezorgvenster | Previous delivery window |

</details>

## Limitations and tips

* This device does not work without your own FedEx API credentials; FedEx has no account login for third-party integrations.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
