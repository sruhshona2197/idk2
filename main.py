# 1
class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def start(self):
        return f"Timer boshlandi: {self.seconds}s"

t = Timer(10)
print(t.start())

# 2
class Playlist:
    def __init__(self, count):
        self.count = count

    def info(self):
        return f"Playlistda {self.count} ta qo‘shiq bor"
p = Playlist(15)
print(p.info())

# 3
class Ticket:
    def __init__(self, price, is_paid):
        self.price = price
        self.is_paid = is_paid

    def check(self):
        if self.is_paid:
            return "To‘langan"
        else:
            return "To‘lanmagan"
t = Ticket(50000, True)
print(t.check())


# 4
class Chat:
    def __init__(self, user):
        self.user = user

    def enter(self):
        return f"{self.user} chatga kirdi"


chat = Chat("Ali")
print(chat.enter())

5
class Game:
    def __init__(self, level):
        self.level = level

    def start(self):
        return f"{self.level}-level boshlandi"

game = Game(1)
print(game.start())
