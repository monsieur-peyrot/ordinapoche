def disassemble(prog, start, end, output_type):
    """
    Désassemble le contenu de prog entre les adresses start et end
    La valeur de output_type indique le type de sortie :
    0 = sortie à l'écran
    1 = sortie dans un fichier
    """
    try:
        if output_type == 1:

            # Si on veut une sortie dans un fichier, on demande le nom de celui-ci
            # et on l'initialise

            print()
            filename = input("Nom du fichier à sauvegarder ? ").upper()
            print()
            file = open(filename, "w")
            start_adress = str(start)
            if start < 10:
                start_adress = "0" + start_adress
            file.write("ADR " + start_adress + "\n")

        instructions = [ "INP", "CLA", "ADD", "TAC", "SFT", "OUT", "STO", "SUB", "JMP", "HRS" ]
        print()
        for i in range(start, end + 1):

            # Pour chaque adresse de start à end, on lit l'instruction...
            instr = prog[i]
            address = str(i)
            if i < 10:
                address = "0" + address

            # ... et on la décode

            instruction = instr[0]
            operande = instr[1:3]

            # Pour toutes les instructions autres que HRS...

            if instruction != "9":

                # ... on affiche le mnémonique de l'instruction ainsi que son opérande...

                print(address + " : " + instr + " : " + instructions[int(instruction)] + " " + operande)

                # ... et on fait de même dans le fichier si demandé
                if output_type == 1:
                    file.write(instructions[int(instruction)] + " " + operande + "\n")

            else:

                # Traitement de l'instruction HRS

                print(address + " : " +  instr + " : " + instructions[int(instruction)])
                if output_type == 1:
                    file.write(instructions[int(instruction)] + "\n")

        # Fermeture du fichier si cela est nécessaire

        if output_type == 1:
            file.close()

        return None

    except:

        # Traitement des erreurs éventuelles

        print()
        print("Une erreur s'est produite lors de l'écriture du désassemblage")
        return None
