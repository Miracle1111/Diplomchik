import random
# class Cafe_type:
#     def __init___(self, spendings, max_entrance):
#         self.spendings = spendings
#         self.max_entrance = max_entrance
# 
#     def get_type(self, id):
#         if id == 0:
#             self.spendings = 25000
#             self.max_entrance = 15
#         elif id == 1:
#             self.spendings = 50000
#             self.max_entrance = 30
#         elif id == 2:
#             self.spendings = 100000
#             self.max_entrance = 60
#         else:
#             print('There is no such type')
#         return (self.spendings, self.max_entrance)
# 
# 
# cafe_1 = Cafe_type()
# 
# 
# class Cafe:
#     def __init__(self, x, y, type):
#         self.x = x
#         self.y = y
#         self.owner = "Computer"
#         self.type = type
#         self.price = random.randint(25, 30)
# 
#     def start(self):
#         self.point = (self.x, self.y)
#         return self.point, self.owner, self.type, self.price
# 
# 
# i = random.randint(1, 5)
# cafe = []
# for i in range(0, i+1):
#     cafe.append(Cafe(1, 2, cafe_1.get_type(2)).start())
# print(cafe)


class Cafe:
    cafe_count = 0
    @staticmethod
    def get_type(id):
        if id == 0:
            spendings = 2800
            max_entrance = 15
        elif id == 1:
            spendings = 5000
            max_entrance = 30
        elif id == 2:
            spendings = 10000
            max_entrance = 50
        else:
            print('There is no such type')
        return (spendings, max_entrance)

    def start(self, x, y, id, price):
        print('Cafe is opened!')
        self.point = (x, y)
        self.owner = "Computer"
        self.entr = entr
        self.price = price
        print(self.point, self.owner, id, self.price, Cafe.get_type(id))
        Cafe.cafe_count +=1


cafes_a = [Cafe() for i in range(random.randint(0, 3))]
for i in cafes_a:
    i.start(2, 3, 1, random.randint(25, 35))
# print(cafe_a.get_type(1))
print(cafes_a)
cafe_b = Cafe()
cafe_b.start(1, 1, 0, random.randint(15, 25))
# print(cafe_b.get_type(0))
print(cafe_b.cafe_count)
cafe_с = Cafe()
cafe_с.start(2, 2, 2, random.randint(30, 45))
# print(cafe_b.get_type(0))
print(cafe_с.cafe_count)






