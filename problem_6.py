

from dataclasses import dataclass, field
from contextlib import contextmanager

class IngredientError(Exception):
    pass

@dataclass
class Ingredient:
    name: str
    category: str
    weight: int
    _availability: str = field(default="UNKNOWN", init=False)

    def __post_init__(self):
        if self.weight <= 0:
            raise IngredientError(f"Invalid weight for {self.name}")

    @property
    def is_heavy(self):
        return self.weight > 200

    def __str__(self):
        return f"{self.name} ({self.category}, {self.weight}g) [{self._availability}]"

    def __gt__(self, other):
        if not isinstance(other, Ingredient):
            return NotImplemented
        return self.weight > other.weight


class PantryChecker:
    def __init__(self, ingredients, categories):
        self.ingredients = ingredients
        self.categories = categories
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.ingredients):
            raise StopIteration

        ingredient = self.ingredients[self.index]
        self.index += 1

        if ingredient.category in self.categories:
            ingredient._availability = "IN STOCK"
        else:
            ingredient._availability = "OUT OF STOCK"

        return ingredient
def pantry_report(checker):
    in_stock = 0
    out_stock = 0

    for ingredient in checker:
        if ingredient._availability == "IN STOCK":
            in_stock += 1
        else:
            out_stock += 1

        yield str(ingredient)

    yield f"Check: {in_stock} in stock, {out_stock} out of stock"


@contextmanager
def kitchen_session(name):
    pantry = []
    print(f"--- Kitchen: {name} ---")
    try:
        yield pantry
    except IngredientError as e:
        print(f"!!! Error: {e}")
    finally:
        print(f"--- Done: {name} ({len(pantry)} ingredients) ---")



with kitchen_session("Breakfast Menu") as pantry:
    pantry.append(Ingredient("Eggs", "Dairy", 150))
    pantry.append(Ingredient("Flour", "Grain", 500))
    pantry.append(Ingredient("Truffle Oil", "Luxury", 30))

    for line in pantry_report(PantryChecker(pantry, ("Dairy", "Grain"))):
        print(line)

    print(pantry[1] > pantry[0])

print()

with kitchen_session("Dinner Menu") as pantry:
    pantry.append(Ingredient("Salt", "Spice", -5))