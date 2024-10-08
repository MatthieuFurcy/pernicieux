## Programmation impérative autour des nombres pernicieux // TP Susset/Noël // CIEL-IR1
## Auteur: M. Matthieu Furcy
## Date : 2024-10-08

# Méthodo:
#    1. Méthode pour déterminer la nature d'un nombre pernicieux
#    2. Méthode pour saisir un nombre à analyser
#    3. Programmation permettant d'analyser les nombres pernicieux compris entre 0 et 1000

### Début du programme

# Méthode pour déterminer la nature d'un nombre pernicieux

def is_pernicious(n):
    # Méthode pour déterminer si un nombre est pernicieux
    def is_prime(n):
        # Méthode pour déterminer si un nombre est premier
        if n < 2: # 0 et 1 ne sont pas des nombres premiers
            return False # booléen
        for i in range(2, n): # On parcourt les nombres de 2 à n
            if n % i == 0: # Si n est divisible par i
                return False # n n'est pas premier
        return True # n est premier
    
    def sum_of_digits(n): 
        # Méthode pour calculer la somme des chiffres d'un nombre
        return sum([int(i) for i in str(n)]) # On retourne la somme des chiffres de n, le nombre à analyser
    
    # un nombre est pernicieux si la somme de ses chiffres est un nombre premier.
    # si cette condition est remplie, la fonction renvoie True, sinon False.

    if is_prime(sum_of_digits(n)): # Si la somme des chiffres de n est premier
        return True # n est pernicieux
    return False # n n'est pas pernicieux

# Méthode pour saisir un nombre à analyser

def get_number():
    # Méthode pour saisir un nombre
    while True: # Boucle infinie
        try:
            n = int(input("Entrez un nombre à analyser: ")) # On saisit un nombre
            if n < 0: # Si le nombre est négatif
                print("Le nombre doit être positif.") # On affiche un message
                continue # On recommence la boucle
            return n # On retourne le nombre
        except ValueError: # Si la saisie n'est pas un nombre
            print("Vous devez saisir un nombre.") # On affiche un message
            continue

# Programmation permettant d'analyser les nombres pernicieux compris entre 0 et 1000

def main():
    # Méthode principale
    print("Analyse des nombres pernicieux compris entre 0 et 1000") # On affiche un message

    for i in range(1001): # On parcourt les nombres de 0 à 1000
        if is_pernicious(i): # Si le nombre est pernicieux
            print(f"{i} est un nombre pernicieux.") # On affiche un message

# Exécution du programme

main() # On exécute la méthode principale

### Fin du programme

# Quelques optimisations que j'aurais pu envisager mais que j'ai volontairement laissées de côté car elles n'étaient pas demandées :
#
# 1. Dans la fonction is_prime(), on vérifie si un nombre est premier en testant tous les diviseurs jusqu'à n, 
#    mais on aurait pu améliorer l'efficacité en limitant la vérification à la racine carrée de n grâce à Mr Erathostène, 
#    ce qui réduirait le nombre d'opérations à effectuer. J'ai choisi de ne pas le faire car ce n'était pas nécessaire 
#    dans le cadre de ce TP.
#
# 2. La conversion en binaire et le comptage des "1" pour déterminer si un nombre est pernicieux 
#    sont effectués à chaque itération. Pour optimiser, on aurait pu calculer ces valeurs une fois pour tous les nombres
#    entre 0 et 1000, puis les stocker dans une table, ce qui aurait évité de refaire les mêmes calculs. 
#    Là encore, ça n'a pas été fait car ça dépasse les besoins du TP.
#
# 3. Si on travaillait sur un intervalle encore plus grand de nombres, on aurait pu stocker 
#    les résultats des tests pour éviter de recalculer plusieurs fois si un nombre est pernicieux ou non. 
#    Ici, l'intervalle de 0 à 1000 reste assez restreint donc l'optimisation est intrinsèque.
#
# 4. On pourrait ajouter des tests pour vérifier que les fonctions fonctionnent correctement, à l'aide d'assertions par exemple
#    mais je n'ai pas jugé cela nécessaire non plus..
