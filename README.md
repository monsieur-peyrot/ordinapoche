# Ordinapoche

Simulateur d'Ordinapoche, ordinateur "en carton" présenté dans le supplément de Science & Vie n°763

Il s'agit d'un pseudo CPU ayant un jeu d'instruction comportant 10 instructions. La mémoire accessible est composée de 100 cases mémoires contenant des nombres entiers positifs à 3 chiffres.
Le premier chiffre correspond au code de l'instruction, les deux chiffres suivants pointent vers une case mémoire.

Les instructions disponibles sont : 

0 : INP : Lit une valeur sur le ruban d'entrée

1 : CLA : Mise à zéro et additionner

2 : ADD : Additionner

3 : TAC : Vérifier le contenu de l'accumulateur

4 : SFT : décaler

5 : OUT : Ecrit une valeur sur le ruban de sortie

6 : STO : Emmagasiner

7 : SUB : Soustraire

8 : JMP : Saut

9 : HRS : Arrêt et mise à zéro


L'assembleur intégré comporte en plus deux directives :

ADR : définit l'adresse de départ du programme à assembler

VAL : définit une valeur numérique

'#   : commentaire


La seule différence avec l'Ordinapoche originel est que la mémoire ne peut contenir que des nombres positifs.

