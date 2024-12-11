import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, special_attack_name, special_attack_multiplier):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.special_attack_name = special_attack_name
        self.special_attack_multiplier = special_attack_multiplier
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        damage_amount = random.randint(1, self.attack_power)
        opponent.health -= damage_amount
        print(f"{self.name} attacks {opponent.name} for {damage_amount} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special_attack(self, opponent):
        special_attack_damage = self.attack_power * self.special_attack_multiplier
        opponent.health -=  special_attack_damage
        print(f"{self.name} uses {self.special_attack_name} against {opponent.name} for {special_attack_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!") 

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self):
        healing_amount = random.randint(1, (self.max_health - self.health))
        self.health += healing_amount
        print(f"You have healed yourself by {healing_amount} and your current health level is {self.health}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, special_attack_name="Power Attack", special_attack_multiplier = 1.5)  # Boost health and attack power

    # Add your power attack method here
    # Inherited from parent Character class - special_attack()
    
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, special_attack_name="Cast Spell", special_attack_multiplier = 2)  # Boost attack power

    # Add your cast spell method here
    # Inherited from parent Character class - special_attack()

## TWO ADDITIONAL CLASSES ##
# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=40, special_attack_name="Quick Shot", special_attack_multiplier = 2.5)  # Boost attack power

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=25, special_attack_name="Holy Strike", special_attack_multiplier = 4)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, special_attack_name="", special_attack_multiplier=1)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_attack(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()
