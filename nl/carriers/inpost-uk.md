# InPost

![InPost](../../media/drivers/inpost-uk/assets/images/large.png)

InPost-pakketten (voorheen *InPost UK*) volgen met hun nummer, plus optioneel je InPost-account (Polen/Italië) met je pakketten en hun **ophaalcode (open code)** voor de Paczkomat/locker.

## In één oogopslag

| | |
|---|---|
| Landen | 🇬🇧 🇵🇱 🇮🇹 🇵🇹 🇪🇸 Verenigd Koninkrijk, Polen, Italië, Portugal en Spanje (account: Polen en Italië) |
| Koppelen met | Trackingnummer · Account |
| Apparaat-ID | `inpost-uk` |
| Flow-kaarten | 8 triggers · 6 condities · 4 acties |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **InPost**.
2. Kies het **land** en vul de **pakketnummers** in (één per regel). Tik op **Pakketten volgen**.
3. Optioneel (Polen/Italië): open **InPost-account gebruiken**, kies het land van het account en tik op **InPost-login openen**. Log in met je telefoonnummer en sms-code.
4. Kopieer daarna het volledige `https://account.inpost-group.com/callback?…`-adres uit de adresbalk, plak het in **Callback-adres** en tik op **Account koppelen**.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| InPost Track & Trace | **Land** | (keuzes: Verenigd Koninkrijk, Polen, Italië, Portugal, Spanje) |
| InPost Track & Trace | **Trackingnummers** | Eén InPost-pakketnummer per regel. |
| InPost Track & Trace | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `inpost_uk_parcel_count` | getal | Actieve pakketten | Active parcels |
| `inpost_uk_status` | tekst | Status | Status |
| `inpost_uk_tracking` | tekst | Trackingnummer | Tracking number |
| `inpost_uk_sender` | tekst | Afzender | Sender |
| `inpost_uk_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `inpost_uk_pickup_count` | getal | Klaar om op te halen | Ready for pickup |
| `inpost_uk_pickup_point` | tekst | Afhaalpunt | Pickup point |
| `inpost_uk_pickup_code` | tekst | Ophaalcode | Pickup code |
| `inpost_uk_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `inpost_uk_last_event` | tekst | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | tekst | Verbindingsstatus | Connection status |
| `inpost_uk_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `inpost_uk_new_package` | Nieuw InPost UK-pakket | New InPost UK package |
| `inpost_uk_status_changed` | InPost UK-pakketstatus gewijzigd | InPost UK package status changed |
| `inpost_uk_package_event_changed` | Nieuwe InPost-trackinggebeurtenis | New InPost tracking event |
| `inpost_uk_out_for_delivery` | InPost-pakket onderweg voor bezorging | InPost parcel out for delivery |
| `inpost_uk_ready_for_pickup` | InPost-pakket klaar om op te halen | InPost parcel ready for pickup |
| `inpost_uk_delivered` | InPost-pakket bezorgd | InPost parcel delivered |
| `inpost_uk_package_problem` | Probleem of retour bij InPost-pakket | InPost parcel has a problem or is returning |
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `inpost_uk_packages_underway` | Er zijn InPost UK-pakketten onderweg | InPost UK packages are underway | — |
| `inpost_uk_out_for_delivery_now` | Er is een/geen InPost-pakket onderweg voor bezorging | A InPost parcel is/is not out for delivery | — |
| `inpost_uk_ready_for_pickup_now` | Er ligt een/geen InPost-pakket klaar om op te halen | A InPost parcel is/is not ready for pickup | — |
| `inpost_uk_any_status_is` | Een InPost-pakket heeft/heeft niet status… | A InPost parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij InPost) |
| `inpost_uk_parcel_is_delivered` | InPost-pakket… is/is niet bezorgd | InPost parcel… is/is not delivered | Trackingnummer |
| `inpost_uk_is_tracking` | InPost-pakket… wordt wel/niet gevolgd | InPost parcel… is/is not being tracked | Trackingnummer |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `inpost_uk_refresh` | Vernieuw InPost UK | Refresh InPost UK | — |
| `inpost_uk_track_parcel` | Volg InPost-pakket… | Track InPost parcel… | Trackingnummer |
| `inpost_uk_untrack_parcel` | Stop met volgen van InPost-pakket… | Stop tracking InPost parcel… | Trackingnummer |
| `inpost_uk_remove_delivered` | Verwijder bezorgde InPost-pakketten | Remove delivered InPost parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 22 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | tekst | Trackingnummer | Tracking number |
| `status` | tekst | Status | Status |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | InPost-statustekst | InPost status text |
| `sender` | tekst | Afzender | Sender |
| `receiver` | tekst | Ontvanger | Recipient |
| `delivery_date` | tekst | Bezorgdatum | Delivery date |
| `delivery_window` | tekst | Bezorgvenster | Delivery window |
| `window_start` | tekst | Begin venster | Window start |
| `window_end` | tekst | Einde venster | Window end |
| `pickup_point` | tekst | Afhaalpunt | Pickup point |
| `last_event` | tekst | Laatste gebeurtenis | Last event |
| `last_event_time` | tekst | Tijd laatste gebeurtenis | Last event time |
| `delivered_at` | tekst | Bezorgd op | Delivered at |
| `direction` | tekst | Richting | Direction |
| `history` | tekst | Statusgeschiedenis | Status history |
| `url` | tekst | Trackinglink | Tracking link |
| `pickup_code` | tekst | Ophaalcode | Pickup code |
| `pickup_deadline` | tekst | Ophalen vóór | Pick up before |
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige InPost-statustekst | Previous InPost status text |

</details>

## Beperkingen en tips

* De accountkoppeling werkt alleen voor Polen en Italië; voor de andere landen volg je pakketnummers.
* Een inloglink werkt maar één keer; open de login opnieuw als het koppelen mislukt.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
