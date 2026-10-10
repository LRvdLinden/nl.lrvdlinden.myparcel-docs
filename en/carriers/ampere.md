# Ampère

![Ampère](../../media/drivers/ampere/assets/images/large.png)

Ampère delivers parcels for bol.com. MyParcel reads the status from Ampère's own parcel page through the link in the bol.com e-mail, with delivery window and status history. With the helper, MyParcel finds Ampère parcels in your bol.com account automatically.

## At a glance

| | |
|---|---|
| Countries | 🇳🇱 Netherlands |
| Connect with | Tracking number · Account |
| Device ID | `ampere` |
| Flow cards | 9 triggers · 8 conditions · 4 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **Ampère**.
2. Use the **Bol.com Homey Login Helper**, sign in once at login.bol.com and paste the generated **bol.com session code**. MyParcel then checks your bol.com orders automatically for Ampère deliveries.
3. **Or manually:** paste the **tracking link from the bol.com e-mail** (e.g. `https://link.bol.com/t/…`).
4. Tap **Connect**.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| Ampère Track & Trace | **Tracking links from the bol.com e-mail** | One link per line, e.g. https://link.bol.com/t/… – parcels from your bol.com account are found automatically when the helper code is set. |
| Ampère Track & Trace | **Show delivered parcels for (days)** | (default: 7) |
| bol.com account (helper) | **bol.com session code** | (stored hidden) |
| bol.com account (helper) | **Ampère Track & Trace URL (fallback)** | — |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `ampere_parcel_count` | number | Actieve pakketten | Active parcels |
| `ampere_total_count` | number | Totaal pakketten | Total parcels |
| `ampere_status` | text | Status | Status |
| `ampere_tracking` | text | Trackingnummer | Tracking number |
| `ampere_sender` | text | Afzender | Sender |
| `ampere_delivery_date` | text | Bezorgdatum | Delivery date |
| `ampere_delivery_window` | text | Bezorgvenster | Delivery window |
| `ampere_window_start` | text | Start bezorgvenster | Delivery window start |
| `ampere_window_end` | text | Einde bezorgvenster | Delivery window end |
| `ampere_delivered` | yes/no | Bezorgd | Delivered |
| `ampere_details_url` | text | Track & Trace-URL | Track & Trace URL |
| `ampere_receiver` | text | Ontvanger | Receiver |
| `ampere_next_delivery` | text | Volgende bezorging | Next delivery |
| `ampere_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `ampere_delivered_count` | number | Recent bezorgd | Recently delivered |
| `ampere_last_event` | text | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `ampere_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `ampere_new_package` | Nieuw Ampère-pakket gevonden | New Ampère parcel found |
| `ampere_status_changed` | Status van Ampère-pakket gewijzigd | Ampère parcel status changed |
| `ampere_package_event_changed` | Nieuwe Ampère-trackinggebeurtenis | New Ampère tracking event |
| `ampere_out_for_delivery` | Ampère-pakket onderweg voor bezorging | Ampère parcel out for delivery |
| `ampere_delivered` | Ampère-pakket bezorgd | Ampère parcel delivered |
| `ampere_package_problem` | Probleem of retour bij Ampère-pakket | Ampère parcel has a problem or is returning |
| `ampere_delivery_updated` | Ampère-bezorginformatie bijgewerkt | Ampère delivery information updated |
| `ampere_delivery_window_changed` | Ampère-bezorgvenster bekend of gewijzigd | Ampère delivery window available or changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `ampere_packages_underway` | Er zijn Ampère-pakketten onderweg | Ampère parcels are underway | — |
| `ampere_delivery_window_known` | Ampère-bezorgvenster is/is niet bekend | Ampère delivery window is/isn't known | — |
| `ampere_is_delivered` | Laatste Ampère-pakket is/is niet bezorgd | Latest Ampère parcel is/isn't delivered | — |
| `ampere_is_connected` | Ampère is/is niet verbonden | Ampère is/isn't connected | — |
| `ampere_out_for_delivery_now` | Er is een/geen Ampère-pakket onderweg voor bezorging | A Ampère parcel is/is not out for delivery | — |
| `ampere_any_status_is` | Een Ampère-pakket heeft/heeft niet status… | A Ampère parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at Ampère) |
| `ampere_parcel_is_delivered` | Ampère-pakket… is/is niet bezorgd | Ampère parcel… is/is not delivered | Tracking number |
| `ampere_is_tracking` | Ampère-pakket… wordt wel/niet gevolgd | Ampère parcel… is/is not being tracked | Tracking number |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `ampere_refresh` | Vernieuw Ampère | Refresh Ampère | — |
| `ampere_track_parcel` | Volg Ampère-pakket via bol.com-link… | Track Ampère parcel from bol.com link… | Tracking number |
| `ampere_untrack_parcel` | Stop met volgen van Ampère-pakket… | Stop tracking Ampère parcel… | Tracking number |
| `ampere_remove_delivered` | Verwijder bezorgde Ampère-pakketten | Remove delivered Ampère parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 27 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `carrier` | text | Vervoerder | Carrier |
| `tracking` | text | Trackingnummer | Tracking number |
| `sender` | text | Afzender | Sender |
| `status` | text | Status | Status |
| `delivery_date` | text | Bezorgdatum | Delivery date |
| `delivery_window` | text | Bezorgvenster | Delivery window |
| `window_start` | text | Start bezorgvenster | Delivery window start |
| `window_end` | text | Einde bezorgvenster | Delivery window end |
| `delivered` | yes/no | Bezorgd | Delivered |
| `track_url` | text | Track & Trace-URL | Track & Trace URL |
| `active_count` | number | Actieve pakketten | Active parcels |
| `total_count` | number | Totaal pakketten | Total parcels |
| `last_update` | text | Laatste update | Last update |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | Ampère-statustekst | Ampère status text |
| `receiver` | text | Ontvanger | Recipient |
| `pickup_point` | text | Afhaalpunt | Pickup point |
| `last_event` | text | Laatste gebeurtenis | Last event |
| `last_event_time` | text | Tijd laatste gebeurtenis | Last event time |
| `delivered_at` | text | Bezorgd op | Delivered at |
| `direction` | text | Richting | Direction |
| `history` | text | Statusgeschiedenis | Status history |
| `url` | text | Trackinglink | Tracking link |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige Ampère-statustekst | Previous Ampère status text |
| `old_delivery_window` | text | Vorig bezorgvenster | Previous delivery window |

</details>

## Limitations and tips

* Only Ampère shipments are shown; PostNL 3S shipments and unverified candidates are filtered out.
* When Ampère's session expires, MyParcel silently starts a new one.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
