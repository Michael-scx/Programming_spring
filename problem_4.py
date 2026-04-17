
from dataclasses import dataclass , field

@dataclass

class MenuItem :
    name : str
    price : float
    quantity : int

    def value(self) -> float :
        return round(self.price * self.quantity , 2)
    
@dataclass

class Restaurant :
    name : str
    menu_items : list = field(default_factory=list)
    total_revenue : float = field(init=False)

    def __post_init__(self):
        self.update_total_revenue()

    def update_total_revenue(self):
        self.total_revenue = round(sum(each_item.value() for each_item in self.menu_items) , 2)

    def add_item(self,item:MenuItem):
        self.menu_items.append(item)
        self.update_total_revenue()

    def serve(self , item_name:str,qty:int) -> bool:
        for each_item in self.menu_items:
            if each_item.name == item_name:
                if qty <= each_item.quantity :
                    each_item.quantity -= qty
                    self.update_total_revenue()
                    return True
        return False
    
    def resupply(self , item_name:str , qty:int):
        for each_item in self.menu_items :
            if each_item.name == item_name:
                each_item.quantity += qty
                self.update_total_revenue()

    
    def report(self) -> str:
        result = f"{self.name} Menu:\n"
    
        for item in self.menu_items:
            result += f"    {item.name}: {item.quantity} servings @ ${item.price} each\n"
    
        result += f"Total revenue: ${self.total_revenue}"
    
        return result


m1 = MenuItem("Burger", 12.99, 20)
m2 = MenuItem("Salad", 8.49, 40)
m3 = MenuItem("Pasta", 14.99, 15)


r = Restaurant("BistroHub")
r.add_item(m1)
r.add_item(m2)
r.add_item(m3)

print(r.total_revenue)
print(r.serve("Burger" , 5))
print(r.serve("Burger" , 25))
r.resupply("Salad" , 10)

print(r.report())








