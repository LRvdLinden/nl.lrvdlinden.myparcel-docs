# Mondial Relay

![Mondial Relay](../../media/drivers/mondial-relay/assets/images/large.png)

> **Nieuw in v0.3.6**

Log in met je Mondial Relay- / InPost-account om je inkomende en verzonden pakketten automatisch te zien, met de laatste stap van elk pakket. Je wachtwoord komt nooit bij Homey.

## In één oogopslag

| | |
|---|---|
| Landen | 🇫🇷 🇧🇪 🇳🇱 🇪🇸 🇵🇹 Frankrijk, België, Nederland, Spanje en Portugal |
| Koppelen met | Account |
| Apparaat-ID | `mondial-relay` |
| Flow-kaarten | 9 triggers · 6 condities · 2 acties |

## Koppelen

1. Zorg dat je account minstens één keer is ingelogd op de website of in de app van Mondial Relay.
2. Open Homey → **Apparaten** → **+** → **MyParcel** → **Mondial Relay** en kies het **land van het account**.
3. Tik op **Mondial Relay-login openen** en log in met je account.
4. Na het inloggen komt de browser uit op een adres dat begint met `https://account.inpost-group.com/callback?code=…` en niet laadt. Dat hoort zo: kopieer het volledige adres uit de adresbalk, plak het in **Adres na het inloggen** en tik op **Account koppelen**.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| Mondial Relay | **Land van het account** | (keuzes: Frankrijk, België, Nederland, Spanje, Portugal) |
| Mondial Relay | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `mondial_relay_parcel_count` | getal | Actieve pakketten | Active parcels |
| `mondial_relay_status` | tekst | Status | Status |
| `mondial_relay_tracking` | tekst | Trackingnummer | Tracking number |
| `mondial_relay_sender` | tekst | Afzender | Sender |
| `mondial_relay_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `mondial_relay_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `mondial_relay_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `mondial_relay_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `mondial_relay_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `mondial_relay_outgoing_count` | getal | Verzonden pakketten onderweg | Sent parcels underway |
| `mondial_relay_last_event` | tekst | Laatste gebeurtenis | Last event |
| `myparcel_connection_status` | tekst | Verbindingsstatus | Connection status |
| `mondial_relay_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

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
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `mondial_relay_packages_underway` | Er zijn/zijn geen Mondial Relay-pakketten onderweg | Mondial Relay parcels are/are not underway | — |
| `mondial_relay_out_for_delivery_now` | Er is een/geen Mondial Relay-pakket onderweg voor bezorging | A Mondial Relay parcel is/is not out for delivery | — |
| `mondial_relay_any_status_is` | Een Mondial Relay-pakket heeft/heeft niet status… | A Mondial Relay parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij Mondial Relay) |
| `mondial_relay_parcel_is_delivered` | Mondial Relay-pakket… is/is niet bezorgd | Mondial Relay parcel… is/is not delivered | Trackingnummer |
| `mondial_relay_is_tracking` | Mondial Relay-pakket… wordt wel/niet gevolgd | Mondial Relay parcel… is/is not being tracked | Trackingnummer |
| `mondial_relay_outgoing_underway` | Er zijn/zijn geen verzonden Mondial Relay-pakketten onderweg | Sent Mondial Relay parcels are/are not underway | — |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `mondial_relay_refresh` | Vernieuw Mondial Relay | Refresh Mondial Relay | — |
| `mondial_relay_remove_delivered` | Verwijder bezorgde Mondial Relay-pakketten | Remove delivered Mondial Relay parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 22 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | tekst | Trackingnummer | Tracking number |
| `status` | tekst | Status | Status |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | Mondial Relay-statustekst | Mondial Relay status text |
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
| `destination` | tekst | Bestemming | Destination |
| `market` | tekst | Land | Country |
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige Mondial Relay-statustekst | Previous Mondial Relay status text |

</details>

## Beperkingen en tips

* **Nog geen betrouwbare status:** Mondial Relay deelt (nog) geen betrouwbare pakketstatus. Alleen de kaarten **nieuw pakket** en **trackinggebeurtenis** gaan af; de statusgebaseerde kaarten (status gewijzigd, onderweg voor bezorging, bezorgd, probleem/retour en de kaarten voor verzonden pakketten) volgen zodra de status bekend is.
* Elke inloglink werkt maar één keer. Mislukt het koppelen, open dan de inlogpagina opnieuw voor een nieuwe link.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
