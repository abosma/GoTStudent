from __future__ import unicode_literals
from __future__ import print_function
import inout


# Kies één van deze DAL's (Data Access Layer)
import in_memory_dal as dal
# import sql_dal as dal

# Deze file bevat de definities voor het gedrag dat geimplementeerd dient te worden voor de leertaak "Activity Diagrams"


def speel_paper_rock_scissors():
    """"
    Speelt Rock, Paper, Scissors tegen de computer, totdat er iemand gewonnen heeft.
    Behoeft geen functionaliteit van de DAL.
    Retourneert of de menselijke speler gewonnen heeft (een boolean).
    Voor het gemak kan gebruik gemaakt worden van de volgende hulp-functies:
      - inout.ask     (om tekst naar het scherm te printen)
      - inout.choose  (eventueel met als argument True om de computer een random keuze te laten maken)
    """

    while True:
        opties = ["Steen", "Papier", "Schaar"]
        hoofdspeler_keuze = inout.choose(opties)
        AI_Keuze = inout.choose(opties, is_ai = True)
        inout.ask("Jij hebt " + hoofdspeler_keuze + " gekozen.\nDe tegenstander heeft " + AI_Keuze + " gekozen.")
        if(hoofdspeler_keuze == AI_Keuze):
            pass
        elif(hoofdspeler_keuze == "Steen" and AI_Keuze == "Papier"):
            inout.ask("Jij hebt verloren!!!")
            return False
            break
        elif(hoofdspeler_keuze == "Steen" and AI_Keuze == "Schaar"):
            inout.ask("Jij hebt gewonnen!!!")
            return True
            break
        elif(hoofdspeler_keuze == "Papier" and AI_Keuze == "Steen"):
            inout.ask("Jij hebt gewonnen!!!")
            return True
            break
        elif(hoofdspeler_keuze == "Papier" and AI_Keuze == "Schaar"):
            inout.ask("Jij hebt verloren!!!")
            return False
            break
        elif(hoofdspeler_keuze == "Schaar" and AI_Keuze == "Steen"):
            inout.ask("Jij hebt verloren!!!")
            return False
            break
        elif(hoofdspeler_keuze == "Schaar" and AI_Keuze == "Papier"):
            inout.ask("Jij hebt gewonnen!!!")
            return True
            break     


def verplaats():
    """"
    Verplaatst het gezelschap naar een naburig land (mits mogelijk).
    Zal intensief gebruik maken van de DAL.
    Voor het gemak kan gebruik gemaakt worden van (o.a.) de volgende hulp-functies:
      - inout.ask     (om tekst naar het scherm te printen)
      - inout.choose  (om te kiezen uit de mogelijke landen)
      - dal.*         (om buren te checken, waterwegen te controleren, enz.)
    """

    return


def bevecht(is_ai):
    """"
    Vecht als Krijger met de vreemdelingen (of het gezelschap i.g.v. AI).
    Zal intensief gebruik maken van de DAL.
    Zal gebruik maken van speel_rock_paper_scissors voor het daadwerkelijke gevecht.
    Indien de AI niet wordt geimplementeert, voeg dan "if is_ai: return" toe als eerste regel.
    Voor het gemak kan gebruik gemaakt worden van (o.a.) de volgende hulp-functies:
      - inout.ask     (om tekst naar het scherm te printen)
      - inout.choose  (om te kiezen uit de mogelijke tegenstander)
      - dal.*         (om vreemdelingen te checken, karakter te verbannen, enz.)
    """

    if is_ai:
        return

    # Onderstaande code dient ter illustratie om te laten zien hoe ed DAL werkt.

    vreemden = dal.geef_vreemden(False)

    spelerKarakter = dal.geef_rol_van_karakter(dal.HOOFDSPELER)          # False, omdat we niet in de AI-ronde zitten

    if len(vreemden) == 1:
        print('Kennelijk maar 1 tegenstander...')
        if(dal.geef_rol_van_karakter(vreemden[0]) == "Krijger"):
            speel_paper_rock_scissors()
        else:
            dal.voeg_toe_aan_gezelschap(False, vreemden[0])
    else:
        for x in vreemden:
            if(dal.geef_rol_van_karakter(x) == "Krijger"):
                speel_paper_rock_scissors()

        

    # En hier nog veel meer functionaliteit, zoals beschreven in de spelregels.


def overtuig(is_ai):
    """"
    Onderhandel als Diplomaat met de vreemdelingen (of het gezelschap i.g.v. AI).
    Zal intensief gebruik maken van de DAL.
    Zal gebruik maken van speel_rock_paper_scissors voor het daadwerkelijke onderhandelen.
    Indien de AI niet wordt geimplementeert, voeg dan "if is_ai: return" toe als eerste regel.
    Voor het gemak kan gebruik gemaakt worden van (o.a.) de volgende hulp-functies:
      - inout.ask     (om tekst naar het scherm te printen)
      - inout.choose  (om te kiezen uit de mogelijke tegenstander)
      - dal.*         (om vreemdelingen te checken, karakter te verbannen, enz.)
    """

    if is_ai:
        return

    # En hier nog veel meer functionaliteit, zoals beschreven in de spelregels.
