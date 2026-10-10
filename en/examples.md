# Flow examples

A few useful Flows to get started. Card titles are as in Homey; the full list is on [Flow cards](flows.md).

## 1. Notify with the parcel image when PostNL is coming

* **When:** *A parcel status changed* (PostNL)
* **And:** *The current parcel status is* `Courier is on the way`
* **Then:** Send a push notification with image: text `[[Package sender]] arrives between [[Delivery window]]`, image the card's **My delivery image** token.

The image is pinned to exactly this parcel and status. To use the image in another Flow (e.g. a time trigger), pick the global token **&lt;device name&gt; · Parcel image**.

## 2. Out for delivery (other carriers)

* **When:** *DPD parcel out for delivery* (or the *out for delivery* card of DHL, GLS, Trunkrs, Dynalogic, Dragonfly, Amazon …)
* **Then:** Send a notification `[[Sender]] arrives today, [[Delivery window]]`.

## 3. Pickup code for Vinted Go or InPost

* **When:** *Vinted Go parcel ready for pickup*
* **Then:** Send a notification `Pick up at [[Pickup point]] with code [[Pickup code]]`.

## 4. New mail with scan

* **When:** *New mail is expected* (PostNL)
* **Then:** Send a notification with the card's **Mail item image** token, or use **&lt;device name&gt; · Latest mail scan** in any other Flow.

## 5. Track a tracking number automatically

* **When:** e.g. an e-mail or webhook Flow that carries the tracking number
* **Then:** *Track Trunkrs parcel…* (or *Track GLS parcel…*, *Track DHL parcel…* …) with the number as argument. Clean up later with *Remove delivered … parcels*.

## 6. Nobody home?

* **When:** Everybody left
* **And:** *A … parcel is out for delivery*
* **Then:** Send a reminder to ask the neighbours or choose a pickup point.

## Advanced Flow tips

* **One trigger card per action chain.** Tokens only exist in the Flow started by *that* card. If you connect two triggers to the same action block that uses a token of one of them, Homey reports *Missing token value* as soon as the other trigger fires.
* **Or use global tokens.** The global PostNL tokens (**Parcel image**, **Latest mail scan**, status, delivery window …) and the MyParcel delivery tokens work in every Flow, whichever card started it. See [Flow tokens](tokens.md).
* Cards fire once per change – also after a restart. You don't need to filter duplicate notifications yourself.
