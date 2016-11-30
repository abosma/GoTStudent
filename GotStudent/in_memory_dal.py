from __future__ import unicode_literals

# Leertaak "Relationeel Model": Creeer een database-schema voor alle data-structuren in deze file.

# region Statische data - verandert niet gedurende het spelverloop

GRENZEN = {
    "The North": {
        "The Riverlands": False,
        "The Iron Islands": True,
        "The Vale": True
    },
    "The Riverlands": {
        "The North": False,
        "The Iron Islands": True,
        "The Westernlands": False,
        "The Reach": False,
        "King's Landing": False,
        "The Vale": False
    },
    "The Iron Islands": {
        "The North": True,
        "The Riverlands": True,
        "The Westernlands": True
    },
    "The Vale": {
        "The North": True,
        "The Riverlands": False,
        "King's Landing": False
    },
    "The Westernlands": {
        "The Riverlands": False,
        "The Iron Islands": True,
        "The Reach": False
    },
    "The Reach": {
        "The Westernlands": False,
        "Dorne": False,
        "The Stormlands": False,
        "King's Landing": False,
        "The Riverlands": False
    },
    "King's Landing": {
        "The Vale": False,
        "The Riverlands": False,
        "The Reach": False,
        "The Stormlands": False,
        "Dragonstone": True
    },
    "The Stormlands": {
        "King's Landing": False,
        "The Reach": False,
        "Dorne": False
    },
    "Dorne": {
        "The Reach": False,
        "The Stormlands": False
    },
    "Dragonstone": {
        "King's Landing": True
    }
}

KARAKTERS = {
    "Daenerys Targaryen": {
        "Familie": "Targaryen of King's Landing",
        "Rol": "Prinses"
    },
    "Jon Snow": {
        "Familie": "Stark of Winterfell",
        "Rol": "Krijger"
    },
    "Sansa Stark": {
        "Familie": "Stark of Winterfell",
        "Rol": "Diplomaat"
    },
    "Arya Stark": {
        "Familie": "Stark of Winterfell",
        "Rol": "Krijger"
    },
    "Tyrion Lannister": {
        "Familie": "Lannister of Casterly Rock",
        "Rol": "Diplomaat"
    },
    "Joffrey Baratheon": {
        "Familie": "Baratheon of Storm's End",
        "Rol": "Krijger"
    },
    "Theon Greyjoy": {
        "Familie": "Greyjoy of Pyke",
        "Rol": "Krijger"
    },
    "Cersei Lannister": {
        "Familie": "Lannister of Casterly Rock",
        "Rol": "Diplomaat"
    },
    "Ramsay Bolton": {
        "Familie": "Bolton",
        "Rol": "Krijger"
    },
    "Margaery Tyrell": {
        "Familie": "Tyrell of Highgarden",
        "Rol": "Diplomaat"
    },
    "Stannis Baratheon": {
        "Familie": "Baratheon of Storm's End",
        "Rol": "Krijger"
    },
    "Eddard Stark": {
        "Familie": "Stark of Winterfell",
        "Rol": "Krijger"
    },
    "Jaime Lannister": {
        "Familie": "Lannister of Casterly Rock",
        "Rol": "Krijger"
    },
    "Robb Stark": {
        "Familie": "Stark of Winterfell",
        "Rol": "Krijger"
    },
    "Petyr Baelish": {
        "Familie": "Stark of Winterfell",
        "Rol": "Diplomaat"
    },
    "Mellisandre": {
        "Familie": "Baratheon of Storm's End",
        "Rol": "Diplomaat"
    },
    "Sandor Clegane": {
        "Familie": "Lannister of Casterly Rock",
        "Rol": "Krijger"
    },
    "Jorah Mormont": {
        "Familie": "Targaryen of King's Landing",
        "Rol": "Krijger"
    },
    "Daario Naharis": {
        "Familie": "Targaryen of King's Landing",
        "Rol": "Krijger"
    },
    "Catelyn Stark": {
        "Familie": "Tully of Riverrun",
        "Rol": "Diplomaat"
    },
    "Robert Baratheon": {
        "Familie": "Baratheon of Storm's End",
        "Rol": "Krijger"
    },
    "Brianne of Tarth": {
        "Familie": "Stark of Winterfell",
        "Rol": "Krijger"
    },
    "Varys": {
        "Familie": "Lannister of Casterly Rock",
        "Rol": "Diplomaat"
    },
    "Davos Seaworth": {
        "Familie": "Baratheon of Storm's End",
        "Rol": "Schipper"
    }
}

VRIENDSCHAPPEN = {
    "Lannister of Casterly Rock": {
        "Lannister of Casterly Rock",
        "Tyrell of Highgarden",
        "Baratheon of Storm's End",
        "Bolton",
        "Arryn of the Eyrie"
    },
    "Tyrell of Highgarden": {
        "Tyrell of Highgarden",
        "Lannister of Casterly Rock",
        "Baratheon of Storm's End",
        "Bolton",
        "Arryn of the Eyrie"
    },
    "Baratheon of Storm's End": {
        "Baratheon of Storm's End",
        "Tyrell of Highgarden",
        "Lannister of Casterly Rock",
        "Bolton",
        "Arryn of the Eyrie"
    },
    "Bolton": {
        "Bolton",
        "Tyrell of Highgarden",
        "Baratheon of Storm's End",
        "Lannister of Casterly Rock",
        "Arryn of the Eyrie"},
    "Arryn of the Eyrie": {
        "Tyrell of Highgarden",
        "Arryn of the Eyrie",
        "Baratheon of Storm's End",
        "Bolton",
        "Lannister of Casterly Rock"
    },
    "Targaryen of King's Landing": {
        "Targaryen of King's Landing",
        "Stark of Winterfell",
        "Greyjoy of Pyke",
        "Tully of Riverrun",
        "Martell of Sunspear"
    },
    "Stark of Winterfell": {
        "Stark of Winterfell",
        "Targaryen of King's Landing",
        "Greyjoy of Pyke",
        "Tully of Riverrun",
        "Martell of Sunspear"
    },
    "Greyjoy of Pyke": {
        "Greyjoy of Pyke",
        "Stark of Winterfell",
        "Targaryen of King's Landing",
        "Tully of Riverrun",
        "Martell of Sunspear"
    },
    "Tully of Riverrun": {
        "Tully of Riverrun",
        "Stark of Winterfell",
        "Greyjoy of Pyke",
        "Targaryen of King's Landing",
        "Martell of Sunspear"
    },
    "Martell of Sunspear": {
        "Martell of Sunspear",
        "Stark of Winterfell",
        "Greyjoy of Pyke",
        "Tully of Riverrun",
        "Targaryen of King's Landing"
    }
}

INITIELE_LOCATIES = {
    "Daenerys Targaryen": "Dragonstone",
    "Jon Snow": "The North",
    "Sansa Stark": "The North",
    "Arya Stark": "The Vale",
    "Tyrion Lannister": "The Westernlands",
    "Joffrey Baratheon": "King's Landing",
    "Theon Greyjoy": "The Iron Islands",
    "Cersei Lannister": "King's Landing",
    "Ramsay Bolton": "The Riverlands",
    "Margaery Tyrell": "The Reach",
    "Stannis Baratheon": "The Reach",
    "Eddard Stark": "King's Landing",
    "Jaime Lannister": "The Westernlands",
    "Robb Stark": "The Vale",
    "Petyr Baelish": "Dorne",
    "Mellisandre": "The Reach",
    "Sandor Clegane": "The Riverlands",
    "Jorah Mormont": "The Westernlands",
    "Daario Naharis": "Dorne",
    "Catelyn Stark": "The Vale",
    "Robert Baratheon": "The Stormlands",
    "Brianne of Tarth": "The North",
    "Varys": "The Stormlands",
    "Davos Seaworth": "Dorne"
}

MOGELIJKE_HOOFDSPELERS = {"Jon Snow", "Tyrion Lannister"}

ROLLEN = {"Krijger": "bevecht", "Schipper": "", "Prinses": "", "Diplomaat": "overtuig"}

# endregion

# region Dynamische data - verandert wel gedurende het spelverloop

HOOFDSPELER = ""
RONDESPELER = ""
GEZELSCHAP = set()
HUIDIGE_LOCATIES = {}


# endregion

# Leertaak SQL: De publieke API dient herschreven te worden, zodat het gebruik maakt van het database-model
# zoals beschreven in leertaak "Relationele Model". Implementeer de nieuwe publieke API in sql_dal.py .
# Let erop dat je confimeert aan de API zoals hier gegeven!

# region Publieke API

def geef_mogelijke_hoofdspelers():
    return sorted(list(MOGELIJKE_HOOFDSPELERS))


def zet_hoofdspeler(gekozen_hoofdspeler):
    global HOOFDSPELER
    HOOFDSPELER = gekozen_hoofdspeler
    voeg_toe_aan_gezelschap(False, gekozen_hoofdspeler)


def zet_ronde_speler(gekozen_rondespeler):
    global RONDESPELER
    RONDESPELER = gekozen_rondespeler


def reset_ronde_speler():
    global RONDESPELER
    RONDESPELER = ""


def geef_gezelschap(is_ai, met_rol=""):
    aanwezigen = set()

    # Voeg alle karakters uit huidige land toe (eventueel met rol)
    for karakter, eigenschappen in KARAKTERS.items():
        if HUIDIGE_LOCATIES[karakter] == geef_huidig_land() and (met_rol == "" or eigenschappen["Rol"] == met_rol):
            aanwezigen.add(karakter)

    if is_ai:       # als AI dit vraagt, haal iedereen uit het gezelschap van de hoofdspeler weg
        gezelschap = aanwezigen.difference(GEZELSCHAP)
    else:           # anders houden we alleen iedereen die ook in het gezelschap zit
        gezelschap = aanwezigen.intersection(GEZELSCHAP)

    return sorted(list(gezelschap))


def geef_vreemden(is_ai, met_rol=""):
    return geef_gezelschap(not is_ai, met_rol)


def geef_actie_voor_rol(rol):
    actie = ROLLEN[rol]
    return actie


def geef_rol_van_karakter(karakter):
    return KARAKTERS[karakter]["Rol"]


def voeg_toe_aan_gezelschap(is_ai, karakter):
    if is_ai:
        GEZELSCHAP.remove(karakter)
    else:
        GEZELSCHAP.add(karakter)


def geef_huidig_land():
    huidige_locatie = HUIDIGE_LOCATIES[HOOFDSPELER]
    return huidige_locatie


def geef_buurlanden():
    huidige_land = geef_huidig_land()
    buurlanden = GRENZEN[huidige_land].keys()
    return sorted(list(buurlanden))


def verban_karakter(karakter):
    if karakter in GEZELSCHAP:
        GEZELSCHAP.remove(karakter)
    HUIDIGE_LOCATIES[karakter] = ""


def geef_familie(karakter):
    return KARAKTERS[karakter]["Familie"]


def geef_vrienden(familie):
    return VRIENDSCHAPPEN[familie]


def is_hoofdspeler_verbannen():
    return HOOFDSPELER not in GEZELSCHAP


def bepaal_waterweg(buurland):
    heeft_waterweg = GRENZEN[geef_huidig_land()][buurland]
    return heeft_waterweg


def zet_huidige_locatie(land):
    for karakter in GEZELSCHAP:
        HUIDIGE_LOCATIES[karakter] = land


def bepaal_schipper():
    schippers = set()
    for karakter, eigenschappen in KARAKTERS.items():
        if eigenschappen["Rol"] == "Schipper":
            schippers.add(karakter)
    return not schippers.isdisjoint(GEZELSCHAP)


def geef_rondespeler():
    return RONDESPELER


def reset_spel():
    global HOOFDSPELER
    global RONDESPELER
    global GEZELSCHAP
    global HUIDIGE_LOCATIES
    HOOFDSPELER = ""
    RONDESPELER = ""
    GEZELSCHAP = set()
    HUIDIGE_LOCATIES = INITIELE_LOCATIES.copy()
    return True

# endregion
