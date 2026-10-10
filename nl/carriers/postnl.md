# PostNL

![PostNL](../../media/drivers/postnl/assets/images/large.png)

Je PostNL-account in Homey: aangekondigde post (Mijn Post) met scans, al je pakketten (Mijn Pakketten) met de officiële Track & Trace-status, bezorgvenster, gewicht, afmetingen en volledige statusgeschiedenis, plus de afbeelding **Mijn Bezorging** voor je Flows en dashboard.

## In één oogopslag

| | |
|---|---|
| Landen | 🇳🇱 Nederland (PostNL-account van jouw.postnl.nl) |
| Koppelen met | Account |
| Apparaat-ID | `postnl` |
| Flow-kaarten | 12 triggers · 7 condities · 1 actie |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **PostNL**.
2. Vul het e-mailadres en wachtwoord in waarmee je inlogt op **jouw.postnl.nl** en tik op **Koppelen**.
3. Je wachtwoord wordt alleen gebruikt om bij PostNL in te loggen; Homey bewaart daarna de verkregen tokens, niet je wachtwoord.
4. Is de aanmelding later verlopen? Gebruik **Herstellen** op het apparaat en log opnieuw in.

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `postnl_mail_expected` | ja/nee | Post verwacht | Mail expected |
| `postnl_mail_count` | getal | Poststukken | Mail items |
| `postnl_package_count` | getal | Pakketten onderweg | Parcels underway |
| `postnl_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `postnl_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `postnl_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `postnl_package_status` | tekst | Pakketstatus | Parcel status |
| `postnl_package_sender` | tekst | Afzender pakket | Parcel sender |
| `postnl_package_receiver` | tekst | Ontvanger pakket | Parcel receiver |
| `postnl_package_tracking` | tekst | Trackingnummer | Tracking number |
| `postnl_package_event` | tekst | Laatste pakketgebeurtenis | Latest parcel event |
| `postnl_package_status_time` | tekst | Tijdstip pakketstatus | Parcel status time |
| `postnl_package_delivered` | ja/nee | Pakket bezorgd | Parcel delivered |
| `postnl_package_shipment_type` | tekst | Type zending | Shipment type |
| `postnl_package_weight` | tekst | Gewicht pakket | Parcel weight |
| `postnl_package_weight_kg` | getal | Gewicht pakket (kg) | Parcel weight (kg) |
| `postnl_package_length` | getal | Lengte pakket | Parcel length |
| `postnl_package_width` | getal | Breedte pakket | Parcel width |
| `postnl_package_height` | getal | Hoogte pakket | Parcel height |
| `postnl_package_status_history` | tekst | Volledige statusgeschiedenis | Full status history |
| `postnl_package_observation_code` | tekst | ObservationCode | Observation code |
| `postnl_package_canonical_status` | tekst | Canonieke status | Canonical status |
| `postnl_package_pickup` | ja/nee | Bezorging bij PostNL-punt | PostNL Point delivery |
| `postnl_package_pickup_point` | tekst | PostNL-punt | PostNL Point |
| `postnl_package_dimensions` | tekst | Afmetingen pakket | Parcel dimensions |
| `postnl_status` | tekst | Verbindingsstatus | Connection status |
| `postnl_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `new_mail` | Er is nieuwe post onderweg | New mail is expected |
| `new_package` | Er is een nieuw pakket gevonden | A new parcel was found |
| `delivery_window_known` | Er is een bezorgvenster bekend | A delivery window became available |
| `package_status_changed` | De status van een pakket is gewijzigd | A parcel status changed |
| `sync_failed` | PostNL-synchronisatie is mislukt | PostNL synchronization failed |
| `login_expired` | De PostNL-aanmelding is verlopen | The PostNL login expired |
| `package_delivered` | Een pakket is bezorgd | A parcel was delivered |
| `delivery_window_changed` | Het bezorgvenster van een pakket is gewijzigd | A parcel delivery window changed |
| `package_event_changed` | Er is een nieuwe PostNL-pakketgebeurtenis | A new PostNL parcel event was received |
| `package_weight_known` | Het gewicht van een pakket is bekend | Parcel weight became available |
| `package_dimensions_known` | De afmetingen van een pakket zijn bekend | Parcel dimensions became available |
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `mail_expected` | Post wordt/wordt niet verwacht | Mail is/isn't expected | — |
| `packages_underway` | Er zijn/zijn geen pakketten onderweg | Parcels are/aren't underway | — |
| `delivery_window_known` | Er is/is geen bezorgvenster bekend | A delivery window is/isn't known | — |
| `postnl_connected` | PostNL is/is niet verbonden | PostNL is/isn't connected | — |
| `package_has_weight` | Het huidige pakket heeft/heeft geen gewichtsinformatie | The current parcel has/doesn't have weight information | — |
| `package_has_dimensions` | Het huidige pakket heeft/heeft geen afmetingen | The current parcel has/doesn't have dimensions | — |
| `package_status_is` | De huidige pakketstatus is/is niet | The current parcel status is/isn't | Status |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `sync_now` | Synchroniseer PostNL | Synchronize PostNL | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 50 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `count` | getal | Aantal poststukken | Number of mail items |
| `id` | tekst | Poststuk-ID | Mail item ID |
| `title` | tekst | Poststuk | Mail item |
| `sender` | tekst | Afzender (indien beschikbaar) | Sender (if available) |
| `date` | tekst | Bezorgdatum | Delivery date |
| `unread` | ja/nee | Ongelezen | Unread |
| `image_available` | ja/nee | Afbeelding beschikbaar | Image available |
| `image` | afbeelding | Afbeelding poststuk | Mail item image |
| `receiver` | tekst | Ontvanger | Receiver |
| `barcode` | tekst | Barcode | Barcode |
| `status` | tekst | Status | Status |
| `status_raw` | tekst | Officiële PostNL-status | Official PostNL status |
| `status_code` | tekst | Officiële PostNL-statuscode | Official PostNL status code |
| `status_event` | tekst | Laatste PostNL-gebeurtenis | Latest PostNL event |
| `status_event_time` | tekst | Laatste statusupdate | Latest status update |
| `delivery_date` | tekst | Bezorgdatum | Delivery date |
| `delivery_window` | tekst | Bezorgvenster | Delivery window |
| `delivery_window_from` | tekst | Bezorgvenster vanaf | Delivery window from |
| `delivery_window_to` | tekst | Bezorgvenster tot | Delivery window to |
| `delivery_window_type` | tekst | Type bezorgvenster | Delivery window type |
| `details_url` | tekst | Tracking-URL | Tracking URL |
| `shipment_type` | tekst | Zendingstype | Shipment type |
| `delivery_address_type` | tekst | Type bezorgadres | Delivery address type |
| `direction` | tekst | Richting | Direction |
| `created_at` | tekst | Aangemaakt op | Created at |
| `delivered` | ja/nee | Bezorgd | Delivered |
| `shared_from` | tekst | Gedeeld via | Shared from |
| `source_account_id` | tekst | Bronaccount-ID | Source account ID |
| `package_status_text` | tekst | Pakketstatus | Package status |
| `package_window_text` | tekst | Tekst bezorgvenster | Delivery window text |
| `package_delivery_date` | tekst | Bezorgdatum pakket | Package delivery date |
| `package_sender` | tekst | Afzender pakket | Package sender |
| `package_tracking` | tekst | Trackingnummer pakket | Package tracking number |
| `package_image_available` | ja/nee | Afbeelding Mijn Bezorging beschikbaar | My delivery image available |
| `package_image` | afbeelding | Afbeelding Mijn Bezorging | My delivery image |
| `weight` | tekst | Gewicht | Weight |
| `dimensions` | tekst | Afmetingen | Dimensions |
| `weight_kg` | getal | Gewicht pakket (kg) | Parcel weight (kg) |
| `dimension_length` | getal | Lengte pakket (cm) | Parcel length (cm) |
| `dimension_width` | getal | Breedte pakket (cm) | Parcel width (cm) |
| `dimension_height` | getal | Hoogte pakket (cm) | Parcel height (cm) |
| `status_history` | tekst | Volledige statusgeschiedenis | Full status history |
| `observation_code` | tekst | PostNL-observatiecode | PostNL observation code |
| `canonical_status` | tekst | Canonieke pakketstatus | Canonical parcel status |
| `pickup` | ja/nee | Bezorging bij PostNL-punt | PostNL Point delivery |
| `pickup_point` | tekst | PostNL-punt | PostNL Point |
| `old_status` | tekst | Vorige status | Previous status |
| `error` | tekst | Foutmelding | Error |
| `old_delivery_window` | tekst | Vorig bezorgvenster | Previous delivery window |
| `old_event` | tekst | Vorige PostNL-gebeurtenis | Previous PostNL event |

</details>

## Beperkingen en tips

* **Flow-afbeelding:** de pakketkaarten (ook de bezorgvensterkaarten) geven de **Mijn Bezorging**-camera-afbeelding mee, vastgezet op precies dat pakket en die status vlak vóór de trigger. Bezorgde pakketten krijgen geen nieuwe tekening en houden de huidige Mijn Bezorging-afbeelding, zodat het token nooit leeg is.
* **Globale afbeeldingstokens:** **Pakketafbeelding** en **Scan laatste poststuk** werken in elke Flow, welke kaart de Flow ook startte. Ze verschijnen als *&lt;apparaatnaam&gt; · Pakketafbeelding* en *&lt;apparaatnaam&gt; · Scan laatste poststuk*.
* Track & Trace wordt alleen voor actieve pakketten opgehaald (max. 3 tegelijk); alleen de 15 meest recente bezorgde pakketten worden bewaard.
* Mijn Post is live: post die je in de PostNL-app verwijdert, verdwijnt na de volgende verversing ook uit Homey. Scans worden niet lokaal opgeslagen.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
