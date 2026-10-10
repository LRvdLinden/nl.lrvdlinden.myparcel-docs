# Royal Mail

![Royal Mail](../../media/drivers/royal-mail/assets/images/large.png)

Royal Mail orders from your **Click & Drop** account (for senders). MyParcel retrieves recent orders automatically; you do not enter tracking numbers.

## At a glance

| | |
|---|---|
| Countries | 🇬🇧 United Kingdom |
| Connect with | API key |
| Device ID | `royal-mail` |
| Flow cards | 3 triggers · 1 condition · 1 action |

## Connect

1. In Royal Mail Click & Drop, create an API integration under **Settings → Integrations → Click & Drop API** and copy its authorisation key.
2. Open Homey → **Devices** → **+** → **MyParcel** → **Royal Mail**.
3. Paste the **Click & Drop API key** and tap **Connect Royal Mail**.

## Settings

| Group | Setting | Explanation |
|---|---|---|
| — | **Click & Drop API key** | (stored hidden) |
| — | **Order history (days)** | (default: 30) |

## Device values (capabilities)

Every value appears on the device in Homey. Not every field is filled for every parcel.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `royal_mail_parcel_count` | number | Actieve pakketten | Active parcels |
| `royal_mail_status` | text | Status | Status |
| `myparcel_connection_status` | text | Verbindingsstatus | Connection status |
| `royal_mail_last_update` | text | Laatste update | Last update |

## Flow cards

### When… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `royal_mail_new_package` | Nieuw Royal Mail-pakket | New Royal Mail package |
| `royal_mail_status_changed` | Royal Mail-pakketstatus gewijzigd | Royal Mail package status changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd | Connection status changed *(applies to all MyParcel devices)* |

### And… (conditions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `royal_mail_packages_underway` | Er zijn Royal Mail-pakketten onderweg | Royal Mail packages are underway | — |

### Then… (actions)

| ID | Nederlands | English | Arguments |
|---|---|---|---|
| `royal_mail_refresh` | Vernieuw Royal Mail | Refresh Royal Mail | — |

## Notable tokens

Tokens passed by this carrier's When cards (not every card has every token).

<details>
<summary>Show all 3 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | text | Trackingnummer | Tracking number |
| `status` | text | Status | Status |
| `previous_status` | text | Vorige status | Previous status |

</details>

## Limitations and tips

* Only for Click & Drop accounts (senders); incoming Royal Mail parcels without Click & Drop are not supported.
* Limited data: parcel count, status and last update.

[← All carriers](README.md) · [Flow cards](../flows.md) · [Flow tokens](../tokens.md) · [Troubleshooting](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
