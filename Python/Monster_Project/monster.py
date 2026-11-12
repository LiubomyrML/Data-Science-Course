class Monster(object):
    def __init__(self, name: str, health: int = 30,  level: int = 1, strength: int = 3, energy = 20, max_health: int = 30, max_energy = 20.):
        self.name = name
        self.level = level
        self.strength = strength

        self.max_health = max_health
        self.health = min(health, max_health)

        self.max_energy = max_energy
        self.energy = min(energy, max_energy)

    def get_status(self):
        ...

    def train(self):
        ...

    def rest(self):
        ...

    def battle_a_monster(self):
        ...

    def quit(self):
        ...


monsters = [
    Monster("Blob"),
    Monster("Ember", health=40, energy=25, level=3, strength=6),
    Monster("Frostfang", health=20, energy=10, level=1, strength=2),
]

for monster in monsters:
    print(
        f"{monster.name}: "
        f"health={monster.health}/{monster.max_health}, "
        f"energy={monster.energy}/{monster.max_energy}, "
        f"level={monster.level}, strength={monster.strength}"
    )