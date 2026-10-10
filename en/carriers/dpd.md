# DPD

![DPD](../../media/drivers/dpd/assets/images/large.png)

Your myDPD account in Homey (the same account as in the DPD app): incoming and sent parcels with one clear status set (registered, in transit, out for delivery, ready at a ParcelShop, delivered, returning, problem), the Follow My Parcel delivery window, weight, dimensions and the full scan history.

## At a glance

| | |
|---|---|
| Countries | 🇳🇱 🇧🇪 🇩🇪 🇱🇺 🇫🇷 🇨🇭 🇬🇧 🇮🇹 🇵🇹 🇵🇱 🇨🇿 🇸🇰 🇭🇺 🇸🇮 🇭🇷 🇪🇪 🇱🇻 🇱🇹 🇦🇷 Netherlands, Belgium, Germany, Luxembourg, France, Switzerland, United Kingdom, Italy (BRT), Portugal, Poland, Czech Republic, Slovakia, Hungary, Slovenia, Croatia, Estonia, Latvia, Lithuania and Argentina |
| Connect with | Account |
| Device ID | `dpd` |
| Flow cards | 12 triggers · 7 conditions · 1 action |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **DPD**.
2. Choose your **country**.
3. Sign in with the e-mail address and password of your **myDPD account** and tap **Connect**.
4. **Poland:** enter your mobile number, tap **Send SMS code** and then **Verify and connect**. Homey only keeps a renewable token, never the code.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| DPD account | **Country** | Changing the country? Use “Repair” on the device to sign in for that country. (choices: Netherlands, Belgium, Germany, Luxembourg, France, Switzerland, United Kingdom, Italy (BRT), Portugal, Poland, Czech Republic, Slovakia, Hungary, Slovenia, Croatia, Estonia, Latvia, Lithuania, Argentina) |
| DPD account | **E-mail address** | — |
| DPD account | **Password** | (stored hidden) |
| DPD account | **Mobile number (Poland only)** | — |
| DPD account | **Show delivered parcels for (days)** | (default: 7) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `dpd_parcel_count` | number | Actieve pakketten | Active parcels |
| `dpd_total_count` | number | Totaal pakketten | Total parcels |
| `dpd_status` | text | Status | Status |
| `dpd_tracking` | text | Trackingnummer | Tracking number |
| `dpd_sender` | text | Afzender | Sender |
| `dpd_receiver` | text | Ontvanger | Receiver |
| `dpd_delivery_date` | text | Bezorgdatum | Delivery date |
| `dpd_delivery_window` | text | Bezorgvenster | Delivery window |
| `dpd_delivery_point` | text | Bezorgpunt | Delivery point |
| `dpd_weight` | text | Gewicht | Weight |
| `dpd_dimensions` | text | Afmetingen | Dimensions |
| `dpd_delivery_type` | text | Type bezorging | Delivery type |
| `dpd_last_event` | text | Laatste gebeurtenis | Last event |
| `dpd_direction` | text | Richting | Direction |
| `dpd_next_delivery` | text | Volgende bezorging | Next delivery |
| `dpd_out_for_delivery_count` | number | Onderweg voor bezorging | Out for delivery |
| `dpd_en_route_pickup_count` | number | Onderweg naar ParcelShop | En route to ParcelShop |
| `dpd_pickup_count` | number | Klaar om op te halen | Ready for pickup |
| `dpd_delivered_count` | number | Recent bezorgd | Recently delivered |
| `dpd_outgoing_count` | number | Verzonden pakketten onderweg | Sent parcels underway |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `dpd_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `dpd_new_package` | Nieuw DPD-pakket | New DPD package |
| `dpd_status_changed` | DPD-pakketstatus gewijzigd | DPD package status changed |
| `dpd_package_event_changed` | Nieuwe DPD-trackinggebeurtenis | New DPD tracking event |
| `dpd_out_for_delivery` | DPD-pakket onderweg voor bezorging | DPD parcel out for delivery |
| `dpd_delivery_window_changed` | Bezorgvenster bekend of gewijzigd | Delivery window available or changed |
| `dpd_delivery_updated` | DPD-bezorginformatie bijgewerkt | DPD delivery information updated |
| `dpd_ready_for_pickup` | DPD-pakket klaar om op te halen | DPD parcel ready for pickup |
| `dpd_delivered` | DPD-pakket bezorgd | DPD package delivered |
| `dpd_package_problem` | Probleem of retour bij DPD-pakket | DPD parcel has a problem or is returning |
| `dpd_outgoing_status_changed` | Status van verzonden DPD-pakket gewijzigd | Status of sent DPD parcel changed |
| `dpd_outgoing_delivered` | Verzonden DPD-pakket bezorgd | Sent DPD parcel delivered |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `dpd_packages_underway` | Er zijn/zijn geen DPD-pakketten onderweg | DPD parcels are/are not underway | — |
| `dpd_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |
| `dpd_out_for_delivery_now` | Er is een/geen DPD-pakket onderweg voor bezorging | A DPD parcel is/is not out for delivery | — |
| `dpd_ready_for_pickup_now` | Er ligt een/geen DPD-pakket klaar om op te halen | A DPD parcel is/is not ready for pickup | — |
| `dpd_any_status_is` | Een DPD-pakket heeft/heeft niet status… | A DPD parcel has/does not have status… | Status (Registered, In transit, Out for delivery, Ready for pickup, Delivered, Returning to sender, Problem, Not yet known at DPD) |
| `dpd_parcel_is_delivered` | DPD-pakket… is/is niet bezorgd | DPD parcel… is/is not delivered | Tracking number |
| `dpd_outgoing_underway` | Er zijn/zijn geen verzonden DPD-pakketten onderweg | Sent DPD parcels are/are not underway | — |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `dpd_refresh` | Vernieuw DPD | Refresh DPD | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 26 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `sender` | text | Afzender | Sender |
| `receiver` | text | Ontvanger | Receiver |
| `delivery_date` | text | Bezorgdatum | Delivery date |
| `delivery_window` | text | Bezorgvenster | Delivery window |
| `delivery_point` | text | Bezorgpunt | Delivery point |
| `weight` | text | Gewicht | Weight |
| `dimensions` | text | Afmetingen | Dimensions |
| `delivery_type` | text | Type bezorging | Delivery type |
| `last_event` | text | Laatste gebeurtenis | Last event |
| `direction` | text | Richting | Direction |
| `status_code` | text | Statuscode | Status code |
| `raw_status` | text | DPD-statustekst | DPD status text |
| `window_start` | text | Begin venster | Window start |
| `window_end` | text | Einde venster | Window end |
| `delivered_at` | text | Bezorgd op | Delivered at |
| `last_event_time` | text | Tijd laatste gebeurtenis | Last event time |
| `history` | text | Statusgeschiedenis | Status history |
| `url` | text | Trackinglink | Tracking link |
| `country` | text | Land | Country |
| `previous_status` | text | Vorige status | Previous status |
| `old_status_code` | text | Vorige statuscode | Previous status code |
| `old_event` | text | Vorige DPD-statustekst | Previous DPD status text |
| `carrier` | text | Vervoerder | Carrier |
| `old_delivery_window` | text | Vorig bezorgvenster | Previous delivery window |

</details>

## Limitations and tips

* Changed the country? Use **Repair** on the device to sign in for that country.
* The delivery window is only fetched for active incoming parcels.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
