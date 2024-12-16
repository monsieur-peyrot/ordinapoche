"""
            *****************
            *  ORDINAPOCHE  *
            *****************

Ce programme permet de simuler l'Ordinapoche,
maquette didactique permettant d'expliquer le
fonctionnement d'un ordinateur.
Voir le supplément du Science & Vie n°763 pour
plus d'informations
"""

from fonctions import *
from assembler import *
from disassembler import *
from run import *

# Initialisations :

prog = empty_prog()
input_tape = []
running = True

# Boucle principale

print()
print()
print("ORDINAPOCHE")
print("v1.1 du 10/11/2024 par Bruno PEYROT")
print()

while running:

    display_menu()
    print()
    choice = user_choice("Quel est votre choix ? ", 1, 9)
    print()

    if choice == 1:

        # Choix 1 : effacement de la mémoire

        prog = empty_prog()
        print("Mémoire effacée !")

    elif choice == 2:

        # Choix 2 : entrée de données en mémoire

        start = user_choice("Quelle est l'adresse de départ ? ", 0, 99)
        end   = user_choice("Quelle est l'adresse de fin    ? ", 0, 99)
        print()
        prog = input_codes(prog, start, end)

    elif choice == 3:

        # Choix 3 : chargement d'un programme Ordinapoche

        load_prog(prog)

    elif choice == 4:

        # Choix 4 : sauvegarde du programme en cours

        save_prog(prog)

    elif choice == 5:

        # Choix 5 : lecture et assemblage d'un fichier source

        assemble(prog)

    elif choice == 6:

        # Choix 6 : désassemblage d'une zone mémoire

        start = user_choice("Quelle est l'adresse de départ ? ", 0, 99)
        end   = user_choice("Quelle est l'adresse de fin    ? ", 0, 99)
        output_type = user_choice("Type de sortie : 0 = écran, 1 = fichier ? ",0, 1)
        disassemble(prog, start, end, output_type)

    elif choice == 7:

        # Choix 7 : création d'un ruban d'entrée

        n = user_choice("Combien d'éléments dans le ruban d'entrée (30 max.) ? ", 0, 30)
        input_tape = create_inputs(n)
        print()
        print("Ruban d'entrée créé !")

    elif choice == 8:

        # Choix 8 : exécution d'un programme Ordinapoche

        PC = user_choice("Quelle est l'adresse de départ ? ", 0, 99)
        output_tape = run_prog(prog, PC, input_tape)

        # Affichage du contenu du ruban de sortie

        if len(output_tape) == 0:
            print()
            print("Ruban de sortie vide !")
            print()
        else:
            print()
            print("Etat du ruban de sortie :")
            print()
            for i in range(len(output_tape)):
                line_number = str(i + 1)
                if len(line_number) < 2:
                    line_number = "0" + line_number
                print(line_number + " : " + output_tape[i])

    else:

        # Choix 9 : Quitter le programme

        running = False

print()
print()
print("Merci d'avoir utilisé ORDINAPOCHE !")
print()


