# Changelog

Current version: **v0.3.7**.

The full version history, release updates and discussions are in the official MyParcel Homey Community topic.

[**View changelog and releases →**](https://community.homey.app/t/app-pro-myparcel/159800)

## v0.3.7 – Correct names in Flow tokens

* Flow token titles and the 'unknown' status now name the right carrier, pickup point titles are generic, Vinted Go device name, updated App Store description.

## v0.3.6 – New carriers and the whole app in 13 languages

* New: [Trunkrs](carriers/trunkrs.md), [Dynalogic](carriers/dynalogic.md), [Dragonfly / Intelcom](carriers/dragonfly.md), [Mondial Relay](carriers/mondial-relay.md) and [Amazon](carriers/amazon.md) (experimental) – with capabilities, Flow cards and tokens, and visible in MyParcel Packages and MyParcel Delivery.
* The whole app is translated into 13 languages; dates, times, weights and dimensions follow your language, widgets show relative times and Arabic is right-to-left.
* Fixed: the *Open sign-in* button for InPost and Post & DHL Germany, the UPS condition *account connected* outside English, and English PostNL screens for Dutch users.

## v0.3.5 – FedEx, Budbee, Vinted Go, InPost, bpost and Ampère rebuilt

* FedEx through the Track API, Budbee with Boxes, **Homerr is now Vinted Go** (with pickup code), **InPost UK is now InPost** (5 countries, account for Poland/Italy), bpost with My bpost and Mail Ahead letters, Ampère through its own parcel page.
* New Flow cards on all six devices (new parcel, status, event, out for delivery, ready for pickup, delivered, problem, sent parcels) plus conditions and actions.
* PostNL: the Flow image uses the My Delivery image, pinned per trigger; new global tokens **Parcel image** and **Latest mail scan**.

## v0.3.4 – DHL, DHL Express and Post & DHL Germany rebuilt

* DHL with its own status codes and no account required; DHL Express with air waybill numbers without an account; Post & DHL Germany with Packstation and sent parcels.
* New widget **DHL Parcels (Germany)**.

## v0.3.3 – GLS without account, DPD rebuilt

* DPD in 19 countries with one clear status set; GLS without an account in 20 countries.
* Lower memory use for PostNL; MyParcel Packages and MyParcel Delivery show all carriers by default.

## v0.3.2 – PostNL & stability

* PostNL rebuilt with direct login, expanded parcel data and the My Post, My Packages, My Delivery and Parcel Journey widgets.
* Fixed: a crash loop on app start and repeated *delivered* triggers.
