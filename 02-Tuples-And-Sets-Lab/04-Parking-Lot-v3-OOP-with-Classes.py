class Parking:
    def __init__(self):
        self.__cars = set()

    def process_car(self, direction, car):
        operations = {
            'IN': self.__cars.add,
            'OUT': self.__cars.add,
        }
        fn = operations[direction]
        fn(car)

    def print_status(self):
        cars_in_parking = self.__cars
        if cars_in_parking:
            print('\n'.join([reg_num for reg_num in cars_in_parking]))
        else:
            print('Parking Lot is Empty')


parking = Parking()

n = int(input())
for _ in range(n):
    tokens = input().split(', ')
    direction, reg_num = tokens
    parking.process_car(direction, reg_num)


parking.print_status()