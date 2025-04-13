class Animal:
    alive: list = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        result = ""
        result += (f"{"{Name: " + self.name}, "
                   f"Health: {self.health}, "
                   f"Hidden: {str(self.hidden) + "}"}")
        return result


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(animal: Animal) -> None:
        if not animal.hidden and not isinstance(animal, Carnivore):
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
