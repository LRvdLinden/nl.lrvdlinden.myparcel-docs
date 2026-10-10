# Flow-kaarten

Overzicht van alle Flow-kaarten in MyParcel v0.3.7, per vervoerder. Elke kaart hoort bij het apparaat van die vervoerder; je kiest het apparaat in de kaart. In totaal: **158 triggers, 121 condities en 58 acties**.

* **Wanneer**-kaarten gaan één keer per wijziging af, ook na een herstart van de app (bestaande pakketten worden bij de eerste synchronisatie na een update stil vastgelegd).
* Condities met *is/is niet* kun je in Homey omkeren.
* Acties **Volg pakket…**, **Stop met volgen…** en **Verwijder bezorgde pakketten** beheren de lijst met trackingnummers zonder de apparaatinstellingen te openen.
* De volledige NL/EN-titels, argumenten en tokens per kaart staan op de pagina van elke [vervoerder](carriers/README.md); de tokens op [Flow-tokens](tokens.md).

## Alle vervoerders

* **Verbindingsstatus is gewijzigd** (`connection_status_changed`) – voor elk MyParcel-apparaat, met tokens *Verbonden*, *Verbindingsstatus* en *Vervoerder*.

## PostNL

[Vervoerderspagina →](carriers/postnl.md)

**Wanneer… (triggers)**

* Er is nieuwe post onderweg (`new_mail`)
* Er is een nieuw pakket gevonden (`new_package`)
* Er is een bezorgvenster bekend (`delivery_window_known`)
* De status van een pakket is gewijzigd (`package_status_changed`)
* PostNL-synchronisatie is mislukt (`sync_failed`)
* De PostNL-aanmelding is verlopen (`login_expired`)
* Een pakket is bezorgd (`package_delivered`)
* Het bezorgvenster van een pakket is gewijzigd (`delivery_window_changed`)
* Er is een nieuwe PostNL-pakketgebeurtenis (`package_event_changed`)
* Het gewicht van een pakket is bekend (`package_weight_known`)
* De afmetingen van een pakket zijn bekend (`package_dimensions_known`)

**En… (condities)**

* Post wordt/wordt niet verwacht (`mail_expected`)
* Er zijn/zijn geen pakketten onderweg (`packages_underway`)
* Er is/is geen bezorgvenster bekend (`delivery_window_known`)
* PostNL is/is niet verbonden (`postnl_connected`)
* Het huidige pakket heeft/heeft geen gewichtsinformatie (`package_has_weight`)
* Het huidige pakket heeft/heeft geen afmetingen (`package_has_dimensions`)
* De huidige pakketstatus is/is niet (`package_status_is`)

**Dan… (acties)**

* Synchroniseer PostNL (`sync_now`)

## DHL

[Vervoerderspagina →](carriers/dhl-parcel.md)

**Wanneer… (triggers)**

* Nieuw DHL-pakket (`dhl_new_package`)
* Zendingstatus is gewijzigd (`status_changed`)
* Nieuwe DHL-trackinggebeurtenis (`dhl_package_event_changed`)
* DHL-pakket onderweg voor bezorging (`dhl_out_for_delivery`)
* DHL-pakket klaar om op te halen (`dhl_ready_for_pickup`)
* Zending is bezorgd (`shipment_delivered`)
* Probleem of retour bij DHL-pakket (`dhl_package_problem`)
* Status van verzonden DHL-pakket gewijzigd (`dhl_outgoing_status_changed`)
* Verzonden DHL-pakket bezorgd (`dhl_outgoing_delivered`)
* Bezorgvenster bekend of gewijzigd (`dhl_delivery_window_changed`)

**En… (condities)**

* Zending is bezorgd (`is_delivered`)
* Bezorgvenster is/is niet bekend (`dhl_delivery_window_known`)
* Er zijn/zijn geen DHL-pakketten onderweg (`dhl_packages_underway`)
* Er is een/geen DHL-pakket onderweg voor bezorging (`dhl_out_for_delivery_now`)
* Er ligt een/geen DHL-pakket klaar om op te halen (`dhl_ready_for_pickup_now`)
* Een DHL-pakket heeft/heeft niet status… (`dhl_any_status_is`)
* DHL-pakket… is/is niet bezorgd (`dhl_parcel_is_delivered`)
* DHL-pakket… wordt wel/niet gevolgd (`dhl_is_tracking`)
* Er zijn/zijn geen verzonden DHL-pakketten onderweg (`dhl_outgoing_underway`)

**Dan… (acties)**

* Zending vernieuwen (`refresh_shipment`)
* Volg DHL-pakket… (`dhl_track_parcel`)
* Stop met volgen van DHL-pakket… (`dhl_untrack_parcel`)
* Verwijder bezorgde DHL-pakketten (`dhl_remove_delivered`)

## DHL Express

[Vervoerderspagina →](carriers/dhl-express.md)

**Wanneer… (triggers)**

* Nieuw DHL Express-pakket gevonden (`dhl_express_new_package`)
* Status DHL Express-pakket gewijzigd (`dhl_express_status_changed`)
* Nieuwe DHL Express-trackinggebeurtenis (`dhl_express_package_event_changed`)
* DHL Express-pakket onderweg voor bezorging (`dhl_express_out_for_delivery`)
* DHL Express-pakket bezorgd (`dhl_express_delivered`)
* Probleem of retour bij DHL Express-pakket (`dhl_express_package_problem`)
* Status van verzonden DHL Express-pakket gewijzigd (`dhl_express_outgoing_status_changed`)
* Verzonden DHL Express-pakket bezorgd (`dhl_express_outgoing_delivered`)
* DHL Express-bezorginformatie bijgewerkt (`dhl_express_delivery_updated`)

**En… (condities)**

* Er zijn DHL Express-pakketten onderweg (`dhl_express_packages_underway`)
* DHL Express is/is niet verbonden (`dhl_express_is_connected`)
* DHL Express-bezorgvenster is/is niet bekend (`dhl_express_delivery_window_known`)
* Er is een/geen DHL Express-pakket onderweg voor bezorging (`dhl_express_out_for_delivery_now`)
* Een DHL Express-pakket heeft/heeft niet status… (`dhl_express_any_status_is`)
* DHL Express-pakket… is/is niet bezorgd (`dhl_express_parcel_is_delivered`)
* DHL Express-pakket… wordt wel/niet gevolgd (`dhl_express_is_tracking`)
* Er zijn/zijn geen verzonden DHL Express-pakketten onderweg (`dhl_express_outgoing_underway`)

**Dan… (acties)**

* Vernieuw DHL Express (`dhl_express_refresh`)
* Volg DHL Express-pakket… (`dhl_express_track_parcel`)
* Stop met volgen van DHL Express-pakket… (`dhl_express_untrack_parcel`)
* Verwijder bezorgde DHL Express-pakketten (`dhl_express_remove_delivered`)

## DPD

[Vervoerderspagina →](carriers/dpd.md)

**Wanneer… (triggers)**

* Nieuw DPD-pakket (`dpd_new_package`)
* DPD-pakketstatus gewijzigd (`dpd_status_changed`)
* Nieuwe DPD-trackinggebeurtenis (`dpd_package_event_changed`)
* DPD-pakket onderweg voor bezorging (`dpd_out_for_delivery`)
* Bezorgvenster bekend of gewijzigd (`dpd_delivery_window_changed`)
* DPD-bezorginformatie bijgewerkt (`dpd_delivery_updated`)
* DPD-pakket klaar om op te halen (`dpd_ready_for_pickup`)
* DPD-pakket bezorgd (`dpd_delivered`)
* Probleem of retour bij DPD-pakket (`dpd_package_problem`)
* Status van verzonden DPD-pakket gewijzigd (`dpd_outgoing_status_changed`)
* Verzonden DPD-pakket bezorgd (`dpd_outgoing_delivered`)

**En… (condities)**

* Er zijn/zijn geen DPD-pakketten onderweg (`dpd_packages_underway`)
* Bezorgvenster is/is niet bekend (`dpd_delivery_window_known`)
* Er is een/geen DPD-pakket onderweg voor bezorging (`dpd_out_for_delivery_now`)
* Er ligt een/geen DPD-pakket klaar om op te halen (`dpd_ready_for_pickup_now`)
* Een DPD-pakket heeft/heeft niet status… (`dpd_any_status_is`)
* DPD-pakket… is/is niet bezorgd (`dpd_parcel_is_delivered`)
* Er zijn/zijn geen verzonden DPD-pakketten onderweg (`dpd_outgoing_underway`)

**Dan… (acties)**

* Vernieuw DPD (`dpd_refresh`)

## UPS

[Vervoerderspagina →](carriers/ups.md)

**Wanneer… (triggers)**

* Nieuw UPS-pakket (`ups_new_package`)
* UPS-pakketstatus gewijzigd (`ups_status_changed`)
* UPS-pakket bezorgd (`ups_delivered`)
* Bezorgvenster bekend of gewijzigd (`ups_delivery_window_changed`)

**En… (condities)**

* Er zijn UPS-pakketten onderweg (`ups_packages_underway`)
* UPS-account is gekoppeld (`ups_account_connected`)
* Bezorgvenster is/is niet bekend (`ups_delivery_window_known`)

**Dan… (acties)**

* Vernieuw UPS (`ups_refresh`)

## Budbee

[Vervoerderspagina →](carriers/budbee.md)

**Wanneer… (triggers)**

* Nieuw Budbee-pakket (`budbee_new_package`)
* Budbee-pakketstatus gewijzigd (`budbee_status_changed`)
* Nieuwe Budbee-trackinggebeurtenis (`budbee_package_event_changed`)
* Budbee-pakket onderweg voor bezorging (`budbee_out_for_delivery`)
* Budbee-pakket klaar om op te halen (`budbee_ready_for_pickup`)
* Budbee-pakket bezorgd (`budbee_delivered`)
* Probleem of retour bij Budbee-pakket (`budbee_package_problem`)
* Status van verzonden Budbee-pakket gewijzigd (`budbee_outgoing_status_changed`)
* Verzonden Budbee-pakket bezorgd (`budbee_outgoing_delivered`)
* Bezorgvenster bekend of gewijzigd (`budbee_delivery_window_changed`)

**En… (condities)**

* Er zijn Budbee-pakketten onderweg (`budbee_packages_underway`)
* Bezorgvenster is/is niet bekend (`budbee_delivery_window_known`)
* Er is een/geen Budbee-pakket onderweg voor bezorging (`budbee_out_for_delivery_now`)
* Er ligt een/geen Budbee-pakket klaar om op te halen (`budbee_ready_for_pickup_now`)
* Een Budbee-pakket heeft/heeft niet status… (`budbee_any_status_is`)
* Budbee-pakket… is/is niet bezorgd (`budbee_parcel_is_delivered`)
* Budbee-pakket… wordt wel/niet gevolgd (`budbee_is_tracking`)
* Er zijn/zijn geen verzonden Budbee-pakketten onderweg (`budbee_outgoing_underway`)

**Dan… (acties)**

* Vernieuw Budbee (`budbee_refresh`)
* Volg Budbee-pakket… (`budbee_track_parcel`)
* Stop met volgen van Budbee-pakket… (`budbee_untrack_parcel`)
* Verwijder bezorgde Budbee-pakketten (`budbee_remove_delivered`)

## Vinted Go

[Vervoerderspagina →](carriers/homerr.md)

**Wanneer… (triggers)**

* Nieuw Vinted Go-pakket (`homerr_new_package`)
* Vinted Go-pakketstatus gewijzigd (`homerr_package_status_changed`)
* Nieuwe Vinted Go-trackinggebeurtenis (`homerr_package_event_changed`)
* Vinted Go-pakket onderweg voor bezorging (`homerr_out_for_delivery`)
* Vinted Go-pakket klaar om op te halen (`homerr_ready_for_pickup`)
* Vinted Go-pakket bezorgd (`homerr_delivered`)
* Probleem of retour bij Vinted Go-pakket (`homerr_package_problem`)
* Status van verzonden Vinted Go-pakket gewijzigd (`homerr_outgoing_status_changed`)
* Verzonden Vinted Go-pakket bezorgd (`homerr_outgoing_delivered`)

**En… (condities)**

* Er zijn Vinted Go-pakketten onderweg (`homerr_packages_underway`)
* Er is een/geen Vinted Go-pakket onderweg voor bezorging (`homerr_out_for_delivery_now`)
* Er ligt een/geen Vinted Go-pakket klaar om op te halen (`homerr_ready_for_pickup_now`)
* Een Vinted Go-pakket heeft/heeft niet status… (`homerr_any_status_is`)
* Vinted Go-pakket… is/is niet bezorgd (`homerr_parcel_is_delivered`)
* Er zijn/zijn geen verzonden Vinted Go-pakketten onderweg (`homerr_outgoing_underway`)

**Dan… (acties)**

* Vernieuw Vinted Go-pakketten (`homerr_refresh`)
* Verwijder bezorgde Vinted Go-pakketten (`homerr_remove_delivered`)

## FedEx

[Vervoerderspagina →](carriers/fedex.md)

**Wanneer… (triggers)**

* Nieuw FedEx-pakket (`fedex_new_package`)
* FedEx-pakketstatus gewijzigd (`fedex_status_changed`)
* Nieuwe FedEx-trackinggebeurtenis (`fedex_package_event_changed`)
* FedEx-pakket onderweg voor bezorging (`fedex_out_for_delivery`)
* FedEx-pakket klaar om op te halen (`fedex_ready_for_pickup`)
* FedEx-pakket bezorgd (`fedex_delivered`)
* Probleem of retour bij FedEx-pakket (`fedex_package_problem`)
* FedEx-bezorgtijd gewijzigd (`fedex_delivery_updated`)

**En… (condities)**

* Er zijn FedEx-pakketten onderweg (`fedex_packages_underway`)
* Er is een/geen FedEx-pakket onderweg voor bezorging (`fedex_out_for_delivery_now`)
* Er ligt een/geen FedEx-pakket klaar om op te halen (`fedex_ready_for_pickup_now`)
* Een FedEx-pakket heeft/heeft niet status… (`fedex_any_status_is`)
* FedEx-pakket… is/is niet bezorgd (`fedex_parcel_is_delivered`)
* FedEx-pakket… wordt wel/niet gevolgd (`fedex_is_tracking`)

**Dan… (acties)**

* Vernieuw FedEx (`fedex_refresh`)
* Volg FedEx-pakket… (`fedex_track_parcel`)
* Stop met volgen van FedEx-pakket… (`fedex_untrack_parcel`)
* Verwijder bezorgde FedEx-pakketten (`fedex_remove_delivered`)

## GLS

[Vervoerderspagina →](carriers/gls.md)

**Wanneer… (triggers)**

* Nieuw GLS-pakket (`gls_new_package`)
* Status GLS-pakket gewijzigd (`gls_status_changed`)
* Nieuwe GLS-trackinggebeurtenis (`gls_package_event_changed`)
* GLS-pakket onderweg voor bezorging (`gls_out_for_delivery`)
* Bezorgvenster bekend of gewijzigd (`gls_delivery_window_changed`)
* GLS-pakket klaar om op te halen (`gls_ready_for_pickup`)
* GLS-pakket bezorgd (`gls_package_delivered`)
* Probleem of retour bij GLS-pakket (`gls_package_problem`)

**En… (condities)**

* Er zijn/zijn geen GLS-pakketten onderweg (`gls_packages_underway`)
* Bezorgvenster is/is niet bekend (`gls_delivery_window_known`)
* Er is een/geen GLS-pakket onderweg voor bezorging (`gls_out_for_delivery_now`)
* Er ligt een/geen GLS-pakket klaar om op te halen (`gls_ready_for_pickup_now`)
* Een GLS-pakket heeft/heeft niet status… (`gls_any_status_is`)
* GLS-pakket… is/is niet bezorgd (`gls_parcel_is_delivered`)
* GLS-pakket… wordt wel/niet gevolgd (`gls_is_tracking`)

**Dan… (acties)**

* Vernieuw GLS (`gls_refresh`)
* Volg GLS-pakket… (`gls_track_parcel`)
* Stop met volgen van GLS-pakket… (`gls_untrack_parcel`)
* Verwijder bezorgde GLS-pakketten (`gls_remove_delivered`)

## InPost

[Vervoerderspagina →](carriers/inpost-uk.md)

**Wanneer… (triggers)**

* Nieuw InPost UK-pakket (`inpost_uk_new_package`)
* InPost UK-pakketstatus gewijzigd (`inpost_uk_status_changed`)
* Nieuwe InPost-trackinggebeurtenis (`inpost_uk_package_event_changed`)
* InPost-pakket onderweg voor bezorging (`inpost_uk_out_for_delivery`)
* InPost-pakket klaar om op te halen (`inpost_uk_ready_for_pickup`)
* InPost-pakket bezorgd (`inpost_uk_delivered`)
* Probleem of retour bij InPost-pakket (`inpost_uk_package_problem`)

**En… (condities)**

* Er zijn InPost UK-pakketten onderweg (`inpost_uk_packages_underway`)
* Er is een/geen InPost-pakket onderweg voor bezorging (`inpost_uk_out_for_delivery_now`)
* Er ligt een/geen InPost-pakket klaar om op te halen (`inpost_uk_ready_for_pickup_now`)
* Een InPost-pakket heeft/heeft niet status… (`inpost_uk_any_status_is`)
* InPost-pakket… is/is niet bezorgd (`inpost_uk_parcel_is_delivered`)
* InPost-pakket… wordt wel/niet gevolgd (`inpost_uk_is_tracking`)

**Dan… (acties)**

* Vernieuw InPost UK (`inpost_uk_refresh`)
* Volg InPost-pakket… (`inpost_uk_track_parcel`)
* Stop met volgen van InPost-pakket… (`inpost_uk_untrack_parcel`)
* Verwijder bezorgde InPost-pakketten (`inpost_uk_remove_delivered`)

## bpost

[Vervoerderspagina →](carriers/bpost.md)

**Wanneer… (triggers)**

* Nieuw bpost-pakket (`bpost_new_package`)
* bpost-pakketstatus gewijzigd (`bpost_status_changed`)
* Nieuwe bpost-trackinggebeurtenis (`bpost_package_event_changed`)
* bpost-pakket onderweg voor bezorging (`bpost_out_for_delivery`)
* bpost-pakket klaar om op te halen (`bpost_ready_for_pickup`)
* bpost-pakket bezorgd (`bpost_delivered`)
* Probleem of retour bij bpost-pakket (`bpost_package_problem`)
* Status van verzonden bpost-pakket gewijzigd (`bpost_outgoing_status_changed`)
* Verzonden bpost-pakket bezorgd (`bpost_outgoing_delivered`)
* bpost-bezorginformatie bijgewerkt (`bpost_delivery_updated`)
* bpost-brief aangekondigd (Mail Ahead) (`bpost_letter_announced`)
* Bezorgvenster bekend of gewijzigd (`bpost_delivery_window_changed`)

**En… (condities)**

* Er zijn bpost-pakketten onderweg (`bpost_packages_underway`)
* My bpost-account is gekoppeld (`bpost_account_connected`)
* Bezorgvenster is/is niet bekend (`bpost_delivery_window_known`)
* Er is een/geen bpost-pakket onderweg voor bezorging (`bpost_out_for_delivery_now`)
* Er ligt een/geen bpost-pakket klaar om op te halen (`bpost_ready_for_pickup_now`)
* Een bpost-pakket heeft/heeft niet status… (`bpost_any_status_is`)
* bpost-pakket… is/is niet bezorgd (`bpost_parcel_is_delivered`)
* bpost-pakket… wordt wel/niet gevolgd (`bpost_is_tracking`)
* Er zijn/zijn geen verzonden bpost-pakketten onderweg (`bpost_outgoing_underway`)

**Dan… (acties)**

* Vernieuw bpost (`bpost_refresh`)
* Volg bpost-pakket… (`bpost_track_parcel`)
* Stop met volgen van bpost-pakket… (`bpost_untrack_parcel`)
* Verwijder bezorgde bpost-pakketten (`bpost_remove_delivered`)

## Royal Mail

[Vervoerderspagina →](carriers/royal-mail.md)

**Wanneer… (triggers)**

* Nieuw Royal Mail-pakket (`royal_mail_new_package`)
* Royal Mail-pakketstatus gewijzigd (`royal_mail_status_changed`)

**En… (condities)**

* Er zijn Royal Mail-pakketten onderweg (`royal_mail_packages_underway`)

**Dan… (acties)**

* Vernieuw Royal Mail (`royal_mail_refresh`)

## Post & DHL Duitsland

[Vervoerderspagina →](carriers/post-dhl-de.md)

**Wanneer… (triggers)**

* Nieuw DHL-pakket (`dhl_de_new_package`)
* Status DHL-pakket gewijzigd (`dhl_de_status_changed`)
* Nieuwe DHL-trackinggebeurtenis (`dhl_de_package_event_changed`)
* DHL-pakket onderweg voor bezorging (`dhl_de_out_for_delivery`)
* DHL-pakket klaar om op te halen (`dhl_de_ready_for_pickup`)
* DHL-pakket bezorgd (`dhl_de_delivered`)
* Probleem of retour bij DHL-pakket (`dhl_de_package_problem`)
* Status van verzonden DHL-pakket gewijzigd (`dhl_de_outgoing_status_changed`)
* Verzonden DHL-pakket bezorgd (`dhl_de_outgoing_delivered`)
* Bezorgvenster bekend of gewijzigd (`dhl_de_delivery_window_changed`)

**En… (condities)**

* Bezorgvenster is/is niet bekend (`dhl_de_delivery_window_known`)
* Er zijn/zijn geen DHL-pakketten onderweg (`dhl_de_packages_underway`)
* Er is een/geen DHL-pakket onderweg voor bezorging (`dhl_de_out_for_delivery_now`)
* Er ligt een/geen DHL-pakket klaar om op te halen (`dhl_de_ready_for_pickup_now`)
* Een DHL-pakket heeft/heeft niet status… (`dhl_de_any_status_is`)
* DHL-pakket… is/is niet bezorgd (`dhl_de_parcel_is_delivered`)
* DHL-pakket… wordt wel/niet gevolgd (`dhl_de_is_tracking`)
* Er zijn/zijn geen verzonden DHL-pakketten onderweg (`dhl_de_outgoing_underway`)

**Dan… (acties)**

* Vernieuw Post & DHL (`dhl_de_refresh`)
* Volg DHL-pakket… (`dhl_de_track_parcel`)
* Stop met volgen van DHL-pakket… (`dhl_de_untrack_parcel`)
* Verwijder bezorgde DHL-pakketten (`dhl_de_remove_delivered`)

## Ampère

[Vervoerderspagina →](carriers/ampere.md)

**Wanneer… (triggers)**

* Nieuw Ampère-pakket gevonden (`ampere_new_package`)
* Status van Ampère-pakket gewijzigd (`ampere_status_changed`)
* Nieuwe Ampère-trackinggebeurtenis (`ampere_package_event_changed`)
* Ampère-pakket onderweg voor bezorging (`ampere_out_for_delivery`)
* Ampère-pakket bezorgd (`ampere_delivered`)
* Probleem of retour bij Ampère-pakket (`ampere_package_problem`)
* Ampère-bezorginformatie bijgewerkt (`ampere_delivery_updated`)
* Ampère-bezorgvenster bekend of gewijzigd (`ampere_delivery_window_changed`)

**En… (condities)**

* Er zijn Ampère-pakketten onderweg (`ampere_packages_underway`)
* Ampère-bezorgvenster is/is niet bekend (`ampere_delivery_window_known`)
* Laatste Ampère-pakket is/is niet bezorgd (`ampere_is_delivered`)
* Ampère is/is niet verbonden (`ampere_is_connected`)
* Er is een/geen Ampère-pakket onderweg voor bezorging (`ampere_out_for_delivery_now`)
* Een Ampère-pakket heeft/heeft niet status… (`ampere_any_status_is`)
* Ampère-pakket… is/is niet bezorgd (`ampere_parcel_is_delivered`)
* Ampère-pakket… wordt wel/niet gevolgd (`ampere_is_tracking`)

**Dan… (acties)**

* Vernieuw Ampère (`ampere_refresh`)
* Volg Ampère-pakket via bol.com-link… (`ampere_track_parcel`)
* Stop met volgen van Ampère-pakket… (`ampere_untrack_parcel`)
* Verwijder bezorgde Ampère-pakketten (`ampere_remove_delivered`)

## Trunkrs

[Vervoerderspagina →](carriers/trunkrs.md)

**Wanneer… (triggers)**

* Nieuw Trunkrs-pakket (`trunkrs_new_package`)
* Status Trunkrs-pakket gewijzigd (`trunkrs_status_changed`)
* Nieuwe Trunkrs-trackinggebeurtenis (`trunkrs_package_event_changed`)
* Trunkrs-pakket onderweg voor bezorging (`trunkrs_out_for_delivery`)
* Trunkrs-pakket bezorgd (`trunkrs_delivered`)
* Probleem of retour bij Trunkrs-pakket (`trunkrs_package_problem`)
* Trunkrs-bezorgtijd gewijzigd (`trunkrs_delivery_window_changed`)

**En… (condities)**

* Er zijn/zijn geen Trunkrs-pakketten onderweg (`trunkrs_packages_underway`)
* Er is een/geen Trunkrs-pakket onderweg voor bezorging (`trunkrs_out_for_delivery_now`)
* Een Trunkrs-pakket heeft/heeft niet status… (`trunkrs_any_status_is`)
* Trunkrs-pakket… is/is niet bezorgd (`trunkrs_parcel_is_delivered`)
* Trunkrs-pakket… wordt wel/niet gevolgd (`trunkrs_is_tracking`)

**Dan… (acties)**

* Vernieuw Trunkrs (`trunkrs_refresh`)
* Volg Trunkrs-pakket… (`trunkrs_track_parcel`)
* Stop met volgen van Trunkrs-pakket… (`trunkrs_untrack_parcel`)
* Verwijder bezorgde Trunkrs-pakketten (`trunkrs_remove_delivered`)

## Dynalogic

[Vervoerderspagina →](carriers/dynalogic.md)

**Wanneer… (triggers)**

* Nieuw Dynalogic-pakket (`dynalogic_new_package`)
* Status Dynalogic-pakket gewijzigd (`dynalogic_status_changed`)
* Nieuwe Dynalogic-trackinggebeurtenis (`dynalogic_package_event_changed`)
* Dynalogic-pakket onderweg voor bezorging (`dynalogic_out_for_delivery`)
* Dynalogic-pakket bezorgd (`dynalogic_delivered`)
* Probleem of retour bij Dynalogic-pakket (`dynalogic_package_problem`)

**En… (condities)**

* Er zijn/zijn geen Dynalogic-pakketten onderweg (`dynalogic_packages_underway`)
* Er is een/geen Dynalogic-pakket onderweg voor bezorging (`dynalogic_out_for_delivery_now`)
* Een Dynalogic-pakket heeft/heeft niet status… (`dynalogic_any_status_is`)
* Dynalogic-pakket… is/is niet bezorgd (`dynalogic_parcel_is_delivered`)
* Dynalogic-pakket… wordt wel/niet gevolgd (`dynalogic_is_tracking`)

**Dan… (acties)**

* Vernieuw Dynalogic (`dynalogic_refresh`)
* Volg Dynalogic-pakket… (`dynalogic_track_parcel`)
* Stop met volgen van Dynalogic-pakket… (`dynalogic_untrack_parcel`)
* Verwijder bezorgde Dynalogic-pakketten (`dynalogic_remove_delivered`)

## Dragonfly / Intelcom

[Vervoerderspagina →](carriers/dragonfly.md)

**Wanneer… (triggers)**

* Nieuw Dragonfly-pakket (`dragonfly_new_package`)
* Status Dragonfly-pakket gewijzigd (`dragonfly_status_changed`)
* Nieuwe Dragonfly-trackinggebeurtenis (`dragonfly_package_event_changed`)
* Dragonfly-pakket onderweg voor bezorging (`dragonfly_out_for_delivery`)
* Dragonfly-pakket bezorgd (`dragonfly_delivered`)
* Probleem of retour bij Dragonfly-pakket (`dragonfly_package_problem`)
* Status van verzonden Dragonfly-pakket gewijzigd (`dragonfly_outgoing_status_changed`)
* Verzonden Dragonfly-pakket bezorgd (`dragonfly_outgoing_delivered`)
* Dragonfly-bezorgtijd gewijzigd (`dragonfly_delivery_window_changed`)

**En… (condities)**

* Er zijn/zijn geen Dragonfly-pakketten onderweg (`dragonfly_packages_underway`)
* Er is een/geen Dragonfly-pakket onderweg voor bezorging (`dragonfly_out_for_delivery_now`)
* Een Dragonfly-pakket heeft/heeft niet status… (`dragonfly_any_status_is`)
* Dragonfly-pakket… is/is niet bezorgd (`dragonfly_parcel_is_delivered`)
* Dragonfly-pakket… wordt wel/niet gevolgd (`dragonfly_is_tracking`)
* Er zijn/zijn geen verzonden Dragonfly-pakketten onderweg (`dragonfly_outgoing_underway`)

**Dan… (acties)**

* Vernieuw Dragonfly (`dragonfly_refresh`)
* Volg Dragonfly-pakket… (`dragonfly_track_parcel`)
* Stop met volgen van Dragonfly-pakket… (`dragonfly_untrack_parcel`)
* Verwijder bezorgde Dragonfly-pakketten (`dragonfly_remove_delivered`)

## Mondial Relay

[Vervoerderspagina →](carriers/mondial-relay.md)

**Wanneer… (triggers)**

* Nieuw Mondial Relay-pakket (`mondial_relay_new_package`)
* Status Mondial Relay-pakket gewijzigd (`mondial_relay_status_changed`)
* Nieuwe Mondial Relay-trackinggebeurtenis (`mondial_relay_package_event_changed`)
* Mondial Relay-pakket onderweg voor bezorging (`mondial_relay_out_for_delivery`)
* Mondial Relay-pakket bezorgd (`mondial_relay_delivered`)
* Probleem of retour bij Mondial Relay-pakket (`mondial_relay_package_problem`)
* Status van verzonden Mondial Relay-pakket gewijzigd (`mondial_relay_outgoing_status_changed`)
* Verzonden Mondial Relay-pakket bezorgd (`mondial_relay_outgoing_delivered`)

**En… (condities)**

* Er zijn/zijn geen Mondial Relay-pakketten onderweg (`mondial_relay_packages_underway`)
* Er is een/geen Mondial Relay-pakket onderweg voor bezorging (`mondial_relay_out_for_delivery_now`)
* Een Mondial Relay-pakket heeft/heeft niet status… (`mondial_relay_any_status_is`)
* Mondial Relay-pakket… is/is niet bezorgd (`mondial_relay_parcel_is_delivered`)
* Mondial Relay-pakket… wordt wel/niet gevolgd (`mondial_relay_is_tracking`)
* Er zijn/zijn geen verzonden Mondial Relay-pakketten onderweg (`mondial_relay_outgoing_underway`)

**Dan… (acties)**

* Vernieuw Mondial Relay (`mondial_relay_refresh`)
* Verwijder bezorgde Mondial Relay-pakketten (`mondial_relay_remove_delivered`)

## Amazon

[Vervoerderspagina →](carriers/amazon.md)

**Wanneer… (triggers)**

* Nieuw Amazon-pakket (`amazon_new_package`)
* Status Amazon-pakket gewijzigd (`amazon_status_changed`)
* Nieuwe Amazon-trackinggebeurtenis (`amazon_package_event_changed`)
* Amazon-pakket onderweg voor bezorging (`amazon_out_for_delivery`)
* Amazon-pakket klaar om op te halen (`amazon_ready_for_pickup`)
* Amazon-pakket bezorgd (`amazon_delivered`)
* Probleem of retour bij Amazon-pakket (`amazon_package_problem`)
* Verwachte Amazon-bezorgdatum gewijzigd (`amazon_delivery_window_changed`)

**En… (condities)**

* Er zijn/zijn geen Amazon-pakketten onderweg (`amazon_packages_underway`)
* Er is een/geen Amazon-pakket onderweg voor bezorging (`amazon_out_for_delivery_now`)
* Er ligt een/geen Amazon-pakket klaar om op te halen (`amazon_ready_for_pickup_now`)
* Een Amazon-pakket heeft/heeft niet status… (`amazon_any_status_is`)
* Amazon-pakket… is/is niet bezorgd (`amazon_parcel_is_delivered`)
* Amazon-pakket… wordt wel/niet gevolgd (`amazon_is_tracking`)

**Dan… (acties)**

* Vernieuw Amazon (`amazon_refresh`)
* Verwijder bezorgde Amazon-pakketten (`amazon_remove_delivered`)
