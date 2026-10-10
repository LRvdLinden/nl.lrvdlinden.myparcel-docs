# Vinted Go

![Vinted Go](../../media/drivers/homerr/assets/images/large.png)

Vinted Go (formerly Homerr): your parcels per account, including sent parcels, with pickup point, **pickup code** and item name.

## At a glance

| | |
|---|---|
| Countries | 🇳🇱 🇧🇪 🇫🇷 🇪🇸 Netherlands, Belgium, France and the other Vinted Go countries |
| Connect with | Account |
| Device ID | `homerr` |
| Flow cards | 10 triggers · 6 conditions · 2 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **Vinted Go**.
2. Enter the e-mail address linked to your Vinted Go shipments and tap **Send verification link**.
3. Open the verification e-mail and paste the **complete link or token** into the screen.
4. Tap **Connect account**. MyParcel stores a rotating login token, not a password.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| Vinted Go | **E-mail address** | — |
| Vinted Go | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `homerr_parcel_count` | number | Pakketten onderweg | Packages underway |
| `homerr_status` | text | Status | Status |
| `homerr_tracking` | text | Trackingnummer | Tracking number |
| `homerr_item` | text | Artikel | Item |
| `homerr_pickup_count` | number | Klaar om op te halen | Ready for pickup |
| `homerr_en_route_pickup_count` | number | Onderweg naar afhaalpunt | En route to pickup point |
| `homerr_pickup_point` | text | Afhaalpunt | Pickup point |
| `homerr_pickup_code` | text | Ophaalcode | Pickup code |
| `homerr_delivered_count` | number | Recent bezorgd | Recently delivered |
| `homerr_outgoing_count` | number | Verzonden pakketten onderweg | Sent parcels underway |
| `homerr_last_event` | text | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `homerr_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `homerr_new_package` | Nieuw Vinted Go-pakket | New Vinted Go parcel |
| `homerr_package_status_changed` | Vinted Go-pakketstatus gewijzigd | Vinted Go package status changed |
| `homerr_package_event_changed` | Nieuwe Vinted Go-trackinggebeurtenis | New Vinted Go tracking event |
| `homerr_out_for_delivery` | Vinted Go-pakket onderweg voor bezorging | Vinted Go parcel out for delivery |
| `homerr_ready_for_pickup` | Vinted Go-pakket klaar om op te halen | Vinted Go parcel ready for pickup |
| `homerr_delivered` | Vinted Go-pakket bezorgd | Vinted Go parcel delivered |
| `homerr_package_problem` | Probleem of retour bij Vinted Go-pakket | Vinted Go parcel has a problem or is returning |
| `homerr_outgoing_status_changed` | Status van verzonden Vinted Go-pakket gewijzigd | Status of sent Vinted Go parcel changed |
| `homerr_outgoing_delivered` | Verzonden Vinted Go-pakket bezorgd | Sent Vinted Go parcel delivered |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `homerr_packages_underway` | Er zijn Vinted Go-pakketten onderweg | Vinted Go packages are underway | — |
| `homerr_out_for_delivery_now` | Er is een/geen Vinted Go-pakket onderweg voor bezorging | A Vinted Go parcel is/is not out for delivery | — |
| `homerr_ready_for_pickup_now` | Er ligt een/geen Vinted Go-pakket klaar om op te halen | A Vinted Go parcel is/is not ready for pickup | — |
| `homerr_any_status_is` | Een Vinted Go-pakket heeft/heeft niet status… | A Vinted Go parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at Vinted Go) |
| `homerr_parcel_is_delivered` | Vinted Go-pakket… is/is niet bezorgd | Vinted Go parcel… is/is not delivered | Tracking number |
| `homerr_outgoing_underway` | Er zijn/zijn geen verzonden Vinted Go-pakketten onderweg | Sent Vinted Go parcels are/are not underway | — |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `homerr_refresh` | Vernieuw Vinted Go-pakketten | Refresh Vinted Go packages | — |
| `homerr_remove_delivered` | Verwijder bezorgde Vinted Go-pakketten | Remove delivered Vinted Go parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 23 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | Vinted Go-statustekst | Vinted Go status text |
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
| `item` | text | Artikel | Item |
| `pickup_code` | text | Ophaalcode | Pickup code |
| `pickup_deadline` | text | Ophalen vóór | Pick up before |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige Vinted Go-statustekst | Previous Vinted Go status text |

</details>

## Limitations and tips

* A parcel's timeline is only fetched on a change; closed parcels are hidden after they were announced.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
