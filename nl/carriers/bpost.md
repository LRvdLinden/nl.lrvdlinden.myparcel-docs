# bpost

![bpost](../../media/drivers/bpost/assets/images/large.png)

Je My bpost-account in Homey: alle inkomende en verzonden pakketten, de bpost-processtappen, het bezorgvenster in Belgische tijd, het aantal stops tot jij aan de beurt bent en **Mail Ahead-brieven**. Zonder account volg je barcodes met een postcode.

## In één oogopslag

| | |
|---|---|
| Landen | 🇧🇪 België |
| Koppelen met | Account · Trackingnummer |
| Apparaat-ID | `bpost` |
| Flow-kaarten | 13 triggers · 9 condities · 4 acties |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **bpost**.
2. Log in met het e-mailadres en wachtwoord van **My bpost** en tik op **My bpost koppelen**. Je wachtwoord wordt één keer gebruikt; MyParcel bewaart bpost-logintokens.
3. **Of** open **Barcodes volgen zonder account**: vul de postcode van het bezorgadres en de barcodes (één per regel, eventueel met afwijkende postcode erachter) in en tik op **Barcodes volgen**.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| My bpost-account (optioneel) | **E-mailadres** | — |
| My bpost-account (optioneel) | **Wachtwoord (alleen om opnieuw in te loggen)** | MyParcel logt één keer in en gebruikt daarna bpost-logintokens; het wachtwoord wordt niet bewaard. (wordt verborgen opgeslagen) |
| bpost Track & Trace | **Postcode van het bezorgadres** | — |
| bpost Track & Trace | **Trackingnummers** | Eén barcode per regel. Zet de postcode achter de barcode als die afwijkt van die hierboven, bijv. 323456789012345678 1000. |
| bpost Track & Trace | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `bpost_parcel_count` | getal | Actieve pakketten | Active parcels |
| `bpost_total_count` | getal | Totaal pakketten | Total parcels |
| `bpost_status` | tekst | Status | Status |
| `bpost_tracking` | tekst | Volgend trackingnummer | Next tracking number |
| `bpost_sender` | tekst | Afzender | Sender |
| `bpost_delivery_date` | tekst | Verwachte bezorging | Expected delivery |
| `bpost_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `bpost_delivery_point` | tekst | Afleverpunt | Delivery point |
| `bpost_weight` | tekst | Gewicht | Weight |
| `bpost_product` | tekst | Product | Product |
| `bpost_partner` | tekst | Bezorgpartner | Delivery partner |
| `bpost_last_event` | tekst | Laatste gebeurtenis | Last event |
| `bpost_receiver` | tekst | Ontvanger | Receiver |
| `bpost_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `bpost_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `bpost_en_route_pickup_count` | getal | Onderweg naar afhaalpunt | En route to pickup point |
| `bpost_pickup_count` | getal | Klaar om op te halen | Ready for pickup |
| `bpost_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `bpost_outgoing_count` | getal | Verzonden pakketten onderweg | Sent parcels underway |
| `bpost_dimensions` | tekst | Afmetingen | Dimensions |
| `bpost_letter_count` | getal | Aangekondigde brieven | Letters announced |
| `bpost_last_letter` | tekst | Laatste brief | Last letter |
| `bpost_account_status` | tekst | Verbindingsstatus | Connection status |
| `bpost_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `bpost_new_package` | Nieuw bpost-pakket | New bpost package |
| `bpost_status_changed` | bpost-pakketstatus gewijzigd | bpost package status changed |
| `bpost_package_event_changed` | Nieuwe bpost-trackinggebeurtenis | New bpost tracking event |
| `bpost_out_for_delivery` | bpost-pakket onderweg voor bezorging | bpost parcel out for delivery |
| `bpost_ready_for_pickup` | bpost-pakket klaar om op te halen | bpost parcel ready for pickup |
| `bpost_delivered` | bpost-pakket bezorgd | bpost package delivered |
| `bpost_package_problem` | Probleem of retour bij bpost-pakket | bpost parcel has a problem or is returning |
| `bpost_outgoing_status_changed` | Status van verzonden bpost-pakket gewijzigd | Status of sent bpost parcel changed |
| `bpost_outgoing_delivered` | Verzonden bpost-pakket bezorgd | Sent bpost parcel delivered |
| `bpost_delivery_updated` | bpost-bezorginformatie bijgewerkt | bpost delivery information updated |
| `bpost_letter_announced` | bpost-brief aangekondigd (Mail Ahead) | bpost letter announced (Mail Ahead) |
| `bpost_delivery_window_changed` | Bezorgvenster bekend of gewijzigd | Delivery window available or changed |
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `bpost_packages_underway` | Er zijn bpost-pakketten onderweg | bpost packages are underway | — |
| `bpost_account_connected` | My bpost-account is gekoppeld | My bpost account is connected | — |
| `bpost_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |
| `bpost_out_for_delivery_now` | Er is een/geen bpost-pakket onderweg voor bezorging | A bpost parcel is/is not out for delivery | — |
| `bpost_ready_for_pickup_now` | Er ligt een/geen bpost-pakket klaar om op te halen | A bpost parcel is/is not ready for pickup | — |
| `bpost_any_status_is` | Een bpost-pakket heeft/heeft niet status… | A bpost parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij bpost) |
| `bpost_parcel_is_delivered` | bpost-pakket… is/is niet bezorgd | bpost parcel… is/is not delivered | Trackingnummer |
| `bpost_is_tracking` | bpost-pakket… wordt wel/niet gevolgd | bpost parcel… is/is not being tracked | Trackingnummer |
| `bpost_outgoing_underway` | Er zijn/zijn geen verzonden bpost-pakketten onderweg | Sent bpost parcels are/are not underway | — |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `bpost_refresh` | Vernieuw bpost | Refresh bpost | — |
| `bpost_track_parcel` | Volg bpost-pakket… | Track bpost parcel… | Trackingnummer |
| `bpost_untrack_parcel` | Stop met volgen van bpost-pakket… | Stop tracking bpost parcel… | Trackingnummer |
| `bpost_remove_delivered` | Verwijder bezorgde bpost-pakketten | Remove delivered bpost parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 31 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | tekst | Trackingnummer | Tracking number |
| `status` | tekst | Status | Status |
| `sender` | tekst | Afzender | Sender |
| `delivery_date` | tekst | Verwachte bezorging | Expected delivery |
| `delivery_window` | tekst | Bezorgvenster | Delivery window |
| `delivery_point` | tekst | Afleverpunt | Delivery point |
| `weight` | tekst | Gewicht (g) | Weight (g) |
| `product` | tekst | Product | Product |
| `partner` | tekst | Bezorgpartner | Delivery partner |
| `last_event` | tekst | Laatste gebeurtenis | Last event |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | bpost-statustekst | bpost status text |
| `receiver` | tekst | Ontvanger | Recipient |
| `window_start` | tekst | Begin venster | Window start |
| `window_end` | tekst | Einde venster | Window end |
| `pickup_point` | tekst | Afhaalpunt | Pickup point |
| `last_event_time` | tekst | Tijd laatste gebeurtenis | Last event time |
| `delivered_at` | tekst | Bezorgd op | Delivered at |
| `direction` | tekst | Richting | Direction |
| `history` | tekst | Statusgeschiedenis | Status history |
| `url` | tekst | Trackinglink | Tracking link |
| `dimensions` | tekst | Afmetingen | Dimensions |
| `stops` | getal | Stops tot jou | Stops until you |
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige bpost-statustekst | Previous bpost status text |
| `old_delivery_window` | tekst | Vorig bezorgvenster | Previous delivery window |
| `date` | tekst | Bezorgdatum | Delivery date |
| `image_url` | tekst | Afbeeldingslink | Image link |
| `letter_count` | getal | Aangekondigde brieven | Letters announced |
| `carrier` | tekst | Vervoerder | Carrier |

</details>

## Beperkingen en tips

* Mail Ahead-brieven en verzonden pakketten zijn alleen beschikbaar met een My bpost-account.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
