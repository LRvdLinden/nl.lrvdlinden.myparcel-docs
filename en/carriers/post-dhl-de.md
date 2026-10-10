# Post & DHL Germany

![Post & DHL Germany](../../media/drivers/post-dhl-de/assets/images/large.png)

Your DHL parcels in Germany with DHL's progress ladder (announced, in transit, out for delivery, delivered), Packstation pickups with the Packstation address, returns, sent parcels and Deutsche Post letters. With the **DHL Parcels (Germany)** and **Deutsche Post Mail** widgets.

## At a glance

| | |
|---|---|
| Countries | 🇩🇪 Germany |
| Connect with | Account · Tracking number |
| Device ID | `post-dhl-de` |
| Flow cards | 11 triggers · 8 conditions · 4 actions |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **Post & DHL Germany**.
2. **Post & DHL app login (works from any country):** tap **Open DHL login**, sign in and after the redirect copy the complete address from the address bar back into the screen (**Address after signing in**). Tap **Connect**.
3. **DHL.de login (only from Germany):** tap **Open DHL.de login**, sign in and copy the `dhllogin://…` address (browser developer tools → Network). This also lets you follow extra tracking numbers.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| DHL Track & Trace | **Tracking numbers** | Extra DHL Paket tracking numbers, one per line (needs the DHL.de login). Add “out” for a parcel you sent yourself. |
| DHL Track & Trace | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `dhl_de_parcel_count` | number | Actieve pakketten | Active packages |
| `dhl_de_status` | text | Status | Status |
| `dhl_de_tracking` | text | Trackingnummer | Tracking number |
| `dhl_de_sender` | text | Afzender | Sender |
| `dhl_de_delivery_date` | text | Bezorgdatum | Delivery date |
| `dhl_de_delivery_window` | text | Bezorgvenster | Delivery window |
| `dhl_de_next_delivery` | text | Volgende bezorging | Next delivery |
| `dhl_de_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `dhl_de_pickup_count` | number | Klaar om op te halen | Ready for pickup |
| `dhl_de_pickup_point` | text | Afhaalpunt | Pickup point |
| `dhl_de_delivered_count` | number | Recent bezorgd | Recently delivered |
| `dhl_de_outgoing_count` | number | Verzonden pakketten onderweg | Sent parcels underway |
| `dhl_de_last_event` | text | Laatste gebeurtenis | Last event |
| `dhl_de_mail_count` | number | Verwachte post | Expected mail |
| `dhl_de_postnumber` | text | Postnummer | Postnumber |
| `dhl_de_account_status` | text | Verbindingsstatus | Connection status |
| `dhl_de_mail_status` | text | Briefaankondiging | Letter announcement |
| `dhl_de_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `dhl_de_new_package` | Nieuw DHL-pakket | New DHL parcel |
| `dhl_de_status_changed` | Status DHL-pakket gewijzigd | DHL parcel status changed |
| `dhl_de_package_event_changed` | Nieuwe DHL-trackinggebeurtenis | New DHL tracking event |
| `dhl_de_out_for_delivery` | DHL-pakket onderweg voor bezorging | DHL parcel out for delivery |
| `dhl_de_ready_for_pickup` | DHL-pakket klaar om op te halen | DHL parcel ready for pickup |
| `dhl_de_delivered` | DHL-pakket bezorgd | DHL parcel delivered |
| `dhl_de_package_problem` | Probleem of retour bij DHL-pakket | DHL parcel has a problem or is returning |
| `dhl_de_outgoing_status_changed` | Status van verzonden DHL-pakket gewijzigd | Status of sent DHL parcel changed |
| `dhl_de_outgoing_delivered` | Verzonden DHL-pakket bezorgd | Sent DHL parcel delivered |
| `dhl_de_delivery_window_changed` | Bezorgvenster bekend of gewijzigd | Delivery window available or changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `dhl_de_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |
| `dhl_de_packages_underway` | Er zijn/zijn geen DHL-pakketten onderweg | DHL parcels are/are not underway | — |
| `dhl_de_out_for_delivery_now` | Er is een/geen DHL-pakket onderweg voor bezorging | A DHL parcel is/is not out for delivery | — |
| `dhl_de_ready_for_pickup_now` | Er ligt een/geen DHL-pakket klaar om op te halen | A DHL parcel is/is not ready for pickup | — |
| `dhl_de_any_status_is` | Een DHL-pakket heeft/heeft niet status… | A DHL parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at Post & DHL Germany) |
| `dhl_de_parcel_is_delivered` | DHL-pakket… is/is niet bezorgd | DHL parcel… is/is not delivered | Tracking number |
| `dhl_de_is_tracking` | DHL-pakket… wordt wel/niet gevolgd | DHL parcel… is/is not being tracked | Tracking number |
| `dhl_de_outgoing_underway` | Er zijn/zijn geen verzonden DHL-pakketten onderweg | Sent DHL parcels are/are not underway | — |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `dhl_de_refresh` | Vernieuw Post & DHL | Refresh Post & DHL | — |
| `dhl_de_track_parcel` | Volg DHL-pakket… | Track DHL parcel… | Tracking number; Direction (Incoming, Outgoing (sent by me)) |
| `dhl_de_untrack_parcel` | Stop met volgen van DHL-pakket… | Stop tracking DHL parcel… | Tracking number |
| `dhl_de_remove_delivered` | Verwijder bezorgde DHL-pakketten | Remove delivered DHL parcels | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 21 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | Post & DHL Germany-statustekst | Post & DHL Germany status text |
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
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige Post & DHL Germany-statustekst | Previous Post & DHL Germany status text |
| `carrier` | text | Vervoerder | Carrier |

</details>

## Limitations and tips

* The DHL.de login only works from a German internet connection; extra tracking numbers need that login.
* A sign-in link only works once; open the login again if connecting fails.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
