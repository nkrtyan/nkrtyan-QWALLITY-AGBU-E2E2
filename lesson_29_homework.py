data = {
    'name': ["Swimming", "Tennis"],
    'price': [40000, 50000],
    'number': [16, 10]
}

class Sport():
    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number


    def calculate(self):
        session_price = self.price / self.number
        print(f'{self.name} - {session_price} AMD per session')


swimming_obj = Sport(data['name'][0], data['price'][0], data['number'][0]) # TODO, no need hardcode the index, instead keep each sport like seperate dict inside the dict
tennis_obj = Sport(data['name'][1], data['price'][1], data['number'][1])

swimming_obj.calculate()
tennis_obj.calculate()

# Nel, OOP is correct, correct dict and call
