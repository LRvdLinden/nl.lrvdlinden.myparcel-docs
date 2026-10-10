# Flow tokens

MyParcel has three kinds of tokens:

1. **Card tokens** – passed by a *When* card (e.g. *Status*, *Sender*, *Delivery window*). They only exist in the Flow started by *that* card.
2. **Global PostNL tokens** – per PostNL device, available in *every* Flow (including the images **Parcel image** and **Latest mail scan**).
3. **Global MyParcel delivery tokens** – the next active delivery across all carriers.

> **Tip:** if an Advanced Flow uses a token of card A in a block that can also be started by card B, Homey reports *Missing token value*. Use one trigger card per action chain, or a global token. See [Troubleshooting](troubleshooting.md#missing-token-value).

## Global PostNL tokens

Every PostNL device creates these tokens as *&lt;device name&gt; · &lt;title&gt;*. The image tokens work in every Flow, whichever card started it.

| Token | Type | Nederlands | English |
|---|---|---|---|
| `mail_expected` | yes/no | Post verwacht | Mail expected |
| `mail_count` | number | Poststukken | Mail items |
| `mail_id` | text | Laatste poststuk-ID | Latest mail item ID |
| `mail_title` | text | Laatste poststuk | Latest mail item |
| `mail_sender` | text | Afzender laatste poststuk | Latest mail sender |
| `mail_date` | text | Bezorgdatum laatste poststuk | Latest mail delivery date |
| `mail_unread` | yes/no | Laatste poststuk ongelezen | Latest mail unread |
| `package_count` | number | Pakketten onderweg | Parcels underway |
| `package_id` | text | Huidig pakket-ID | Current parcel ID |
| `package_sender` | text | Afzender pakket | Parcel sender |
| `package_receiver` | text | Ontvanger pakket | Parcel receiver |
| `package_title` | text | Pakket | Parcel |
| `package_barcode` | text | Barcode pakket | Parcel barcode |
| `package_status` | text | Pakketstatus | Parcel status |
| `package_status_raw` | text | Officiële PostNL-status | Official PostNL status |
| `package_status_code` | text | Officiële PostNL-statuscode | Official PostNL status code |
| `package_status_event` | text | Laatste PostNL-statusgebeurtenis | Latest PostNL status event |
| `package_status_event_time` | text | Tijdstip laatste PostNL-status | Latest PostNL status time |
| `package_delivery_date` | text | Bezorgdatum pakket | Parcel delivery date |
| `package_delivery_window` | text | Bezorgvenster pakket | Parcel delivery window |
| `package_delivery_window_from` | text | Bezorgvenster pakket vanaf | Parcel delivery window from |
| `package_delivery_window_to` | text | Bezorgvenster pakket tot | Parcel delivery window to |
| `package_delivery_window_type` | text | Type bezorgvenster pakket | Parcel delivery window type |
| `package_details_url` | text | Tracking-URL pakket | Parcel tracking URL |
| `package_shipment_type` | text | Zendingstype pakket | Parcel shipment type |
| `package_delivery_address_type` | text | Type bezorgadres pakket | Parcel delivery address type |
| `package_direction` | text | Richting pakket | Parcel direction |
| `package_created_at` | text | Pakket aangemaakt op | Parcel created at |
| `package_delivered` | yes/no | Pakket bezorgd | Parcel delivered |
| `package_shared_from` | text | Pakket gedeeld via | Parcel shared from |
| `package_source_account_id` | text | Bronaccount-ID pakket | Parcel source account ID |
| `package_tracking` | text | Trackingnummer pakket | Parcel tracking number |
| `package_weight` | text | Gewicht pakket | Parcel weight |
| `package_weight_kg` | number | Gewicht pakket (kg) | Parcel weight (kg) |
| `package_dimensions` | text | Afmetingen pakket | Parcel dimensions |
| `package_dimension_length` | number | Lengte pakket (cm) | Parcel length (cm) |
| `package_dimension_width` | number | Breedte pakket (cm) | Parcel width (cm) |
| `package_dimension_height` | number | Hoogte pakket (cm) | Parcel height (cm) |
| `package_status_history` | text | Volledige pakketstatusgeschiedenis | Full parcel status history |
| `package_observation_code` | text | PostNL-observatiecode | PostNL observation code |
| `package_canonical_status` | text | Canonieke pakketstatus | Canonical parcel status |
| `package_pickup` | yes/no | Bezorging bij PostNL-punt | PostNL Point delivery |
| `package_pickup_point` | text | PostNL-punt | PostNL Point |
| `next_delivery` | text | Volgende bezorging | Next delivery |
| `connection_status` | text | PostNL-verbindingsstatus | PostNL connection status |
| `last_update` | text | Laatste PostNL-update | Last PostNL update |
| `old_status` | text | Vorige pakketstatus | Previous parcel status |
| `last_error` | text | Laatste PostNL-fout | Last PostNL error |
| `last_trigger` | text | Laatste PostNL-trigger | Last PostNL trigger |
| `last_trigger_time` | text | Tijdstip laatste PostNL-trigger | Last PostNL trigger time |
| `package_image` | image | **Pakketafbeelding** | **Parcel image** |
| `mail_image` | image | **Scan laatste poststuk** | **Latest mail scan** |

## Global MyParcel delivery tokens

These tokens show the next active delivery across all MyParcel carriers. The title follows Homey's language.

| Token | Type | Nederlands | English |
|---|---|---|---|
| `myparcel_delivery_image` | image | MyParcel bezorging afbeelding | MyParcel delivery image |
| `myparcel_delivery_carrier` | text | Bezorgvervoerder | Delivery carrier |
| `myparcel_delivery_status` | text | Bezorgstatus | Delivery status |
| `myparcel_delivery_sender` | text | Afzender bezorging | Delivery sender |
| `myparcel_delivery_tracking` | text | Trackingnummer bezorging | Delivery tracking number |
| `myparcel_delivery_date` | text | Bezorgdatum | Delivery date |
| `myparcel_delivery_window` | text | Bezorgvenster | Delivery window |

## Card tokens per carrier

Tokens passed by this carrier's When cards (not every card has every token).

### PostNL

<details>
<summary>Show all 50 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `count` | number | Number of mail items |
| `id` | text | Mail item ID |
| `title` | text | Mail item |
| `sender` | text | Sender (if available) |
| `date` | text | Delivery date |
| `unread` | yes/no | Unread |
| `image_available` | yes/no | Image available |
| `image` | image | Mail item image |
| `receiver` | text | Receiver |
| `barcode` | text | Barcode |
| `status` | text | Status |
| `status_raw` | text | Official PostNL status |
| `status_code` | text | Official PostNL status code |
| `status_event` | text | Latest PostNL event |
| `status_event_time` | text | Latest status update |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `delivery_window_from` | text | Delivery window from |
| `delivery_window_to` | text | Delivery window to |
| `delivery_window_type` | text | Delivery window type |
| `details_url` | text | Tracking URL |
| `shipment_type` | text | Shipment type |
| `delivery_address_type` | text | Delivery address type |
| `direction` | text | Direction |
| `created_at` | text | Created at |
| `delivered` | yes/no | Delivered |
| `shared_from` | text | Shared from |
| `source_account_id` | text | Source account ID |
| `package_status_text` | text | Package status |
| `package_window_text` | text | Delivery window text |
| `package_delivery_date` | text | Package delivery date |
| `package_sender` | text | Package sender |
| `package_tracking` | text | Package tracking number |
| `package_image_available` | yes/no | My delivery image available |
| `package_image` | image | My delivery image |
| `weight` | text | Weight |
| `dimensions` | text | Dimensions |
| `weight_kg` | number | Parcel weight (kg) |
| `dimension_length` | number | Parcel length (cm) |
| `dimension_width` | number | Parcel width (cm) |
| `dimension_height` | number | Parcel height (cm) |
| `status_history` | text | Full status history |
| `observation_code` | text | PostNL observation code |
| `canonical_status` | text | Canonical parcel status |
| `pickup` | yes/no | PostNL Point delivery |
| `pickup_point` | text | PostNL Point |
| `old_status` | text | Previous status |
| `error` | text | Error |
| `old_delivery_window` | text | Previous delivery window |
| `old_event` | text | Previous PostNL event |

</details>

### DHL

<details>
<summary>Show all 25 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | DHL status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `service` | text | DHL service |
| `previous_status` | text | Previous status |
| `last_update` | text | Last update |
| `delivered` | yes/no | Delivered |
| `active_parcels` | number | Active parcels |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous DHL status text |
| `carrier` | text | Carrier |

</details>

### DHL Express

<details>
<summary>Show all 30 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `carrier` | text | Carrier |
| `tracking` | text | Tracking number |
| `sender` | text | Sender |
| `receiver` | text | Receiver |
| `status` | text | Status |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `service` | text | Service |
| `origin` | text | Origin |
| `destination` | text | Destination |
| `last_event` | text | Last event |
| `delivered` | yes/no | Delivered |
| `active_count` | number | Active parcels |
| `total_count` | number | Total parcels |
| `last_update` | text | Last update |
| `status_code` | text | Status code |
| `raw_status` | text | DHL Express status text |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `pieces` | number | Pieces |
| `proof_of_delivery` | text | Proof of delivery |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous DHL Express status text |

</details>

### DPD

<details>
<summary>Show all 26 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `sender` | text | Sender |
| `receiver` | text | Receiver |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `delivery_point` | text | Delivery point |
| `weight` | text | Weight |
| `dimensions` | text | Dimensions |
| `delivery_type` | text | Delivery type |
| `last_event` | text | Last event |
| `direction` | text | Direction |
| `status_code` | text | Status code |
| `raw_status` | text | DPD status text |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `delivered_at` | text | Delivered at |
| `last_event_time` | text | Last event time |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `country` | text | Country |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous DPD status text |
| `carrier` | text | Carrier |
| `old_delivery_window` | text | Previous delivery window |

</details>

### UPS

<details>
<summary>Show all 14 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `sender` | text | Sender |
| `delivery_date` | text | Expected delivery |
| `delivery_window` | text | Delivery window |
| `service` | text | UPS service |
| `ship_from` | text | Ship from |
| `ship_to` | text | Ship to |
| `access_point` | text | UPS Access Point |
| `last_event` | text | Last event |
| `previous_status` | text | Previous status |
| `carrier` | text | Carrier |
| `window_start` | text | Delivery window start |
| `window_end` | text | Delivery window end |

</details>

### Budbee

<details>
<summary>Show all 22 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | Budbee status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `pickup_deadline` | text | Pick up before |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous Budbee status text |
| `carrier` | text | Carrier |

</details>

### Vinted Go

<details>
<summary>Show all 23 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | Vinted Go status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `item` | text | Item |
| `pickup_code` | text | Pickup code |
| `pickup_deadline` | text | Pick up before |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous Vinted Go status text |

</details>

### FedEx

<details>
<summary>Show all 26 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | FedEx status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `service` | text | Service |
| `weight` | text | Weight |
| `dimensions` | text | Dimensions |
| `origin` | text | Origin |
| `destination` | text | Destination |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous FedEx status text |
| `old_delivery_window` | text | Previous delivery window |

</details>

### GLS

<details>
<summary>Show all 22 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | GLS status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | ParcelShop |
| `weight` | text | Weight |
| `dimensions` | text | Dimensions |
| `delivered_at` | text | Delivered at |
| `last_event_time` | text | Last event time |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `country` | text | Country |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous GLS status text |
| `carrier` | text | Carrier |

</details>

### InPost

<details>
<summary>Show all 22 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | InPost status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `pickup_code` | text | Pickup code |
| `pickup_deadline` | text | Pick up before |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous InPost status text |

</details>

### bpost

<details>
<summary>Show all 31 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `sender` | text | Sender |
| `delivery_date` | text | Expected delivery |
| `delivery_window` | text | Delivery window |
| `delivery_point` | text | Delivery point |
| `weight` | text | Weight (g) |
| `product` | text | Product |
| `partner` | text | Delivery partner |
| `last_event` | text | Last event |
| `status_code` | text | Status code |
| `raw_status` | text | bpost status text |
| `receiver` | text | Recipient |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `dimensions` | text | Dimensions |
| `stops` | number | Stops until you |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous bpost status text |
| `old_delivery_window` | text | Previous delivery window |
| `date` | text | Delivery date |
| `image_url` | text | Image link |
| `letter_count` | number | Letters announced |
| `carrier` | text | Carrier |

</details>

### Royal Mail

<details>
<summary>Show all 3 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `previous_status` | text | Previous status |

</details>

### Post & DHL Germany

<details>
<summary>Show all 21 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | Post & DHL Germany status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous Post & DHL Germany status text |
| `carrier` | text | Carrier |

</details>

### Ampère

<details>
<summary>Show all 27 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `carrier` | text | Carrier |
| `tracking` | text | Tracking number |
| `sender` | text | Sender |
| `status` | text | Status |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Delivery window start |
| `window_end` | text | Delivery window end |
| `delivered` | yes/no | Delivered |
| `track_url` | text | Track & Trace URL |
| `active_count` | number | Active parcels |
| `total_count` | number | Total parcels |
| `last_update` | text | Last update |
| `status_code` | text | Status code |
| `raw_status` | text | Ampère status text |
| `receiver` | text | Recipient |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous Ampère status text |
| `old_delivery_window` | text | Previous delivery window |

</details>

### Trunkrs

<details>
<summary>Show all 22 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | Trunkrs status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `service` | text | Service |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous Trunkrs status text |
| `old_delivery_window` | text | Previous delivery window |

</details>

### Dynalogic

<details>
<summary>Show all 21 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | Dynalogic status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `destination` | text | Destination |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous Dynalogic status text |

</details>

### Dragonfly / Intelcom

<details>
<summary>Show all 24 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | Dragonfly / Intelcom status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `service` | text | Service |
| `country` | text | Country |
| `carrier` | text | Carrier |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous Dragonfly / Intelcom status text |
| `old_delivery_window` | text | Previous delivery window |

</details>

### Mondial Relay

<details>
<summary>Show all 22 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | Mondial Relay status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `destination` | text | Destination |
| `market` | text | Country |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous Mondial Relay status text |

</details>

### Amazon

<details>
<summary>Show all 24 tokens</summary>

| Token | Type | Title |
|---|---|---|
| `tracking` | text | Tracking number |
| `status` | text | Status |
| `status_code` | text | Status code |
| `raw_status` | text | Amazon status text |
| `sender` | text | Sender |
| `receiver` | text | Recipient |
| `delivery_date` | text | Delivery date |
| `delivery_window` | text | Delivery window |
| `window_start` | text | Window start |
| `window_end` | text | Window end |
| `pickup_point` | text | Pickup point |
| `last_event` | text | Last event |
| `last_event_time` | text | Last event time |
| `delivered_at` | text | Delivered at |
| `direction` | text | Direction |
| `history` | text | Status history |
| `url` | text | Tracking link |
| `item` | text | Item |
| `delivery_carrier` | text | Delivery carrier |
| `order_id` | text | Order number |
| `previous_status` | text | Previous status |
| `old_status_code` | text | Previous status code |
| `old_event` | text | Previous Amazon status text |
| `old_delivery_window` | text | Previous delivery window |

</details>

[Flow cards](flows.md) · [Device data](device.md) · [Flow examples](examples.md)
