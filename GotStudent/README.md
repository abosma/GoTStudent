Game engine + game (Game of Thrones)
====================================

Deze repo bevat python-code voor de casus-opdracht voor Modelleren 2016.


Inhoud
------

Bestand          | Omschrijving
---------------- | ------------------------------------------------------------
engine.py        | De game engine
got.py           | De Game of Thrones game voor de engine.
acties.py        | De handelingen die een spel-karakter kan uitvoeren (RPS, bevecht, onderhandel, verplaats). *Deze functionaliteit dient door de studie geimplementeerd te worden in leertaak "Activity Diagrams".
in_memory_dal.py | De InMemory Data-Access-Layer, is vluchtig (volatile)
sql_dal.py       | De SQL Data-Access-Layer (biedt persistentie). *Deze implementatie dient door de studie geimplementeerd te worden in leertaak "SQL".
sql.py           | SQLite-helpers
inout.py         | input/output-helpers
init_db.sql      | Initiele database setup-script (SQLite) voor de Game of Thrones game. *Dit script dient door de studie geimplementeerd te worden in leertaak "Relationele Model".


Dependencies
------------
De code maakt gebruik van enkele dependencies. Als je IDE ondersteuning biedt voor *requirements.txt* dan wordt dit automatisch voor je geregeld. Zo niet, voer dan het volgende commando uit in je console: *pip install -r requirements.txt*

Package  | Omschrijving
-------- | -------------------------------------------------------------------------
future   | Zorgt dat de code zowel Python2 als Python3 compatible is.
termcolor| Maakt het mogelijk kleuren te gebruiken in de console.
colorama | Maakt het mogelijk termcolor werkend te krijgen in de Windows 10 console.


Hoe werkt de engine?
--------------------

Wanneer je *engine.py* runt, wordt *got.py* ingeladen. De engine-cycle is als volgt:

Stap     | Functie
-------- | -------------------------------------------------------------------------
1.	Reset/initaliseer de game | **got.reset_game()**
2.	Herhaal zolang het spel niet voorbij is | **got.is_game_over()**
    3.1 Toon wereld-informatie | **got.toon_wereld_informatie**
    3.2 Voor 'Fase' 1 (speler) en 2 (AI) |
        3.2.1 Bepaald 'Ronde Actie' |	**got.bepaal_ronde_actie**
        3.2.2 Als 'Actie' niet leeg is, voor actie uit | **got.[actie_naam]** (doorgeefluik naar **acties.[actie_naam]**)
    3.3 Verplaats speler |	**got.verplaats()** (doorgeefluik naar **acties.verplaats**)
4.	Toon afsluitende tekst | **got.toon_game_over()**

De game-logica van Game of Thrones wordt dus compleet bepaald door de invulling van de desbestreffende functies in **got.py**.


Waarom is van de werking van de engine geen BPMN-diagram aangeleverd?
---------------------------------------------------------------------
De student dient dit BPMN-model te ontwerpen voor de leertaak "BPMN".


Wat is het nut van de DAL (Data-Access-Layer)
---------------------------------------------
De DAL dient ter abstractie van de Data-toegang. Deze abstractie is technologie-onafhankelijk. De DAL biedt een publieke API
die geimplementeerd dient te worden door specifieke DALs. Één complete uitwerking van de DAL is **in_memory_dal.py**. Deze DAL
gebruikt als technologie de in-memory datastructuren van Python (Lists/Tuples/Sets/Globale variabelen). Een tweede DAL
wordt geimplementeerd door **sql_dal.py**, die deels is meegeleverd. Deze DAL dient als technologie een relationele (SQL) database
te gebruiken en zal worden geimplementeerd door de student in leertaak "SQL".
Merk op dat de DAL zowel in *got.py* als *actions.py* geimporteert (of gewisselt) dient te worden. Zie de import-statements
van deze bestanden.


Wat is het nut van **actions.py**
---------------------------------
De implementatie van de daadwerkelijke acties die een speler kan uitvoeren zijn worden geimplementeerd in **actions.py**.
Het is de bedoeling dat de programmeur gebruik maakt van de DAL om de game-state te bevragen en te manipuleren.
Deze functionaliteit wordt geimplementeerd door de student in leertaak "Activity Diagram".


Wat dient *niet* verder aangepast te worden en mag als black-box worden beschouwd?
----------------------------------------------------------------------------------
- *engine.py*
- *got.py*
- *in_memory_dal.py*
- *sql.py*
- *inout.py*

Om gevoel te krijgen voor de engine en het gebruik van de hulp-functies, wordt aangeraden om
*got.py* te bestuderen.


Wat dient *wel* verder aangepast te worden voor een leertaak?
-------------------------------------------------------------
- *acties.py* voor leertaak "Activity Diagrams"
- *init_db.sql* voor leertaak "Relationele Model"
- *sql_dal.py* voor leertaak "SQL" (hiervoor dient eerst leertaak "Relationele Model" te zijn afgerond).


Waartoe dient de *is_ai* parameter in diverse functies?
-------------------------------------------------------
Deze parameter geeft aan of fase 1 (menselijke speler) of fase 2 (AI speler) gespeeld wordt. De gevorderde gebruiker
is vrij deze functionaliteit te implementeren voor de AI, maar bedenk dat het geen makkelijke opgave is (en niet verplicht).
Als je besluit de AI niet te implementeren, dan dienen *actie.bevecht* en *actie.overtuig* direct retourneren wanneer de
AI aan de beurt is (dit gedrag is al geimplementeerd in de gedeeltelijke uitwerking).

Welke hulp-functies kan ik gebruiken?
-------------------------------------

**sql.py** bevat een hulpfunctie voor het uitvoeren van SQL-queries, te weten execute. De eerste parameter is de SQL-statement (een String).
De SQL-statement kan placeholders bevatten (in de vorm ?'s (vraagtekens)) die in-volgorde ingevuldt worden door de overige paramters.
De wijze van SQL-statements heten "prepared statements" en dienen ter beveiliging van de database. Zie de deels ingevulde *sql_dal.py* voor
een voorbeeld of lees erover op https://docs.python.org/2/library/sqlite3.html .
**inout.py** bevat hulp-functies voor invoer van de gebruiker en uitvoer naar het scherm.

Functie  | Omschrijving
-------- | --------------------------------------------------------------------------------------------------------------
inout.show_list(lst)          | print ieder element in de lijst *lst* op een aparte regel, voorafgaand met een "-"-teken.
inout.ask(text)               | print de string *question* in het blauw.
inout.warn(text)              | print de string *text* in het geel.
inout.choose(lst, is_ai)	  | geeft de gebruiker de optie een element te kiezen uit de lijst *lst*. De huidige selectie is in het rood. Retourneert de keuze (string). Waneer *is_ai* waar is, kiest de AI random een element uit de lijst.
sql.execute(query, *params)   | Voert de SQL-query *query* uit de database **got.db**, met optionele parameters *params* en retourneert optioneel de eerste kolom als een lijst.


Recente wijzigingen
-------------------

Versie  | Wijziging (major)
------- | -------------------------------------------------------------------------
v2.0    | - DAL-abstractie
        | - AI mechanisme gestreamlined
        | - *actions.py* extern geplaatst
