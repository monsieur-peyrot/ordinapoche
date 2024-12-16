def assemble(prog):

    try:

        # Ouverture et lecture du fichier source à assembler

        filename = input("Quel est le nom du fichier que vous voulez assembler ? ")
        file = open(filename, "r")
        text = file.read()
        text = text + "\n"
        text = text.upper()
        file.close()

        # Initialisations

        codes = [ "INP", "CLA", "ADD", "TAC", "SFT", "OUT", "STO", "SUB", "JMP", "HRS", "ADR", "VAL" ]
        numbers = "0123456789"
        temp = []
        PC = 0
        n = 0
        first = 0
        index = 0
        error = False
        error_code = 0
        print()

        # Assemblage du code source

        while not(error) and index < len(text):

            # On parcourt le code source jusqu'à trouver un retour charriot...

            if ord(text[index]) == 10:

                # ... quand c'est le cas, on extrait la ligne correspondante

                line = text[first:index]
                first = index + 1
                n += 1
                number = str(n)
                while (len(number) < 3):
                    number = "0" + number

                # On affiche le numéro de la ligne ainsi que la ligne en cours de traitement

                print(number, ":", line)

                # Si la ligne n'est pas vide...

                if len(line) != 0:

                    # ... on la découpe en mot

                    words = line.split()

                    # Si le premier mot de la ligne est "#", le reste de la ligne est
                    # traitée comme un commentaire

                    if words[0][0] != "#":

                        # Sinon on regarde le premier mot de la ligne et on vérifie
                        # qu'il se trouve bien dans la ligne des mots acceptés

                        code = words[0]
                        if code not in codes:

                            # Si c'est pas le cas, on renverra le code d'erreur 1

                            error = True
                            error_code = 1
                        else:

                            # Sinon, on récupère le code de l'instruction

                            code_instr = codes.index(code)
                            if code_instr < 9:

                                # Si le code de l'instruction est compris entre 0 et 8...

                                if len(words) == 1:

                                    # ... et qu'il n'y a pas d'opérande, on renverra le code d'erreur 3

                                    error = True
                                    error_code = 3

                                elif len(words) > 2:

                                    # S'il y a plus qu'un seul opérande, on renverra le code d'erreur 4

                                    error = True
                                    error_code = 4

                                else:

                                    operande = words[1]

                                    if len(operande) < 2:

                                        # Si l'opérande ne fait qu'un caractère, on rajoute un "0" devant

                                        operande = "0" + operande

                                    if len(operande) != 2:

                                    # Si l'opérande n'a pas une longueur de 2, on renverra le code d'erreur 5

                                        error = True
                                        error_code = 5

                                    else:

                                        if operande[0] not in numbers or operande[1] not in numbers:

                                            # Si l'opérande n'est pas une valeur numérique, on renverra le code d'erreur 5

                                            error = True
                                            error_code = 6

                                        else:

                                            # Si tout va bien, on détermine le code de l'instruction correspondant à la ligne
                                            # en cours de traitement, et on l'ajoute dans la liste temporaire

                                            instr = str(code_instr) + operande
                                            temp.append((PC, instr))

                                            # On passe à l'adresse mémoire suivante

                                            PC += 1

                            elif code_instr == 9:

                                # Si le code est 9 (instruction HRS)...

                                if len(words) != 1:

                                    # S'il y a des opérandes, on renverra le code d'erreur 2

                                    error = True
                                    error_code = 2

                                else:

                                    # Sinon on rajoute l'instruction "900" dans la liste temp

                                    temp.append((PC, "900"))

                                    # On passe à l'adresse mémoire suivante

                                    PC += 1

                            elif code_instr == 10:

                                # Traitement du mnémonique ADR

                                if len(words) == 1:

                                    # S'il n'y a pas d'opérande, renvoi du code d'erreur 3

                                    error = True
                                    error_code = 3

                                elif len(words) > 2:

                                    # S'il y a plus qu'un seul opérande, renvoi du code d'erreur 4

                                    error = True
                                    error_code = 4

                                else:

                                    # Récupération de l'opérande

                                    operande = words[1]

                                    if len(operande) < 2:

                                        # Si l'opérande ne fait qu'un caractère, on rajoute un "0" devant

                                        operande = "0" + operande

                                    if len(operande) != 2:

                                        # Si la longueur de l'opérande est différente de 2, renvoi du code d'erreur 5

                                        error = True
                                        error_code = 5

                                    else:

                                        if operande[0] not in numbers or operande[1] not in numbers:

                                            # Si l'opérande n'est pas un nombre, renvoi du code d'erreur 5

                                            error = True
                                            error_code = 6

                                        else:

                                            # Si tout va bien, l'opérande devient la nouvelle adresse

                                            PC = int(operande)

                            elif code_instr == 11:

                                # Traitement du mnémonique VAL

                                if len(words) == 1:

                                    # S'il n'y a pas d'opérande, renvoi du code d'erreur 3

                                    error = True
                                    error_code = 3

                                elif len(words) > 2:

                                    # S'il y a plus qu'un seul opérande, renvoi du code d'erreur 5

                                    error = True
                                    error_code = 4

                                else:

                                    # Récupération de l'opérande

                                    operande = words[1]
                                    if len(operande) > 3:

                                        # Si l'opérande fait plus de trois caractères, renvoi du code d'erreur 5

                                        error = True
                                        error_code = 7

                                    else:

                                        # On rajoute éventuellement des "0" au début de l'opérande pour atteindre les 3 caractères

                                        while len(operande) < 3:
                                            operande = "0" + operande

                                        # Si l'opérande n'est pas un nombre, renvoi du code d'erreur 5

                                        if operande[0] not in numbers or operande[1] not in numbers or operande[2] not in numbers:
                                            error = True
                                            error_code = 6

                                        else:

                                            # Si tout va bien, on met la valeur de l'opérande dans la liste temp

                                            temp.append((PC, operande))

                                            # On passe à l'adresse suivante

                                            PC += 1

            # On examine le caractère suivant du code source

            index += 1

        if error:

            # Si une erreur s'est produite lors de l'assemblage, on affiche le code correspondant

            print()
            print("ERREUR", error_code, "à la ligne", n, ":", line)
            errors = [ "Ok", "Instruction non reconnue", "Pas d'opérande après HRS", \
                       "Opérande manquant", "Nombre trop grand d'opérandes", \
                       "L'opérande doit comporter au plus deux chiffres", \
                       "L'opérande doit être une valeur numérique", \
                       "Une valeur doit comporter au plus trois chiffres"]
            print(errors[error_code])
            print()

        else:

            # Assemblage réussi

            print()
            print("Assemblage réussi !")

            # Recopie du programme assemblé dans la mémoire de l'Ordinapoche

            for i in range(len(temp)):
                address = temp[i][0]
                value = temp[i][1]
                prog[address] = value

            return None

    except:

        # Traitement des erreurs éventuelles

        print()
        print("Une erreur s'est produite lors de la lecture du fichier", filename)
        return None
