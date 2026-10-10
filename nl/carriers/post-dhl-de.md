# Post & DHL Duitsland

![Post & DHL Duitsland](../../media/drivers/post-dhl-de/assets/images/large.png)

Je DHL-pakketten in Duitsland met de statusladder van DHL (aangekondigd, onderweg, wordt bezorgd, bezorgd), Packstation-ophalingen met het Packstation-adres, retouren, verzonden pakketten en Deutsche Post-brieven. Met de widgets **DHL-pakketten (Duitsland)** en **Deutsche Post Poststukken**.

## In één oogopslag

| | |
|---|---|
| Landen | 🇩🇪 Duitsland |
| Koppelen met | Account · Trackingnummer |
| Apparaat-ID | `post-dhl-de` |
| Flow-kaarten | 11 triggers · 8 condities · 4 acties |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **Post & DHL Duitsland**.
2. **Post & DHL-app-login (werkt vanuit elk land):** tik op **DHL-login openen**, log in en kopieer na de doorverwijzing het volledige adres uit de adresbalk terug naar het scherm (**Adres na het inloggen**). Tik op **Koppelen**.
3. **DHL.de-login (alleen vanuit Duitsland):** tik op **DHL.de-login openen**, log in en kopieer het `dhllogin://…`-adres (ontwikkelaarstools van de browser → Netwerk). Hiermee kun je ook extra trackingnummers volgen.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| DHL Track & Trace | **Trackingnummers** | Extra DHL Paket-trackingnummers, één per regel (werkt met de DHL.de-login). Voeg “uit” toe voor een pakket dat je zelf verstuurt. |
| DHL Track & Trace | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `dhl_de_parcel_count` | getal | Actieve pakketten | Active packages |
| `dhl_de_status` | tekst | Status | Status |
| `dhl_de_tracking` | tekst | Trackingnummer | Tracking number |
| `dhl_de_sender` | tekst | Afzender | Sender |
| `dhl_de_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `dhl_de_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `dhl_de_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `dhl_de_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `dhl_de_pickup_count` | getal | Klaar om op te halen | Ready for pickup |
| `dhl_de_pickup_point` | tekst | Afhaalpunt | Pickup point |
| `dhl_de_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `dhl_de_outgoing_count` | getal | Verzonden pakketten onderweg | Sent parcels underway |
| `dhl_de_last_event` | tekst | Laatste gebeurtenis | Last event |
| `dhl_de_mail_count` | getal | Verwachte post | Expected mail |
| `dhl_de_postnumber` | tekst | Postnummer | Postnumber |
| `dhl_de_account_status` | tekst | Verbindingsstatus | Connection status |
| `dhl_de_mail_status` | tekst | Briefaankondiging | Letter announcement |
| `dhl_de_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

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
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `dhl_de_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |
| `dhl_de_packages_underway` | Er zijn/zijn geen DHL-pakketten onderweg | DHL parcels are/are not underway | — |
| `dhl_de_out_for_delivery_now` | Er is een/geen DHL-pakket onderweg voor bezorging | A DHL parcel is/is not out for delivery | — |
| `dhl_de_ready_for_pickup_now` | Er ligt een/geen DHL-pakket klaar om op te halen | A DHL parcel is/is not ready for pickup | — |
| `dhl_de_any_status_is` | Een DHL-pakket heeft/heeft niet status… | A DHL parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij Post & DHL Germany) |
| `dhl_de_parcel_is_delivered` | DHL-pakket… is/is niet bezorgd | DHL parcel… is/is not delivered | Trackingnummer |
| `dhl_de_is_tracking` | DHL-pakket… wordt wel/niet gevolgd | DHL parcel… is/is not being tracked | Trackingnummer |
| `dhl_de_outgoing_underway` | Er zijn/zijn geen verzonden DHL-pakketten onderweg | Sent DHL parcels are/are not underway | — |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `dhl_de_refresh` | Vernieuw Post & DHL | Refresh Post & DHL | — |
| `dhl_de_track_parcel` | Volg DHL-pakket… | Track DHL parcel… | Trackingnummer; Richting (Inkomend, Uitgaand (door mij verzonden)) |
| `dhl_de_untrack_parcel` | Stop met volgen van DHL-pakket… | Stop tracking DHL parcel… | Trackingnummer |
| `dhl_de_remove_delivered` | Verwijder bezorgde DHL-pakketten | Remove delivered DHL parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 21 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | tekst | Trackingnummer | Tracking number |
| `status` | tekst | Status | Status |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | Post & DHL Germany-statustekst | Post & DHL Germany status text |
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
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige Post & DHL Germany-statustekst | Previous Post & DHL Germany status text |
| `carrier` | tekst | Vervoerder | Carrier |

</details>

## Beperkingen en tips

* De DHL.de-login werkt alleen vanaf een Duitse internetverbinding; extra trackingnummers hebben die login nodig.
* Een inloglink werkt maar één keer; open de login opnieuw als het koppelen mislukt.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
