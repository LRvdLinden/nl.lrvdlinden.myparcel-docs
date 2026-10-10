# DPD

![DPD](../../media/drivers/dpd/assets/images/large.png)

Je myDPD-account in Homey (hetzelfde account als in de DPD-app): inkomende en verzonden pakketten met één duidelijke statusset (aangemeld, onderweg, wordt bezorgd, klaar bij ParcelShop, bezorgd, retour, probleem), het Follow My Parcel-bezorgvenster, gewicht, afmetingen en de volledige scangeschiedenis.

## In één oogopslag

| | |
|---|---|
| Landen | 🇳🇱 🇧🇪 🇩🇪 🇱🇺 🇫🇷 🇨🇭 🇬🇧 🇮🇹 🇵🇹 🇵🇱 🇨🇿 🇸🇰 🇭🇺 🇸🇮 🇭🇷 🇪🇪 🇱🇻 🇱🇹 🇦🇷 Nederland, België, Duitsland, Luxemburg, Frankrijk, Zwitserland, Verenigd Koninkrijk, Italië (BRT), Portugal, Polen, Tsjechië, Slowakije, Hongarije, Slovenië, Kroatië, Estland, Letland, Litouwen en Argentinië |
| Koppelen met | Account |
| Apparaat-ID | `dpd` |
| Flow-kaarten | 12 triggers · 7 condities · 1 actie |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **DPD**.
2. Kies je **land**.
3. Log in met het e-mailadres en wachtwoord van je **myDPD-account** en tik op **Koppelen**.
4. **Polen:** vul je mobiele nummer in, tik op **Sms-code versturen** en daarna op **Controleren en koppelen**. Homey bewaart alleen een vernieuwbaar token, nooit de code.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| DPD-account | **Land** | Ander land? Gebruik “Repareren” op het apparaat om voor dat land in te loggen. (keuzes: Nederland, België, Duitsland, Luxemburg, Frankrijk, Zwitserland, Verenigd Koninkrijk, Italië (BRT), Portugal, Polen, Tsjechië, Slowakije, Hongarije, Slovenië, Kroatië, Estland, Letland, Litouwen, Argentinië) |
| DPD-account | **E-mailadres** | — |
| DPD-account | **Wachtwoord** | (wordt verborgen opgeslagen) |
| DPD-account | **Mobiel nummer (alleen Polen)** | — |
| DPD-account | **Bezorgde pakketten tonen gedurende (dagen)** | (standaard: 7) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `dpd_parcel_count` | getal | Actieve pakketten | Active parcels |
| `dpd_total_count` | getal | Totaal pakketten | Total parcels |
| `dpd_status` | tekst | Status | Status |
| `dpd_tracking` | tekst | Trackingnummer | Tracking number |
| `dpd_sender` | tekst | Afzender | Sender |
| `dpd_receiver` | tekst | Ontvanger | Receiver |
| `dpd_delivery_date` | tekst | Bezorgdatum | Delivery date |
| `dpd_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `dpd_delivery_point` | tekst | Bezorgpunt | Delivery point |
| `dpd_weight` | tekst | Gewicht | Weight |
| `dpd_dimensions` | tekst | Afmetingen | Dimensions |
| `dpd_delivery_type` | tekst | Type bezorging | Delivery type |
| `dpd_last_event` | tekst | Laatste gebeurtenis | Last event |
| `dpd_direction` | tekst | Richting | Direction |
| `dpd_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `dpd_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `dpd_en_route_pickup_count` | getal | Onderweg naar ParcelShop | En route to ParcelShop |
| `dpd_pickup_count` | getal | Klaar om op te halen | Ready for pickup |
| `dpd_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `dpd_outgoing_count` | getal | Verzonden pakketten onderweg | Sent parcels underway |
| `myparcel_connection_status` | tekst | Verbindingsstatus | Connection status |
| `dpd_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

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
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `dpd_packages_underway` | Er zijn/zijn geen DPD-pakketten onderweg | DPD parcels are/are not underway | — |
| `dpd_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |
| `dpd_out_for_delivery_now` | Er is een/geen DPD-pakket onderweg voor bezorging | A DPD parcel is/is not out for delivery | — |
| `dpd_ready_for_pickup_now` | Er ligt een/geen DPD-pakket klaar om op te halen | A DPD parcel is/is not ready for pickup | — |
| `dpd_any_status_is` | Een DPD-pakket heeft/heeft niet status… | A DPD parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij DPD) |
| `dpd_parcel_is_delivered` | DPD-pakket… is/is niet bezorgd | DPD parcel… is/is not delivered | Trackingnummer |
| `dpd_outgoing_underway` | Er zijn/zijn geen verzonden DPD-pakketten onderweg | Sent DPD parcels are/are not underway | — |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `dpd_refresh` | Vernieuw DPD | Refresh DPD | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 26 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | tekst | Trackingnummer | Tracking number |
| `status` | tekst | Status | Status |
| `sender` | tekst | Afzender | Sender |
| `receiver` | tekst | Ontvanger | Receiver |
| `delivery_date` | tekst | Bezorgdatum | Delivery date |
| `delivery_window` | tekst | Bezorgvenster | Delivery window |
| `delivery_point` | tekst | Bezorgpunt | Delivery point |
| `weight` | tekst | Gewicht | Weight |
| `dimensions` | tekst | Afmetingen | Dimensions |
| `delivery_type` | tekst | Type bezorging | Delivery type |
| `last_event` | tekst | Laatste gebeurtenis | Last event |
| `direction` | tekst | Richting | Direction |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | DPD-statustekst | DPD status text |
| `window_start` | tekst | Begin venster | Window start |
| `window_end` | tekst | Einde venster | Window end |
| `delivered_at` | tekst | Bezorgd op | Delivered at |
| `last_event_time` | tekst | Tijd laatste gebeurtenis | Last event time |
| `history` | tekst | Statusgeschiedenis | Status history |
| `url` | tekst | Trackinglink | Tracking link |
| `country` | tekst | Land | Country |
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige DPD-statustekst | Previous DPD status text |
| `carrier` | tekst | Vervoerder | Carrier |
| `old_delivery_window` | tekst | Vorig bezorgvenster | Previous delivery window |

</details>

## Beperkingen en tips

* Land gewijzigd? Gebruik **Herstellen** op het apparaat om voor dat land opnieuw in te loggen.
* Het bezorgvenster wordt alleen opgehaald voor actieve inkomende pakketten.

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
