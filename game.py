from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Lung"

def battle(hero: enemy,Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Bubbles")
    hero = hero("Bubbles the great")


    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{hero.name} enters the arena with {hero.health} health.")

    goblin = Goblin("Gribble")

    print(f"{hero.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")

    print(f"{hero.name}) swings...")
    heroDamage = hero.attack()
    goblin.take_damage(heroDamage)

    print(f"{goblin.name}) swings...")
    goblinDamage = goblin.attack()
    hero.take_damage(goblinDamage)

    print("{goblin.name}")

if __name__ == "__main__":
    main()
