from __future__ import unicode_literals
import sql
import os
import inout

# Leertaak SQL: De publieke API dient hier geimplementeerd te worden, zodat het gebruik maakt van het database-model
# zoals ontworpen in leertaak "Relationele Model".
# Let erop dat de methode-signatures niet gewijzigd mogen worden!
# Onderstaande methoden bevatten nu onzin-implementaties (behalve reset_spel).


DB_FILE = "got.db"
INIT_SCRIPT_FILE = "init_db.sql"

# Voorbeeld van een SQL-query
SQL_GEEF_MOGELIJKE_HOOFDSPELERS = """
select Naam 
from   Karakter
where  Naam = ?
"""


# Voorbeeld van het gebruik van de sql-helper functie sql.execute
def geef_mogelijke_hoofdspelers():
    mogelijke_hoofd_spelers = sql.execute(SQL_GEEF_MOGELIJKE_HOOFDSPELERS, "Piet")
    return mogelijke_hoofd_spelers


def zet_hoofdspeler(gekozen_hoofdspeler):
    pass


def zet_ronde_speler(gekozen_rondespeler):
    pass


def reset_ronde_speler():
    pass


def geef_gezelschap(is_ai, met_rol='%'):
    if is_ai:
        return
    return []


def geef_vreemden(is_ai, met_rol='%'):
    return []


def geef_actie_voor_rol(rol):
    return "Wat kan ik?"


def geef_rol_van_karakter(karakter):
    return "Wie ben ik?"


def voeg_toe_aan_gezelschap(is_ai, karakter):
    pass


def geef_huidig_land():
    return "Waar ben ik?"


def geef_buurlanden():
    return []


def reset_spel():
    """
    Verwijdert en herlaadt de database als de speler opnieuw wil beginnen.
    Deze methode werkt out-of-the-box en hoeft niet aangepast te worden voor de leertaak.
    :returns of de speler het spel wil herinitialiseren

    """
    if os.path.exists(DB_FILE):
        inout.ask("Wil je verder waar je gebleven was?")
        keuze = inout.choose(["Ja", "Nee"])
        if keuze == "Nee":
            os.remove(DB_FILE)
            sql.execute_script(INIT_SCRIPT_FILE)

    return keuze == "Nee"


def verban_karakter(karakter):
    pass


def geef_familie(karakter):
    pass


def geef_vrienden(familie):
    pass


def is_hoofdspeler_verbannen():
    return False


def bepaal_waterweg(buurland):
    pass


def zet_huidige_locatie(land):
    pass


def bepaal_schipper():
    pass


def geef_rondespeler():
    pass
