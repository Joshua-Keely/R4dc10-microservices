# Imports
import requests


# Functions
def recherche_adresse(adresse, code_postal):
    """Recherche une adresse et retourne les informations de la ville"""
    adresse_parsed = adresse.replace(" ", "+")
    url = "https://api-adresse.data.gouv.fr/search/?q=" + adresse_parsed + "&postcode=" + code_postal
    r = requests.get(url)
    contenu = r.json()
    nom_ville = contenu["features"][0]["properties"]["city"]
    gps_x = contenu["features"][0]["properties"]["x"]
    gps_y = contenu["features"][0]["properties"]["y"]
    citycode = contenu["features"][0]["properties"]["citycode"]
    code_postal = contenu["features"][0]["properties"]["postcode"]
    url_pop = "https://geo.api.gouv.fr/communes?code=" + citycode + "&fields=population"
    population = requests.get(url_pop).json()[0]["population"]
    print(
        "Commune: " + nom_ville + " " + code_postal + "\n"
                                                      "Coordonnées GPS: " + "x: " + str(gps_x) + " y: " + str(
            gps_y) + "\n"
                     "Population: " + str(population)
    )


def ask_adresse():
    """Demande une adresse et un code postal"""
    adresse = input("Entrez une adresse: ")
    code_postal = input("Entrez un code postal: ")
    print(recherche_adresse(adresse, code_postal))


# Main
ask_adresse()
