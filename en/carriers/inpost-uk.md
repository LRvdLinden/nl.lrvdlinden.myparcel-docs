# InPost

![InPost](../../media/drivers/inpost-uk/assets/images/large.png)

Follow InPost parcels (formerly *InPost UK*) with their number, plus optionally your InPost account (Poland/Italy) with your parcels and their **pickup (open) code** for the Paczkomat/locker.

## At a glance

| | |
|---|---|
| Countries | 🇬🇧 🇵🇱 🇮🇹 🇵🇹 🇪🇸 United Kingdom, Poland, Italy, Portugal and Spain (account: Poland and Italy) |
| Connect with | Tracking number · Account |
| Device ID | `inpost-uk` |
| Flow cards | 8 triggers · 6 conditions · 4 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **InPost**.
2. Choose the **country** and enter the **parcel numbers** (one per line). Tap **Track parcels**.
3. Optional (Poland/Italy): open **Use an InPost account**, choose the account country and tap **Open InPost sign-in**. Sign in with your phone number and SMS code.
4. Then copy the full `https://account.inpost-group.com/callback?…` address from the address bar, paste it into **Callback address** and tap **Connect account**.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| InPost Track & Trace | **Country** | (choices: United Kingdom, Poland, Italy, Portugal, Spain) |
| InPost Track & Trace | **Tracking numbers** | One InPost parcel number per line. |
| InPost Track & Trace | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `inpost_uk_parcel_count` | number | Actieve pakketten | Active parcels |
| `inpost_uk_status` | text | Status | Status |
| `inpost_uk_tracking` | text | Trackingnummer | Tracking number |
| `inpost_uk_sender` | text | Afzender | Sender |
| `inpost_uk_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `inpost_uk_pickup_count` | number | Klaar om op te halen | Ready for pickup |
| `inpost_uk_pickup_point` | text | Afhaalpunt | Pickup point |
| `inpost_uk_pickup_code` | text | Ophaalcode | Pickup code |
| `inpost_uk_delivered_count` | number | Recent bezorgd | Recently delivered |
| `inpost_uk_last_event` | text | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `inpost_uk_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `inpost_uk_new_package` | Nieuw InPost UK-pakket | New InPost UK package |
| `inpost_uk_status_changed` | InPost UK-pakketstatus gewijzigd | InPost UK package status changed |
| `inpost_uk_package_event_changed` | Nieuwe InPost-trackinggebeurtenis | New InPost tracking event |
| `inpost_uk_out_for_delivery` | InPost-pakket onderweg voor bezorging | InPost parcel out for delivery |
| `inpost_uk_ready_for_pickup` | InPost-pakket klaar om op te halen | InPost parcel ready for pickup |
| `inpost_uk_delivered` | InPost-pakket bezorgd | InPost parcel delivered |
| `inpost_uk_package_problem` | Probleem of retour bij InPost-pakket | InPost parcel has a problem or is returning |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `inpost_uk_packages_underway` | Er zijn InPost UK-pakketten onderweg | InPost UK packages are underway | — |
| `inpost_uk_out_for_delivery_now` | Er is een/geen InPost-pakket onderweg voor bezorging | A InPost parcel is/is not out for delivery | — |
| `inpost_uk_ready_for_pickup_now` | Er ligt een/geen InPost-pakket klaar om op te halen | A InPost parcel is/is not ready for pickup | — |
| `inpost_uk_any_status_is` | Een InPost-pakket heeft/heeft niet status… | A InPost parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at InPost) |
| `inpost_uk_parcel_is_delivered` | InPost-pakket… is/is niet bezorgd | InPost parcel… is/is not delivered | Tracking number |
| `inpost_uk_is_tracking` | InPost-pakket… wordt wel/niet gevolgd | InPost parcel… is/is not being tracked | Tracking number |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `inpost_uk_refresh` | Vernieuw InPost UK | Refresh InPost UK | — |
| `inpost_uk_track_parcel` | Volg InPost-pakket… | Track InPost parcel… | Tracking number |
| `inpost_uk_untrack_parcel` | Stop met volgen van InPost-pakket… | Stop tracking InPost parcel… | Tracking number |
| `inpost_uk_remove_delivered` | Verwijder bezorgde InPost-pakketten | Remove delivered InPost parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 22 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | InPost-statustekst | InPost status text |
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
| `pickup_code` | text | Ophaalcode | Pickup code |
| `pickup_deadline` | text | Ophalen vóór | Pick up before |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige InPost-statustekst | Previous InPost status text |

</details>

## Limitations and tips

* The account link only works for Poland and Italy; for the other countries you follow parcel numbers.
* A sign-in link only works once; open the sign-in again if connecting fails.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
