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

class Object:
    def __init__(self, value = 0,object_type = 0):
       self.value = value
       self.type = object_type

class Mapper:
    def __init__(self,size, computer_objects = 3):
        self.matrix = []
        for _ in range(size):
            row = []
            for _ in range(size):
                row.append(Object())
            self.matrix.append(row)
        self.size = size
        self.computer_objects = computer_objects

    def addObject(self,Object):
        if(self.computer_objects == 0):
            print("No free space for you, cowboy")
            return
        while True:
            x = random.randint(0,self.size)
            y = random.randint(0,self.size)
            if (self.matrix[x][y].value == 0): #NOTE: 0 stands for no owner
                self.matrix[x][y].value = 1 #NOTE: 1 stands for computer owner
                self.matrix[x][y].type = Object.type 
                self.computer_objects-=1
                break
        Object.x = x
        Object.y = y
    def addUserObject(self,Object,x,y):
        if (self.matrix[x][y].value == 0):
            self.matrix[x][y].value = 2 #NOTE: 2 stands for user owner
            self.matrix[x][y].type = Object.type 
            Object.x = x
            Object.y = y
        else:
            print("This space is ocupied")
    
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

    def start(self, id, price , owner = "Computer"):
        print('Cafe is opened!')
        self.type = id
        self.owner = owner
        self.price = price
        self.x = 0
        self.y = 0
        self.spendings,self.max_entrance = Cafe.get_type(id)
        print(self.owner, id, self.price)
        Cafe.cafe_count +=1

def draw(Object):
    if Object.val  == 1:
        #TODO draw compture building
        if Object.type == 0:
            #TODO draw computer small
    if Object.val == 2:
        #TODO draw user building

cafes_a = [Cafe() for i in range(random.randint(0, 3))]
for i in cafes_a:
    i.start(1, random.randint(25, 35))
print(cafes_a)
cafe_b = Cafe()
cafe_b.start(0, random.randint(15, 25))
print(cafe_b.cafe_count)
cafe_с = Cafe()
cafe_с.start(2, random.randint(30, 45))
print(cafe_с.cafe_count)

map = Mapper(4)
map.addObject(cafe_b)


for i in range(map.size):
    for j in range(map.size):
        draw(map[i][j])