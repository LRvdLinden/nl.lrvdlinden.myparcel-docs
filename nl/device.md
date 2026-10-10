# Apparaatgegevens

Elke vervoerder is een eigen apparaat in Homey. Hieronder de apparaatwaarden (capabilities) per vervoerder in v0.3.7. De beschikbaarheid van gegevens verschilt per vervoerder en pakket; niet elk veld is altijd gevuld en MyParcel verzint nooit gegevens die de vervoerder niet levert.

Gemeenschappelijk:

* **Verbindingsstatus** (`myparcel_connection_status`) – op (bijna) elk apparaat; wordt het apparaat *Niet verbonden*, dan verschijnt er een melding in de Tijdlijn.
* Een netwerkstoring toont een waarschuwing met de laatst bekende gegevens in plaats van het apparaat onbeschikbaar te maken.
* Bezorgde pakketten blijven het ingestelde aantal dagen zichtbaar (instelling *Bezorgde pakketten tonen (dagen)*).
* Slim pollen: elke 15 minuten als een bezorging dichtbij is, anders elke 45 minuten, rustig in de nacht.

## PostNL

| ID | Naam | Type |
|---|---|---|
| `postnl_mail_expected` | Post verwacht | ja/nee |
| `postnl_mail_count` | Poststukken | getal |
| `postnl_package_count` | Pakketten onderweg | getal |
| `postnl_next_delivery` | Volgende bezorging | tekst |
| `postnl_delivery_date` | Bezorgdatum | tekst |
| `postnl_delivery_window` | Bezorgvenster | tekst |
| `postnl_package_status` | Pakketstatus | tekst |
| `postnl_package_sender` | Afzender pakket | tekst |
| `postnl_package_receiver` | Ontvanger pakket | tekst |
| `postnl_package_tracking` | Trackingnummer | tekst |
| `postnl_package_event` | Laatste pakketgebeurtenis | tekst |
| `postnl_package_status_time` | Tijdstip pakketstatus | tekst |
| `postnl_package_delivered` | Pakket bezorgd | ja/nee |
| `postnl_package_shipment_type` | Type zending | tekst |
| `postnl_package_weight` | Gewicht pakket | tekst |
| `postnl_package_weight_kg` | Gewicht pakket (kg) | getal |
| `postnl_package_length` | Lengte pakket | getal |
| `postnl_package_width` | Breedte pakket | getal |
| `postnl_package_height` | Hoogte pakket | getal |
| `postnl_package_status_history` | Volledige statusgeschiedenis | tekst |
| `postnl_package_observation_code` | ObservationCode | tekst |
| `postnl_package_canonical_status` | Canonieke status | tekst |
| `postnl_package_pickup` | Bezorging bij PostNL-punt | ja/nee |
| `postnl_package_pickup_point` | PostNL-punt | tekst |
| `postnl_package_dimensions` | Afmetingen pakket | tekst |
| `postnl_status` | Verbindingsstatus | tekst |
| `postnl_last_update` | Laatste update | tekst |

[PostNL →](carriers/postnl.md)

## DHL

| ID | Naam | Type |
|---|---|---|
| `dhl_parcel_count` | Actieve pakketten | getal |
| `dhl_status` | Status | tekst |
| `dhl_tracking_number` | Trackingnummer | tekst |
| `dhl_sender` | Afzender | tekst |
| `dhl_receiver` | Ontvanger | tekst |
| `dhl_delivery_date` | Bezorgdatum | tekst |
| `dhl_delivery_window` | Bezorgvenster | tekst |
| `dhl_next_delivery` | Volgende bezorging | tekst |
| `dhl_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `dhl_en_route_pickup_count` | Onderweg naar afhaalpunt | getal |
| `dhl_pickup_count` | Klaar om op te halen | getal |
| `dhl_pickup_point` | Afhaalpunt | tekst |
| `dhl_delivered_count` | Recent bezorgd | getal |
| `dhl_outgoing_count` | Verzonden pakketten onderweg | getal |
| `dhl_last_event` | Laatste gebeurtenis | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `dhl_last_update` | Laatste update | tekst |

[DHL →](carriers/dhl-parcel.md)

## DHL Express

| ID | Naam | Type |
|---|---|---|
| `dhl_express_parcel_count` | Actieve pakketten | getal |
| `dhl_express_total_count` | Totaal pakketten | getal |
| `dhl_express_status` | Status | tekst |
| `dhl_express_tracking` | Trackingnummer | tekst |
| `dhl_express_sender` | Afzender | tekst |
| `dhl_express_receiver` | Ontvanger | tekst |
| `dhl_express_delivery_date` | Bezorgdatum | tekst |
| `dhl_express_delivery_window` | Bezorgvenster | tekst |
| `dhl_express_next_delivery` | Volgende bezorging | tekst |
| `dhl_express_service` | Service | tekst |
| `dhl_express_origin` | Herkomst | tekst |
| `dhl_express_destination` | Bestemming | tekst |
| `dhl_express_pieces` | Colli | getal |
| `dhl_express_last_event` | Laatste gebeurtenis | tekst |
| `dhl_express_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `dhl_express_delivered_count` | Recent bezorgd | getal |
| `dhl_express_delivered` | Bezorgd | ja/nee |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `dhl_express_last_update` | Laatste update | tekst |

[DHL Express →](carriers/dhl-express.md)

## DPD

| ID | Naam | Type |
|---|---|---|
| `dpd_parcel_count` | Actieve pakketten | getal |
| `dpd_total_count` | Totaal pakketten | getal |
| `dpd_status` | Status | tekst |
| `dpd_tracking` | Trackingnummer | tekst |
| `dpd_sender` | Afzender | tekst |
| `dpd_receiver` | Ontvanger | tekst |
| `dpd_delivery_date` | Bezorgdatum | tekst |
| `dpd_delivery_window` | Bezorgvenster | tekst |
| `dpd_delivery_point` | Bezorgpunt | tekst |
| `dpd_weight` | Gewicht | tekst |
| `dpd_dimensions` | Afmetingen | tekst |
| `dpd_delivery_type` | Type bezorging | tekst |
| `dpd_last_event` | Laatste gebeurtenis | tekst |
| `dpd_direction` | Richting | tekst |
| `dpd_next_delivery` | Volgende bezorging | tekst |
| `dpd_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `dpd_en_route_pickup_count` | Onderweg naar ParcelShop | getal |
| `dpd_pickup_count` | Klaar om op te halen | getal |
| `dpd_delivered_count` | Recent bezorgd | getal |
| `dpd_outgoing_count` | Verzonden pakketten onderweg | getal |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `dpd_last_update` | Laatste update | tekst |

[DPD →](carriers/dpd.md)

## UPS

| ID | Naam | Type |
|---|---|---|
| `ups_parcel_count` | Actieve pakketten | getal |
| `ups_total_count` | Totaal pakketten | getal |
| `ups_status` | Status | tekst |
| `ups_tracking` | Volgend trackingnummer | tekst |
| `ups_sender` | Afzender | tekst |
| `ups_delivery_date` | Verwachte bezorging | tekst |
| `ups_delivery_window` | Bezorgvenster | tekst |
| `ups_service` | UPS-service | tekst |
| `ups_ship_from` | Verzonden vanaf | tekst |
| `ups_ship_to` | Bestemming | tekst |
| `ups_access_point` | UPS Access Point | tekst |
| `ups_last_event` | Laatste gebeurtenis | tekst |
| `ups_country` | UPS-land | tekst |
| `ups_locale` | UPS-locale | tekst |
| `ups_account_status` | Verbindingsstatus | tekst |
| `ups_last_update` | Laatste update | tekst |

[UPS →](carriers/ups.md)

## Budbee

| ID | Naam | Type |
|---|---|---|
| `budbee_parcel_count` | Actieve pakketten | getal |
| `budbee_status` | Status | tekst |
| `budbee_tracking` | Trackingnummer | tekst |
| `budbee_sender` | Afzender | tekst |
| `budbee_delivery_date` | Bezorgdatum | tekst |
| `budbee_delivery_window` | Bezorgvenster | tekst |
| `budbee_next_delivery` | Volgende bezorging | tekst |
| `budbee_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `budbee_en_route_pickup_count` | Onderweg naar afhaalpunt | getal |
| `budbee_pickup_count` | Klaar om op te halen | getal |
| `budbee_pickup_point` | Afhaalpunt | tekst |
| `budbee_delivered_count` | Recent bezorgd | getal |
| `budbee_outgoing_count` | Verzonden pakketten onderweg | getal |
| `budbee_last_event` | Laatste gebeurtenis | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `budbee_last_update` | Laatste update | tekst |

[Budbee →](carriers/budbee.md)

## Vinted Go

| ID | Naam | Type |
|---|---|---|
| `homerr_parcel_count` | Pakketten onderweg | getal |
| `homerr_status` | Status | tekst |
| `homerr_tracking` | Trackingnummer | tekst |
| `homerr_item` | Artikel | tekst |
| `homerr_pickup_count` | Klaar om op te halen | getal |
| `homerr_en_route_pickup_count` | Onderweg naar afhaalpunt | getal |
| `homerr_pickup_point` | Afhaalpunt | tekst |
| `homerr_pickup_code` | Ophaalcode | tekst |
| `homerr_delivered_count` | Recent bezorgd | getal |
| `homerr_outgoing_count` | Verzonden pakketten onderweg | getal |
| `homerr_last_event` | Laatste gebeurtenis | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `homerr_last_update` | Laatste update | tekst |

[Vinted Go →](carriers/homerr.md)

## FedEx

| ID | Naam | Type |
|---|---|---|
| `fedex_parcel_count` | Pakketten onderweg | getal |
| `fedex_status` | Status | tekst |
| `fedex_tracking` | Trackingnummer | tekst |
| `fedex_sender` | Afzender | tekst |
| `fedex_receiver` | Ontvanger | tekst |
| `fedex_delivery_date` | Bezorgdatum | tekst |
| `fedex_delivery_window` | Bezorgvenster | tekst |
| `fedex_next_delivery` | Volgende bezorging | tekst |
| `fedex_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `fedex_pickup_count` | Klaar om op te halen | getal |
| `fedex_pickup_point` | Afhaalpunt | tekst |
| `fedex_delivered_count` | Recent bezorgd | getal |
| `fedex_last_event` | Laatste gebeurtenis | tekst |
| `fedex_service` | Dienst | tekst |
| `fedex_weight` | Gewicht | tekst |
| `fedex_dimensions` | Afmetingen | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `fedex_last_update` | Laatste update | tekst |

[FedEx →](carriers/fedex.md)

## GLS

| ID | Naam | Type |
|---|---|---|
| `gls_parcel_count` | Pakketten onderweg | getal |
| `gls_status` | Status | tekst |
| `gls_next_delivery` | Volgende bezorging | tekst |
| `gls_delivery_window` | Bezorgvenster | tekst |
| `gls_tracking` | Trackingnummer | tekst |
| `gls_sender` | Afzender | tekst |
| `gls_receiver` | Ontvanger | tekst |
| `gls_last_event` | Laatste gebeurtenis | tekst |
| `gls_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `gls_en_route_pickup_count` | Onderweg naar ParcelShop | getal |
| `gls_pickup_count` | Klaar om op te halen | getal |
| `gls_pickup_point` | ParcelShop | tekst |
| `gls_delivered_count` | Recent bezorgd | getal |
| `gls_weight` | Gewicht | getal |
| `gls_dimensions` | Afmetingen | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `gls_last_update` | Laatste update | tekst |

[GLS →](carriers/gls.md)

## InPost

| ID | Naam | Type |
|---|---|---|
| `inpost_uk_parcel_count` | Actieve pakketten | getal |
| `inpost_uk_status` | Status | tekst |
| `inpost_uk_tracking` | Trackingnummer | tekst |
| `inpost_uk_sender` | Afzender | tekst |
| `inpost_uk_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `inpost_uk_pickup_count` | Klaar om op te halen | getal |
| `inpost_uk_pickup_point` | Afhaalpunt | tekst |
| `inpost_uk_pickup_code` | Ophaalcode | tekst |
| `inpost_uk_delivered_count` | Recent bezorgd | getal |
| `inpost_uk_last_event` | Laatste gebeurtenis | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `inpost_uk_last_update` | Laatste update | tekst |

[InPost →](carriers/inpost-uk.md)

## bpost

| ID | Naam | Type |
|---|---|---|
| `bpost_parcel_count` | Actieve pakketten | getal |
| `bpost_total_count` | Totaal pakketten | getal |
| `bpost_status` | Status | tekst |
| `bpost_tracking` | Volgend trackingnummer | tekst |
| `bpost_sender` | Afzender | tekst |
| `bpost_delivery_date` | Verwachte bezorging | tekst |
| `bpost_delivery_window` | Bezorgvenster | tekst |
| `bpost_delivery_point` | Afleverpunt | tekst |
| `bpost_weight` | Gewicht | tekst |
| `bpost_product` | Product | tekst |
| `bpost_partner` | Bezorgpartner | tekst |
| `bpost_last_event` | Laatste gebeurtenis | tekst |
| `bpost_receiver` | Ontvanger | tekst |
| `bpost_next_delivery` | Volgende bezorging | tekst |
| `bpost_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `bpost_en_route_pickup_count` | Onderweg naar afhaalpunt | getal |
| `bpost_pickup_count` | Klaar om op te halen | getal |
| `bpost_delivered_count` | Recent bezorgd | getal |
| `bpost_outgoing_count` | Verzonden pakketten onderweg | getal |
| `bpost_dimensions` | Afmetingen | tekst |
| `bpost_letter_count` | Aangekondigde brieven | getal |
| `bpost_last_letter` | Laatste brief | tekst |
| `bpost_account_status` | Verbindingsstatus | tekst |
| `bpost_last_update` | Laatste update | tekst |

[bpost →](carriers/bpost.md)

## Royal Mail

| ID | Naam | Type |
|---|---|---|
| `royal_mail_parcel_count` | Actieve pakketten | getal |
| `royal_mail_status` | Status | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `royal_mail_last_update` | Laatste update | tekst |

[Royal Mail →](carriers/royal-mail.md)

## Post & DHL Duitsland

| ID | Naam | Type |
|---|---|---|
| `dhl_de_parcel_count` | Actieve pakketten | getal |
| `dhl_de_status` | Status | tekst |
| `dhl_de_tracking` | Trackingnummer | tekst |
| `dhl_de_sender` | Afzender | tekst |
| `dhl_de_delivery_date` | Bezorgdatum | tekst |
| `dhl_de_delivery_window` | Bezorgvenster | tekst |
| `dhl_de_next_delivery` | Volgende bezorging | tekst |
| `dhl_de_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `dhl_de_pickup_count` | Klaar om op te halen | getal |
| `dhl_de_pickup_point` | Afhaalpunt | tekst |
| `dhl_de_delivered_count` | Recent bezorgd | getal |
| `dhl_de_outgoing_count` | Verzonden pakketten onderweg | getal |
| `dhl_de_last_event` | Laatste gebeurtenis | tekst |
| `dhl_de_mail_count` | Verwachte post | getal |
| `dhl_de_postnumber` | Postnummer | tekst |
| `dhl_de_account_status` | Verbindingsstatus | tekst |
| `dhl_de_mail_status` | Briefaankondiging | tekst |
| `dhl_de_last_update` | Laatste update | tekst |

[Post & DHL Duitsland →](carriers/post-dhl-de.md)

## Ampère

| ID | Naam | Type |
|---|---|---|
| `ampere_parcel_count` | Actieve pakketten | getal |
| `ampere_total_count` | Totaal pakketten | getal |
| `ampere_status` | Status | tekst |
| `ampere_tracking` | Trackingnummer | tekst |
| `ampere_sender` | Afzender | tekst |
| `ampere_delivery_date` | Bezorgdatum | tekst |
| `ampere_delivery_window` | Bezorgvenster | tekst |
| `ampere_window_start` | Start bezorgvenster | tekst |
| `ampere_window_end` | Einde bezorgvenster | tekst |
| `ampere_delivered` | Bezorgd | ja/nee |
| `ampere_details_url` | Track & Trace-URL | tekst |
| `ampere_receiver` | Ontvanger | tekst |
| `ampere_next_delivery` | Volgende bezorging | tekst |
| `ampere_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `ampere_delivered_count` | Recent bezorgd | getal |
| `ampere_last_event` | Laatste gebeurtenis | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `ampere_last_update` | Laatste update | tekst |

[Ampère →](carriers/ampere.md)

## Trunkrs

| ID | Naam | Type |
|---|---|---|
| `trunkrs_parcel_count` | Actieve pakketten | getal |
| `trunkrs_status` | Status | tekst |
| `trunkrs_tracking` | Trackingnummer | tekst |
| `trunkrs_sender` | Afzender | tekst |
| `trunkrs_receiver` | Ontvanger | tekst |
| `trunkrs_delivery_date` | Bezorgdatum | tekst |
| `trunkrs_delivery_window` | Bezorgvenster | tekst |
| `trunkrs_next_delivery` | Volgende bezorging | tekst |
| `trunkrs_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `trunkrs_delivered_count` | Recent bezorgd | getal |
| `trunkrs_last_event` | Laatste gebeurtenis | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `trunkrs_last_update` | Laatste update | tekst |

[Trunkrs →](carriers/trunkrs.md)

## Dynalogic

| ID | Naam | Type |
|---|---|---|
| `dynalogic_parcel_count` | Actieve pakketten | getal |
| `dynalogic_status` | Status | tekst |
| `dynalogic_tracking` | Trackingnummer | tekst |
| `dynalogic_sender` | Afzender | tekst |
| `dynalogic_receiver` | Ontvanger | tekst |
| `dynalogic_delivery_date` | Bezorgdatum | tekst |
| `dynalogic_delivery_window` | Bezorgvenster | tekst |
| `dynalogic_next_delivery` | Volgende bezorging | tekst |
| `dynalogic_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `dynalogic_delivered_count` | Recent bezorgd | getal |
| `dynalogic_last_event` | Laatste gebeurtenis | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `dynalogic_last_update` | Laatste update | tekst |

[Dynalogic →](carriers/dynalogic.md)

## Dragonfly / Intelcom

| ID | Naam | Type |
|---|---|---|
| `dragonfly_parcel_count` | Actieve pakketten | getal |
| `dragonfly_status` | Status | tekst |
| `dragonfly_tracking` | Trackingnummer | tekst |
| `dragonfly_sender` | Afzender | tekst |
| `dragonfly_delivery_date` | Bezorgdatum | tekst |
| `dragonfly_delivery_window` | Bezorgvenster | tekst |
| `dragonfly_next_delivery` | Volgende bezorging | tekst |
| `dragonfly_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `dragonfly_delivered_count` | Recent bezorgd | getal |
| `dragonfly_outgoing_count` | Verzonden pakketten onderweg | getal |
| `dragonfly_last_event` | Laatste gebeurtenis | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `dragonfly_last_update` | Laatste update | tekst |

[Dragonfly / Intelcom →](carriers/dragonfly.md)

## Mondial Relay

| ID | Naam | Type |
|---|---|---|
| `mondial_relay_parcel_count` | Actieve pakketten | getal |
| `mondial_relay_status` | Status | tekst |
| `mondial_relay_tracking` | Trackingnummer | tekst |
| `mondial_relay_sender` | Afzender | tekst |
| `mondial_relay_delivery_date` | Bezorgdatum | tekst |
| `mondial_relay_delivery_window` | Bezorgvenster | tekst |
| `mondial_relay_next_delivery` | Volgende bezorging | tekst |
| `mondial_relay_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `mondial_relay_delivered_count` | Recent bezorgd | getal |
| `mondial_relay_outgoing_count` | Verzonden pakketten onderweg | getal |
| `mondial_relay_last_event` | Laatste gebeurtenis | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `mondial_relay_last_update` | Laatste update | tekst |

[Mondial Relay →](carriers/mondial-relay.md)

## Amazon

| ID | Naam | Type |
|---|---|---|
| `amazon_parcel_count` | Actieve pakketten | getal |
| `amazon_status` | Status | tekst |
| `amazon_tracking` | Trackingnummer | tekst |
| `amazon_item` | Artikel | tekst |
| `amazon_carrier` | Bezorgdienst | tekst |
| `amazon_delivery_date` | Bezorgdatum | tekst |
| `amazon_next_delivery` | Volgende bezorging | tekst |
| `amazon_out_for_delivery_count` | Onderweg voor bezorging | getal |
| `amazon_pickup_count` | Klaar om op te halen | getal |
| `amazon_delivered_count` | Recent bezorgd | getal |
| `amazon_last_event` | Laatste gebeurtenis | tekst |
| `myparcel_connection_status` | Verbindingsstatus | tekst |
| `amazon_last_update` | Laatste update | tekst |

[Amazon →](carriers/amazon.md)
