# -*-coding:Latin-1 -*
#  Ce petit programme permet de convertir des chiffres et des lettres en émojis discord les repésantants.
print("/!\VERSION BETA : Le programme ne prend pas en charge les sauts de ligne et certains caractères avec accent (flm) /!\ ")
message = input("Quel message voulez-vous convertir en émojis Discord ?")
print("Voici votre message à copier-coller : \n")

message = str(message)  # Convertion en texte
chiffres = {"0": "zero", "1": ":one:", "2": ":two:", "3": ":three:", "4": ":four:", "5": ":five:", "6": ":six:", "7": ":seven:", "8": ":eight:", "9": ":nine:", "ç": ":regional_indicator_c:", "é": ":regional_indicator_e:", "è": ":regional_indicator_e:", "ê": ":regional_indicator_e:", "à": ":regional_indicator_a:", "ù": ":regional_indicator_u:"} #  Création d'un dictionnaire pour les chiffres, ç, é, è, ê, à et ù vers émojis.
caractere = 0  # Compte du nombre de caractères traités
message = message.lower()  # On met tous les caractères en minuscule.

while len(message) > caractere:  # Tant que le nombre de caractère de message sera inférieur au nombre de message traités.
    if message[caractere] == "a" or message[caractere] == "b" or message[caractere] == "c" or message[caractere] == "d" or message[caractere] == "e" or message[caractere] == "f" or message[caractere] == "g" or message[caractere] == "h" or message[caractere] == "i" or message[caractere] == "j" or message[caractere] == "k" or message[caractere] == "l" or message[caractere] == "m" or message[caractere] == "n" or message[caractere] == "o" or message[caractere] == "p" or message[caractere] == "q" or message[caractere] == "r" or message[caractere] == "s" or message[caractere] == "t" or message[caractere] == "u" or message[caractere] == "v" or message[caractere] == "w" or message[caractere] == "x" or message[caractere] == "y" or message[caractere] == "z":  # Si cractère = lettre.
        print(":regional_indicator_" + message[caractere] + ":", end=" ")
    elif message[caractere] == "0" or message[caractere] == "1" or message[caractere] == "2" or message[caractere] == "3" or message[caractere] == "4" or message[caractere] == "5" or message[caractere] == "6" or message[caractere] == "7" or message[caractere] == "8" or message[caractere] == "9" or message[caractere] == "ç" or message[caractere] == "é" or message[caractere] == "è" or message[caractere] == "ê" or message[caractere] == "à" or message[caractere] == "ù":  # Si cracatère = chiffre
        print(chiffres[message[caractere]], end=" ")
    else: #  Autres caractères
        print(message[caractere], end=" ")
    caractere = caractere + 1 #  On ajoute 1 au caractère traité.

input("\n\nAppuyez sur la touche \"Entrer\" pour quitter le programme.")  # Quitter le programme.
