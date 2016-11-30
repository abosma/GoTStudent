from __future__ import unicode_literals
from __future__ import print_function
import inout
import actions

# Kies één van deze dal's (Data Access Layer)
import in_memory_dal as dal
# import sql_dal as dal


# region Initialization
# De volgende functies zijn van belang bij het opzetten van het spel.

def reset_game():
    if dal.reset_spel():
        kies_hoofdrol_karakter()


def kies_hoofdrol_karakter():
    inout.ask("Met welke held ga jij deze queeste voltooien? ")
    mogelijke_hoofdspelers = dal.geef_mogelijke_hoofdspelers()
    gekozen_hoofdspeler = inout.choose(mogelijke_hoofdspelers)
    dal.zet_hoofdspeler(gekozen_hoofdspeler)


# endregion

# region Round Information

def toon_wereld_informatie():
    toon_huidig_land()
    toon_buur_landen()
    toon_gezelschap()
    toon_vreemden()
    print("")  # lege regel


def toon_huidig_land():
    huidig_land = dal.geef_huidig_land()
    print("Je bent momenteel in " + huidig_land)


def toon_buur_landen():
    buur_landen = dal.geef_buurlanden()
    print("De volgende landen zijn om je heen: ")
    inout.show_list(buur_landen)


def toon_gezelschap():
    gezelschap = dal.geef_gezelschap(False)

    if len(gezelschap) > 0:
        print("Je reist met het volgende gezelschap: ")
        inout.show_list(gezelschap)
    else:
        print("Je reist alleen.")


def toon_vreemden():
    vreemden = dal.geef_vreemden(False)

    if len(vreemden) > 0:
        print("De volgende vreemden kom je tegen: ")
        inout.show_list(vreemden)
    else:
        print('Er is niemand aanwezig.')


# endregion

# region Phase


def bepaal_ronde_actie(is_ai):

    # Er kan alleen een actie worden gedaan als er vreemden zijn op de huidige locatie
    vreemden = dal.geef_vreemden(is_ai)
    if len(vreemden) == 0:
        print("Er zijn geen vreemden wiens lot we kunnen tarten :(")
        dal.reset_ronde_speler()
        return ''

    # Maak keuze uit gezelschap of overslaan
    opties = dal.geef_gezelschap(is_ai)
    if len(opties) == 0:    # Kan optreden voor AI
        return ''

    opties.append('De helden zullen deze ronde rusten!')

    if is_ai:
        inout.warn("AI doet een tegenzet!")

    inout.ask("Welke held mag zijn of haar heldendaden vertonen deze ronde? ")
    ronde_speler = inout.choose(opties, is_ai)

    is_ronde_speler_gekozen = ronde_speler != 'De helden zullen deze ronde rusten!'

    if is_ronde_speler_gekozen:
        dal.zet_ronde_speler(ronde_speler)
        rol = dal.geef_rol_van_karakter(ronde_speler)
        actie = dal.geef_actie_voor_rol(rol)
        print(ronde_speler + ' zal zijn of haar kunsten vertonen!')
    else:
        dal.reset_ronde_speler()
        actie = ''

    return actie


# endregion

# region Actions

def speel_paper_rock_scissors():
    gewonnen = actions.speel_paper_rock_scissors()
    return gewonnen


def verplaats():
    actions.verplaats()


def bevecht(is_ai):
    actions.bevecht(is_ai)


def overtuig(is_ai):
    actions.overtuig(is_ai)

# endregion

# region Termination and finalization


def is_game_over():
    gewonnen = heeft_speler_gewonnen()
    verloren = heeft_speler_verloren()
    return gewonnen or verloren


def heeft_speler_gewonnen():
    gezelschap = dal.geef_gezelschap(False)
    heeft_prinses = 'Daenerys Targaryen' in gezelschap
    return heeft_prinses


def heeft_speler_verloren():
    is_hoofdspeler_verbannen = dal.is_hoofdspeler_verbannen()
    return is_hoofdspeler_verbannen


def toon_game_over():
    if heeft_speler_gewonnen():
        print("Bravo! Bis! Opperbaas! Je hebt de prinses geredt en zult eeuwige roem tegemoet gaan!")
    else:
        print(
            "Boeh! Bah! Faalhaas! Je was de strijd niet waardig en zult tot in den eeuwigheid bespot worden in liederen!")

# endregion
