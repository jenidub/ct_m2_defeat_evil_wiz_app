import math
import random

# *** START of CHARACTER CREATION FUNCTIONALITY *** # 
## BASE CHARACTER CLASS ##
class Character:
    # Basic Character Info
    def __init__(self, name, health, attack_power, health_lost=0):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.health_lost = health_lost #Store the last amount of health lost for evade/heal methods
        self.attack_occurred = False

    # Attack Method
    def attack(self, opponent):
        self.health_lost = self.attack_power
        opponent.health -= self.attack_power
        self.attack_occurred = True
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if type(self).__name__ == "EvilWizard":
            print(f"Current Stats: {opponent.name} - {opponent.health} vs. {self.name} - {self.health}\n")

    # Heal Method
    def heal(self):
        healing_amount = random.randint(1, (self.max_health - self.health))
        self.health += healing_amount
        print(f"You have healed yourself by {healing_amount} and your current health level is {self.health}")

    # Special Attack Power Random Multiplier
    def special_attack_multiplier(self):
        multiplier = math.ceil(random.random() * random.randint(1,3))
        print("multiplier: ", multiplier)
        return multiplier
    
    # Display the current stats 
    def display_stats(self):
        print("\n************")
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        print("************\n")
        

## CHARACTER CHILD CLASSES ##
# Warrior class (Inherited from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    def special_abilities(self, opponent):
        ability_choice = input("Which ability would you like to use? 1 - Power Attack | 2 - Duck Defense  ")
        if (ability_choice == "1"):
            self.power_attack(opponent)
        elif (ability_choice == "2"):
            self.duck_defense()

    # Power Attack Method
    def power_attack(self, opponent):
        print("In power attack mode...")
        special_attack_damage = self.attack_power * self.special_attack_multiplier()
        opponent.health -=  special_attack_damage
        print(f"{self.name} uses the Power Attack against {opponent.name} for {special_attack_damage} damage!")
        
    def duck_defense(self):
        print("In duck defense mode...")
        if (self.attack_occurred):
            self.health += self.health_lost
            self.attack_occurred = False

# Mage class (Inherited from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    def special_abilities(self, opponent):
        ability_choice = input("Which ability would you like to use? 1 - Cast Spell | 2 - Restore Spell  ")
        if (ability_choice == "1"):
            self.cast_spell(opponent)
        elif (ability_choice == "2"):
            self.restore_spell()

    # Add your cast spell method here
    def cast_spell(self, opponent):
        special_attack_damage = self.attack_power * self.special_attack_multiplier()
        opponent.health -=  special_attack_damage
        print(f"{self.name} uses the Cast Spell against {opponent.name} for {special_attack_damage} damage!")
        
    def restore_spell(self):
        if (self.attack_occurred):
            self.health += self.health_lost
            self.attack_occurred = False

# Archer class (Inherited from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=40)  # Boost attack power

    def special_abilities(self, opponent):
        ability_choice = input("Which ability would you like to use? 1 - Quick Shot | 2 - Evade Attack  ")
        if (ability_choice == "1"):
            self.quick_shot(opponent)
        elif (ability_choice == "2"):
            self.evade_attack()

    def quick_shot(self, opponent):
        special_attack_damage = self.attack_power * self.special_attack_multiplier()
        opponent.health -=  special_attack_damage
        print(f"{self.name} uses the Quick Shot against {opponent.name} for {special_attack_damage} damage!")

    def evade_attack(self):
        if (self.attack_occurred):
            self.health += self.health_lost
            self.attack_occurred = False

# Paladin class (Inherited from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=25)

    def special_abilities(self, opponent):
        ability_choice = input("Which ability would you like to use? 1 - Holy Strike | 2 - Divine Shield  ")
        if (ability_choice == "1"):
            self.holy_strike(opponent)
        elif (ability_choice == "2"):
            self.divine_shield()

    def holy_strike(self, opponent):
        special_attack_damage = self.attack_power * self.special_attack_multiplier()
        opponent.health -=  special_attack_damage
        print(f"{self.name} uses the Holy Strike against {opponent.name} for {special_attack_damage} damage!")

    def divine_shield(self):
        self.health += self.health_lost
        self.attack_occurred = False

## VILLAIN CHARACTER CLASS ##
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# *** END of CHARACTER CREATION FUNCTIONALITY *** # 

# *** START of GAME FUNCTIONALITY *** #
## CREATE CHARACTER METHOD ##
# Function to create player character based on user input
def create_character():
    print("\nChoose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("\nEnter the number of your class choice: ")
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

## BATTLE FUNCTION METHOD ##
# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")
        print("\n")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_abilities(wizard)
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

    if wizard.health <= 0 or player.health <= 0:
        print("\n*********************")
        if (wizard.health <= 0):
            print(f"{wizard.name} has been defeated by {player.name}!")
        else:
            print(f"{player.name} has been defeated by {wizard.name}!")
        print("Thank you for playing the Defeat the Evil Wizard by JeniDub")
        print("*********************\n")

## MAIN GAME FUNCTION ##
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
