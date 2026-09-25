import random

class Hero:
    """A playable character who battles enemies in the arena."""

    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack_power = 25

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(1, self.attack_power)
    
    def take_damage(self, damage):
        """Reduce health without allowing it to fail below zero."""
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
            
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0 