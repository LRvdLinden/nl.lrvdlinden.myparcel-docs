# GLS

![GLS](../../media/drivers/gls/assets/images/large.png)

Follow GLS parcels through GLS' own public tracking – no MyGLS account needed. Just your country, delivery postal code and tracking numbers. Existing devices with a MyGLS business account keep working.

## At a glance

| | |
|---|---|
| Countries | 🇳🇱 🇧🇪 🇩🇪 🇦🇹 🇨🇭 🇱🇺 🇫🇷 🇮🇹 🇩🇰 🇫🇮 🇮🇪 🇵🇱 🇨🇿 🇸🇰 🇭🇺 🇸🇮 🇭🇷 🇷🇸 🇺🇸 🇨🇦 20 countries: Netherlands (with weight, dimensions, delivery window, ParcelShop and history), Belgium, Germany, Austria, Switzerland, Luxembourg, France, Italy, Denmark, Finland, Ireland, Poland, Czech Republic, Slovakia, Hungary, Slovenia, Croatia, Serbia, United States and Canada |
| Connect with | Tracking number |
| Device ID | `gls` |
| Flow cards | 9 triggers · 7 conditions · 4 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **GLS**.
2. Choose your **country** and enter the **delivery postal code** (GLS only shares parcel details with the postal code the parcel is delivered to).
3. Optionally enter **tracking numbers**: one per line, the long parcel number or the short track ID from the GLS e-mail/SMS. Add a different postal code after the number when needed.
4. Tap **Add GLS**. You can add more later in the device settings or with a Flow.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| GLS Track & Trace | **Country** | (choices: Netherlands, Belgium, Germany, Austria, Switzerland, Luxembourg, France, Italy, Denmark, Finland, Ireland, Poland, Czech Republic, Slovakia, Hungary, Slovenia, Croatia, Serbia, United States, Canada) |
| GLS Track & Trace | **Delivery postal code** | The postal code your GLS parcels are delivered to. GLS only shares parcel details for the matching postal code. |
| GLS Track & Trace | **Tracking numbers** | One parcel per line: the long parcel number or the short track ID from the GLS e-mail/SMS. Add a different postal code after the number when needed, e.g. 12345678901 1234AB. |
| GLS Track & Trace | **Remove delivered parcels after (days)** | Delivered parcels stay visible for this many days and are then removed from the list. 0 = keep them. (default: 7) |
| MyGLS business account (optional) | **MyGLS username** | — |
| MyGLS business account (optional) | **MyGLS password** | (stored hidden) |
| MyGLS business account (optional) | **API subscription key** | (stored hidden) |
| MyGLS business account (optional) | **Parcel-list endpoint** | — |
| MyGLS business account (optional) | **Parcel-details endpoint** | — |
| MyGLS business account (optional) | **Automatic discovery days** | (default: 21) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `gls_parcel_count` | number | Pakketten onderweg | Parcels underway |
| `gls_status` | text | Status | Status |
| `gls_next_delivery` | text | Volgende bezorging | Next delivery |
| `gls_delivery_window` | text | Bezorgvenster | Delivery window |
| `gls_tracking` | text | Trackingnummer | Tracking number |
| `gls_sender` | text | Afzender | Sender |
| `gls_receiver` | text | Ontvanger | Recipient |
| `gls_last_event` | text | Laatste gebeurtenis | Last event |
| `gls_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `gls_en_route_pickup_count` | number | Onderweg naar ParcelShop | En route to ParcelShop |
| `gls_pickup_count` | number | Klaar om op te halen | Ready for pickup |
| `gls_pickup_point` | text | ParcelShop | ParcelShop |
| `gls_delivered_count` | number | Recent bezorgd | Recently delivered |
| `gls_weight` | number | Gewicht | Weight |
| `gls_dimensions` | text | Afmetingen | Dimensions |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `gls_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `gls_new_package` | Nieuw GLS-pakket | New GLS parcel |
| `gls_status_changed` | Status GLS-pakket gewijzigd | GLS parcel status changed |
| `gls_package_event_changed` | Nieuwe GLS-trackinggebeurtenis | New GLS tracking event |
| `gls_out_for_delivery` | GLS-pakket onderweg voor bezorging | GLS parcel out for delivery |
| `gls_delivery_window_changed` | Bezorgvenster bekend of gewijzigd | Delivery window available or changed |
| `gls_ready_for_pickup` | GLS-pakket klaar om op te halen | GLS parcel ready for pickup |
| `gls_package_delivered` | GLS-pakket bezorgd | GLS parcel delivered |
| `gls_package_problem` | Probleem of retour bij GLS-pakket | GLS parcel has a problem or is returning |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `gls_packages_underway` | Er zijn/zijn geen GLS-pakketten onderweg | GLS parcels are/are not underway | — |
| `gls_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |
| `gls_out_for_delivery_now` | Er is een/geen GLS-pakket onderweg voor bezorging | A GLS parcel is/is not out for delivery | — |
| `gls_ready_for_pickup_now` | Er ligt een/geen GLS-pakket klaar om op te halen | A GLS parcel is/is not ready for pickup | — |
| `gls_any_status_is` | Een GLS-pakket heeft/heeft niet status… | A GLS parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at GLS) |
| `gls_parcel_is_delivered` | GLS-pakket… is/is niet bezorgd | GLS parcel… is/is not delivered | Tracking number |
| `gls_is_tracking` | GLS-pakket… wordt wel/niet gevolgd | GLS parcel… is/is not being tracked | Tracking number |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `gls_refresh` | Vernieuw GLS | Refresh GLS | — |
| `gls_track_parcel` | Volg GLS-pakket… | Track GLS parcel… | Tracking number |
| `gls_untrack_parcel` | Stop met volgen van GLS-pakket… | Stop tracking GLS parcel… | Tracking number |
| `gls_remove_delivered` | Verwijder bezorgde GLS-pakketten | Remove delivered GLS parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 22 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | GLS-statustekst | GLS status text |
| `sender` | text | Afzender | Sender |
| `receiver` | text | Ontvanger | Recipient |
| `delivery_date` | text | Bezorgdatum | Delivery date |
| `delivery_window` | text | Bezorgvenster | Delivery window |
| `window_start` | text | Begin venster | Window start |
| `window_end` | text | Einde venster | Window end |
| `pickup_point` | text | ParcelShop | ParcelShop |
| `weight` | text | Gewicht | Weight |
| `dimensions` | text | Afmetingen | Dimensions |
| `delivered_at` | text | Bezorgd op | Delivered at |
| `last_event_time` | text | Tijd laatste gebeurtenis | Last event time |
| `history` | text | Statusgeschiedenis | Status history |
| `url` | text | Trackinglink | Tracking link |
| `country` | text | Land | Country |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige GLS-statustekst | Previous GLS status text |
| `carrier` | text | Vervoerder | Carrier |

</details>

## Limitations and tips

* Outside the Netherlands GLS returns fewer details (e.g. no weight/dimensions or delivery window).
* Delivered parcels are not polled again and are removed after the configured number of days (0 = keep).

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
