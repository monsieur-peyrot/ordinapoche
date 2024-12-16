def run_prog(prog, PC, input_tape):
    """"
    Lance un programme. prog contient la mémoire de l'Ordinapoche.
    PC est le Program Counter au début de l'exécution.
    input_tape est une liste contenant toutes les valeurs du ruban d'entrée.
    La fonction renvoie une liste correspondant aux valeurs du ruban de sortie.
    """

    # Initialisations

    output_tape = []
    index_input = 0
    accu = 0
    sgn_accu = 1
    prog_running = True

    # Boucle d'exécution

    while prog_running:

        # Lecture de l'instruction contenue dans la case mémoire pointée par PC

        instr = prog[PC]

        # Récupération du code de l'instruction ainsi que de l'opérande

        instruction = instr[0]
        operande = instr[1:3]
        address = int(operande)

        # Exécution de l'instruction en fonction de son code (de 0 à 9)

        if instruction == "0":

            # INP : lecture du ruban d'entrée

            if index_input >= len(input_tape):
                prog_running = False
                print()
                print("Ruban d'entrée vide : arrêt du programme !")
            else:
                prog[address] = input_tape[index_input]
                index_input += 1

        elif instruction == "1":

            # CLA : mise à zéro et additionner

            accu = int(prog[address])
            sgn_accu = 1

        elif instruction == "2":

            # ADD : additionner

            accu += int(prog[address])
            if accu >= 1000:
                accu = str(accu)[1:]

        elif instruction == "3":

            # TAC : vérifier le contenu de l'accumulateur

            if sgn_accu < 0:
                PC = address - 1

        elif instruction == "4":

            # SFT : décaler

            accu_str = str(accu)

            # Décalage vers la gauche correspondant au premier chiffre de l'opérande

            while(len(accu_str)<4):
                accu_str = "0" + accu_str
            accu_str += "000000000"
            accu_str = accu_str[int(operande[0]):]

            # Décalage vers la droite correspondant au deuxième chiffre de l'opérande

            for i in range(int(operande[1])):
                accu_str = "0" + accu_str
            accu_str = accu_str[0:4]
            accu = int(accu_str)

        elif instruction == "5":

            # OUT : sortie

            output_tape.append(prog[address])

        elif instruction == "6":

            # STO : emmagasiner

            accu_str = str(accu)
            while len(accu_str) < 3:
                accu_str = "0" + accu_str
            prog[address] = accu_str

        elif instruction == "7":

            # SUB : soustraire

            accu -= int(prog[address])
            if accu < 0:
                sgn_accu = -1
                accu = abs(accu)
            if accu > 1000:
                accu = str(accu)[1:]

        elif instruction == "8":

            # JMP : saut

            PC = address - 1

        elif instruction == "9":

            # HRS : arrêt et mise à zéro

            prog_running = False
            print()
            print("Instruction HRS rencontrée : arrêt du programme !")

        # On passe à l'instruction suivante

        PC += 1
        if PC == 100:
            PC = 0

    return output_tape
