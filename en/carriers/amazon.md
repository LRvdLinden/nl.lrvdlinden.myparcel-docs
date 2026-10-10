# Amazon

![Amazon](../../media/drivers/amazon/assets/images/large.png)

> **New in v0.3.6** · **Experimental**

**Experimental.** Sign in on Amazon's own page to see the shipments of your orders, with item, delivery carrier, expected delivery date, out for delivery, ready for pickup and delivered.

## At a glance

| | |
|---|---|
| Countries | 🇳🇱 🇧🇪 🇩🇪 🇫🇷 🇬🇧 🇮🇪 🇪🇸 🇮🇹 🇸🇪 🇵🇱 🇺🇸 🇨🇦 🇲🇽 🇧🇷 🇦🇺 🇯🇵 🇮🇳 17 Amazon stores: Netherlands, Belgium, Germany, France, United Kingdom, Ireland, Spain, Italy, Sweden, Poland, United States, Canada, Mexico, Brazil, Australia, Japan and India |
| Connect with | Account |
| Device ID | `amazon` |
| Flow cards | 9 triggers · 6 conditions · 2 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **Amazon** and choose your **Amazon store**.
2. Tap **Open Amazon sign-in** and complete every step Amazon asks for (password, verification code, puzzle or passkey). Password, code and puzzle stay at Amazon.
3. You end on a page that may look blank or show an error – that is expected. Copy the full address from the address bar, paste it into **Address after signing in** and tap **Connect account**.
4. Homey only keeps a sign-in token. You can remove access at any time under **Manage Your Content and Devices** on Amazon.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| Amazon | **Amazon store** | The Amazon website your orders are placed on. After changing it, run Repair if Amazon asks you to sign in again. (choices: Netherlands, Belgium, Germany, France, United Kingdom, Ireland, Spain, Italy, Sweden, Poland, United States, Canada, Mexico, Brazil, Australia, Japan, India) |
| Amazon | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `amazon_parcel_count` | number | Actieve pakketten | Active parcels |
| `amazon_status` | text | Status | Status |
| `amazon_tracking` | text | Trackingnummer | Tracking number |
| `amazon_item` | text | Artikel | Item |
| `amazon_carrier` | text | Bezorgdienst | Delivery carrier |
| `amazon_delivery_date` | text | Bezorgdatum | Delivery date |
| `amazon_next_delivery` | text | Volgende bezorging | Next delivery |
| `amazon_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `amazon_pickup_count` | number | Klaar om op te halen | Ready for pickup |
| `amazon_delivered_count` | number | Recent bezorgd | Recently delivered |
| `amazon_last_event` | text | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `amazon_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `amazon_new_package` | Nieuw Amazon-pakket | New Amazon parcel |
| `amazon_status_changed` | Status Amazon-pakket gewijzigd | Amazon parcel status changed |
| `amazon_package_event_changed` | Nieuwe Amazon-trackinggebeurtenis | New Amazon tracking event |
| `amazon_out_for_delivery` | Amazon-pakket onderweg voor bezorging | Amazon parcel out for delivery |
| `amazon_ready_for_pickup` | Amazon-pakket klaar om op te halen | Amazon parcel ready for pickup |
| `amazon_delivered` | Amazon-pakket bezorgd | Amazon parcel delivered |
| `amazon_package_problem` | Probleem of retour bij Amazon-pakket | Amazon parcel has a problem or is returning |
| `amazon_delivery_window_changed` | Verwachte Amazon-bezorgdatum gewijzigd | Amazon expected delivery date changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `amazon_packages_underway` | Er zijn/zijn geen Amazon-pakketten onderweg | Amazon parcels are/are not underway | — |
| `amazon_out_for_delivery_now` | Er is een/geen Amazon-pakket onderweg voor bezorging | A Amazon parcel is/is not out for delivery | — |
| `amazon_ready_for_pickup_now` | Er ligt een/geen Amazon-pakket klaar om op te halen | A Amazon parcel is/is not ready for pickup | — |
| `amazon_any_status_is` | Een Amazon-pakket heeft/heeft niet status… | A Amazon parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at Amazon) |
| `amazon_parcel_is_delivered` | Amazon-pakket… is/is niet bezorgd | Amazon parcel… is/is not delivered | Tracking number |
| `amazon_is_tracking` | Amazon-pakket… wordt wel/niet gevolgd | Amazon parcel… is/is not being tracked | Tracking number |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `amazon_refresh` | Vernieuw Amazon | Refresh Amazon | — |
| `amazon_remove_delivered` | Verwijder bezorgde Amazon-pakketten | Remove delivered Amazon parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 24 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | Amazon-statustekst | Amazon status text |
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
| `delivery_carrier` | text | Bezorgdienst | Delivery carrier |
| `order_id` | text | Bestelnummer | Order number |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige Amazon-statustekst | Previous Amazon status text |
| `old_delivery_window` | text | Vorig bezorgvenster | Previous delivery window |

</details>

## Limitations and tips

* **Experimental:** Amazon can change its pages at any time; data may then be missing temporarily.
* **At most 10 shipments are read per poll**; delivered shipments are only read once.
* Each sign-in link only works once. Changed the store, or does Amazon ask you to sign in again? Use **Repair**.
* No delivery window: Amazon only gives an expected delivery date. The *expected delivery date changed* card fires when that date changes.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
