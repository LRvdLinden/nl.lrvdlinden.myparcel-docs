# Install and connect

## 1. Install the app

Install **MyParcel** from the [Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/). The app runs on Homey Pro (local platform) with Homey version 12.3.0 or newer.

## 2. Add a carrier

1. Open Homey → **Devices** → **+** → **MyParcel**.
2. Choose your carrier. Every carrier is **its own device**; add one per carrier (or per account) you use.
3. Follow the pairing screen. Depending on the carrier:
   * **Account** – sign in with your carrier account (PostNL, DPD, bpost, Vinted Go, Post & DHL Germany, Mondial Relay, Amazon; optional for DHL, DHL Express and InPost). For some carriers you open a sign-in page and then paste the address you ended on back into Homey.
   * **Tracking number** – enter tracking numbers, sometimes with a postal code (GLS, Trunkrs, Dynalogic, Dragonfly / Intelcom, Budbee, InPost, DHL, DHL Express, bpost).
   * **API key** – FedEx (Track API) and Royal Mail (Click & Drop).
4. Wait for the first sync to finish. Existing parcels are then recorded silently, so you do not get a flood of *new parcel* notifications.

The exact steps are on each [carrier](carriers/README.md) page.

## 3. Add tracking numbers later

For carriers that work with tracking numbers you can add or remove numbers through:

* the **device settings** (one number per line, sometimes with a postal code after it), or
* the Flow actions **Track parcel…**, **Stop tracking parcel…** and **Remove delivered parcels**.

Add `out` (or ` out`) after a number for a parcel you send yourself, where the carrier supports it (DHL, DHL Express, Post & DHL Germany, Dragonfly).

## 4. Widgets and Flows

* Put the [widgets](widgets.md) on your Homey Dashboard. **MyParcel Packages** and **MyParcel Delivery** show all carriers by default, including devices you add later.
* Build [Flows](flows.md) with your carrier's cards; see the [examples](examples.md).

## Good to know

* **Smart polling:** every 15 minutes when a delivery is near, every 45 minutes otherwise and quiet at night. Delivered parcels are no longer polled.
* **Passwords:** where possible MyParcel only stores tokens, not your password.
* **Repair:** when a login has expired, use **Repair** on the device – no need to remove the device. See [Troubleshooting](troubleshooting.md).
* Not every carrier provides the same data; empty fields mean the carrier does not return that value.

[Homey App Store](https://homey.app/en-us/app/nl.lrvdlinden.MyParcel/MyParcel/test/) · [Homey Community](https://community.homey.app/t/app-pro-myparcel/159800)
