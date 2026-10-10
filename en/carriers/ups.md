# UPS

![UPS](../../media/drivers/ups/assets/images/large.png)

UPS shipments in Homey through your UPS account (UPS My Choice dashboard), with service, ship-from and ship-to, Access Point, delivery date and delivery window. Alternatively you can follow plain tracking numbers.

## At a glance

| | |
|---|---|
| Countries | 🌍 Worldwide (country and UPS locale configurable) |
| Connect with | Account · Tracking number |
| Device ID | `ups` |
| Flow cards | 5 triggers · 3 conditions · 1 action |

## Connect

1. Open Homey → **Devices** → **+** → **MyParcel** → **UPS**.
2. Choose **country** and **language**.
3. Sign in to UPS with the **UPS Token Helper**, open the UPS dashboard, wait until the helper reports that the web session is ready and paste the `web_session` pairing value into **UPS login callback**. Tap **Connect UPS**.
4. **Manual fallback:** enter tracking numbers and tap **Add tracking numbers**.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| — | **Country code** | — |
| — | **UPS locale** | — |
| — | **UPS login callback** | (stored hidden) |
| — | **UPS authorization code** | (stored hidden) |
| — | **UPS OAuth state** | (stored hidden) |
| — | **UPS access/session token** | (stored hidden) |
| — | **UPS refresh token** | (stored hidden) |
| — | **Manual fallback tracking numbers** | — |
| — | **UPS web session** | (stored hidden) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `ups_parcel_count` | number | Actieve pakketten | Active parcels |
| `ups_total_count` | number | Totaal pakketten | Total packages |
| `ups_status` | text | Status | Status |
| `ups_tracking` | text | Volgend trackingnummer | Next tracking number |
| `ups_sender` | text | Afzender | Sender |
| `ups_delivery_date` | text | Verwachte bezorging | Expected delivery |
| `ups_delivery_window` | text | Bezorgvenster | Delivery window |
| `ups_service` | text | UPS-service | UPS service |
| `ups_ship_from` | text | Verzonden vanaf | Ship from |
| `ups_ship_to` | text | Bestemming | Ship to |
| `ups_access_point` | text | UPS Access Point | UPS Access Point |
| `ups_last_event` | text | Laatste gebeurtenis | Last event |
| `ups_country` | text | UPS-land | UPS country |
| `ups_locale` | text | UPS-locale | UPS locale |
| `ups_account_status` | text | Verbindingsstatus | Connection status |
| `ups_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `ups_new_package` | Nieuw UPS-pakket | New UPS package |
| `ups_status_changed` | UPS-pakketstatus gewijzigd | UPS package status changed |
| `ups_delivered` | UPS-pakket bezorgd | UPS package delivered |
| `ups_delivery_window_changed` | Bezorgvenster bekend of gewijzigd | Delivery window available or changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `ups_packages_underway` | Er zijn UPS-pakketten onderweg | UPS packages are underway | — |
| `ups_account_connected` | UPS-account is gekoppeld | UPS account is connected | — |
| `ups_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `ups_refresh` | Vernieuw UPS | Refresh UPS | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 14 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `sender` | text | Afzender | Sender |
| `delivery_date` | text | Verwachte bezorging | Expected delivery |
| `delivery_window` | text | Bezorgvenster | Delivery window |
| `service` | text | UPS-service | UPS service |
| `ship_from` | text | Verzonden vanaf | Ship from |
| `ship_to` | text | Bestemming | Ship to |
| `access_point` | text | UPS Access Point | UPS Access Point |
| `last_event` | text | Laatste gebeurtenis | Last event |
| `previous_status` | text | Vorige status | Previous status |
| `carrier` | text | Vervoerder | Carrier |
| `window_start` | text | Start bezorgvenster | Delivery window start |
| `window_end` | text | Einde bezorgvenster | Delivery window end |

</details>

## Limitations and tips

* UPS has fewer Flow cards than the rebuilt carriers (for now): new parcel, status changed, delivered and delivery window.
* The UPS web session can expire; then use **Repair** with a new helper value.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
