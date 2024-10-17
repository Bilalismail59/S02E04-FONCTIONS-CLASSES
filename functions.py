## Simple

# Définition
def say_hello():
    print("Salut")

# Appeler
say_hello()

## Avec paramètres

# Définition en ajoutant des PARAMÈTRES
def say_hi(name):
    print("Salut " + name)


# Appel en donnant un ARGUMENT
say_hi("Dave")
say_hi("Alice")

## Avec retour

# Définition avec le mot-clé `return` pour retourner une valeur
def build_hello(name: str) -> str:
    return f"Hello {name.upper()}"

result = build_hello("Dave")
print(build_hello("Alice"))

# Valeur par défaut

def with_default(name: str = "Anonyme") -> None:
    print(f"Hello {name.upper()}")

with_default()
with_default("Bob")

## Lambda (fonction anonyme à une seule instruction)
multiply = lambda x, y: x * y
print(multiply(12, 3))

## Gestion d'erreur
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Erreur : division par zéro impossible"

print(divide(10, 2))
print(divide(10, 0))

###################################

# pour accepter plusieurs on utilise l'UNION `|` (depuis la v 3.10)
def calculate_area(height: int | float, width: int | float) -> int | float:
    """
    Calcule la surface d'un rectangle

    Args:
        height (int, float): la hauteur du rectangle
        width (int, float): la largeur du rectangle

    Return:
        float: la surface du rectangle
    """
    print("height", height)
    return height * width


def calculate_diag(height: int | float, width: int | float) -> float:
    """Calcule de la diagonale d'un rectangle

    Args:
        height (int | float): la hauteur du rectangle
        width (int | float): la largeur

    Returns:
        float: la diagonale
    """
    try:
        return (height**2 + width**2)**0.5
    except TypeError:
        return "Erreur : les paramètres doivent être des nombres."


perimeter = lambda h, w: (h + w) * 2

height = 4
width = 3

area = calculate_area(height, width)
print(area)

print(perimeter(height, width))

diag = calculate_diag(height, width)
print(diag)

## Note
# Lors de l'appel on peut préciser le nom de l'arguement
# on précise le nom du paramètre et l'ordre n'importe pas
print(calculate_area(width=25, height=50))

# pratique quand plusieurs paramètres par défaut
def bonus(email, name = "", age = None, role = "guest"):
    print(name, age, email, role)

bonus("bob@mail.fr", role="admin")


