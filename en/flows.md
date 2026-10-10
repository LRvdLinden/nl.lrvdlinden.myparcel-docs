# Flow cards

Overview of all Flow cards in MyParcel v0.3.7, per carrier. Every card belongs to that carrier's device; you pick the device in the card. In total: **158 triggers, 121 conditions and 58 actions**.

* **When** cards fire once per change, also after an app restart (existing parcels are recorded silently on the first sync after an update).
* Conditions with *is/is not* can be inverted in Homey.
* The actions **Track parcel…**, **Stop tracking parcel…** and **Remove delivered parcels** manage the tracking-number list without opening the device settings.
* The full NL/EN titles, arguments and tokens per card are on each [carrier](carriers/README.md) page; the tokens on [Flow tokens](tokens.md).

## All carriers

* **Connection status changed** (`connection_status_changed`) – for every MyParcel device, with tokens *Connected*, *Connection status* and *Carrier*.

## PostNL

[Carrier page →](carriers/postnl.md)

**When… (triggers)**

* New mail is expected (`new_mail`)
* A new parcel was found (`new_package`)
* A delivery window became available (`delivery_window_known`)
* A parcel status changed (`package_status_changed`)
* PostNL synchronization failed (`sync_failed`)
* The PostNL login expired (`login_expired`)
* A parcel was delivered (`package_delivered`)
* A parcel delivery window changed (`delivery_window_changed`)
* A new PostNL parcel event was received (`package_event_changed`)
* Parcel weight became available (`package_weight_known`)
* Parcel dimensions became available (`package_dimensions_known`)

**And… (conditions)**

* Mail is/isn't expected (`mail_expected`)
* Parcels are/aren't underway (`packages_underway`)
* A delivery window is/isn't known (`delivery_window_known`)
* PostNL is/isn't connected (`postnl_connected`)
* The current parcel has/doesn't have weight information (`package_has_weight`)
* The current parcel has/doesn't have dimensions (`package_has_dimensions`)
* The current parcel status is/isn't (`package_status_is`)

**Then… (actions)**

* Synchronize PostNL (`sync_now`)

## DHL

[Carrier page →](carriers/dhl-parcel.md)

**When… (triggers)**

* New DHL parcel (`dhl_new_package`)
* Shipment status changed (`status_changed`)
* New DHL tracking event (`dhl_package_event_changed`)
* DHL parcel out for delivery (`dhl_out_for_delivery`)
* DHL parcel ready for pickup (`dhl_ready_for_pickup`)
* Shipment delivered (`shipment_delivered`)
* DHL parcel has a problem or is returning (`dhl_package_problem`)
* Status of sent DHL parcel changed (`dhl_outgoing_status_changed`)
* Sent DHL parcel delivered (`dhl_outgoing_delivered`)
* Delivery window available or changed (`dhl_delivery_window_changed`)

**And… (conditions)**

* Shipment is delivered (`is_delivered`)
* Delivery window is/isn't known (`dhl_delivery_window_known`)
* DHL parcels are/are not underway (`dhl_packages_underway`)
* A DHL parcel is/is not out for delivery (`dhl_out_for_delivery_now`)
* A DHL parcel is/is not ready for pickup (`dhl_ready_for_pickup_now`)
* A DHL parcel has/does not have status… (`dhl_any_status_is`)
* DHL parcel… is/is not delivered (`dhl_parcel_is_delivered`)
* DHL parcel… is/is not being tracked (`dhl_is_tracking`)
* Sent DHL parcels are/are not underway (`dhl_outgoing_underway`)

**Then… (actions)**

* Refresh shipment (`refresh_shipment`)
* Track DHL parcel… (`dhl_track_parcel`)
* Stop tracking DHL parcel… (`dhl_untrack_parcel`)
* Remove delivered DHL parcels (`dhl_remove_delivered`)

## DHL Express

[Carrier page →](carriers/dhl-express.md)

**When… (triggers)**

* New DHL Express parcel found (`dhl_express_new_package`)
* DHL Express parcel status changed (`dhl_express_status_changed`)
* New DHL Express tracking event (`dhl_express_package_event_changed`)
* DHL Express parcel out for delivery (`dhl_express_out_for_delivery`)
* DHL Express parcel delivered (`dhl_express_delivered`)
* DHL Express parcel has a problem or is returning (`dhl_express_package_problem`)
* Status of sent DHL Express parcel changed (`dhl_express_outgoing_status_changed`)
* Sent DHL Express parcel delivered (`dhl_express_outgoing_delivered`)
* DHL Express delivery information updated (`dhl_express_delivery_updated`)

**And… (conditions)**

* DHL Express parcels are underway (`dhl_express_packages_underway`)
* DHL Express is/isn't connected (`dhl_express_is_connected`)
* DHL Express delivery window is/isn't known (`dhl_express_delivery_window_known`)
* A DHL Express parcel is/is not out for delivery (`dhl_express_out_for_delivery_now`)
* A DHL Express parcel has/does not have status… (`dhl_express_any_status_is`)
* DHL Express parcel… is/is not delivered (`dhl_express_parcel_is_delivered`)
* DHL Express parcel… is/is not being tracked (`dhl_express_is_tracking`)
* Sent DHL Express parcels are/are not underway (`dhl_express_outgoing_underway`)

**Then… (actions)**

* Refresh DHL Express (`dhl_express_refresh`)
* Track DHL Express parcel… (`dhl_express_track_parcel`)
* Stop tracking DHL Express parcel… (`dhl_express_untrack_parcel`)
* Remove delivered DHL Express parcels (`dhl_express_remove_delivered`)

## DPD

[Carrier page →](carriers/dpd.md)

**When… (triggers)**

* New DPD package (`dpd_new_package`)
* DPD package status changed (`dpd_status_changed`)
* New DPD tracking event (`dpd_package_event_changed`)
* DPD parcel out for delivery (`dpd_out_for_delivery`)
* Delivery window available or changed (`dpd_delivery_window_changed`)
* DPD delivery information updated (`dpd_delivery_updated`)
* DPD parcel ready for pickup (`dpd_ready_for_pickup`)
* DPD package delivered (`dpd_delivered`)
* DPD parcel has a problem or is returning (`dpd_package_problem`)
* Status of sent DPD parcel changed (`dpd_outgoing_status_changed`)
* Sent DPD parcel delivered (`dpd_outgoing_delivered`)

**And… (conditions)**

* DPD parcels are/are not underway (`dpd_packages_underway`)
* Delivery window is/isn't known (`dpd_delivery_window_known`)
* A DPD parcel is/is not out for delivery (`dpd_out_for_delivery_now`)
* A DPD parcel is/is not ready for pickup (`dpd_ready_for_pickup_now`)
* A DPD parcel has/does not have status… (`dpd_any_status_is`)
* DPD parcel… is/is not delivered (`dpd_parcel_is_delivered`)
* Sent DPD parcels are/are not underway (`dpd_outgoing_underway`)

**Then… (actions)**

* Refresh DPD (`dpd_refresh`)

## UPS

[Carrier page →](carriers/ups.md)

**When… (triggers)**

* New UPS package (`ups_new_package`)
* UPS package status changed (`ups_status_changed`)
* UPS package delivered (`ups_delivered`)
* Delivery window available or changed (`ups_delivery_window_changed`)

**And… (conditions)**

* UPS packages are underway (`ups_packages_underway`)
* UPS account is connected (`ups_account_connected`)
* Delivery window is/isn't known (`ups_delivery_window_known`)

**Then… (actions)**

* Refresh UPS (`ups_refresh`)

## Budbee

[Carrier page →](carriers/budbee.md)

**When… (triggers)**

* New Budbee package (`budbee_new_package`)
* Budbee package status changed (`budbee_status_changed`)
* New Budbee tracking event (`budbee_package_event_changed`)
* Budbee parcel out for delivery (`budbee_out_for_delivery`)
* Budbee parcel ready for pickup (`budbee_ready_for_pickup`)
* Budbee parcel delivered (`budbee_delivered`)
* Budbee parcel has a problem or is returning (`budbee_package_problem`)
* Status of sent Budbee parcel changed (`budbee_outgoing_status_changed`)
* Sent Budbee parcel delivered (`budbee_outgoing_delivered`)
* Delivery window available or changed (`budbee_delivery_window_changed`)

**And… (conditions)**

* Budbee packages are underway (`budbee_packages_underway`)
* Delivery window is/isn't known (`budbee_delivery_window_known`)
* A Budbee parcel is/is not out for delivery (`budbee_out_for_delivery_now`)
* A Budbee parcel is/is not ready for pickup (`budbee_ready_for_pickup_now`)
* A Budbee parcel has/does not have status… (`budbee_any_status_is`)
* Budbee parcel… is/is not delivered (`budbee_parcel_is_delivered`)
* Budbee parcel… is/is not being tracked (`budbee_is_tracking`)
* Sent Budbee parcels are/are not underway (`budbee_outgoing_underway`)

**Then… (actions)**

* Refresh Budbee (`budbee_refresh`)
* Track Budbee parcel… (`budbee_track_parcel`)
* Stop tracking Budbee parcel… (`budbee_untrack_parcel`)
* Remove delivered Budbee parcels (`budbee_remove_delivered`)

## Vinted Go

[Carrier page →](carriers/homerr.md)

**When… (triggers)**

* New Vinted Go parcel (`homerr_new_package`)
* Vinted Go package status changed (`homerr_package_status_changed`)
* New Vinted Go tracking event (`homerr_package_event_changed`)
* Vinted Go parcel out for delivery (`homerr_out_for_delivery`)
* Vinted Go parcel ready for pickup (`homerr_ready_for_pickup`)
* Vinted Go parcel delivered (`homerr_delivered`)
* Vinted Go parcel has a problem or is returning (`homerr_package_problem`)
* Status of sent Vinted Go parcel changed (`homerr_outgoing_status_changed`)
* Sent Vinted Go parcel delivered (`homerr_outgoing_delivered`)

**And… (conditions)**

* Vinted Go packages are underway (`homerr_packages_underway`)
* A Vinted Go parcel is/is not out for delivery (`homerr_out_for_delivery_now`)
* A Vinted Go parcel is/is not ready for pickup (`homerr_ready_for_pickup_now`)
* A Vinted Go parcel has/does not have status… (`homerr_any_status_is`)
* Vinted Go parcel… is/is not delivered (`homerr_parcel_is_delivered`)
* Sent Vinted Go parcels are/are not underway (`homerr_outgoing_underway`)

**Then… (actions)**

* Refresh Vinted Go packages (`homerr_refresh`)
* Remove delivered Vinted Go parcels (`homerr_remove_delivered`)

## FedEx

[Carrier page →](carriers/fedex.md)

**When… (triggers)**

* New FedEx package (`fedex_new_package`)
* FedEx package status changed (`fedex_status_changed`)
* New FedEx tracking event (`fedex_package_event_changed`)
* FedEx parcel out for delivery (`fedex_out_for_delivery`)
* FedEx parcel ready for pickup (`fedex_ready_for_pickup`)
* FedEx parcel delivered (`fedex_delivered`)
* FedEx parcel has a problem or is returning (`fedex_package_problem`)
* FedEx delivery time changed (`fedex_delivery_updated`)

**And… (conditions)**

* FedEx packages are underway (`fedex_packages_underway`)
* A FedEx parcel is/is not out for delivery (`fedex_out_for_delivery_now`)
* A FedEx parcel is/is not ready for pickup (`fedex_ready_for_pickup_now`)
* A FedEx parcel has/does not have status… (`fedex_any_status_is`)
* FedEx parcel… is/is not delivered (`fedex_parcel_is_delivered`)
* FedEx parcel… is/is not being tracked (`fedex_is_tracking`)

**Then… (actions)**

* Refresh FedEx (`fedex_refresh`)
* Track FedEx parcel… (`fedex_track_parcel`)
* Stop tracking FedEx parcel… (`fedex_untrack_parcel`)
* Remove delivered FedEx parcels (`fedex_remove_delivered`)

## GLS

[Carrier page →](carriers/gls.md)

**When… (triggers)**

* New GLS parcel (`gls_new_package`)
* GLS parcel status changed (`gls_status_changed`)
* New GLS tracking event (`gls_package_event_changed`)
* GLS parcel out for delivery (`gls_out_for_delivery`)
* Delivery window available or changed (`gls_delivery_window_changed`)
* GLS parcel ready for pickup (`gls_ready_for_pickup`)
* GLS parcel delivered (`gls_package_delivered`)
* GLS parcel has a problem or is returning (`gls_package_problem`)

**And… (conditions)**

* GLS parcels are/are not underway (`gls_packages_underway`)
* Delivery window is/isn't known (`gls_delivery_window_known`)
* A GLS parcel is/is not out for delivery (`gls_out_for_delivery_now`)
* A GLS parcel is/is not ready for pickup (`gls_ready_for_pickup_now`)
* A GLS parcel has/does not have status… (`gls_any_status_is`)
* GLS parcel… is/is not delivered (`gls_parcel_is_delivered`)
* GLS parcel… is/is not being tracked (`gls_is_tracking`)

**Then… (actions)**

* Refresh GLS (`gls_refresh`)
* Track GLS parcel… (`gls_track_parcel`)
* Stop tracking GLS parcel… (`gls_untrack_parcel`)
* Remove delivered GLS parcels (`gls_remove_delivered`)

## InPost

[Carrier page →](carriers/inpost-uk.md)

**When… (triggers)**

* New InPost UK package (`inpost_uk_new_package`)
* InPost UK package status changed (`inpost_uk_status_changed`)
* New InPost tracking event (`inpost_uk_package_event_changed`)
* InPost parcel out for delivery (`inpost_uk_out_for_delivery`)
* InPost parcel ready for pickup (`inpost_uk_ready_for_pickup`)
* InPost parcel delivered (`inpost_uk_delivered`)
* InPost parcel has a problem or is returning (`inpost_uk_package_problem`)

**And… (conditions)**

* InPost UK packages are underway (`inpost_uk_packages_underway`)
* A InPost parcel is/is not out for delivery (`inpost_uk_out_for_delivery_now`)
* A InPost parcel is/is not ready for pickup (`inpost_uk_ready_for_pickup_now`)
* A InPost parcel has/does not have status… (`inpost_uk_any_status_is`)
* InPost parcel… is/is not delivered (`inpost_uk_parcel_is_delivered`)
* InPost parcel… is/is not being tracked (`inpost_uk_is_tracking`)

**Then… (actions)**

* Refresh InPost UK (`inpost_uk_refresh`)
* Track InPost parcel… (`inpost_uk_track_parcel`)
* Stop tracking InPost parcel… (`inpost_uk_untrack_parcel`)
* Remove delivered InPost parcels (`inpost_uk_remove_delivered`)

## bpost

[Carrier page →](carriers/bpost.md)

**When… (triggers)**

* New bpost package (`bpost_new_package`)
* bpost package status changed (`bpost_status_changed`)
* New bpost tracking event (`bpost_package_event_changed`)
* bpost parcel out for delivery (`bpost_out_for_delivery`)
* bpost parcel ready for pickup (`bpost_ready_for_pickup`)
* bpost package delivered (`bpost_delivered`)
* bpost parcel has a problem or is returning (`bpost_package_problem`)
* Status of sent bpost parcel changed (`bpost_outgoing_status_changed`)
* Sent bpost parcel delivered (`bpost_outgoing_delivered`)
* bpost delivery information updated (`bpost_delivery_updated`)
* bpost letter announced (Mail Ahead) (`bpost_letter_announced`)
* Delivery window available or changed (`bpost_delivery_window_changed`)

**And… (conditions)**

* bpost packages are underway (`bpost_packages_underway`)
* My bpost account is connected (`bpost_account_connected`)
* Delivery window is/isn't known (`bpost_delivery_window_known`)
* A bpost parcel is/is not out for delivery (`bpost_out_for_delivery_now`)
* A bpost parcel is/is not ready for pickup (`bpost_ready_for_pickup_now`)
* A bpost parcel has/does not have status… (`bpost_any_status_is`)
* bpost parcel… is/is not delivered (`bpost_parcel_is_delivered`)
* bpost parcel… is/is not being tracked (`bpost_is_tracking`)
* Sent bpost parcels are/are not underway (`bpost_outgoing_underway`)

**Then… (actions)**

* Refresh bpost (`bpost_refresh`)
* Track bpost parcel… (`bpost_track_parcel`)
* Stop tracking bpost parcel… (`bpost_untrack_parcel`)
* Remove delivered bpost parcels (`bpost_remove_delivered`)

## Royal Mail

[Carrier page →](carriers/royal-mail.md)

**When… (triggers)**

* New Royal Mail package (`royal_mail_new_package`)
* Royal Mail package status changed (`royal_mail_status_changed`)

**And… (conditions)**

* Royal Mail packages are underway (`royal_mail_packages_underway`)

**Then… (actions)**

* Refresh Royal Mail (`royal_mail_refresh`)

## Post & DHL Germany

[Carrier page →](carriers/post-dhl-de.md)

**When… (triggers)**

* New DHL parcel (`dhl_de_new_package`)
* DHL parcel status changed (`dhl_de_status_changed`)
* New DHL tracking event (`dhl_de_package_event_changed`)
* DHL parcel out for delivery (`dhl_de_out_for_delivery`)
* DHL parcel ready for pickup (`dhl_de_ready_for_pickup`)
* DHL parcel delivered (`dhl_de_delivered`)
* DHL parcel has a problem or is returning (`dhl_de_package_problem`)
* Status of sent DHL parcel changed (`dhl_de_outgoing_status_changed`)
* Sent DHL parcel delivered (`dhl_de_outgoing_delivered`)
* Delivery window available or changed (`dhl_de_delivery_window_changed`)

**And… (conditions)**

* Delivery window is/isn't known (`dhl_de_delivery_window_known`)
* DHL parcels are/are not underway (`dhl_de_packages_underway`)
* A DHL parcel is/is not out for delivery (`dhl_de_out_for_delivery_now`)
* A DHL parcel is/is not ready for pickup (`dhl_de_ready_for_pickup_now`)
* A DHL parcel has/does not have status… (`dhl_de_any_status_is`)
* DHL parcel… is/is not delivered (`dhl_de_parcel_is_delivered`)
* DHL parcel… is/is not being tracked (`dhl_de_is_tracking`)
* Sent DHL parcels are/are not underway (`dhl_de_outgoing_underway`)

**Then… (actions)**

* Refresh Post & DHL (`dhl_de_refresh`)
* Track DHL parcel… (`dhl_de_track_parcel`)
* Stop tracking DHL parcel… (`dhl_de_untrack_parcel`)
* Remove delivered DHL parcels (`dhl_de_remove_delivered`)

## Ampère

[Carrier page →](carriers/ampere.md)

**When… (triggers)**

* New Ampère parcel found (`ampere_new_package`)
* Ampère parcel status changed (`ampere_status_changed`)
* New Ampère tracking event (`ampere_package_event_changed`)
* Ampère parcel out for delivery (`ampere_out_for_delivery`)
* Ampère parcel delivered (`ampere_delivered`)
* Ampère parcel has a problem or is returning (`ampere_package_problem`)
* Ampère delivery information updated (`ampere_delivery_updated`)
* Ampère delivery window available or changed (`ampere_delivery_window_changed`)

**And… (conditions)**

* Ampère parcels are underway (`ampere_packages_underway`)
* Ampère delivery window is/isn't known (`ampere_delivery_window_known`)
* Latest Ampère parcel is/isn't delivered (`ampere_is_delivered`)
* Ampère is/isn't connected (`ampere_is_connected`)
* A Ampère parcel is/is not out for delivery (`ampere_out_for_delivery_now`)
* A Ampère parcel has/does not have status… (`ampere_any_status_is`)
* Ampère parcel… is/is not delivered (`ampere_parcel_is_delivered`)
* Ampère parcel… is/is not being tracked (`ampere_is_tracking`)

**Then… (actions)**

* Refresh Ampère (`ampere_refresh`)
* Track Ampère parcel from bol.com link… (`ampere_track_parcel`)
* Stop tracking Ampère parcel… (`ampere_untrack_parcel`)
* Remove delivered Ampère parcels (`ampere_remove_delivered`)

## Trunkrs

[Carrier page →](carriers/trunkrs.md)

**When… (triggers)**

* New Trunkrs parcel (`trunkrs_new_package`)
* Trunkrs parcel status changed (`trunkrs_status_changed`)
* New Trunkrs tracking event (`trunkrs_package_event_changed`)
* Trunkrs parcel out for delivery (`trunkrs_out_for_delivery`)
* Trunkrs parcel delivered (`trunkrs_delivered`)
* Trunkrs parcel has a problem or is returning (`trunkrs_package_problem`)
* Trunkrs delivery time changed (`trunkrs_delivery_window_changed`)

**And… (conditions)**

* Trunkrs parcels are/are not underway (`trunkrs_packages_underway`)
* A Trunkrs parcel is/is not out for delivery (`trunkrs_out_for_delivery_now`)
* A Trunkrs parcel has/does not have status… (`trunkrs_any_status_is`)
* Trunkrs parcel… is/is not delivered (`trunkrs_parcel_is_delivered`)
* Trunkrs parcel… is/is not being tracked (`trunkrs_is_tracking`)

**Then… (actions)**

* Refresh Trunkrs (`trunkrs_refresh`)
* Track Trunkrs parcel… (`trunkrs_track_parcel`)
* Stop tracking Trunkrs parcel… (`trunkrs_untrack_parcel`)
* Remove delivered Trunkrs parcels (`trunkrs_remove_delivered`)

## Dynalogic

[Carrier page →](carriers/dynalogic.md)

**When… (triggers)**

* New Dynalogic parcel (`dynalogic_new_package`)
* Dynalogic parcel status changed (`dynalogic_status_changed`)
* New Dynalogic tracking event (`dynalogic_package_event_changed`)
* Dynalogic parcel out for delivery (`dynalogic_out_for_delivery`)
* Dynalogic parcel delivered (`dynalogic_delivered`)
* Dynalogic parcel has a problem or is returning (`dynalogic_package_problem`)

**And… (conditions)**

* Dynalogic parcels are/are not underway (`dynalogic_packages_underway`)
* A Dynalogic parcel is/is not out for delivery (`dynalogic_out_for_delivery_now`)
* A Dynalogic parcel has/does not have status… (`dynalogic_any_status_is`)
* Dynalogic parcel… is/is not delivered (`dynalogic_parcel_is_delivered`)
* Dynalogic parcel… is/is not being tracked (`dynalogic_is_tracking`)

**Then… (actions)**

* Refresh Dynalogic (`dynalogic_refresh`)
* Track Dynalogic parcel… (`dynalogic_track_parcel`)
* Stop tracking Dynalogic parcel… (`dynalogic_untrack_parcel`)
* Remove delivered Dynalogic parcels (`dynalogic_remove_delivered`)

## Dragonfly / Intelcom

[Carrier page →](carriers/dragonfly.md)

**When… (triggers)**

* New Dragonfly parcel (`dragonfly_new_package`)
* Dragonfly parcel status changed (`dragonfly_status_changed`)
* New Dragonfly tracking event (`dragonfly_package_event_changed`)
* Dragonfly parcel out for delivery (`dragonfly_out_for_delivery`)
* Dragonfly parcel delivered (`dragonfly_delivered`)
* Dragonfly parcel has a problem or is returning (`dragonfly_package_problem`)
* Status of sent Dragonfly parcel changed (`dragonfly_outgoing_status_changed`)
* Sent Dragonfly parcel delivered (`dragonfly_outgoing_delivered`)
* Dragonfly delivery time changed (`dragonfly_delivery_window_changed`)

**And… (conditions)**

* Dragonfly parcels are/are not underway (`dragonfly_packages_underway`)
* A Dragonfly parcel is/is not out for delivery (`dragonfly_out_for_delivery_now`)
* A Dragonfly parcel has/does not have status… (`dragonfly_any_status_is`)
* Dragonfly parcel… is/is not delivered (`dragonfly_parcel_is_delivered`)
* Dragonfly parcel… is/is not being tracked (`dragonfly_is_tracking`)
* Sent Dragonfly parcels are/are not underway (`dragonfly_outgoing_underway`)

**Then… (actions)**

* Refresh Dragonfly (`dragonfly_refresh`)
* Track Dragonfly parcel… (`dragonfly_track_parcel`)
* Stop tracking Dragonfly parcel… (`dragonfly_untrack_parcel`)
* Remove delivered Dragonfly parcels (`dragonfly_remove_delivered`)

## Mondial Relay

[Carrier page →](carriers/mondial-relay.md)

**When… (triggers)**

* New Mondial Relay parcel (`mondial_relay_new_package`)
* Mondial Relay parcel status changed (`mondial_relay_status_changed`)
* New Mondial Relay tracking event (`mondial_relay_package_event_changed`)
* Mondial Relay parcel out for delivery (`mondial_relay_out_for_delivery`)
* Mondial Relay parcel delivered (`mondial_relay_delivered`)
* Mondial Relay parcel has a problem or is returning (`mondial_relay_package_problem`)
* Status of sent Mondial Relay parcel changed (`mondial_relay_outgoing_status_changed`)
* Sent Mondial Relay parcel delivered (`mondial_relay_outgoing_delivered`)

**And… (conditions)**

* Mondial Relay parcels are/are not underway (`mondial_relay_packages_underway`)
* A Mondial Relay parcel is/is not out for delivery (`mondial_relay_out_for_delivery_now`)
* A Mondial Relay parcel has/does not have status… (`mondial_relay_any_status_is`)
* Mondial Relay parcel… is/is not delivered (`mondial_relay_parcel_is_delivered`)
* Mondial Relay parcel… is/is not being tracked (`mondial_relay_is_tracking`)
* Sent Mondial Relay parcels are/are not underway (`mondial_relay_outgoing_underway`)

**Then… (actions)**

* Refresh Mondial Relay (`mondial_relay_refresh`)
* Remove delivered Mondial Relay parcels (`mondial_relay_remove_delivered`)

## Amazon

[Carrier page →](carriers/amazon.md)

**When… (triggers)**

* New Amazon parcel (`amazon_new_package`)
* Amazon parcel status changed (`amazon_status_changed`)
* New Amazon tracking event (`amazon_package_event_changed`)
* Amazon parcel out for delivery (`amazon_out_for_delivery`)
* Amazon parcel ready for pickup (`amazon_ready_for_pickup`)
* Amazon parcel delivered (`amazon_delivered`)
* Amazon parcel has a problem or is returning (`amazon_package_problem`)
* Amazon expected delivery date changed (`amazon_delivery_window_changed`)

**And… (conditions)**

* Amazon parcels are/are not underway (`amazon_packages_underway`)
* A Amazon parcel is/is not out for delivery (`amazon_out_for_delivery_now`)
* A Amazon parcel is/is not ready for pickup (`amazon_ready_for_pickup_now`)
* A Amazon parcel has/does not have status… (`amazon_any_status_is`)
* Amazon parcel… is/is not delivered (`amazon_parcel_is_delivered`)
* Amazon parcel… is/is not being tracked (`amazon_is_tracking`)

**Then… (actions)**

* Refresh Amazon (`amazon_refresh`)
* Remove delivered Amazon parcels (`amazon_remove_delivered`)
