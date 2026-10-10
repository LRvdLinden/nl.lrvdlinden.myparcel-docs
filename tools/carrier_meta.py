# Hand-written per-carrier text for the generated MyParcel docs (nl + en).
ORDER = ['postnl', 'dhl-parcel', 'dhl-express', 'dpd', 'ups', 'budbee', 'homerr', 'fedex', 'gls',
         'inpost-uk', 'bpost', 'royal-mail', 'post-dhl-de', 'ampere', 'trunkrs', 'dynalogic',
         'dragonfly', 'mondial-relay', 'amazon']

# Carriers that get the 'New in v0.3.6' badge.
NEW_IN_036 = {'trunkrs', 'dynalogic', 'dragonfly', 'mondial-relay', 'amazon'}

M = {}

M['postnl'] = dict(
    name={'nl': 'PostNL', 'en': 'PostNL'},
    flags='🇳🇱',
    methods=['Account'],
    countries={'nl': 'Nederland (PostNL-account van jouw.postnl.nl)', 'en': 'Netherlands (PostNL account from jouw.postnl.nl)'},
    intro={
        'nl': 'Je PostNL-account in Homey: aangekondigde post (Mijn Post) met scans, al je pakketten (Mijn Pakketten) met de officiële Track & Trace-status, bezorgvenster, gewicht, afmetingen en volledige statusgeschiedenis, plus de afbeelding **Mijn Bezorging** voor je Flows en dashboard.',
        'en': 'Your PostNL account in Homey: announced mail (My Post) with scans, all your parcels (My Packages) with the official Track & Trace status, delivery window, weight, dimensions and full status history, plus the **My Delivery** image for your Flows and dashboard.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **PostNL**.',
               'Vul het e-mailadres en wachtwoord in waarmee je inlogt op **jouw.postnl.nl** en tik op **Koppelen**.',
               'Je wachtwoord wordt alleen gebruikt om bij PostNL in te loggen; Homey bewaart daarna de verkregen tokens, niet je wachtwoord.',
               'Is de aanmelding later verlopen? Gebruik **Herstellen** op het apparaat en log opnieuw in.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **PostNL**.',
               'Enter the e-mail address and password you use on **jouw.postnl.nl** and tap **Connect**.',
               'Your password is only used to sign in to PostNL; Homey then stores the resulting tokens, not your password.',
               'Login expired later on? Use **Repair** on the device and sign in again.']},
    limits={
        'nl': ['**Flow-afbeelding:** de pakketkaarten (ook de bezorgvensterkaarten) geven de **Mijn Bezorging**-camera-afbeelding mee, vastgezet op precies dat pakket en die status vlak vóór de trigger. Bezorgde pakketten krijgen geen nieuwe tekening en houden de huidige Mijn Bezorging-afbeelding, zodat het token nooit leeg is.',
               '**Globale afbeeldingstokens:** **Pakketafbeelding** en **Scan laatste poststuk** werken in elke Flow, welke kaart de Flow ook startte. Ze verschijnen als *&lt;apparaatnaam&gt; · Pakketafbeelding* en *&lt;apparaatnaam&gt; · Scan laatste poststuk*.',
               'Track & Trace wordt alleen voor actieve pakketten opgehaald (max. 3 tegelijk); alleen de 15 meest recente bezorgde pakketten worden bewaard.',
               'Mijn Post is live: post die je in de PostNL-app verwijdert, verdwijnt na de volgende verversing ook uit Homey. Scans worden niet lokaal opgeslagen.'],
        'en': ['**Flow image:** parcel cards (also the delivery-window cards) pass the **My Delivery** camera image, pinned to exactly that parcel and status right before the trigger. Delivered parcels get no new drawing and keep the current My Delivery image, so the token is never empty.',
               '**Global image tokens:** **Parcel image** and **Latest mail scan** work in every Flow, whichever card started it. They appear as *&lt;device name&gt; · Parcel image* and *&lt;device name&gt; · Latest mail scan*.',
               'Track & Trace is only fetched for active parcels (max. 3 at a time); only the 15 most recent delivered parcels are kept.',
               'My Post is live-only: mail you remove in the PostNL app also disappears from Homey after the next refresh. Scans are not stored locally.']},
)

M['dhl-parcel'] = dict(
    name={'nl': 'DHL', 'en': 'DHL'},
    flags='🇳🇱',
    methods=['Account', 'Tracking'],
    countries={'nl': 'Nederland (My DHL-account en DHL Parcel-trackingnummers)', 'en': 'Netherlands (My DHL account and DHL Parcel tracking numbers)'},
    intro={
        'nl': 'DHL Parcel (eCommerce) in Homey: je My DHL-pakketten met DHL\'s eigen statuscodes (onderweg, klaar bij een ServicePoint/ParcelStation, bezorgd bij de buren of in de brievenbus, retouren), het bezorgvenster en de statusgeschiedenis. Een account is optioneel: losse trackingnummers werken ook.',
        'en': 'DHL Parcel (eCommerce) in Homey: your My DHL parcels with DHL\'s own status codes (out for delivery, ready at a ServicePoint/ParcelStation, delivered at neighbours or in the mailbox, returns), the delivery window and status history. An account is optional: plain tracking numbers work too.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **DHL**.',
               'Vul je **My DHL-account** (e-mailadres en wachtwoord) in om al je pakketten automatisch te zien, **of** vul alleen **trackingnummers** in (één per regel, bijv. `JJD…` of `3S…`). Allebei kan ook.',
               'Voeg optioneel een postcode toe voor de trackinglink en `out` voor een pakket dat je zelf verstuurt.',
               'Tik op **DHL toevoegen**. Nummers toevoegen kan later via de apparaatinstellingen of met een Flow.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **DHL**.',
               'Enter your **My DHL account** (e-mail address and password) to see all your parcels automatically, **or** only enter **tracking numbers** (one per line, e.g. `JJD…` or `3S…`). You can also do both.',
               'Optionally add a postal code for the tracking link and `out` for a parcel you send yourself.',
               'Tap **Add DHL**. You can add numbers later in the device settings or with a Flow.']},
    limits={
        'nl': ['De statusgeschiedenis wordt alleen opgehaald als een status verandert.',
               'Zonder account worden trackingnummers via DHL\'s openbare tracking gelezen; afzender en ontvanger zijn dan niet altijd bekend.'],
        'en': ['Status history is only fetched when a status changes.',
               'Without an account, tracking numbers are read through DHL\'s public tracking; sender and receiver are not always known then.']},
)

M['dhl-express'] = dict(
    name={'nl': 'DHL Express', 'en': 'DHL Express'},
    flags='🌍',
    methods=['Tracking', 'Account'],
    countries={'nl': 'Wereldwijd', 'en': 'Worldwide'},
    intro={
        'nl': 'Internationale DHL Express-zendingen volgen met hun luchtvrachtbriefnummer (10 cijfers) – zonder account. Optioneel combineer je dat met je MyDHL+-account om ook de zendingen uit dat account te zien.',
        'en': 'Follow international DHL Express shipments with their air waybill number (10 digits) – no account needed. Optionally combine that with your MyDHL+ account to also see the shipments in that account.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **DHL Express**.',
               'Vul de **luchtvrachtbriefnummers** in (één per regel, bijv. `1234567890`; voeg `out` toe voor een zending die je zelf verstuurt) en tik op **Zendingen volgen**.',
               'Optioneel: open **MyDHL+-account gebruiken** en log in met e-mailadres en wachtwoord (plus verificatiecode als DHLPass erom vraagt).',
               'Blokkeert DHLPass de directe login, gebruik dan de **DHL Express Homey Login Helper** en plak de `DHLEXPRESS1`-sessiecode via **Koppelen met helpercode**.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **DHL Express**.',
               'Enter the **air waybill numbers** (one per line, e.g. `1234567890`; add `out` for a shipment you send yourself) and tap **Track shipments**.',
               'Optional: open **Use a MyDHL+ account** and sign in with e-mail address and password (plus a verification code when DHLPass asks for one).',
               'If DHLPass blocks the direct login, use the **DHL Express Homey Login Helper** and paste the `DHLEXPRESS1` session code via **Connect with helper code**.']},
    limits={
        'nl': ['**Aanvraaglimiet:** DHL Express staat ongeveer één opvraging per 40 minuten toe. Meerdere nummers worden om de beurt bijgewerkt (zendingen bij de koerier eerst) en MyParcel wacht langer als DHL vraagt om te vertragen.',
               'Er is geen apart bezorgvenster bij alle zendingen; dat hangt af van wat DHL Express teruggeeft.'],
        'en': ['**Rate limit:** DHL Express allows about one lookup per 40 minutes. Several numbers are refreshed in turn (shipments with the courier first) and MyParcel backs off when DHL asks to slow down.',
               'Not every shipment has a delivery window; that depends on what DHL Express returns.']},
)

M['dpd'] = dict(
    name={'nl': 'DPD', 'en': 'DPD'},
    flags='🇳🇱 🇧🇪 🇩🇪 🇱🇺 🇫🇷 🇨🇭 🇬🇧 🇮🇹 🇵🇹 🇵🇱 🇨🇿 🇸🇰 🇭🇺 🇸🇮 🇭🇷 🇪🇪 🇱🇻 🇱🇹 🇦🇷',
    methods=['Account'],
    countries={'nl': 'Nederland, België, Duitsland, Luxemburg, Frankrijk, Zwitserland, Verenigd Koninkrijk, Italië (BRT), Portugal, Polen, Tsjechië, Slowakije, Hongarije, Slovenië, Kroatië, Estland, Letland, Litouwen en Argentinië',
               'en': 'Netherlands, Belgium, Germany, Luxembourg, France, Switzerland, United Kingdom, Italy (BRT), Portugal, Poland, Czech Republic, Slovakia, Hungary, Slovenia, Croatia, Estonia, Latvia, Lithuania and Argentina'},
    intro={
        'nl': 'Je myDPD-account in Homey (hetzelfde account als in de DPD-app): inkomende en verzonden pakketten met één duidelijke statusset (aangemeld, onderweg, wordt bezorgd, klaar bij ParcelShop, bezorgd, retour, probleem), het Follow My Parcel-bezorgvenster, gewicht, afmetingen en de volledige scangeschiedenis.',
        'en': 'Your myDPD account in Homey (the same account as in the DPD app): incoming and sent parcels with one clear status set (registered, in transit, out for delivery, ready at a ParcelShop, delivered, returning, problem), the Follow My Parcel delivery window, weight, dimensions and the full scan history.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **DPD**.',
               'Kies je **land**.',
               'Log in met het e-mailadres en wachtwoord van je **myDPD-account** en tik op **Koppelen**.',
               '**Polen:** vul je mobiele nummer in, tik op **Sms-code versturen** en daarna op **Controleren en koppelen**. Homey bewaart alleen een vernieuwbaar token, nooit de code.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **DPD**.',
               'Choose your **country**.',
               'Sign in with the e-mail address and password of your **myDPD account** and tap **Connect**.',
               '**Poland:** enter your mobile number, tap **Send SMS code** and then **Verify and connect**. Homey only keeps a renewable token, never the code.']},
    limits={
        'nl': ['Land gewijzigd? Gebruik **Herstellen** op het apparaat om voor dat land opnieuw in te loggen.',
               'Het bezorgvenster wordt alleen opgehaald voor actieve inkomende pakketten.'],
        'en': ['Changed the country? Use **Repair** on the device to sign in for that country.',
               'The delivery window is only fetched for active incoming parcels.']},
)

M['ups'] = dict(
    name={'nl': 'UPS', 'en': 'UPS'},
    flags='🌍',
    methods=['Account', 'Tracking'],
    countries={'nl': 'Wereldwijd (land en UPS-taal instelbaar)', 'en': 'Worldwide (country and UPS locale configurable)'},
    intro={
        'nl': 'UPS-zendingen in Homey via je UPS-account (UPS My Choice-dashboard), met service, verzend- en bezorgadres, Access Point, bezorgdatum en bezorgvenster. Als alternatief kun je losse trackingnummers volgen.',
        'en': 'UPS shipments in Homey through your UPS account (UPS My Choice dashboard), with service, ship-from and ship-to, Access Point, delivery date and delivery window. Alternatively you can follow plain tracking numbers.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **UPS**.',
               'Kies **land** en **taal**.',
               'Log in bij UPS met de **UPS Token Helper**, open het UPS-dashboard, wacht tot de helper meldt dat de websessie klaar is en plak de `web_session`-koppelwaarde in **UPS-login-callback**. Tik op **UPS koppelen**.',
               '**Handmatig alternatief:** vul trackingnummers in en tik op **Trackingnummers toevoegen**.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **UPS**.',
               'Choose **country** and **language**.',
               'Sign in to UPS with the **UPS Token Helper**, open the UPS dashboard, wait until the helper reports that the web session is ready and paste the `web_session` pairing value into **UPS login callback**. Tap **Connect UPS**.',
               '**Manual fallback:** enter tracking numbers and tap **Add tracking numbers**.']},
    limits={
        'nl': ['UPS heeft (nog) minder Flow-kaarten dan de vernieuwde vervoerders: nieuw pakket, status gewijzigd, bezorgd en bezorgvenster.',
               'De UPS-websessie kan verlopen; gebruik dan **Herstellen** met een nieuwe helperwaarde.'],
        'en': ['UPS has fewer Flow cards than the rebuilt carriers (for now): new parcel, status changed, delivered and delivery window.',
               'The UPS web session can expire; then use **Repair** with a new helper value.']},
)

M['budbee'] = dict(
    name={'nl': 'Budbee', 'en': 'Budbee'},
    flags='🇳🇱 🇧🇪 🇸🇪 🇩🇰 🇫🇮',
    methods=['Tracking'],
    countries={'nl': 'Nederland, België en de andere Budbee-landen (tracking via Budbee)', 'en': 'Netherlands, Belgium and the other Budbee countries (tracking through Budbee)'},
    intro={
        'nl': 'Budbee-thuisbezorgingen en Budbee Boxes. Een pakket dat *in de Box is afgeleverd* is klaar om op te halen, *opgehaald* betekent bezorgd. Met ETA als bezorgvenster, ophaaldeadline, retouren/verzonden pakketten en gebeurtenisteksten in je eigen taal.',
        'en': 'Budbee home deliveries and Budbee Boxes. A parcel *delivered in the Box* is ready for pickup, *picked up* means delivered. With ETA as delivery window, pickup deadline, returns/sent parcels and event texts in your own language.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **Budbee**.',
               'Vul je **tracking-/bestelnummers** in (één per regel, uit de winkelmail of de Budbee-link). Er is geen account nodig.',
               'Tik op **Budbee-apparaat toevoegen**. Nummers toevoegen kan later via de apparaatinstellingen of met een Flow.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **Budbee**.',
               'Enter your **tracking/order numbers** (one per line, from the shop e-mail or the Budbee link). No account is needed.',
               'Tap **Add Budbee device**. You can add numbers later in the device settings or with a Flow.']},
    limits={
        'nl': ['Budbee heeft geen account-koppeling: alleen nummers die je toevoegt worden gevolgd.'],
        'en': ['Budbee has no account link: only numbers you add are followed.']},
)

M['homerr'] = dict(
    name={'nl': 'Vinted Go', 'en': 'Vinted Go'},
    flags='🇳🇱 🇧🇪 🇫🇷 🇪🇸',
    methods=['Account'],
    countries={'nl': 'Nederland, België, Frankrijk en de andere Vinted Go-landen', 'en': 'Netherlands, Belgium, France and the other Vinted Go countries'},
    intro={
        'nl': 'Vinted Go (voorheen Homerr): je pakketten per account, ook verzonden pakketten, met afhaalpunt, **ophaalcode** en artikelnaam.',
        'en': 'Vinted Go (formerly Homerr): your parcels per account, including sent parcels, with pickup point, **pickup code** and item name.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **Vinted Go**.',
               'Vul het e-mailadres in dat aan je Vinted Go-zendingen is gekoppeld en tik op **Verificatielink versturen**.',
               'Open de verificatiemail en plak de **volledige link of het token** in het scherm.',
               'Tik op **Account koppelen**. MyParcel bewaart een roterend logintoken, geen wachtwoord.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **Vinted Go**.',
               'Enter the e-mail address linked to your Vinted Go shipments and tap **Send verification link**.',
               'Open the verification e-mail and paste the **complete link or token** into the screen.',
               'Tap **Connect account**. MyParcel stores a rotating login token, not a password.']},
    limits={
        'nl': ['De tijdlijn van een pakket wordt alleen opgehaald als er iets verandert; afgesloten pakketten worden verborgen nadat ze zijn gemeld.'],
        'en': ['A parcel\'s timeline is only fetched on a change; closed parcels are hidden after they were announced.']},
)

M['fedex'] = dict(
    name={'nl': 'FedEx', 'en': 'FedEx'},
    flags='🌍',
    methods=['API'],
    countries={'nl': 'Wereldwijd', 'en': 'Worldwide'},
    intro={
        'nl': 'FedEx-zendingen via de officiële **FedEx Track API** met je eigen API-sleutel: FedEx-statuscodes inclusief retouren, klaar om op te halen bij een FedEx-locatie, bezorgvenster, service, gewicht, afmetingen en statusgeschiedenis.',
        'en': 'FedEx shipments through the official **FedEx Track API** with your own API key: FedEx status codes incl. returns, ready for pickup at a FedEx location, delivery window, service, weight, dimensions and status history.'},
    connect={
        'nl': ['Maak op het FedEx Developer Portal een project aan met toegang tot de **Track API** en noteer de **Client ID** en **Client Secret**.',
               'Open Homey → **Apparaten** → **+** → **MyParcel** → **FedEx**.',
               'Vul Client ID, Client Secret en de **trackingnummers** (één per regel) in en tik op **FedEx koppelen**.',
               'Het OAuth-token wordt door MyParcel zelf bewaard en vernieuwd.'],
        'en': ['Create a project on the FedEx Developer Portal with access to the **Track API** and note the **Client ID** and **Client Secret**.',
               'Open Homey → **Devices** → **+** → **MyParcel** → **FedEx**.',
               'Enter Client ID, Client Secret and the **tracking numbers** (one per line) and tap **Connect FedEx**.',
               'MyParcel keeps and renews the OAuth token on its own.']},
    limits={
        'nl': ['Zonder eigen FedEx API-gegevens werkt dit apparaat niet; FedEx heeft geen accountlogin voor externe koppelingen.'],
        'en': ['This device does not work without your own FedEx API credentials; FedEx has no account login for third-party integrations.']},
)

M['gls'] = dict(
    name={'nl': 'GLS', 'en': 'GLS'},
    flags='🇳🇱 🇧🇪 🇩🇪 🇦🇹 🇨🇭 🇱🇺 🇫🇷 🇮🇹 🇩🇰 🇫🇮 🇮🇪 🇵🇱 🇨🇿 🇸🇰 🇭🇺 🇸🇮 🇭🇷 🇷🇸 🇺🇸 🇨🇦',
    methods=['Tracking'],
    countries={'nl': '20 landen: Nederland (met gewicht, afmetingen, bezorgvenster, ParcelShop en geschiedenis), België, Duitsland, Oostenrijk, Zwitserland, Luxemburg, Frankrijk, Italië, Denemarken, Finland, Ierland, Polen, Tsjechië, Slowakije, Hongarije, Slovenië, Kroatië, Servië, Verenigde Staten en Canada',
               'en': '20 countries: Netherlands (with weight, dimensions, delivery window, ParcelShop and history), Belgium, Germany, Austria, Switzerland, Luxembourg, France, Italy, Denmark, Finland, Ireland, Poland, Czech Republic, Slovakia, Hungary, Slovenia, Croatia, Serbia, United States and Canada'},
    intro={
        'nl': 'GLS-pakketten volgen via GLS\' eigen openbare tracking – geen MyGLS-account nodig. Alleen je land, bezorgpostcode en trackingnummers. Bestaande apparaten met een MyGLS-zakelijk account blijven werken.',
        'en': 'Follow GLS parcels through GLS\' own public tracking – no MyGLS account needed. Just your country, delivery postal code and tracking numbers. Existing devices with a MyGLS business account keep working.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **GLS**.',
               'Kies je **land** en vul de **bezorgpostcode** in (GLS deelt pakketgegevens alleen met de postcode waar het pakket bezorgd wordt).',
               'Vul optioneel **trackingnummers** in: één per regel, het lange pakketnummer of de korte track-ID uit de GLS-mail/sms. Zet een afwijkende postcode achter het nummer.',
               'Tik op **GLS toevoegen**. Later meer toevoegen kan via de apparaatinstellingen of met een Flow.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **GLS**.',
               'Choose your **country** and enter the **delivery postal code** (GLS only shares parcel details with the postal code the parcel is delivered to).',
               'Optionally enter **tracking numbers**: one per line, the long parcel number or the short track ID from the GLS e-mail/SMS. Add a different postal code after the number when needed.',
               'Tap **Add GLS**. You can add more later in the device settings or with a Flow.']},
    limits={
        'nl': ['Buiten Nederland levert GLS minder details (bijv. geen gewicht/afmetingen of bezorgvenster).',
               'Bezorgde pakketten worden niet opnieuw opgevraagd en na het ingestelde aantal dagen verwijderd (0 = bewaren).'],
        'en': ['Outside the Netherlands GLS returns fewer details (e.g. no weight/dimensions or delivery window).',
               'Delivered parcels are not polled again and are removed after the configured number of days (0 = keep).']},
)

M['inpost-uk'] = dict(
    name={'nl': 'InPost', 'en': 'InPost'},
    flags='🇬🇧 🇵🇱 🇮🇹 🇵🇹 🇪🇸',
    methods=['Tracking', 'Account'],
    countries={'nl': 'Verenigd Koninkrijk, Polen, Italië, Portugal en Spanje (account: Polen en Italië)', 'en': 'United Kingdom, Poland, Italy, Portugal and Spain (account: Poland and Italy)'},
    intro={
        'nl': 'InPost-pakketten (voorheen *InPost UK*) volgen met hun nummer, plus optioneel je InPost-account (Polen/Italië) met je pakketten en hun **ophaalcode (open code)** voor de Paczkomat/locker.',
        'en': 'Follow InPost parcels (formerly *InPost UK*) with their number, plus optionally your InPost account (Poland/Italy) with your parcels and their **pickup (open) code** for the Paczkomat/locker.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **InPost**.',
               'Kies het **land** en vul de **pakketnummers** in (één per regel). Tik op **Pakketten volgen**.',
               'Optioneel (Polen/Italië): open **InPost-account gebruiken**, kies het land van het account en tik op **InPost-login openen**. Log in met je telefoonnummer en sms-code.',
               'Kopieer daarna het volledige `https://account.inpost-group.com/callback?…`-adres uit de adresbalk, plak het in **Callback-adres** en tik op **Account koppelen**.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **InPost**.',
               'Choose the **country** and enter the **parcel numbers** (one per line). Tap **Track parcels**.',
               'Optional (Poland/Italy): open **Use an InPost account**, choose the account country and tap **Open InPost sign-in**. Sign in with your phone number and SMS code.',
               'Then copy the full `https://account.inpost-group.com/callback?…` address from the address bar, paste it into **Callback address** and tap **Connect account**.']},
    limits={
        'nl': ['De accountkoppeling werkt alleen voor Polen en Italië; voor de andere landen volg je pakketnummers.',
               'Een inloglink werkt maar één keer; open de login opnieuw als het koppelen mislukt.'],
        'en': ['The account link only works for Poland and Italy; for the other countries you follow parcel numbers.',
               'A sign-in link only works once; open the sign-in again if connecting fails.']},
)

M['bpost'] = dict(
    name={'nl': 'bpost', 'en': 'bpost'},
    flags='🇧🇪',
    methods=['Account', 'Tracking'],
    countries={'nl': 'België', 'en': 'Belgium'},
    intro={
        'nl': 'Je My bpost-account in Homey: alle inkomende en verzonden pakketten, de bpost-processtappen, het bezorgvenster in Belgische tijd, het aantal stops tot jij aan de beurt bent en **Mail Ahead-brieven**. Zonder account volg je barcodes met een postcode.',
        'en': 'Your My bpost account in Homey: all incoming and sent parcels, the bpost process steps, the delivery window in Belgian time, stops until you and **Mail Ahead letters**. Without an account you follow barcodes with a postal code.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **bpost**.',
               'Log in met het e-mailadres en wachtwoord van **My bpost** en tik op **My bpost koppelen**. Je wachtwoord wordt één keer gebruikt; MyParcel bewaart bpost-logintokens.',
               '**Of** open **Barcodes volgen zonder account**: vul de postcode van het bezorgadres en de barcodes (één per regel, eventueel met afwijkende postcode erachter) in en tik op **Barcodes volgen**.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **bpost**.',
               'Sign in with the e-mail address and password of **My bpost** and tap **Connect My bpost**. Your password is used once; MyParcel keeps bpost login tokens.',
               '**Or** open **Track barcodes without an account**: enter the delivery postal code and the barcodes (one per line, optionally with a different postal code after it) and tap **Track barcodes**.']},
    limits={
        'nl': ['Mail Ahead-brieven en verzonden pakketten zijn alleen beschikbaar met een My bpost-account.'],
        'en': ['Mail Ahead letters and sent parcels are only available with a My bpost account.']},
)

M['royal-mail'] = dict(
    name={'nl': 'Royal Mail', 'en': 'Royal Mail'},
    flags='🇬🇧',
    methods=['API'],
    countries={'nl': 'Verenigd Koninkrijk', 'en': 'United Kingdom'},
    intro={
        'nl': 'Royal Mail-bestellingen uit je **Click & Drop**-account (voor verzenders). MyParcel haalt recente bestellingen automatisch op; je vult geen trackingnummers in.',
        'en': 'Royal Mail orders from your **Click & Drop** account (for senders). MyParcel retrieves recent orders automatically; you do not enter tracking numbers.'},
    connect={
        'nl': ['Maak in Royal Mail Click & Drop een API-integratie aan via **Settings → Integrations → Click & Drop API** en kopieer de autorisatiesleutel.',
               'Open Homey → **Apparaten** → **+** → **MyParcel** → **Royal Mail**.',
               'Plak de **Click & Drop API-sleutel** en tik op **Royal Mail koppelen**.'],
        'en': ['In Royal Mail Click & Drop, create an API integration under **Settings → Integrations → Click & Drop API** and copy its authorisation key.',
               'Open Homey → **Devices** → **+** → **MyParcel** → **Royal Mail**.',
               'Paste the **Click & Drop API key** and tap **Connect Royal Mail**.']},
    limits={
        'nl': ['Alleen voor Click & Drop-accounts (verzenders); inkomende Royal Mail-pakketten zonder Click & Drop worden niet ondersteund.',
               'Beperkte gegevens: aantal pakketten, status en laatste update.'],
        'en': ['Only for Click & Drop accounts (senders); incoming Royal Mail parcels without Click & Drop are not supported.',
               'Limited data: parcel count, status and last update.']},
)

M['post-dhl-de'] = dict(
    name={'nl': 'Post & DHL Duitsland', 'en': 'Post & DHL Germany'},
    flags='🇩🇪',
    methods=['Account', 'Tracking'],
    countries={'nl': 'Duitsland', 'en': 'Germany'},
    intro={
        'nl': 'Je DHL-pakketten in Duitsland met de statusladder van DHL (aangekondigd, onderweg, wordt bezorgd, bezorgd), Packstation-ophalingen met het Packstation-adres, retouren, verzonden pakketten en Deutsche Post-brieven. Met de widgets **DHL-pakketten (Duitsland)** en **Deutsche Post Poststukken**.',
        'en': 'Your DHL parcels in Germany with DHL\'s progress ladder (announced, in transit, out for delivery, delivered), Packstation pickups with the Packstation address, returns, sent parcels and Deutsche Post letters. With the **DHL Parcels (Germany)** and **Deutsche Post Mail** widgets.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **Post & DHL Duitsland**.',
               '**Post & DHL-app-login (werkt vanuit elk land):** tik op **DHL-login openen**, log in en kopieer na de doorverwijzing het volledige adres uit de adresbalk terug naar het scherm (**Adres na het inloggen**). Tik op **Koppelen**.',
               '**DHL.de-login (alleen vanuit Duitsland):** tik op **DHL.de-login openen**, log in en kopieer het `dhllogin://…`-adres (ontwikkelaarstools van de browser → Netwerk). Hiermee kun je ook extra trackingnummers volgen.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **Post & DHL Germany**.',
               '**Post & DHL app login (works from any country):** tap **Open DHL login**, sign in and after the redirect copy the complete address from the address bar back into the screen (**Address after signing in**). Tap **Connect**.',
               '**DHL.de login (only from Germany):** tap **Open DHL.de login**, sign in and copy the `dhllogin://…` address (browser developer tools → Network). This also lets you follow extra tracking numbers.']},
    limits={
        'nl': ['De DHL.de-login werkt alleen vanaf een Duitse internetverbinding; extra trackingnummers hebben die login nodig.',
               'Een inloglink werkt maar één keer; open de login opnieuw als het koppelen mislukt.'],
        'en': ['The DHL.de login only works from a German internet connection; extra tracking numbers need that login.',
               'A sign-in link only works once; open the login again if connecting fails.']},
)

M['ampere'] = dict(
    name={'nl': 'Ampère', 'en': 'Ampère'},
    flags='🇳🇱',
    methods=['Tracking', 'Account'],
    countries={'nl': 'Nederland', 'en': 'Netherlands'},
    intro={
        'nl': 'Ampère bezorgt pakketten voor bol.com. MyParcel leest de status van Ampère\'s eigen pakketpagina via de link in de bol.com-mail, met bezorgvenster en statusgeschiedenis. Met de helper vindt MyParcel Ampère-pakketten automatisch in je bol.com-account.',
        'en': 'Ampère delivers parcels for bol.com. MyParcel reads the status from Ampère\'s own parcel page through the link in the bol.com e-mail, with delivery window and status history. With the helper, MyParcel finds Ampère parcels in your bol.com account automatically.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **Ampère**.',
               'Gebruik de **Bol.com Homey Login Helper**, log één keer in via login.bol.com en plak de gegenereerde **bol.com-sessiecode**. MyParcel controleert daarna automatisch je bol.com-bestellingen op Ampère-bezorgingen.',
               '**Of handmatig:** plak de **trackinglink uit de bol.com-mail** (bijv. `https://link.bol.com/t/…`).',
               'Tik op **Koppelen**.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **Ampère**.',
               'Use the **Bol.com Homey Login Helper**, sign in once at login.bol.com and paste the generated **bol.com session code**. MyParcel then checks your bol.com orders automatically for Ampère deliveries.',
               '**Or manually:** paste the **tracking link from the bol.com e-mail** (e.g. `https://link.bol.com/t/…`).',
               'Tap **Connect**.']},
    limits={
        'nl': ['Alleen Ampère-zendingen worden getoond; PostNL-3S-zendingen en niet-bevestigde kandidaten worden gefilterd.',
               'Verloopt de Ampère-sessie, dan start MyParcel stil een nieuwe sessie.'],
        'en': ['Only Ampère shipments are shown; PostNL 3S shipments and unverified candidates are filtered out.',
               'When Ampère\'s session expires, MyParcel silently starts a new one.']},
)

M['trunkrs'] = dict(
    name={'nl': 'Trunkrs', 'en': 'Trunkrs'},
    flags='🇳🇱',
    methods=['Tracking'],
    countries={'nl': 'Nederland', 'en': 'Netherlands'},
    intro={
        'nl': 'Trunkrs bezorgt same-day en in de avond. Volg Trunkrs-pakketten met hun nummer en de postcode van het bezorgadres – geen account nodig. Met het bezorgvenster van Trunkrs, onderweg, bezorgd, geschiedenis en gebeurtenisteksten in je eigen taal.',
        'en': 'Trunkrs delivers same-day and in the evening. Follow Trunkrs parcels with their number and the delivery postal code – no account needed. With the Trunkrs delivery window, out for delivery, delivered, history and event texts in your own language.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **Trunkrs**.',
               'Vul de **postcode van het bezorgadres** in (verplicht, bijv. `1234AB`).',
               'Vul optioneel de **Trunkrs-nummers** in, één per regel. Voor een pakket naar een ander adres zet je de postcode achter het nummer: `419719666 1234AB`.',
               'Tik op **Trunkrs toevoegen**. Nummers toevoegen kan later via de apparaatinstellingen of met een Flow.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **Trunkrs**.',
               'Enter the **delivery postcode** (required, e.g. `1234AB`).',
               'Optionally enter the **Trunkrs numbers**, one per line. For a parcel delivered to another address, add its postcode after the number: `419719666 1234AB`.',
               'Tap **Add Trunkrs**. You can add numbers later in the device settings or with a Flow.']},
    limits={
        'nl': ['Trunkrs toont een pakket alleen samen met de Nederlandse postcode van het bezorgadres.',
               'Geen account-koppeling: alleen nummers die je toevoegt worden gevolgd.'],
        'en': ['Trunkrs only shows a parcel together with the Dutch delivery postcode.',
               'No account link: only numbers you add are followed.']},
)

M['dynalogic'] = dict(
    name={'nl': 'Dynalogic', 'en': 'Dynalogic'},
    flags='🇳🇱 🇧🇪',
    methods=['Tracking'],
    countries={'nl': 'Nederland en België', 'en': 'Netherlands and Belgium'},
    intro={
        'nl': 'Dynalogic bezorgt grote en waardevolle zendingen (bijv. elektronica). Volg bezorgingen met het ordernummer en de postcode – geen account nodig. Statussen komen uit Dynalogic\'s eigen scenario-/stap-/resultaatcodes (bezorgd, wordt bezorgd, probleem, retour), met afzender, ontvanger en geschiedenis.',
        'en': 'Dynalogic delivers large and valuable shipments (e.g. electronics). Follow deliveries with the order number and postcode – no account needed. Statuses come from Dynalogic\'s own scenario/step/result codes (delivered, out for delivery, problem, returning), with sender, receiver and history.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **Dynalogic**.',
               'Kies het **land** (Nederland of België) en vul de **postcode van het bezorgadres** in (verplicht; NL `1234AB`, BE `1000`).',
               'Vul optioneel de **ordernummers** in, één per regel; zet een afwijkende postcode achter het nummer.',
               'Tik op **Dynalogic toevoegen**. Ordernummers toevoegen kan later via de apparaatinstellingen of met een Flow.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **Dynalogic**.',
               'Choose the **country** (Netherlands or Belgium) and enter the **delivery postcode** (required; NL `1234AB`, BE `1000`).',
               'Optionally enter the **order numbers**, one per line; add a different postcode after the number.',
               'Tap **Add Dynalogic**. You can add order numbers later in the device settings or with a Flow.']},
    limits={
        'nl': ['**Geen bezorgvenster:** Dynalogic levert (nog) geen gestructureerd bezorgvenster. De capability *Bezorgvenster* blijft leeg en er is geen kaart *bezorgtijd gewijzigd*.',
               'Dynalogic toont een bezorging alleen samen met de postcode van het bezorgadres.'],
        'en': ['**No delivery window:** Dynalogic does not provide a structured delivery window (yet). The *Delivery window* capability stays empty and there is no *delivery time changed* card.',
               'Dynalogic only shows a delivery together with the delivery postcode.']},
)

M['dragonfly'] = dict(
    name={'nl': 'Dragonfly / Intelcom', 'en': 'Dragonfly / Intelcom'},
    flags='🇳🇱 🇦🇺 🇨🇦',
    methods=['Tracking'],
    countries={'nl': 'Nederland en Australië (Dragonfly), Canada (Intelcom)', 'en': 'Netherlands and Australia (Dragonfly), Canada (Intelcom)'},
    intro={
        'nl': 'Volg pakketten van Dragonfly (Nederland, Australië) en Intelcom (Canada) met hun trackingnummer – geen account nodig. Met bezorgvenster (ETA), onderweg, bezorgd, geschiedenis in je eigen taal (als Dragonfly die heeft) en pakketten die je zelf verstuurt. Voor Canada heet het apparaat Intelcom.',
        'en': 'Follow Dragonfly (Netherlands, Australia) and Intelcom (Canada) parcels with their tracking number – no account needed. With delivery window (ETA), out for delivery, delivered, history in your language (when Dragonfly has it) and parcels you send yourself. For Canada the device is named Intelcom.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **Dragonfly / Intelcom**.',
               'Kies het **land**: Nederland (Dragonfly), Australië (Dragonfly) of Canada (Intelcom).',
               'Vul optioneel **trackingnummers** in, één per regel (bijv. `INTLCMB2C000999999`). Zet ` out` achter een code voor een pakket dat je zelf verstuurt.',
               'Tik op **Apparaat toevoegen**. Codes toevoegen kan later via de apparaatinstellingen of met een Flow.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **Dragonfly / Intelcom**.',
               'Choose the **country**: Netherlands (Dragonfly), Australia (Dragonfly) or Canada (Intelcom).',
               'Optionally enter **tracking numbers**, one per line (e.g. `INTLCMB2C000999999`). Add ` out` after a code for a parcel you send yourself.',
               'Tap **Add device**. You can add codes later in the device settings or with a Flow.']},
    limits={
        'nl': ['Geen account-koppeling: alleen nummers die je toevoegt (en ophaaltaken voor verzonden pakketten) worden gevolgd.'],
        'en': ['No account link: only numbers you add (and pickup tasks for sent parcels) are followed.']},
)

M['mondial-relay'] = dict(
    name={'nl': 'Mondial Relay', 'en': 'Mondial Relay'},
    flags='🇫🇷 🇧🇪 🇳🇱 🇪🇸 🇵🇹',
    methods=['Account'],
    countries={'nl': 'Frankrijk, België, Nederland, Spanje en Portugal', 'en': 'France, Belgium, Netherlands, Spain and Portugal'},
    intro={
        'nl': 'Log in met je Mondial Relay- / InPost-account om je inkomende en verzonden pakketten automatisch te zien, met de laatste stap van elk pakket. Je wachtwoord komt nooit bij Homey.',
        'en': 'Sign in with your Mondial Relay / InPost account to see your incoming and sent parcels automatically, with the latest step of every parcel. Your password never reaches Homey.'},
    connect={
        'nl': ['Zorg dat je account minstens één keer is ingelogd op de website of in de app van Mondial Relay.',
               'Open Homey → **Apparaten** → **+** → **MyParcel** → **Mondial Relay** en kies het **land van het account**.',
               'Tik op **Mondial Relay-login openen** en log in met je account.',
               'Na het inloggen komt de browser uit op een adres dat begint met `https://account.inpost-group.com/callback?code=…` en niet laadt. Dat hoort zo: kopieer het volledige adres uit de adresbalk, plak het in **Adres na het inloggen** en tik op **Account koppelen**.'],
        'en': ['Make sure your account has signed in at least once on the Mondial Relay website or app.',
               'Open Homey → **Devices** → **+** → **MyParcel** → **Mondial Relay** and choose the **account country**.',
               'Tap **Open Mondial Relay sign-in** and sign in with your account.',
               'After signing in, the browser ends on an address starting with `https://account.inpost-group.com/callback?code=…` that does not load. That is expected: copy the full address from the address bar, paste it into **Address after signing in** and tap **Connect account**.']},
    limits={
        'nl': ['**Nog geen betrouwbare status:** Mondial Relay deelt (nog) geen betrouwbare pakketstatus. Alleen de kaarten **nieuw pakket** en **trackinggebeurtenis** gaan af; de statusgebaseerde kaarten (status gewijzigd, onderweg voor bezorging, bezorgd, probleem/retour en de kaarten voor verzonden pakketten) volgen zodra de status bekend is.',
               'Elke inloglink werkt maar één keer. Mislukt het koppelen, open dan de inlogpagina opnieuw voor een nieuwe link.'],
        'en': ['**No reliable status yet:** Mondial Relay does not share a reliable parcel status (yet). Only the **new parcel** and **tracking event** cards fire; the status-based cards (status changed, out for delivery, delivered, problem/returning and the sent-parcel cards) will follow once the status is known.',
               'Each sign-in link only works once. If connecting fails, open the sign-in page again for a new link.']},
)

M['amazon'] = dict(
    name={'nl': 'Amazon', 'en': 'Amazon'},
    flags='🇳🇱 🇧🇪 🇩🇪 🇫🇷 🇬🇧 🇮🇪 🇪🇸 🇮🇹 🇸🇪 🇵🇱 🇺🇸 🇨🇦 🇲🇽 🇧🇷 🇦🇺 🇯🇵 🇮🇳',
    methods=['Account'],
    experimental=True,
    countries={'nl': '17 Amazon-winkels: Nederland, België, Duitsland, Frankrijk, Verenigd Koninkrijk, Ierland, Spanje, Italië, Zweden, Polen, Verenigde Staten, Canada, Mexico, Brazilië, Australië, Japan en India',
               'en': '17 Amazon stores: Netherlands, Belgium, Germany, France, United Kingdom, Ireland, Spain, Italy, Sweden, Poland, United States, Canada, Mexico, Brazil, Australia, Japan and India'},
    intro={
        'nl': '**Experimenteel.** Log in op de eigen pagina van Amazon om de zendingen van je bestellingen te zien, met artikel, bezorgende vervoerder, verwachte bezorgdatum, onderweg, klaar om op te halen en bezorgd.',
        'en': '**Experimental.** Sign in on Amazon\'s own page to see the shipments of your orders, with item, delivery carrier, expected delivery date, out for delivery, ready for pickup and delivered.'},
    connect={
        'nl': ['Open Homey → **Apparaten** → **+** → **MyParcel** → **Amazon** en kies je **Amazon-winkel**.',
               'Tik op **Amazon-login openen** en doorloop elke stap die Amazon vraagt (wachtwoord, verificatiecode, puzzel of passkey). Wachtwoord, code en puzzel blijven bij Amazon.',
               'Je komt uit op een pagina die leeg kan lijken of een fout toont – dat hoort zo. Kopieer het volledige adres uit de adresbalk, plak het in **Adres na het inloggen** en tik op **Account koppelen**.',
               'Homey bewaart alleen een inlogtoken. Toegang intrekken kan altijd via **Inhoud en apparaten beheren** bij Amazon.'],
        'en': ['Open Homey → **Devices** → **+** → **MyParcel** → **Amazon** and choose your **Amazon store**.',
               'Tap **Open Amazon sign-in** and complete every step Amazon asks for (password, verification code, puzzle or passkey). Password, code and puzzle stay at Amazon.',
               'You end on a page that may look blank or show an error – that is expected. Copy the full address from the address bar, paste it into **Address after signing in** and tap **Connect account**.',
               'Homey only keeps a sign-in token. You can remove access at any time under **Manage Your Content and Devices** on Amazon.']},
    limits={
        'nl': ['**Experimenteel:** Amazon kan zijn pagina\'s op elk moment wijzigen; gegevens kunnen dan tijdelijk ontbreken.',
               '**Maximaal 10 zendingen per pollronde** worden gelezen; bezorgde zendingen worden maar één keer gelezen.',
               'Elke inloglink werkt maar één keer. Andere winkel gekozen of vraagt Amazon opnieuw om in te loggen? Gebruik **Herstellen**.',
               'Geen bezorgvenster: Amazon geeft alleen een verwachte bezorgdatum. De kaart *verwachte bezorgdatum gewijzigd* gaat af als die datum verandert.'],
        'en': ['**Experimental:** Amazon can change its pages at any time; data may then be missing temporarily.',
               '**At most 10 shipments are read per poll**; delivered shipments are only read once.',
               'Each sign-in link only works once. Changed the store, or does Amazon ask you to sign in again? Use **Repair**.',
               'No delivery window: Amazon only gives an expected delivery date. The *expected delivery date changed* card fires when that date changes.']},
)
