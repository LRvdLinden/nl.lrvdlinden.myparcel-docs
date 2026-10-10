# GLS

![GLS](../../media/drivers/gls/assets/images/large.png)

GLS-pakketten volgen via GLS' eigen openbare tracking – geen MyGLS-account nodig. Alleen je land, bezorgpostcode en trackingnummers. Bestaande apparaten met een MyGLS-zakelijk account blijven werken.

## In één oogopslag

| | |
|---|---|
| Landen | 🇳🇱 🇧🇪 🇩🇪 🇦🇹 🇨🇭 🇱🇺 🇫🇷 🇮🇹 🇩🇰 🇫🇮 🇮🇪 🇵🇱 🇨🇿 🇸🇰 🇭🇺 🇸🇮 🇭🇷 🇷🇸 🇺🇸 🇨🇦 20 landen: Nederland (met gewicht, afmetingen, bezorgvenster, ParcelShop en geschiedenis), België, Duitsland, Oostenrijk, Zwitserland, Luxemburg, Frankrijk, Italië, Denemarken, Finland, Ierland, Polen, Tsjechië, Slowakije, Hongarije, Slovenië, Kroatië, Servië, Verenigde Staten en Canada |
| Koppelen met | Trackingnummer |
| Apparaat-ID | `gls` |
| Flow-kaarten | 9 triggers · 7 condities · 4 acties |

## Koppelen

1. Open Homey → **Apparaten** → **+** → **MyParcel** → **GLS**.
2. Kies je **land** en vul de **bezorgpostcode** in (GLS deelt pakketgegevens alleen met de postcode waar het pakket bezorgd wordt).
3. Vul optioneel **trackingnummers** in: één per regel, het lange pakketnummer of de korte track-ID uit de GLS-mail/sms. Zet een afwijkende postcode achter het nummer.
4. Tik op **GLS toevoegen**. Later meer toevoegen kan via de apparaatinstellingen of met een Flow.

## Instellingen

| Groep | Instelling | Uitleg |
|---|---|---|
| GLS Track & Trace | **Land** | (keuzes: Nederland, België, Duitsland, Oostenrijk, Zwitserland, Luxemburg, Frankrijk, Italië, Denemarken, Finland, Ierland, Polen, Tsjechië, Slowakije, Hongarije, Slovenië, Kroatië, Servië, Verenigde Staten, Canada) |
| GLS Track & Trace | **Bezorgpostcode** | De postcode waar je GLS-pakketten bezorgd worden. GLS geeft alleen pakketgegevens vrij bij de juiste postcode. |
| GLS Track & Trace | **Trackingnummers** | Eén pakket per regel: het lange pakketnummer of de korte track-ID uit de GLS-mail/sms. Zet zo nodig een afwijkende postcode achter het nummer, bijv. 12345678901 1234AB. |
| GLS Track & Trace | **Bezorgde pakketten verwijderen na (dagen)** | Bezorgde pakketten blijven zo veel dagen zichtbaar en worden daarna uit de lijst gehaald. 0 = laten staan. (standaard: 7) |
| MyGLS-zakelijk account (optioneel) | **MyGLS gebruikersnaam** | — |
| MyGLS-zakelijk account (optioneel) | **MyGLS wachtwoord** | (wordt verborgen opgeslagen) |
| MyGLS-zakelijk account (optioneel) | **API-abonnementssleutel** | (wordt verborgen opgeslagen) |
| MyGLS-zakelijk account (optioneel) | **Pakketlijst-endpoint** | — |
| MyGLS-zakelijk account (optioneel) | **Pakketdetails-endpoint** | — |
| MyGLS-zakelijk account (optioneel) | **Dagen automatisch zoeken** | (standaard: 21) |

## Apparaatwaarden (capabilities)

Elke waarde verschijnt op het apparaat in Homey. Niet elk veld is voor elk pakket gevuld.

| ID | Type | Nederlands | English |
|---|---|---|---|
| `gls_parcel_count` | getal | Pakketten onderweg | Parcels underway |
| `gls_status` | tekst | Status | Status |
| `gls_next_delivery` | tekst | Volgende bezorging | Next delivery |
| `gls_delivery_window` | tekst | Bezorgvenster | Delivery window |
| `gls_tracking` | tekst | Trackingnummer | Tracking number |
| `gls_sender` | tekst | Afzender | Sender |
| `gls_receiver` | tekst | Ontvanger | Recipient |
| `gls_last_event` | tekst | Laatste gebeurtenis | Last event |
| `gls_out_for_delivery_count` | getal | Onderweg voor bezorging | Out for delivery |
| `gls_en_route_pickup_count` | getal | Onderweg naar ParcelShop | En route to ParcelShop |
| `gls_pickup_count` | getal | Klaar om op te halen | Ready for pickup |
| `gls_pickup_point` | tekst | ParcelShop | ParcelShop |
| `gls_delivered_count` | getal | Recent bezorgd | Recently delivered |
| `gls_weight` | getal | Gewicht | Weight |
| `gls_dimensions` | tekst | Afmetingen | Dimensions |
| `myparcel_connection_status` | tekst | Verbindingsstatus | Connection status |
| `gls_last_update` | tekst | Laatste update | Last update |

## Flow-kaarten

### Wanneer… (triggers)

| ID | Nederlands | English |
|---|---|---|
| `gls_new_package` | Nieuw GLS-pakket | New GLS parcel |
| `gls_status_changed` | Status GLS-pakket gewijzigd | GLS parcel status changed |
| `gls_package_event_changed` | Nieuwe GLS-trackinggebeurtenis | New GLS tracking event |
| `gls_out_for_delivery` | GLS-pakket onderweg voor bezorging | GLS parcel out for delivery |
| `gls_delivery_window_changed` | Bezorgvenster bekend of gewijzigd | Delivery window available or changed |
| `gls_ready_for_pickup` | GLS-pakket klaar om op te halen | GLS parcel ready for pickup |
| `gls_package_delivered` | GLS-pakket bezorgd | GLS parcel delivered |
| `gls_package_problem` | Probleem of retour bij GLS-pakket | GLS parcel has a problem or is returning |
| `connection_status_changed` | Verbindingsstatus is gewijzigd *(geldt voor alle MyParcel-apparaten)* | Connection status changed |

### En… (condities)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `gls_packages_underway` | Er zijn/zijn geen GLS-pakketten onderweg | GLS parcels are/are not underway | — |
| `gls_delivery_window_known` | Bezorgvenster is/is niet bekend | Delivery window is/isn't known | — |
| `gls_out_for_delivery_now` | Er is een/geen GLS-pakket onderweg voor bezorging | A GLS parcel is/is not out for delivery | — |
| `gls_ready_for_pickup_now` | Er ligt een/geen GLS-pakket klaar om op te halen | A GLS parcel is/is not ready for pickup | — |
| `gls_any_status_is` | Een GLS-pakket heeft/heeft niet status… | A GLS parcel has/does not have status… | Status (Aangemeld, Onderweg, Onderweg voor bezorging, Klaar om op te halen, Bezorgd, Retour naar afzender, Probleem, Nog niet bekend bij GLS) |
| `gls_parcel_is_delivered` | GLS-pakket… is/is niet bezorgd | GLS parcel… is/is not delivered | Trackingnummer |
| `gls_is_tracking` | GLS-pakket… wordt wel/niet gevolgd | GLS parcel… is/is not being tracked | Trackingnummer |

### Dan… (acties)

| ID | Nederlands | English | Argumenten |
|---|---|---|---|
| `gls_refresh` | Vernieuw GLS | Refresh GLS | — |
| `gls_track_parcel` | Volg GLS-pakket… | Track GLS parcel… | Trackingnummer |
| `gls_untrack_parcel` | Stop met volgen van GLS-pakket… | Stop tracking GLS parcel… | Trackingnummer |
| `gls_remove_delivered` | Verwijder bezorgde GLS-pakketten | Remove delivered GLS parcels | — |

## Belangrijke tokens

Tokens die de Wanneer-kaarten van deze vervoerder meegeven (niet elke kaart heeft elk token).

<details>
<summary>Toon alle 22 tokens</summary>

| Token | Type | Nederlands | English |
|---|---|---|---|
| `tracking` | tekst | Trackingnummer | Tracking number |
| `status` | tekst | Status | Status |
| `status_code` | tekst | Statuscode | Status code |
| `raw_status` | tekst | GLS-statustekst | GLS status text |
| `sender` | tekst | Afzender | Sender |
| `receiver` | tekst | Ontvanger | Recipient |
| `delivery_date` | tekst | Bezorgdatum | Delivery date |
| `delivery_window` | tekst | Bezorgvenster | Delivery window |
| `window_start` | tekst | Begin venster | Window start |
| `window_end` | tekst | Einde venster | Window end |
| `pickup_point` | tekst | ParcelShop | ParcelShop |
| `weight` | tekst | Gewicht | Weight |
| `dimensions` | tekst | Afmetingen | Dimensions |
| `delivered_at` | tekst | Bezorgd op | Delivered at |
| `last_event_time` | tekst | Tijd laatste gebeurtenis | Last event time |
| `history` | tekst | Statusgeschiedenis | Status history |
| `url` | tekst | Trackinglink | Tracking link |
| `country` | tekst | Land | Country |
| `previous_status` | tekst | Vorige status | Previous status |
| `old_status_code` | tekst | Vorige statuscode | Previous status code |
| `old_event` | tekst | Vorige GLS-statustekst | Previous GLS status text |
| `carrier` | tekst | Vervoerder | Carrier |

</details>

## Beperkingen en tips

* Buiten Nederland levert GLS minder details (bijv. geen gewicht/afmetingen of bezorgvenster).
* Bezorgde pakketten worden niet opnieuw opgevraagd en na het ingestelde aantal dagen verwijderd (0 = bewaren).

[← Alle vervoerders](README.md) · [Flow-kaarten](../flows.md) · [Flow-tokens](../tokens.md) · [Problemen oplossen](../troubleshooting.md) · [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
