KNIGHTS = [
    {
        "name": "Lancelot",
        "max_hp": 80,
        "hp": 80,
        "armor": 20,
        "weapon": 45
    },
    {
        "name": "King Arthur",
        "max_hp": 100,
        "hp": 100,
        "armor": 30,
        "weapon": 35
    }
]


class Knight:

    knights_in_game = 0

    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.max_hp = kwargs["max_hp"]
        self.hp = kwargs["hp"]
        self.armor = kwargs["armor"]
        self.weapon = kwargs["weapon"]
        self.guarding = False
        self.alive = True
        Knight.knights_in_game += 1

    def attack(self, opponent):
        if self.guarding:
            self.guarding = False
            self.armor -= 10
            print(f"{self.name} опускає щит")

        print(f"{self.name} наносить удар.")

        damage = opponent.armor - self.weapon
        opponent.hp += damage
        if opponent.hp <= 0:
            print(f"{opponent.name} впав з коня. Це кінець для нього!")
            opponent.alive = False
            return
        print(f"{opponent.name} отримав {damage} шкоди, і зараз має {opponent.hp}ХП")

    @classmethod  # декоратор
    def amount(cls):
        print("У грі на даний момент", cls.knights_in_game, "лицарів")

    @staticmethod
    def heal(knights, health):
        print("_____________________")
        for knight in knights:
            knight.hp += health
            if knight.hp > knight.max_hp:
                knight.hp = knight.max_hp
                print(f"{knight.name} випив зілля здоров'я і повністю одужав")
            else:
                print(f"{knight.name} випив зілля здоров'я і відновив {health} очків здоров'я")
            knight.alive = True
        print("_____________________")

    @staticmethod
    def guard(knights, id):
        print("---------------------")

        knight = knights[id]

        if not knight.guarding:
            knight.armor += 10
            knight.guarding = True
            print(f"{knight.name} піднімає щит")
        else:
            print(f"{knight.name} знову блокує")

        print("---------------------")




def prepare(knights):
    return [Knight(**i) for i in knights]


def battle(knights):
    knights[0].attack(knights[1])
    knights[1].attack(knights[0])


Knight.amount()
pair = prepare(KNIGHTS)
Knight.guard(pair, 1)
battle(pair)  # round 1
Knight.heal(pair, 10)
battle(pair)  # round 2
Knight.amount()
