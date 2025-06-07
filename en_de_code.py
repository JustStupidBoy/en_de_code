from base64 import *
import msvcrt

def wait_for_any_key(): #retour menu
    print_gradient("Appuyez sur une touche pour continuer...")
    msvcrt.getch()
    main()

def print_gradient(text): #colorier texte
    start_rgb = (230, 200, 255)
    end_rgb = (100, 0, 150)

    length = len(text)
    for i, char in enumerate(text):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / length)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / length)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / length)
        print(f"\033[38;2;{r};{g};{b}m{char}\033[0m", end='')
    print()

#menu

def main():
    print_gradient("--------------------------------------")
    print_gradient("1. Encoder")
    print_gradient("2. Décoder")
    print_gradient("--------------------------------------")
    while True:
        try:
            print_gradient("Choix numéro : ")
            main_choice = int(input())
            if main_choice == 1:
                encoder()
                break
            elif main_choice == 2:
                decoder()
                break
            else:
                print_gradient("Veuillez entrer un 1 ou 2.")
        except ValueError:
            print_gradient("Veuillez entrer un 1 ou 2.")

#result

def encoder16(x):
    encoded = b16encode(x.encode()).decode()
    print_gradient("--------------------------------------")
    print_gradient(encoded)
    print_gradient("--------------------------------------")
    wait_for_any_key()

def encoder32(x):
    encoded = b32encode(x.encode()).decode()
    print_gradient("--------------------------------------")
    print_gradient(encoded)
    print_gradient("--------------------------------------")
    wait_for_any_key()

def encoder64(x):
    encoded = b64encode(x.encode()).decode()
    print_gradient("--------------------------------------")
    print_gradient(encoded)
    print_gradient("--------------------------------------")
    wait_for_any_key()

def decoder16(x):
    try:
        decoded = b16decode(x.encode()).decode()
        print_gradient("--------------------------------------")
        print_gradient(decoded)
        print_gradient("--------------------------------------")
        wait_for_any_key()
    except Exception as e:
        print_gradient(f"Erreur de décodage base16 : {e}")
        wait_for_any_key()

def decoder32(x):
    try:
        decoded = b32decode(x.encode()).decode()
        print_gradient("--------------------------------------")
        print_gradient(decoded)
        print_gradient("--------------------------------------")
        wait_for_any_key()
    except Exception as e:
        print_gradient(f"Erreur de décodage base32 : {e}")
        wait_for_any_key()

def decoder64(x):
    try:
        decoded = b64decode(x.encode()).decode()
        print_gradient("--------------------------------------")
        print_gradient(decoded)
        print_gradient("--------------------------------------")
        wait_for_any_key()

    except Exception as e:
        print_gradient(f"Erreur de décodage base64 : {e}")
        wait_for_any_key()

#choose message to decode/encode

def encoder():
    while True:
        print_gradient("--------------------------------------")
        print_gradient("Entrer le message à encoder :")
        x = input().strip()
        if not x:
            print_gradient("Erreur : le message ne peut pas être vide.")
        elif x.isdigit():
            print_gradient("Erreur : entrez un vrai message, pas juste un nombre.")
        else:
            break

    print_gradient("--------------------------------------")
    print_gradient("En quelle base souhaitez-vous l'encoder :")
    print_gradient("1. base 16")
    print_gradient("2. base 32")
    print_gradient("3. base 64")
    print_gradient("--------------------------------------")
    choice_encoder(x)

def decoder():
    while True:
        print_gradient("--------------------------------------")
        print_gradient("Entrer le message à décoder :")
        x = input().strip()
        if not x:
            print_gradient("Erreur : le message ne peut pas être vide.")
        elif x.isdigit():
            print_gradient("Erreur : entrez un vrai message, pas juste un nombre.")
        else:
            break

    print_gradient("--------------------------------------")
    print_gradient("En quelle base souhaitez-vous le décoder :")
    print_gradient("1. base 16")
    print_gradient("2. base 32")
    print_gradient("3. base 64")
    print_gradient("--------------------------------------")
    choice_decoder(x)

#choice base 16 / 32 / 64

def choice_encoder(x):
    while True:
        try:
            print_gradient("Choix numéro : ")
            b = int(input())
            if b == 1:
                encoder16(x)
                break
            elif b == 2:
                encoder32(x)
                break
            elif b == 3:
                encoder64(x)
                break
            else:
                print_gradient("Veuillez entrer un nombre entre 1 et 3.")
        except ValueError:
            print_gradient("Erreur : entrez un nombre entier (1, 2 ou 3).")

def choice_decoder(x):
    while True:
        try:
            print_gradient("Choix numéro : ")
            b = int(input())
            if b == 1:
                decoder16(x)
                break
            elif b == 2:
                decoder32(x)
                break
            elif b == 3:
                decoder64(x)
                break
            else:
                print_gradient("Veuillez entrer un nombre entre 1 et 3.")
        except ValueError:
            print_gradient("Erreur : entrez un nombre entier (1, 2 ou 3).")

#lancer

if __name__ == "__main__":
    main()
