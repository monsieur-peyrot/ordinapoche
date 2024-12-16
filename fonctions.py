"""
Fonctions principales utilisées par ordinapoche.py
"""



def display_menu():
    """
    Affichage du menu principal
    """
    print()
    print()
    print()
    print("      ORDINAPOCHE")
    print("      -----------")
    print()
    print("1: Effacer la mémoire")
    print("2: Ecrire en mémoire")
    print("3: Lire un programme Ordinapoche")
    print("4: Sauvegarder le programme Ordinapoche en cours")
    print("5: Lire et assembler un fichier source Ordinapoche")
    print("6: Désassembler une zone mémoire")
    print("7: Ecrire un ruban d'entrée")
    print("8: Executer un programme")
    print("9: Quitter")
    return None



def user_choice(question, first, last):
    """
    Permet à l'utilisateur de rentrer un nombre entier entre first et last
    """
    correct = False
    while not(correct):
        try:
            choix = int(input(question))
            if first <= choix <= last:
                correct = True
            else:
                print()
                print("Vous devez entrer un nombre entier compris entre", first, "et", last, "!")
        except:
            print()
            print("Vous devez entrer un nombre entier compris entre", first, "et", last, "!")
    return choix



def empty_prog():
    """
    Crée un programme vide (un tableau de 100 cases toutes à "000")
    """
    prog = []
    for i in range(100):
        prog.append("000")
    return prog



def input_codes(prog, start, end):
    """
    Crée un programme dans la mémoire de l'ordinapoche
    """
    numbers = "0123456789"
    print()
    for i in range(start, end + 1):
        valid = False
        while not(valid):
            inp = input("Veuillez entrez le contenu de l'adresse n°" + str(i) + " : ")
            while len(inp) < 3:
                inp = "0" + inp
            if len(inp) == 3 and inp[0] in numbers and inp[1] in numbers and inp[2] in numbers:
                valid = True
            if not valid:
                print()
                print("Saisie incorrecte, veuillez recommencer !")
                print()
        prog[i] = inp
    return prog



def load_prog(prog):
    """
    Charge un fichier Ordinapoche en mémoire"
    """
    try:
        numbers = "0123456789"
        filename = input("Nom du fichier programme à charger ? ").upper()
        file = open(filename, "r")
        text = file.read()
        file.close()
        print()
        temp = ["000"] * 100
        for i in range(0, 100):
            temp[i] = text[i*4:i*4+3]
            address = str(i)
            if i < 10:
                address = "0" + address
            print(address + " : " + temp[i])
            for j in range(3):
                if temp[i][j] not in numbers:
                    print()
                    print("Code incorrect rencontré ! Annulation du chargement du fichier !")
                    raise RuntimeError()
        for i in range(0, 100):
            prog[i] = temp[i]
        print()
        print("Programme chargé en mémoire !")
        return None
    except FileNotFoundError:
        print()
        print("Fichier non trouvé !")
        return None
    except:
        print()
        print("Une erreur s'est produite lors de la lecture du fichier", filename)
        return None



def save_prog(prog):
    """
    Sauvegarde dans un fichier l'intégralité de la mémoire de l'Ordinapoche
    """
    try:
        filename = input("Nom du fichier à sauvegarder ? ").upper()
        file = open(filename, "w")
        for i in range(0, 100):
            file.write(prog[i] + "\n")
        file.close()
        print()
        print("Programme sauvegardé !")
        return None
    except:
        print()
        print("Une erreur s'est produite lors de l'écriture du fichier", filename)
        return None



def create_inputs(n):
    """
    Crée une liste contenant les valeurs du ruban d'entrée de l'Ordinapoche
    """
    input_tape = []
    numbers = "0123456789"
    print()
    for i in range(1, n + 1):
        valid = False
        while not(valid):
            inp = input("Veuillez entrez la donnée n°" + str(i) + " : ")
            while len(inp) < 3:
                inp = "0" + inp
            if len(inp) == 3 and inp[0] in numbers and inp[1] in numbers and inp[2] in numbers:
                valid = True
            if not valid:
                print()
                print("Saisie incorrecte, veuillez recommencer !")
                print()
        input_tape.append(inp)
    return input_tape