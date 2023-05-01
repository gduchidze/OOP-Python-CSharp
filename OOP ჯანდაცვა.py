class Insurance:
    def __init__(self, name, operation_price, num_operations, country="France"):
        self.__name = name
        self.operation_price = operation_price
        self.num_operations = num_operations
        self.country = country

    def __str__(self):
        return f"დაზიანება: {self.__name}, ქვეყანა: {self.country}"

    def __eq__(self, other):
        if isinstance(other, Insurance):
            return self.operation_price == other.operation_price
        elif isinstance(other, int):
            return self.operation_price == other
        else:
            return NotImplemented

class User:
    def __init__(self, name, balance):
        self.__name = name
        self.account_amount = balance

    def __str__(self):
        return f"მომხმარებელი: {self.__name},  თანხა ანგარიშზე {self.account_amount}"

    def funding_request(self, insurance, num_operations):
        funding_needed = insurance.operation_price * num_operations
        if funding_needed > self.account_amount:
            print(f"თქვენ დაგიფინანსდათ {num_operations} ოპერაცია სრულიად")

        elif num_operations > 3:
            print("თქვენი მოთხოვნა უარყოფილია , ერთ მომხმარებელს მხოლოდ 3 ოპერაცია უფინანსდება")
        else:

            print(f"თქვენი მოთხოვნა უარყოფილია , საკმარისი თანხა გაქვთ ოპერაციის დასაფინანსებლად")

    def change(self, amount):
        self.account_amount += amount



ins1 = Insurance("ფეხის ოპერაცია", 50000, 2)
ins2 = Insurance("გულის შეტევა", 100000, 1, "Denmark")
user1 = User("პოლ პოგბა", 260000)
user2 = User("კრისტიან ერიქსენი", 150000)

print(ins1)
print(user1)
user1.funding_request(ins1, 2)
user1.change(5000000)
print(user1)

print(ins2)
print(user2)
user2.funding_request(ins2, 2)






print(ins1 == ins2)
print(ins1 == 5000)





