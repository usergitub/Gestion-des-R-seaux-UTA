# Informations initiales
compte_principal = 17225
compte_uta_money = 176249

# Tarifs pour Internet, SMS et Appel
tarifs = {
    'internet': {
        'jour': {1: (100, 100), 2: (200, 200), 3: (500, 1500)},
        'semaine': {1: (1000, 3000), 2: (1500, 4500), 3: (2000, 6000)},
        'mois': {1: (2500, 7500), 2: (5000, 15000), 3: (10000, 30000)}
    },
    'sms': {
        'jour': {1: (100, 100), 2: (200, 200), 3: (500, 150)},
        'semaine': {1: (1000, 300), 2: (1500, 450), 3: (2000, 600)},
        'mois': {1: (2500, 750), 2: (5000, 1500), 3: (10000, 3000)}
    },
    'appel': {
        'jour': {1: (100, 10), 2: (200, 20), 3: (500, 50)},
        'semaine': {1: (1000, 100), 2: (1500, 150), 3: (2000, 200)},
        'mois': {1: (2500, 400), 2: (3000, 1000), 3: (10000, 10000)}
    }
}

# Fonction pour afficher les options disponibles
def afficher_options(categorie, duree):
    options = tarifs[categorie][duree]
    print(f"Choisissez une option pour {categorie.capitalize()} ({duree}):")
    for key, value in options.items():
        print(f"{key}- {value[0]}f pour {value[1]} {categorie.capitalize()}")
    choix = int(input("Votre choix : "))
    return options[choix]

# Fonction principale
def souscrire_pass():
    global compte_uta_money, compte_principal  # Ajout de ces lignes

    # Affichage du solde initial
    print("Solde des comptes:")
    print(f"Compte Principal : {compte_principal}f")
    print(f"Compte UTA Money : {compte_uta_money}f")

    code_verification = input("Entrez votre code de vérification : ")

    # Vérification du code de vérification
    if code_verification != "#2024#":
        print("Code de vérification incorrect. Opération annulée.")
        return

    while True:
        print("Options disponibles:")
        print("1- Appel")
        print("2- Internet")
        print("3- SMS")

        try:
            choix_categorie = int(input("Votre choix : "))
            categories = {1: 'appel', 2: 'internet', 3: 'sms'}

            if choix_categorie not in categories:
                raise ValueError("Erreur de choix. Veuillez réessayer.")

            categorie = categories[choix_categorie]
            break  # Sortir de la boucle si l'entrée est valide

        except ValueError as e:
            print(f"Erreur : {e}")

    print(f"\nVous avez choisi {categorie.capitalize()}.")

    while True:
        print("Choisissez la durée:")
        print("1- Jour")
        print("2- Semaine")
        print("3- Mois")

        try:
            choix_duree = int(input("Votre choix : "))
            duree_options = {1: 'jour', 2: 'semaine', 3: 'mois'}

            if choix_duree not in duree_options:
                raise ValueError("Erreur de choix. Veuillez réessayer.")

            duree = duree_options[choix_duree]
            break  # Sortir de la boucle si l'entrée est valide

        except ValueError as e:
            print(f"Erreur : {e}")

    tarif, quantite = afficher_options(categorie, duree)

    montant_total = tarif
    duree_pass = 0

    if duree == 'jour':
        duree_pass = 1
    elif duree == 'semaine':
        duree_pass = 7
    elif duree == 'mois':
        duree_pass = 30

    print(f"\nVous allez souscrire {tarif}f pour {quantite} {categorie} valable {duree_pass} jours.")

    while True:
        print("\nChoisissez le compte de paiement:")
        print("1- Compte Principal")
        print("2- UTA Money")

        try:
            choix_compte = int(input("Votre choix : "))

            if choix_compte not in [1, 2]:
                raise ValueError("Erreur de choix. Veuillez réessayer.")

            if choix_compte == 1:
                compte = "Compte Principal"
                compte_principal -= montant_total
            elif choix_compte == 2:
                # Vérification du code secret pour UTA Money
                code_secret_uta_money = input("Entrez le code secret UTA Money : ")
                if code_secret_uta_money != "0901":
                    raise ValueError("Code secret incorrect. Veuillez réessayer.")

                compte = "UTA Money"
                compte_uta_money -= montant_total

            break  # Sortir de la boucle si l'entrée est valide

        except ValueError as e:
            print(f"Erreur : {e}")

    print(f"\nFélicitations !!! Vous disposez de {quantite} {categorie} après votre achat du pass {categorie} valable {duree_pass} jour(s).")
    print(f"{compte} : {compte_principal}f")
    print(f"Compte UTA Money : {compte_uta_money}f")

# Exécution du programme
souscrire_pass()





