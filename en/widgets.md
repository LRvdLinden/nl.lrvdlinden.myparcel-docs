# Widgets

MyParcel has eight Homey Dashboard widgets. Add them through the Dashboard → **Add widget** → **MyParcel** and choose the device (or devices) the widget should show.

## For all carriers

### MyParcel Packages

Widget ID: `myparcel-pakketten` · height 360

List of the parcels of all your MyParcel carriers, with logo, translated status, sender, date and delivery window or last update. Tap a parcel for a popup with every detail the carrier provides (tracking number, last event, weight, dimensions, pickup point …).

**Setting:** **Show all carriers (including newly added ones)** – on by default: every MyParcel carrier device is shown, also devices you add later. Turn it off to only show the devices selected for this widget.

### MyParcel Delivery

Widget ID: `myparcel-bezorging` · height 420

The active deliveries of all selected carriers together, with carrier branding, sender, status, delivery date/window and a timeline that follows each carrier's own status.

**Setting:** **Show all carriers (including newly added ones)** – as above.

## PostNL

| Widget | ID | What you see |
|---|---|---|
| **My Post** | `poststukken` | Announced mail with scans (live; refreshes every minute while the widget is open). |
| **My Packages** | `postnl-mijn-pakketten` | Your PostNL parcels with status and delivery moment. |
| **My Delivery** | `postnl-pakketdetails` | The active parcel with the animated PostNL van, live delivery window and progress. |
| **Parcel Journey** | `postnl-pakket-reis` | The timeline of a PostNL parcel, step by step. |

These widgets show one PostNL device.

## Post & DHL Germany

| Widget | ID | What you see |
|---|---|---|
| **DHL Parcels (Germany)** (*DHL Pakete*) | `dhl-de-pakete` | Your DHL parcels in Germany with status, Packstation and sent parcels. |
| **Deutsche Post Mail** | `deutsche-post-poststukken` | Announced Deutsche Post letters. |

## Good to know

* Widgets refresh a device at most once every 5 minutes; they do not start a full sync per open screen.
* Dates and times follow your language; widgets show relative times ("2 hours ago"). Arabic is shown right-to-left.
* Available data depends on the carrier and parcel.

[Device data](device.md) · [Carriers](carriers/README.md)
