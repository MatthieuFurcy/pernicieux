## Programmation impérative autour des nombres pernicieux // TP Susset/Noël // CIEL-IR1
## Auteur: M. Matthieu Furcy
## Date : 2024-10-08

# Méthodo:
#    1. Méthode pour déterminer si un nombre est premier
#    2. Méthode pour convertir un nombre en binaire
#    3. Méthode pour déterminer la nature d'un nombre pernicieux
#    4. Méthode pour saisir un nombre à analyser
#    5. Programmation permettant d'analyser les nombres pernicieux compris entre 0 et 1000

### Début du programme

# Méthode pour déterminer si un nombre est premier

def is_prime(n):
    if n < 2:  # 0 et 1 ne sont pas premiers
        return False # On retourne faux
    for i in range(2, int(n**0.5) + 1):  # On vérifie jusqu'à la racine carrée de n grâce à eratosthène
        if n % i == 0:  # Si n est divisible par i
            return False # On retourne faux
    return True # Sinon, on retourne vrai

# Méthode pour convertir un nombre en binaire

def to_binary(n): 
    if n == 0: # Si n est 0
        return "0"  # 0 en binaire est 0
    binary_digits = [] # On crée un tableau vide pour stocker les chiffres binaires
    while n > 0: # Tant que n est supérieur à 0
        binary_digits.append(str(n % 2))  # On ajoute le reste (0 ou 1) au tableau
        n //= 2  # On divise n par 2
    return ''.join(reversed(binary_digits))  # On inverse le tableau et on joint les chiffres pour former une chaîne

# Méthode pour déterminer la nature d'un nombre pernicieux

def is_pernicious(n):
    # Convertit le nombre en binaire et compte le nombre de '1'
    count_of_ones = to_binary(n).count('1') # On compte le nombre de '1' dans la représentation binaire
    # Vérifie si ce nombre est premier
    return is_prime(count_of_ones) 

# Méthode pour saisir un nombre à analyser

def get_number():
    while True:  # Boucle infinie
        try: 
            n = int(input("Entrez un nombre à analyser: "))  # On saisit un nombre
            if n < 0:  # Si le nombre est négatif
                print("Le nombre doit être positif.")  # On affiche un message
                continue  # On recommence la boucle
            return n  # On retourne le nombre
        except ValueError:  # Si la saisie n'est pas un nombre
            print("Vous devez saisir un nombre.")  # On affiche un message
            continue

# Programmation permettant d'analyser les nombres pernicieux compris entre 0 et 1000

def main():
    # Méthode principale
    print("Analyse des nombres pernicieux compris entre 0 et 1000")  # On affiche un message

    for i in range(1001):  # On parcourt les nombres de 0 à 1000
        if is_pernicious(i):  # Si le nombre est pernicieux
            print(f"{i} est un nombre pernicieux.")  # On affiche un message

# Exécution du programme

main()  # On exécute la méthode principale

### Fin du programme

# Remarque:
# 1. Des assertions auraient pu être ajoutés pour vérifier le bon fonctionnement de la fonction is_pernicious,
#    mais cela n'était pas demandé.
