# Flow-tokens

MyParcel kent drie soorten tokens:

1. **Kaart-tokens** – meegegeven door een *Wanneer*-kaart (bijv. *Status*, *Afzender*, *Bezorgvenster*). Ze bestaan alleen in de Flow die door díe kaart is gestart.
2. **Globale PostNL-tokens** – per PostNL-apparaat, beschikbaar in élke Flow (ook de afbeeldingen **Pakketafbeelding** en **Scan laatste poststuk**).
3. **Globale MyParcel-bezorgtokens** – de eerstvolgende actieve bezorging over alle vervoerders heen.

> **Tip:** gebruik je in een Advanced Flow een token van kaart A in een blok dat ook door kaart B gestart kan worden, dan meldt Homey *Missing token value*. Gebruik één trigger-kaart per actieketen, of een globaal token. Zie [Problemen oplossen](troubleshooting.md#missing-token-value).

## Globale PostNL-tokens

Elk PostNL-apparaat maakt deze tokens aan als *&lt;apparaatnaam&gt; · &lt;titel&gt;*. De afbeeldingstokens werken in elke Flow, welke kaart de Flow ook startte.

| Token | Type | Nederlands | English |
|---|---|---|---|
| `mail_expected` | ja/nee | Post verwacht | Mail expected |
| `mail_count` | getal | Poststukken | Mail items |
| `mail_id` | tekst | Laatste poststuk-ID | Latest mail item ID |
| `mail_title` | tekst | Laatste poststuk | Latest mail item |
| `mail_sender` | tekst | Afzender laatste poststuk | Latest mail sender |
| `mail_date` | tekst | Bezorgdatum laatste poststuk | Latest mail delivery date |
| `mail_unread` | ja/nee | Laatste poststuk ongelezen | Latest mail unread |
| `package_count` | getal | Pakketten onderweg | Parcels underway |
| `package_id` | tekst | Huidig pakket-ID | Current parcel ID |
| `package_sender` | tekst | Afzender pakket | Parcel sender |
| `package_receiver` | tekst | Ontvanger pakket | Parcel receiver |
| `package_title` | tekst | Pakket | Parcel |
| `package_barcode` | tekst | Barcode pakket | Parcel barcode |
| `package_status` | tekst | Pakketstatus | Parcel status |
| `package_status_raw` | tekst | Officiële PostNL-status | Official PostNL status |
| `package_status_code` | tekst | Officiële PostNL-statuscode | Official PostNL status code |
| `package_status_event` | tekst | Laatste PostNL-statusgebeurtenis | Latest PostNL status event |
| `package_status_event_time` | tekst | Tijdstip laatste PostNL-status | Latest PostNL status time |
| `package_delivery_date` | tekst | Bezorgdatum pakket | Parcel delivery date |
| `package_delivery_window` | tekst | Bezorgvenster pakket | Parcel delivery window |
| `package_delivery_window_from` | tekst | Bezorgvenster pakket vanaf | Parcel delivery window from |
| `package_delivery_window_to` | tekst | Bezorgvenster pakket tot | Parcel delivery window to |
| `package_delivery_window_type` | tekst | Type bezorgvenster pakket | Parcel delivery window type |
| `package_details_url` | tekst | Tracking-URL pakket | Parcel tracking URL |
| `package_shipment_type` | tekst | Zendingstype pakket | Parcel shipment type |
| `package_delivery_address_type` | tekst | Type bezorgadres pakket | Parcel delivery address type |
| `package_direction` | tekst | Richting pakket | Parcel direction |
| `package_created_at` | tekst | Pakket aangemaakt op | Parcel created at |
| `package_delivered` | ja/nee | Pakket bezorgd | Parcel delivered |
| `package_shared_from` | tekst | Pakket gedeeld via | Parcel shared from |
| `package_source_account_id` | tekst | Bronaccount-ID pakket | Parcel source account ID |
| `package_tracking` | tekst | Trackingnummer pakket | Parcel tracking number |
| `package_weight` | tekst | Gewicht pakket | Parcel weight |
| `package_weight_kg` | getal | Gewicht pakket (kg) | Parcel weight (kg) |
| `package_dimensions` | tekst | Afmetingen pakket | Parcel dimensions |
| `package_dimension_length` | getal | Lengte pakket (cm) | Parcel length (cm) |
| `package_dimension_width` | getal | Breedte pakket (cm) | Parcel width (cm) |
| `package_dimension_height` | getal | Hoogte pakket (cm) | Parcel height (cm) |
| `package_status_history` | tekst | Volledige pakketstatusgeschiedenis | Full parcel status history |
| `package_observation_code` | tekst | PostNL-observatiecode | PostNL observation code |
| `package_canonical_status` | tekst | Canonieke pakketstatus | Canonical parcel status |
| `package_pickup` | ja/nee | Bezorging bij PostNL-punt | PostNL Point delivery |
| `package_pickup_point` | tekst | PostNL-punt | PostNL Point |
| `next_delivery` | tekst | Volgende bezorging | Next delivery |
| `connection_status` | tekst | PostNL-verbindingsstatus | PostNL connection status |
| `last_update` | tekst | Laatste PostNL-update | Last PostNL update |
| `old_status` | tekst | Vorige pakketstatus | Previous parcel status |
| `last_error` | tekst | Laatste PostNL-fout | Last PostNL error |
| `last_trigger` | tekst | Laatste PostNL-trigger | Last PostNL trigger |
| `last_trigger_time` | tekst | Tijdstip laatste PostNL-trigger | Last PostNL trigger time |
| `package_image` | afbeelding | **Pakketafbeelding** | **Parcel image** |
| `mail_image` | afbeelding | **Scan laatste poststuk** | **Latest mail scan** |

## Globale MyParcel-bezorgtokens

Deze tokens tonen de eerstvolgende actieve bezorging van alle MyParcel-vervoerders samen. De titel volgt de taal van Homey.

| Token | Type | Nederlands | English |
|---|---|---|---|
| `myparcel_delivery_image` | afbeelding | MyParcel bezorging afbeelding | MyParcel delivery image |
| `myparcel_delivery_carrier` | tekst | Bezorgvervoerder | Delivery carrier |
| `myparcel_delivery_status` | tekst | Bezorgstatus | Delivery status |
| `myparcel_delivery_sender` | tekst | Afzender bezorging | Delivery sender |
| `myparcel_delivery_tracking` | tekst | Trackingnummer bezorging | Delivery tracking number |
| `myparcel_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `myparcel_delivery_window` | tekst | Bezorgvenster | Delivery window |

## Kaart-tokens per vervoerder

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

### PostNL

<details>
<summary>Toon alle 50 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `count` | getal | Aantal poststukken |
| `id` | tekst | Poststuk-ID |
| `title` | tekst | Poststuk |
| `sender` | tekst | Afzender (indien beschikbaar) |
| `date` | tekst | Bezorgdatum |
| `unread` | ja/nee | Ongelezen |
| `image_available` | ja/nee | Afbeelding beschikbaar |
| `image` | afbeelding | Afbeelding poststuk |
| `receiver` | tekst | Ontvanger |
| `barcode` | tekst | Barcode |
| `status` | tekst | Status |
| `status_raw` | tekst | Officiële PostNL-status |
| `status_code` | tekst | Officiële PostNL-statuscode |
| `status_event` | tekst | Laatste PostNL-gebeurtenis |
| `status_event_time` | tekst | Laatste statusupdate |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `delivery_window_from` | tekst | Bezorgvenster vanaf |
| `delivery_window_to` | tekst | Bezorgvenster tot |
| `delivery_window_type` | tekst | Type bezorgvenster |
| `details_url` | tekst | Tracking-URL |
| `shipment_type` | tekst | Zendingstype |
| `delivery_address_type` | tekst | Type bezorgadres |
| `direction` | tekst | Richting |
| `created_at` | tekst | Aangemaakt op |
| `delivered` | ja/nee | Bezorgd |
| `shared_from` | tekst | Gedeeld via |
| `source_account_id` | tekst | Bronaccount-ID |
| `package_status_text` | tekst | Pakketstatus |
| `package_window_text` | tekst | Tekst bezorgvenster |
| `package_delivery_date` | tekst | Bezorgdatum pakket |
| `package_sender` | tekst | Afzender pakket |
| `package_tracking` | tekst | Trackingnummer pakket |
| `package_image_available` | ja/nee | Afbeelding Mijn Bezorging beschikbaar |
| `package_image` | afbeelding | Afbeelding Mijn Bezorging |
| `weight` | tekst | Gewicht |
| `dimensions` | tekst | Afmetingen |
| `weight_kg` | getal | Gewicht pakket (kg) |
| `dimension_length` | getal | Lengte pakket (cm) |
| `dimension_width` | getal | Breedte pakket (cm) |
| `dimension_height` | getal | Hoogte pakket (cm) |
| `status_history` | tekst | Volledige statusgeschiedenis |
| `observation_code` | tekst | PostNL-observatiecode |
| `canonical_status` | tekst | Canonieke pakketstatus |
| `pickup` | ja/nee | Bezorging bij PostNL-punt |
| `pickup_point` | tekst | PostNL-punt |
| `old_status` | tekst | Vorige status |
| `error` | tekst | Foutmelding |
| `old_delivery_window` | tekst | Vorig bezorgvenster |
| `old_event` | tekst | Vorige PostNL-gebeurtenis |

</details>

### DHL

<details>
<summary>Toon alle 25 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | DHL-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `service` | tekst | DHL-dienst |
| `previous_status` | tekst | Vorige status |
| `last_update` | tekst | Laatste update |
| `delivered` | ja/nee | Bezorgd |
| `active_parcels` | getal | Actieve pakketten |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige DHL-statustekst |
| `carrier` | tekst | Vervoerder |

</details>

### DHL Express

<details>
<summary>Toon alle 30 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `carrier` | tekst | Vervoerder |
| `tracking` | tekst | Trackingnummer |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `status` | tekst | Status |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `service` | tekst | Service |
| `origin` | tekst | Herkomst |
| `destination` | tekst | Bestemming |
| `last_event` | tekst | Laatste gebeurtenis |
| `delivered` | ja/nee | Bezorgd |
| `active_count` | getal | Actieve pakketten |
| `total_count` | getal | Totaal pakketten |
| `last_update` | tekst | Laatste update |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | DHL Express-statustekst |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `pieces` | getal | Colli |
| `proof_of_delivery` | tekst | Afleverbewijs |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige DHL Express-statustekst |

</details>

### DPD

<details>
<summary>Toon alle 26 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `delivery_point` | tekst | Bezorgpunt |
| `weight` | tekst | Gewicht |
| `dimensions` | tekst | Afmetingen |
| `delivery_type` | tekst | Type bezorging |
| `last_event` | tekst | Laatste gebeurtenis |
| `direction` | tekst | Richting |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | DPD-statustekst |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `delivered_at` | tekst | Bezorgd op |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `country` | tekst | Land |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige DPD-statustekst |
| `carrier` | tekst | Vervoerder |
| `old_delivery_window` | tekst | Vorig bezorgvenster |

</details>

### UPS

<details>
<summary>Toon alle 14 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `sender` | tekst | Afzender |
| `delivery_date` | tekst | Verwachte bezorging |
| `delivery_window` | tekst | Bezorgvenster |
| `service` | tekst | UPS-service |
| `ship_from` | tekst | Verzonden vanaf |
| `ship_to` | tekst | Bestemming |
| `access_point` | tekst | UPS Access Point |
| `last_event` | tekst | Laatste gebeurtenis |
| `previous_status` | tekst | Vorige status |
| `carrier` | tekst | Vervoerder |
| `window_start` | tekst | Start bezorgvenster |
| `window_end` | tekst | Einde bezorgvenster |

</details>

### Budbee

<details>
<summary>Toon alle 22 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | Budbee-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `pickup_deadline` | tekst | Ophalen vóór |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige Budbee-statustekst |
| `carrier` | tekst | Vervoerder |

</details>

### Vinted Go

<details>
<summary>Toon alle 23 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | Vinted Go-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `item` | tekst | Artikel |
| `pickup_code` | tekst | Ophaalcode |
| `pickup_deadline` | tekst | Ophalen vóór |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige Vinted Go-statustekst |

</details>

### FedEx

<details>
<summary>Toon alle 26 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | FedEx-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `service` | tekst | Dienst |
| `weight` | tekst | Gewicht |
| `dimensions` | tekst | Afmetingen |
| `origin` | tekst | Herkomst |
| `destination` | tekst | Bestemming |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige FedEx-statustekst |
| `old_delivery_window` | tekst | Vorig bezorgvenster |

</details>

### GLS

<details>
<summary>Toon alle 22 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | GLS-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | ParcelShop |
| `weight` | tekst | Gewicht |
| `dimensions` | tekst | Afmetingen |
| `delivered_at` | tekst | Bezorgd op |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `country` | tekst | Land |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige GLS-statustekst |
| `carrier` | tekst | Vervoerder |

</details>

### InPost

<details>
<summary>Toon alle 22 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | InPost-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `pickup_code` | tekst | Ophaalcode |
| `pickup_deadline` | tekst | Ophalen vóór |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige InPost-statustekst |

</details>

### bpost

<details>
<summary>Toon alle 31 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `sender` | tekst | Afzender |
| `delivery_date` | tekst | Verwachte bezorging |
| `delivery_window` | tekst | Bezorgvenster |
| `delivery_point` | tekst | Afleverpunt |
| `weight` | tekst | Gewicht (g) |
| `product` | tekst | Product |
| `partner` | tekst | Bezorgpartner |
| `last_event` | tekst | Laatste gebeurtenis |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | bpost-statustekst |
| `receiver` | tekst | Ontvanger |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `dimensions` | tekst | Afmetingen |
| `stops` | getal | Stops tot jou |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige bpost-statustekst |
| `old_delivery_window` | tekst | Vorig bezorgvenster |
| `date` | tekst | Bezorgdatum |
| `image_url` | tekst | Afbeeldingslink |
| `letter_count` | getal | Aangekondigde brieven |
| `carrier` | tekst | Vervoerder |

</details>

### Royal Mail

<details>
<summary>Toon alle 3 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `previous_status` | tekst | Vorige status |

</details>

### Post & DHL Duitsland

<details>
<summary>Toon alle 21 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | Post & DHL Germany-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige Post & DHL Germany-statustekst |
| `carrier` | tekst | Vervoerder |

</details>

### Ampère

<details>
<summary>Toon alle 27 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `carrier` | tekst | Vervoerder |
| `tracking` | tekst | Trackingnummer |
| `sender` | tekst | Afzender |
| `status` | tekst | Status |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Start bezorgvenster |
| `window_end` | tekst | Einde bezorgvenster |
| `delivered` | ja/nee | Bezorgd |
| `track_url` | tekst | Track & Trace-URL |
| `active_count` | getal | Actieve pakketten |
| `total_count` | getal | Totaal pakketten |
| `last_update` | tekst | Laatste update |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | Ampère-statustekst |
| `receiver` | tekst | Ontvanger |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige Ampère-statustekst |
| `old_delivery_window` | tekst | Vorig bezorgvenster |

</details>

### Trunkrs

<details>
<summary>Toon alle 22 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | Trunkrs-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `service` | tekst | Dienst |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige Trunkrs-statustekst |
| `old_delivery_window` | tekst | Vorig bezorgvenster |

</details>

### Dynalogic

<details>
<summary>Toon alle 21 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | Dynalogic-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `destination` | tekst | Bestemming |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige Dynalogic-statustekst |

</details>

### Dragonfly / Intelcom

<details>
<summary>Toon alle 24 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | Dragonfly / Intelcom-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `service` | tekst | Dienst |
| `country` | tekst | Land |
| `carrier` | tekst | Vervoerder |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige Dragonfly / Intelcom-statustekst |
| `old_delivery_window` | tekst | Vorig bezorgvenster |

</details>

### Mondial Relay

<details>
<summary>Toon alle 22 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | Mondial Relay-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `destination` | tekst | Bestemming |
| `market` | tekst | Land |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige Mondial Relay-statustekst |

</details>

### Amazon

<details>
<summary>Toon alle 24 tokens</summary>

| Token | Type | Titel |
|---|---|---|
| `tracking` | tekst | Trackingnummer |
| `status` | tekst | Status |
| `status_code` | tekst | Statuscode |
| `raw_status` | tekst | Amazon-statustekst |
| `sender` | tekst | Afzender |
| `receiver` | tekst | Ontvanger |
| `delivery_date` | tekst | Bezorgdatum |
| `delivery_window` | tekst | Bezorgvenster |
| `window_start` | tekst | Begin venster |
| `window_end` | tekst | Einde venster |
| `pickup_point` | tekst | Afhaalpunt |
| `last_event` | tekst | Laatste gebeurtenis |
| `last_event_time` | tekst | Tijd laatste gebeurtenis |
| `delivered_at` | tekst | Bezorgd op |
| `direction` | tekst | Richting |
| `history` | tekst | Statusgeschiedenis |
| `url` | tekst | Trackinglink |
| `item` | tekst | Artikel |
| `delivery_carrier` | tekst | Bezorgdienst |
| `order_id` | tekst | Bestelnummer |
| `previous_status` | tekst | Vorige status |
| `old_status_code` | tekst | Vorige statuscode |
| `old_event` | tekst | Vorige Amazon-statustekst |
| `old_delivery_window` | tekst | Vorig bezorgvenster |

</details>

[Flow-kaarten](flows.md) · [Apparaatgegevens](device.md) · [Flow-voorbeelden](examples.md)
