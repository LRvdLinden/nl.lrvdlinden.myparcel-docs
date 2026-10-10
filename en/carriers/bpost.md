# bpost

![bpost](../../media/drivers/bpost/assets/images/large.png)

Your My bpost account in Homey: all incoming and sent parcels, the bpost process steps, the delivery window in Belgian time, stops until you and **Mail Ahead letters**. Without an account you follow barcodes with a postal code.

## At a glance

| | |
|---|---|
| Countries | 🇧🇪 Belgium |
| Connect with | Account · Tracking number |
| Device ID | `bpost` |
| Flow cards | 13 triggers · 9 conditions · 4 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **bpost**.
2. Sign in with the e-mail address and password of **My bpost** and tap **Connect My bpost**. Your password is used once; MyParcel keeps bpost login tokens.
3. **Or** open **Track barcodes without an account**: enter the delivery postal code and the barcodes (one per line, optionally with a different postal code after it) and tap **Track barcodes**.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| My bpost account (optional) | **E-mail address** | — |
| My bpost account (optional) | **Password (only to sign in again)** | MyParcel signs in once and then uses bpost login tokens; the password is not kept. (stored hidden) |
| bpost Track & Trace | **Delivery postal code** | — |
| bpost Track & Trace | **Tracking numbers** | One barcode per line. Add the postal code after the barcode when it differs from the one above, e.g. 323456789012345678 1000. |
| bpost Track & Trace | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `bpost_parcel_count` | number | Actieve pakketten | Active parcels |
| `bpost_total_count` | number | Totaal pakketten | Total parcels |
| `bpost_status` | text | Status | Status |
| `bpost_tracking` | text | Volgend trackingnummer | Next tracking number |
| `bpost_sender` | text | Afzender | Sender |
| `bpost_delivery_date` | text | Verwachte bezorging | Expected delivery |
| `bpost_delivery_window` | text | Bezorgvenster | Delivery window |
| `bpost_delivery_point` | text | Afleverpunt | Delivery point |
| `bpost_weight` | text | Gewicht | Weight |
| `bpost_product` | text | Product | Product |
| `bpost_partner` | text | Bezorgpartner | Delivery partner |
| `bpost_last_event` | text | Laatste gebeurtenis | Last event |
| `bpost_receiver` | text | Ontvanger | Receiver |
| `bpost_next_delivery` | text | Volgende bezorging | Next delivery |
| `bpost_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `bpost_en_route_pickup_count` | number | Onderweg naar afhaalpunt | En route to pickup point |
| `bpost_pickup_count` | number | Klaar om op te halen | Ready for pickup |
| `bpost_delivered_count` | number | Recent bezorgd | Recently delivered |
| `bpost_outgoing_count` | number | Verzonden pakketten onderweg | Sent parcels underway |
| `bpost_dimensions` | text | Afmetingen | Dimensions |
| `bpost_letter_count` | number | Aangekondigde brieven | Letters announced |
| `bpost_last_letter` | text | Laatste brief | Last letter |
| `bpost_account_status` | text | Verbindingsstatus | Connection status |
| `bpost_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `bpost_new_package` | Nieuw bpost-pakket | New bpost package |
| `bpost_status_changed` | bpost-pakketstatus gewijzigd | bpost package status changed |
| `bpost_package_event_changed` | Nieuwe bpost-trackinggebeurtenis | New bpost tracking event |
| `bpost_out_for_delivery` | bpost-pakket onderweg voor bezorging | bpost parcel out for delivery |
| `bpost_ready_for_pickup` | bpost-pakket klaar om op te halen | bpost parcel ready for pickup |
| `bpost_delivered` | bpost-pakket bezorgd | bpost package delivered |
| `bpost_package_problem` | Probleem of retour bij bpost-pakket | bpost parcel has a problem or is returning |
| `bpost_outgoing_status_changed` | Status van verzonden bpost-pakket gewijzigd | Status of sent bpost parcel changed |
| `bpost_outgoing_delivered` | Verzonden bpost-pakket bezorgd | Sent bpost parcel delivered |
| `bpost_delivery_updated` | bpost-bezorginformatie bijgewerkt | bpost delivery information updated |
| `bpost_letter_announced` | bpost-brief aangekondigd (Mail Ahead) | bpost letter announced (Mail Ahead) |
| `bpost_delivery_window_changed` | Bezorgvenster bekend of gewijzigd | Delivery window available or changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `bpost_packages_underway` | Er zijn bpost-pakketten onderweg | bpost packages are underway | — |
| `bpost_account_connected` | My bpost-account is gekoppeld | My bpost account is connected | — |
| `bpost_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |
| `bpost_out_for_delivery_now` | Er is een/geen bpost-pakket onderweg voor bezorging | A bpost parcel is/is not out for delivery | — |
| `bpost_ready_for_pickup_now` | Er ligt een/geen bpost-pakket klaar om op te halen | A bpost parcel is/is not ready for pickup | — |
| `bpost_any_status_is` | Een bpost-pakket heeft/heeft niet status… | A bpost parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at bpost) |
| `bpost_parcel_is_delivered` | bpost-pakket… is/is niet bezorgd | bpost parcel… is/is not delivered | Tracking number |
| `bpost_is_tracking` | bpost-pakket… wordt wel/niet gevolgd | bpost parcel… is/is not being tracked | Tracking number |
| `bpost_outgoing_underway` | Er zijn/zijn geen verzonden bpost-pakketten onderweg | Sent bpost parcels are/are not underway | — |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `bpost_refresh` | Vernieuw bpost | Refresh bpost | — |
| `bpost_track_parcel` | Volg bpost-pakket… | Track bpost parcel… | Tracking number |
| `bpost_untrack_parcel` | Stop met volgen van bpost-pakket… | Stop tracking bpost parcel… | Tracking number |
| `bpost_remove_delivered` | Verwijder bezorgde bpost-pakketten | Remove delivered bpost parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 31 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `sender` | text | Afzender | Sender |
| `delivery_date` | text | Verwachte bezorging | Expected delivery |
| `delivery_window` | text | Bezorgvenster | Delivery window |
| `delivery_point` | text | Afleverpunt | Delivery point |
| `weight` | text | Gewicht (g) | Weight (g) |
| `product` | text | Product | Product |
| `partner` | text | Bezorgpartner | Delivery partner |
| `last_event` | text | Laatste gebeurtenis | Last event |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | bpost-statustekst | bpost status text |
| `receiver` | text | Ontvanger | Recipient |
| `window_start` | text | Begin venster | Window start |
| `window_end` | text | Einde venster | Window end |
| `pickup_point` | text | Afhaalpunt | Pickup point |
| `last_event_time` | text | Tijd laatste gebeurtenis | Last event time |
| `delivered_at` | text | Bezorgd op | Delivered at |
| `direction` | text | Richting | Direction |
| `history` | text | Statusgeschiedenis | Status history |
| `url` | text | Trackinglink | Tracking link |
| `dimensions` | text | Afmetingen | Dimensions |
| `stops` | number | Stops tot jou | Stops until you |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige bpost-statustekst | Previous bpost status text |
| `old_delivery_window` | text | Vorig bezorgvenster | Previous delivery window |
| `date` | text | Bezorgdatum | Delivery date |
| `image_url` | text | Afbeeldingslink | Image link |
| `letter_count` | number | Aangekondigde brieven | Letters announced |
| `carrier` | text | Vervoerder | Carrier |

</details>

## Limitations and tips

* Mail Ahead letters and sent parcels are only available with a My bpost account.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
