# -*-coding:Latin-1 -*
#  Ce petit programme permet de convertir des chiffres et des lettres en �mojis discord les rep�santants.
print("/!\VERSION BETA : Le programme ne prend pas en charge les sauts de ligne et certains caract�res avec accent (flm) /!\ ")
message = input("Quel message voulez-vous convertir en �mojis Discord ?")
print("Voici votre message � copier-coller : \n")

message = str(message)  # Convertion en texte
chiffres = {"0": "zero", "1": ":one:", "2": ":two:", "3": ":three:", "4": ":four:", "5": ":five:", "6": ":six:", "7": ":seven:", "8": ":eight:", "9": ":nine:", "�": ":regional_indicator_c:", "�": ":regional_indicator_e:", "�": ":regional_indicator_e:", "�": ":regional_indicator_e:", "�": ":regional_indicator_a:", "�": ":regional_indicator_u:"} #  Cr�ation d'un dictionnaire pour les chiffres, �, �, �, �, � et � vers �mojis.
caractere = 0  # Compte du nombre de caract�res trait�s
message = message.lower()  # On met tous les caract�res en minuscule.

while len(message) > caractere:  # Tant que le nombre de caract�re de message sera inf�rieur au nombre de message trait�s.
    if message[caractere] == "a" or message[caractere] == "b" or message[caractere] == "c" or message[caractere] == "d" or message[caractere] == "e" or message[caractere] == "f" or message[caractere] == "g" or message[caractere] == "h" or message[caractere] == "i" or message[caractere] == "j" or message[caractere] == "k" or message[caractere] == "l" or message[caractere] == "m" or message[caractere] == "n" or message[caractere] == "o" or message[caractere] == "p" or message[caractere] == "q" or message[caractere] == "r" or message[caractere] == "s" or message[caractere] == "t" or message[caractere] == "u" or message[caractere] == "v" or message[caractere] == "w" or message[caractere] == "x" or message[caractere] == "y" or message[caractere] == "z":  # Si cract�re = lettre.
        print(":regional_indicator_" + message[caractere] + ":", end=" ")
    elif message[caractere] == "0" or message[caractere] == "1" or message[caractere] == "2" or message[caractere] == "3" or message[caractere] == "4" or message[caractere] == "5" or message[caractere] == "6" or message[caractere] == "7" or message[caractere] == "8" or message[caractere] == "9" or message[caractere] == "�" or message[caractere] == "�" or message[caractere] == "�" or message[caractere] == "�" or message[caractere] == "�" or message[caractere] == "�":  # Si cracat�re = chiffre
        print(chiffres[message[caractere]], end=" ")
    else: #  Autres caract�res
        print(message[caractere], end=" ")
    caractere = caractere + 1 #  On ajoute 1 au caract�re trait�.

input("\n\nAppuyez sur la touche \"Entrer\" pour quitter le programme.")  # Quitter le programme.
