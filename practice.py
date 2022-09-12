item1='phone'
item1_price=100
item1_quantity=5
item1_price_total=item1_price*item1_quantity

print(type(item1))
print(type(item1_price))
print(type(item1_quantity))
print(type(item1_price_total))

class Item:
    def __init__(self, name: str,price: float,quantity=0):
    #    Run validations to the received arguments
    # assert price>=0
    # assert quantity>=0
       
       
       
    #    Assign to self objects
        self.name=name
        self.price=price
        self.quantity=quantity
        # print(f'This is an instance created: {name}')
        
    def calculate_total_price(self):
        return self.price* self.quantity

item1=Item('phone',-100,5)
# print(item1.calculate_total_price(item1.price,item1.quantity))

item2=Item('laptop',1000,3)
# print(item2.calculate_total_price(item2.price,item2.quantity))

# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)
print(item1.calculate_total_price())
print(item2.calculate_total_price())
