# Troubleshooting

## Device says "Not connected" or the login expired

1. Open the device → **⚙ Settings** → **Repair** and sign in again or paste a new code. No need to remove the device: Flows and widgets keep working.
2. Check that your parcels are also visible in the carrier's app or website.
3. Changed the country or store (DPD, Amazon)? Use **Repair** to sign in for that country or store.

During a temporary network hiccup the device stays available with a warning and the last known data; MyParcel tries again later.

## Sign-in links work only once

For **Amazon**, **Mondial Relay**, **InPost** and **Post & DHL Germany** you open a sign-in page and then paste the address you ended on back into Homey. Every sign-in link is single-use:

* If connecting fails, open the sign-in page **again** from the pairing screen – you get a new link.
* Copy the **full** address from the address bar. A page that does not load or shows an error (e.g. `https://account.inpost-group.com/callback?code=…`) is normal.
* Paste the address quickly; an old code is rejected by the carrier.

## A parcel does not appear

* **Tracking-number carriers** (GLS, Trunkrs, Dynalogic, Dragonfly, Budbee, InPost, DHL, DHL Express, FedEx): check the number and – where needed – the **postal code**. GLS, Trunkrs, Dynalogic and bpost (without account) only show a parcel with the right delivery postal code; add a different postal code after the number.
* **Account carriers:** the parcel has to be linked to your account at the carrier.
* **Amazon** reads at most 10 shipments per poll; more shipments appear in the next rounds.
* Delivered parcels disappear after the configured number of days (*Show delivered parcels for (days)*).

## Updates arrive slowly (rate limits)

* MyParcel polls smartly: every 15 minutes when a delivery is near, every 45 minutes otherwise, quiet at night.
* **DHL Express** allows about one lookup per 40 minutes; several air waybills are refreshed in turn and MyParcel backs off when DHL asks to slow down.
* Widgets refresh a device at most once every 5 minutes.
* Use the **Refresh …** / **Synchronize PostNL** action if you want to refresh right away.

## Missing token value

Homey shows *Missing token value: …* (e.g. `package_image`) when a Flow uses a token the starting card did not pass. This mostly happens in **Advanced Flow**, when two trigger cards are connected to the same action block and the block uses a token of one of them.

Solutions:

* Use **one trigger card per action chain**, or
* use a **global token** that works in every Flow: **&lt;device name&gt; · Parcel image**, **&lt;device name&gt; · Latest mail scan** or the MyParcel delivery tokens. See [Flow tokens](tokens.md).

Since v0.3.5 the PostNL image in parcel Flows is never empty: delivered parcels keep the current My Delivery image.

## A card does not fire

* Cards fire **once per change**. After an update or restart, existing parcels are recorded silently, so there are no notifications for parcels that were already known.
* **Mondial Relay** has no reliable status yet: only *new parcel* and *tracking event* fire.
* **Dynalogic** provides no delivery window, so there is no *delivery time changed* card.

## Still stuck?

Send a diagnostic report via Homey → **Settings** → **Apps** → **MyParcel** → **Send diagnostic report** and post the code in the [Homey Community topic](https://community.homey.app/t/app-pro-myparcel/159800).
