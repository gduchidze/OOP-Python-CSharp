class Ticket:
    def __init__(self, movie_name, ticket_price, num_tickets, language='Geo'):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.num_tickets = num_tickets
        self.language = language

    def __str__(self):
        return f"ფილმის სახელი: {self.movie_name}, ბილეთის ფასი: {self.ticket_price}, რაოდენობა: {self.num_tickets}, ენა: {self.language}"

    def __eq__(self, other):
        if isinstance(other, Ticket):
            return self.num_tickets == other.num_tickets
        elif isinstance(other, int):
            return self.num_tickets == other
        else:
            return NotImplemented


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"სახელი: {self.name}, ბალანსი: {self.balance}"

    def purchase_ticket(self, ticket, num_tickets):
        if num_tickets <= ticket.num_tickets and num_tickets * ticket.ticket_price <= self.balance:
            ticket.num_tickets -= num_tickets
            self.balance -= num_tickets * ticket.ticket_price
            print(f"თქვენ იყიდეთ {num_tickets} ბილეთი")
        else:
            if num_tickets > ticket.num_tickets:
                print("არარის საკმარისი ბილეთი.")
            else:
                print("არარის საკმარისი თანხა ბალანსზე.")

    def deposit(self, amount):
        self.balance += amount

t1 = Ticket("ქალის სურნელი", 10, 5, 'ENG')
t2 = Ticket("ნათლია", 12, 7)
u1 = User("ლევანი", 50)
u2 = User("ზურა", 20)
print(t1)
print(t2)
u1.purchase_ticket(t1, 2)
u1.deposit(30)
print(u1)
print(t1 == t2)
print(t1 == 5)
print(t1 == 5)
