class Store:
    def __init__(self, emps, slots) -> None:
        self.emps = emps
        self.slots = slots

class Employee:
    def __init__(self) -> None:
        pass

game = Store([1])
print(game.emps)