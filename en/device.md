# Device data

Every carrier is its own device in Homey. Below are the device values (capabilities) per carrier in v0.3.7. Available data depends on the carrier and parcel; not every field is always filled and MyParcel never makes up data the carrier does not provide.

Common to all:

* **Connection status** (`myparcel_connection_status`) – on (almost) every device; when a device becomes *Not connected*, a Timeline notification appears.
* A network hiccup shows a warning with the last known data instead of making the device unavailable.
* Delivered parcels stay visible for the configured number of days (setting *Show delivered parcels for (days)*).
* Smart polling: every 15 minutes when a delivery is near, every 45 minutes otherwise, quiet at night.

## PostNL

| ID | Name | Type |
|---|---|---|
| `postnl_mail_expected` | Mail expected | yes/no |
| `postnl_mail_count` | Mail items | number |
| `postnl_package_count` | Parcels underway | number |
| `postnl_next_delivery` | Next delivery | text |
| `postnl_delivery_date` | Delivery date | text |
| `postnl_delivery_window` | Delivery window | text |
| `postnl_package_status` | Parcel status | text |
| `postnl_package_sender` | Parcel sender | text |
| `postnl_package_receiver` | Parcel receiver | text |
| `postnl_package_tracking` | Tracking number | text |
| `postnl_package_event` | Latest parcel event | text |
| `postnl_package_status_time` | Parcel status time | text |
| `postnl_package_delivered` | Parcel delivered | yes/no |
| `postnl_package_shipment_type` | Shipment type | text |
| `postnl_package_weight` | Parcel weight | text |
| `postnl_package_weight_kg` | Parcel weight (kg) | number |
| `postnl_package_length` | Parcel length | number |
| `postnl_package_width` | Parcel width | number |
| `postnl_package_height` | Parcel height | number |
| `postnl_package_status_history` | Full status history | text |
| `postnl_package_observation_code` | Observation code | text |
| `postnl_package_canonical_status` | Canonical status | text |
| `postnl_package_pickup` | PostNL Point delivery | yes/no |
| `postnl_package_pickup_point` | PostNL Point | text |
| `postnl_package_dimensions` | Parcel dimensions | text |
| `postnl_status` | Connection status | text |
| `postnl_last_update` | Last update | text |

[PostNL →](carriers/postnl.md)

## DHL

| ID | Name | Type |
|---|---|---|
| `dhl_parcel_count` | Active parcels | number |
| `dhl_status` | Status | text |
| `dhl_tracking_number` | Tracking number | text |
| `dhl_sender` | Sender | text |
| `dhl_receiver` | Receiver | text |
| `dhl_delivery_date` | Delivery date | text |
| `dhl_delivery_window` | Delivery window | text |
| `dhl_next_delivery` | Next delivery | text |
| `dhl_out_for_delivery_count` | Out for delivery | number |
| `dhl_en_route_pickup_count` | En route to pickup point | number |
| `dhl_pickup_count` | Ready for pickup | number |
| `dhl_pickup_point` | Pickup point | text |
| `dhl_delivered_count` | Recently delivered | number |
| `dhl_outgoing_count` | Sent parcels underway | number |
| `dhl_last_event` | Last event | text |
| `myparcel_connection_status` | Connection status | text |
| `dhl_last_update` | Last update | text |

[DHL →](carriers/dhl-parcel.md)

## DHL Express

| ID | Name | Type |
|---|---|---|
| `dhl_express_parcel_count` | Active parcels | number |
| `dhl_express_total_count` | Total parcels | number |
| `dhl_express_status` | Status | text |
| `dhl_express_tracking` | Tracking number | text |
| `dhl_express_sender` | Sender | text |
| `dhl_express_receiver` | Receiver | text |
| `dhl_express_delivery_date` | Delivery date | text |
| `dhl_express_delivery_window` | Delivery window | text |
| `dhl_express_next_delivery` | Next delivery | text |
| `dhl_express_service` | Service | text |
| `dhl_express_origin` | Origin | text |
| `dhl_express_destination` | Destination | text |
| `dhl_express_pieces` | Pieces | number |
| `dhl_express_last_event` | Last event | text |
| `dhl_express_out_for_delivery_count` | Out for delivery | number |
| `dhl_express_delivered_count` | Recently delivered | number |
| `dhl_express_delivered` | Delivered | yes/no |
| `myparcel_connection_status` | Connection status | text |
| `dhl_express_last_update` | Last update | text |

[DHL Express →](carriers/dhl-express.md)

## DPD

| ID | Name | Type |
|---|---|---|
| `dpd_parcel_count` | Active parcels | number |
| `dpd_total_count` | Total parcels | number |
| `dpd_status` | Status | text |
| `dpd_tracking` | Tracking number | text |
| `dpd_sender` | Sender | text |
| `dpd_receiver` | Receiver | text |
| `dpd_delivery_date` | Delivery date | text |
| `dpd_delivery_window` | Delivery window | text |
| `dpd_delivery_point` | Delivery point | text |
| `dpd_weight` | Weight | text |
| `dpd_dimensions` | Dimensions | text |
| `dpd_delivery_type` | Delivery type | text |
| `dpd_last_event` | Last event | text |
| `dpd_direction` | Direction | text |
| `dpd_next_delivery` | Next delivery | text |
| `dpd_out_for_delivery_count` | Out for delivery | number |
| `dpd_en_route_pickup_count` | En route to ParcelShop | number |
| `dpd_pickup_count` | Ready for pickup | number |
| `dpd_delivered_count` | Recently delivered | number |
| `dpd_outgoing_count` | Sent parcels underway | number |
| `myparcel_connection_status` | Connection status | text |
| `dpd_last_update` | Last update | text |

[DPD →](carriers/dpd.md)

## UPS

| ID | Name | Type |
|---|---|---|
| `ups_parcel_count` | Active parcels | number |
| `ups_total_count` | Total packages | number |
| `ups_status` | Status | text |
| `ups_tracking` | Next tracking number | text |
| `ups_sender` | Sender | text |
| `ups_delivery_date` | Expected delivery | text |
| `ups_delivery_window` | Delivery window | text |
| `ups_service` | UPS service | text |
| `ups_ship_from` | Ship from | text |
| `ups_ship_to` | Ship to | text |
| `ups_access_point` | UPS Access Point | text |
| `ups_last_event` | Last event | text |
| `ups_country` | UPS country | text |
| `ups_locale` | UPS locale | text |
| `ups_account_status` | Connection status | text |
| `ups_last_update` | Last update | text |

[UPS →](carriers/ups.md)

## Budbee

| ID | Name | Type |
|---|---|---|
| `budbee_parcel_count` | Active parcels | number |
| `budbee_status` | Status | text |
| `budbee_tracking` | Tracking number | text |
| `budbee_sender` | Sender | text |
| `budbee_delivery_date` | Delivery date | text |
| `budbee_delivery_window` | Delivery window | text |
| `budbee_next_delivery` | Next delivery | text |
| `budbee_out_for_delivery_count` | Out for delivery | number |
| `budbee_en_route_pickup_count` | En route to pickup point | number |
| `budbee_pickup_count` | Ready for pickup | number |
| `budbee_pickup_point` | Pickup point | text |
| `budbee_delivered_count` | Recently delivered | number |
| `budbee_outgoing_count` | Sent parcels underway | number |
| `budbee_last_event` | Last event | text |
| `myparcel_connection_status` | Connection status | text |
| `budbee_last_update` | Last update | text |

[Budbee →](carriers/budbee.md)

## Vinted Go

| ID | Name | Type |
|---|---|---|
| `homerr_parcel_count` | Packages underway | number |
| `homerr_status` | Status | text |
| `homerr_tracking` | Tracking number | text |
| `homerr_item` | Item | text |
| `homerr_pickup_count` | Ready for pickup | number |
| `homerr_en_route_pickup_count` | En route to pickup point | number |
| `homerr_pickup_point` | Pickup point | text |
| `homerr_pickup_code` | Pickup code | text |
| `homerr_delivered_count` | Recently delivered | number |
| `homerr_outgoing_count` | Sent parcels underway | number |
| `homerr_last_event` | Last event | text |
| `myparcel_connection_status` | Connection status | text |
| `homerr_last_update` | Last update | text |

[Vinted Go →](carriers/homerr.md)

## FedEx

| ID | Name | Type |
|---|---|---|
| `fedex_parcel_count` | Parcels underway | number |
| `fedex_status` | Status | text |
| `fedex_tracking` | Tracking number | text |
| `fedex_sender` | Sender | text |
| `fedex_receiver` | Receiver | text |
| `fedex_delivery_date` | Delivery date | text |
| `fedex_delivery_window` | Delivery window | text |
| `fedex_next_delivery` | Next delivery | text |
| `fedex_out_for_delivery_count` | Out for delivery | number |
| `fedex_pickup_count` | Ready for pickup | number |
| `fedex_pickup_point` | Pickup point | text |
| `fedex_delivered_count` | Recently delivered | number |
| `fedex_last_event` | Last event | text |
| `fedex_service` | Service | text |
| `fedex_weight` | Weight | text |
| `fedex_dimensions` | Dimensions | text |
| `myparcel_connection_status` | Connection status | text |
| `fedex_last_update` | Last update | text |

[FedEx →](carriers/fedex.md)

## GLS

| ID | Name | Type |
|---|---|---|
| `gls_parcel_count` | Parcels underway | number |
| `gls_status` | Status | text |
| `gls_next_delivery` | Next delivery | text |
| `gls_delivery_window` | Delivery window | text |
| `gls_tracking` | Tracking number | text |
| `gls_sender` | Sender | text |
| `gls_receiver` | Recipient | text |
| `gls_last_event` | Last event | text |
| `gls_out_for_delivery_count` | Out for delivery | number |
| `gls_en_route_pickup_count` | En route to ParcelShop | number |
| `gls_pickup_count` | Ready for pickup | number |
| `gls_pickup_point` | ParcelShop | text |
| `gls_delivered_count` | Recently delivered | number |
| `gls_weight` | Weight | number |
| `gls_dimensions` | Dimensions | text |
| `myparcel_connection_status` | Connection status | text |
| `gls_last_update` | Last update | text |

[GLS →](carriers/gls.md)

## InPost

| ID | Name | Type |
|---|---|---|
| `inpost_uk_parcel_count` | Active parcels | number |
| `inpost_uk_status` | Status | text |
| `inpost_uk_tracking` | Tracking number | text |
| `inpost_uk_sender` | Sender | text |
| `inpost_uk_out_for_delivery_count` | Out for delivery | number |
| `inpost_uk_pickup_count` | Ready for pickup | number |
| `inpost_uk_pickup_point` | Pickup point | text |
| `inpost_uk_pickup_code` | Pickup code | text |
| `inpost_uk_delivered_count` | Recently delivered | number |
| `inpost_uk_last_event` | Last event | text |
| `myparcel_connection_status` | Connection status | text |
| `inpost_uk_last_update` | Last update | text |

[InPost →](carriers/inpost-uk.md)

## bpost

| ID | Name | Type |
|---|---|---|
| `bpost_parcel_count` | Active parcels | number |
| `bpost_total_count` | Total parcels | number |
| `bpost_status` | Status | text |
| `bpost_tracking` | Next tracking number | text |
| `bpost_sender` | Sender | text |
| `bpost_delivery_date` | Expected delivery | text |
| `bpost_delivery_window` | Delivery window | text |
| `bpost_delivery_point` | Delivery point | text |
| `bpost_weight` | Weight | text |
| `bpost_product` | Product | text |
| `bpost_partner` | Delivery partner | text |
| `bpost_last_event` | Last event | text |
| `bpost_receiver` | Receiver | text |
| `bpost_next_delivery` | Next delivery | text |
| `bpost_out_for_delivery_count` | Out for delivery | number |
| `bpost_en_route_pickup_count` | En route to pickup point | number |
| `bpost_pickup_count` | Ready for pickup | number |
| `bpost_delivered_count` | Recently delivered | number |
| `bpost_outgoing_count` | Sent parcels underway | number |
| `bpost_dimensions` | Dimensions | text |
| `bpost_letter_count` | Letters announced | number |
| `bpost_last_letter` | Last letter | text |
| `bpost_account_status` | Connection status | text |
| `bpost_last_update` | Last update | text |

[bpost →](carriers/bpost.md)

## Royal Mail

| ID | Name | Type |
|---|---|---|
| `royal_mail_parcel_count` | Active parcels | number |
| `royal_mail_status` | Status | text |
| `myparcel_connection_status` | Connection status | text |
| `royal_mail_last_update` | Last update | text |

[Royal Mail →](carriers/royal-mail.md)

## Post & DHL Germany

| ID | Name | Type |
|---|---|---|
| `dhl_de_parcel_count` | Active packages | number |
| `dhl_de_status` | Status | text |
| `dhl_de_tracking` | Tracking number | text |
| `dhl_de_sender` | Sender | text |
| `dhl_de_delivery_date` | Delivery date | text |
| `dhl_de_delivery_window` | Delivery window | text |
| `dhl_de_next_delivery` | Next delivery | text |
| `dhl_de_out_for_delivery_count` | Out for delivery | number |
| `dhl_de_pickup_count` | Ready for pickup | number |
| `dhl_de_pickup_point` | Pickup point | text |
| `dhl_de_delivered_count` | Recently delivered | number |
| `dhl_de_outgoing_count` | Sent parcels underway | number |
| `dhl_de_last_event` | Last event | text |
| `dhl_de_mail_count` | Expected mail | number |
| `dhl_de_postnumber` | Postnumber | text |
| `dhl_de_account_status` | Connection status | text |
| `dhl_de_mail_status` | Letter announcement | text |
| `dhl_de_last_update` | Last update | text |

[Post & DHL Germany →](carriers/post-dhl-de.md)

## Ampère

| ID | Name | Type |
|---|---|---|
| `ampere_parcel_count` | Active parcels | number |
| `ampere_total_count` | Total parcels | number |
| `ampere_status` | Status | text |
| `ampere_tracking` | Tracking number | text |
| `ampere_sender` | Sender | text |
| `ampere_delivery_date` | Delivery date | text |
| `ampere_delivery_window` | Delivery window | text |
| `ampere_window_start` | Delivery window start | text |
| `ampere_window_end` | Delivery window end | text |
| `ampere_delivered` | Delivered | yes/no |
| `ampere_details_url` | Track & Trace URL | text |
| `ampere_receiver` | Receiver | text |
| `ampere_next_delivery` | Next delivery | text |
| `ampere_out_for_delivery_count` | Out for delivery | number |
| `ampere_delivered_count` | Recently delivered | number |
| `ampere_last_event` | Last event | text |
| `myparcel_connection_status` | Connection status | text |
| `ampere_last_update` | Last update | text |

[Ampère →](carriers/ampere.md)

## Trunkrs

| ID | Name | Type |
|---|---|---|
| `trunkrs_parcel_count` | Active parcels | number |
| `trunkrs_status` | Status | text |
| `trunkrs_tracking` | Tracking number | text |
| `trunkrs_sender` | Sender | text |
| `trunkrs_receiver` | Receiver | text |
| `trunkrs_delivery_date` | Delivery date | text |
| `trunkrs_delivery_window` | Delivery window | text |
| `trunkrs_next_delivery` | Next delivery | text |
| `trunkrs_out_for_delivery_count` | Out for delivery | number |
| `trunkrs_delivered_count` | Recently delivered | number |
| `trunkrs_last_event` | Last event | text |
| `myparcel_connection_status` | Connection status | text |
| `trunkrs_last_update` | Last update | text |

[Trunkrs →](carriers/trunkrs.md)

## Dynalogic

| ID | Name | Type |
|---|---|---|
| `dynalogic_parcel_count` | Active parcels | number |
| `dynalogic_status` | Status | text |
| `dynalogic_tracking` | Tracking number | text |
| `dynalogic_sender` | Sender | text |
| `dynalogic_receiver` | Receiver | text |
| `dynalogic_delivery_date` | Delivery date | text |
| `dynalogic_delivery_window` | Delivery window | text |
| `dynalogic_next_delivery` | Next delivery | text |
| `dynalogic_out_for_delivery_count` | Out for delivery | number |
| `dynalogic_delivered_count` | Recently delivered | number |
| `dynalogic_last_event` | Last event | text |
| `myparcel_connection_status` | Connection status | text |
| `dynalogic_last_update` | Last update | text |

[Dynalogic →](carriers/dynalogic.md)

## Dragonfly / Intelcom

| ID | Name | Type |
|---|---|---|
| `dragonfly_parcel_count` | Active parcels | number |
| `dragonfly_status` | Status | text |
| `dragonfly_tracking` | Tracking number | text |
| `dragonfly_sender` | Sender | text |
| `dragonfly_delivery_date` | Delivery date | text |
| `dragonfly_delivery_window` | Delivery window | text |
| `dragonfly_next_delivery` | Next delivery | text |
| `dragonfly_out_for_delivery_count` | Out for delivery | number |
| `dragonfly_delivered_count` | Recently delivered | number |
| `dragonfly_outgoing_count` | Sent parcels underway | number |
| `dragonfly_last_event` | Last event | text |
| `myparcel_connection_status` | Connection status | text |
| `dragonfly_last_update` | Last update | text |

[Dragonfly / Intelcom →](carriers/dragonfly.md)

## Mondial Relay

| ID | Name | Type |
|---|---|---|
| `mondial_relay_parcel_count` | Active parcels | number |
| `mondial_relay_status` | Status | text |
| `mondial_relay_tracking` | Tracking number | text |
| `mondial_relay_sender` | Sender | text |
| `mondial_relay_delivery_date` | Delivery date | text |
| `mondial_relay_delivery_window` | Delivery window | text |
| `mondial_relay_next_delivery` | Next delivery | text |
| `mondial_relay_out_for_delivery_count` | Out for delivery | number |
| `mondial_relay_delivered_count` | Recently delivered | number |
| `mondial_relay_outgoing_count` | Sent parcels underway | number |
| `mondial_relay_last_event` | Last event | text |
| `myparcel_connection_status` | Connection status | text |
| `mondial_relay_last_update` | Last update | text |

[Mondial Relay →](carriers/mondial-relay.md)

## Amazon

| ID | Name | Type |
|---|---|---|
| `amazon_parcel_count` | Active parcels | number |
| `amazon_status` | Status | text |
| `amazon_tracking` | Tracking number | text |
| `amazon_item` | Item | text |
| `amazon_carrier` | Delivery carrier | text |
| `amazon_delivery_date` | Delivery date | text |
| `amazon_next_delivery` | Next delivery | text |
| `amazon_out_for_delivery_count` | Out for delivery | number |
| `amazon_pickup_count` | Ready for pickup | number |
| `amazon_delivered_count` | Recently delivered | number |
| `amazon_last_event` | Last event | text |
| `myparcel_connection_status` | Connection status | text |
| `amazon_last_update` | Last update | text |

[Amazon →](carriers/amazon.md)
