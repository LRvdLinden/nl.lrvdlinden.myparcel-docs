# Mondial Relay

![Mondial Relay](../../media/drivers/mondial-relay/assets/images/large.png)

> **New in v0.3.6**

Sign in with your Mondial Relay / InPost account to see your incoming and sent parcels automatically, with the latest step of every parcel. Your password never reaches Homey.

## At a glance

| | |
|---|---|
| Countries | 🇫🇷 🇧🇪 🇳🇱 🇪🇸 🇵🇹 France, Belgium, Netherlands, Spain and Portugal |
| Connect with | Account |
| Device ID | `mondial-relay` |
| Flow cards | 9 triggers · 6 conditions · 2 actions |

## Connect

1. Make sure your account has signed in at least once on the Mondial Relay website or app.
2. Open Homey → **Devices** → **+** → **MyParcel** → **Mondial Relay** and choose the **account country**.
3. Tap **Open Mondial Relay sign-in** and sign in with your account.
4. After signing in, the browser ends on an address starting with `https://account.inpost-group.com/callback?code=…` that does not load. That is expected: copy the full address from the address bar, paste it into **Address after signing in** and tap **Connect account**.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| Mondial Relay | **Account country** | (choices: France, Belgium, Netherlands, Spain, Portugal) |
| Mondial Relay | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `mondial_relay_parcel_count` | number | Actieve pakketten | Active parcels |
| `mondial_relay_status` | text | Status | Status |
| `mondial_relay_tracking` | text | Trackingnummer | Tracking number |
| `mondial_relay_sender` | text | Afzender | Sender |
| `mondial_relay_delivery_date` | text | Bezorgdatum | Delivery date |
| `mondial_relay_delivery_window` | text | Bezorgvenster | Delivery window |
| `mondial_relay_next_delivery` | text | Volgende bezorging | Next delivery |
| `mondial_relay_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `mondial_relay_delivered_count` | number | Recent bezorgd | Recently delivered |
| `mondial_relay_outgoing_count` | number | Verzonden pakketten onderweg | Sent parcels underway |
| `mondial_relay_last_event` | text | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `mondial_relay_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `mondial_relay_new_package` | Nieuw Mondial Relay-pakket | New Mondial Relay parcel |
| `mondial_relay_status_changed` | Status Mondial Relay-pakket gewijzigd | Mondial Relay parcel status changed |
| `mondial_relay_package_event_changed` | Nieuwe Mondial Relay-trackinggebeurtenis | New Mondial Relay tracking event |
| `mondial_relay_out_for_delivery` | Mondial Relay-pakket onderweg voor bezorging | Mondial Relay parcel out for delivery |
| `mondial_relay_delivered` | Mondial Relay-pakket bezorgd | Mondial Relay parcel delivered |
| `mondial_relay_package_problem` | Probleem of retour bij Mondial Relay-pakket | Mondial Relay parcel has a problem or is returning |
| `mondial_relay_outgoing_status_changed` | Status van verzonden Mondial Relay-pakket gewijzigd | Status of sent Mondial Relay parcel changed |
| `mondial_relay_outgoing_delivered` | Verzonden Mondial Relay-pakket bezorgd | Sent Mondial Relay parcel delivered |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `mondial_relay_packages_underway` | Er zijn/zijn geen Mondial Relay-pakketten onderweg | Mondial Relay parcels are/are not underway | — |
| `mondial_relay_out_for_delivery_now` | Er is een/geen Mondial Relay-pakket onderweg voor bezorging | A Mondial Relay parcel is/is not out for delivery | — |
| `mondial_relay_any_status_is` | Een Mondial Relay-pakket heeft/heeft niet status… | A Mondial Relay parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at Mondial Relay) |
| `mondial_relay_parcel_is_delivered` | Mondial Relay-pakket… is/is niet bezorgd | Mondial Relay parcel… is/is not delivered | Tracking number |
| `mondial_relay_is_tracking` | Mondial Relay-pakket… wordt wel/niet gevolgd | Mondial Relay parcel… is/is not being tracked | Tracking number |
| `mondial_relay_outgoing_underway` | Er zijn/zijn geen verzonden Mondial Relay-pakketten onderweg | Sent Mondial Relay parcels are/are not underway | — |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `mondial_relay_refresh` | Vernieuw Mondial Relay | Refresh Mondial Relay | — |
| `mondial_relay_remove_delivered` | Verwijder bezorgde Mondial Relay-pakketten | Remove delivered Mondial Relay parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 22 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | Mondial Relay-statustekst | Mondial Relay status text |
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
| `market` | text | Land | Country |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige Mondial Relay-statustekst | Previous Mondial Relay status text |

</details>

## Limitations and tips

* **No reliable status yet:** Mondial Relay does not share a reliable parcel status (yet). Only the **new parcel** and **tracking event** cards fire; the status-based cards (status changed, out for delivery, delivered, problem/returning and the sent-parcel cards) will follow once the status is known.
* Each sign-in link only works once. If connecting fails, open the sign-in page again for a new link.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
