# Flow-voorbeelden

Een paar handige Flows om mee te beginnen. De kaarttitels staan zoals in Homey; de volledige lijst vind je op [Flow-kaarten](flows.md).

## 1. Melding met pakketafbeelding als PostNL eraan komt

* **Wanneer:** *De status van een pakket is gewijzigd* (PostNL)
* **En:** *De huidige pakketstatus is* `Bezorger is onderweg`
* **Dan:** Stuur een push-melding met afbeelding: tekst `[[Afzender pakket]] komt tussen [[Bezorgvenster]]`, afbeelding het token **Afbeelding Mijn Bezorging** van de kaart.

De afbeelding is vastgezet op precies dit pakket en deze status. Gebruik je de afbeelding in een andere Flow (bijv. een tijd-trigger), kies dan het globale token **&lt;apparaatnaam&gt; · Pakketafbeelding**.

## 2. Onderweg voor bezorging (andere vervoerders)

* **Wanneer:** *DPD-pakket onderweg voor bezorging* (of de *onderweg voor bezorging*-kaart van DHL, GLS, Trunkrs, Dynalogic, Dragonfly, Amazon …)
* **Dan:** Stuur een melding `[[Afzender]] komt vandaag, [[Bezorgvenster]]`.

## 3. Ophaalcode bij Vinted Go of InPost

* **Wanneer:** *Vinted Go-pakket klaar om op te halen*
* **Dan:** Stuur een melding `Ophalen bij [[Afhaalpunt]] met code [[Ophaalcode]]`.

## 4. Nieuwe post met scan

* **Wanneer:** *Er is nieuwe post onderweg* (PostNL)
* **Dan:** Stuur een melding met het token **Afbeelding poststuk** van de kaart, of gebruik **&lt;apparaatnaam&gt; · Scan laatste poststuk** in elke andere Flow.

## 5. Trackingnummer automatisch volgen

* **Wanneer:** bijv. een e-mail- of webhook-Flow met het trackingnummer
* **Dan:** *Volg Trunkrs-pakket…* (of *Volg GLS-pakket…*, *Volg DHL-pakket…* …) met het nummer als argument. Ruim later op met *Verwijder bezorgde … pakketten*.

## 6. Niemand thuis?

* **Wanneer:** Iedereen is vertrokken
* **En:** *Er is een … pakket onderweg voor bezorging*
* **Dan:** Stuur een herinnering om de buren te vragen of een afhaalpunt te kiezen.

## Tips voor Advanced Flow

* **Eén trigger-kaart per actieketen.** Tokens bestaan alleen in de Flow die door díe kaart is gestart. Koppel je twee triggers aan hetzelfde actieblok dat een token van één van beide gebruikt, dan meldt Homey *Missing token value* zodra de andere trigger afgaat.
* **Of gebruik globale tokens.** De globale PostNL-tokens (**Pakketafbeelding**, **Scan laatste poststuk**, status, bezorgvenster …) en de MyParcel-bezorgtokens werken in elke Flow, welke kaart de Flow ook startte. Zie [Flow-tokens](tokens.md).
* Kaarten gaan één keer per wijziging af – ook na een herstart. Je hoeft zelf geen dubbele meldingen af te vangen.
