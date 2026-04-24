

class SupplyError(Exception):
    pass


class IngredientNotFoundError(SupplyError):
    def __init__(self, ingredient_name):
        self.ingredient_name = ingredient_name
        super().__init__(f"ingredient not found: {ingredient_name}")


class InsufficientIngredientError(SupplyError):
    def __init__(self, ingredient_name, requested, available):
        self.ingredient_name = ingredient_name
        self.requested = requested
        self.available = available
        self.shortage = requested - available

        super().__init__(
            f"cannot use {requested} of {ingredient_name}: "
            f"only {available} in stock, short by {self.shortage}"
        )


class InvalidQuantityError(SupplyError):
    def __init__(self, quantity):
        self.quantity = quantity
        super().__init__(f"invalid quantity: {quantity}. must be positive")


class Restaurant:
    def __init__(self):
        self.ingredients = {}

    def add_ingredient(self, name, cost, quantity):
        if quantity <= 0:
            raise InvalidQuantityError(quantity)

        if name not in self.ingredients:
            self.ingredients[name] = {"cost": cost, "quantity": quantity}
        else:
            self.ingredients[name]["quantity"] += quantity
            self.ingredients[name]["cost"] = cost

    def use(self, name, quantity):
        if quantity <= 0:
            raise InvalidQuantityError(quantity)

        try:
            ingredient = self.ingredients[name]
        except KeyError:
            raise IngredientNotFoundError(name) from None

        if quantity > ingredient["quantity"]:
            raise InsufficientIngredientError(
                name, quantity, ingredient["quantity"]
            )

        ingredient["quantity"] -= quantity
        return round(quantity * ingredient["cost"], 2)

    def total_value(self):
        total = sum(
            item["cost"] * item["quantity"]
            for item in self.ingredients.values()
        )
        return round(total, 2)
    




rest = Restaurant()

rest.add_ingredient("Olive Oil", 8.75, 40)
rest.add_ingredient("Flour", 2.30, 200)
rest.add_ingredient("Butter", 4.50, 80)

print(f"total value: {rest.total_value()}")

cost = rest.use("Flour", 50)
print(f"used 50 flour for: {cost}")
print(f"total value: {rest.total_value()}")

rest.add_ingredient("Olive Oil", 9.25, 30)
print(f"total value: {rest.total_value()}")

tests = [
    lambda: rest.use("Saffron", 5),
    lambda: rest.use("Butter", 100),
    lambda: rest.add_ingredient("Salt", 1.50, -10),
]

for test in tests:
    try:
        test()
    except SupplyError as e:
        print(e)
