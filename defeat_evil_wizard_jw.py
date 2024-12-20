import math
import random

# *** END GAME ASCII ART *** #
win_ascii = '''
 __    __    _____     ____   ________     ____     ______    __      __
 ) )  ( (   (_   _)   / ___) (___  ___)   / __ \   (   __ \   ) \    / (
( (    ) )    | |    / /         ) )     / /  \ \   ) (__) )   \ \  / / 
 \ \  / /     | |   ( (         ( (     ( ()  () ) (    __/     \ \/ /  
  \ \/ /      | |   ( (          ) )    ( ()  () )  ) \ \  _     \  /    
   \  /      _| |__  \ \___     ( (      \ \__/ /  ( ( \ \_))     )(    
    \/      /_____(   \____)    /__\      \____/    )_) \__/     /__\                                                                                                                               
'''

loss_ascii = '''
__      __    ____     __    __                   
) \    / (   / __ \    ) )  ( (                   
 \ \  / /   / /  \ \  ( (    ) )                  
  \ \/ /   ( ()  () )  ) )  ( (                   
   \  /    ( ()  () ) ( (    ) )                  
    )(      \ \__/ /   ) \__/ (                   
   /__\      \____/    \______/                   
                                                  
 _____         ____      _____   ________  _______
(_   _)       / __ \    / ____\ (___  ___) \     /
  | |        / /  \ \  ( (___       ) )     \   / 
  | |       ( ()  () )  \___ \     ( (       ) (  
  | |   __  ( ()  () )      ) )     ) )      \_/  
__| |___) )  \ \__/ /   ___/ /     ( (        _   
\________/    \____/   /____/      /__\      (_)  
'''

# *** START of CHARACTER CREATION FUNCTIONALITY *** # 
## BASE CHARACTER CLASS ##
class Character:
    # Basic Character Info
    def __init__(self, name, health, attack_power, health_lost=0, healing_turns=3, special_attack_turns=4):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.special_attack_turns = special_attack_turns # Limited number of Special Attack turns
        self.healing_turns = healing_turns # Limited number of Healing turns 
        self.max_health = health  # Store the original health for maximum limit
        self.health_lost = health_lost #Store the last amount of health lost for evade/heal methods
        self.attack_occurred = False

    # Attack Method - Player will attack with a random amount 
    # of damage between 1 and the character's attack_power
    def attack(self, opponent):
        damage_done = math.ceil(self.attack_power * (random.random()))
        self.health_lost = damage_done
        opponent.health -= damage_done
        self.attack_occurred = True
        print(f"{self.name} attacks {opponent.name} for {damage_done} damage!")
        if type(self).__name__ == "EvilWizard":
            print(f"Current Stats: {opponent.name} - {opponent.health} vs. {self.name} - {self.health}\n")

    # Heal Method - Player will heal themselves in a random amount between
    # 1 and the difference between the player's max health and their current health
    def heal(self):
        if self.healing_turns > 0:
            healing_amount = random.randint(1, (self.max_health - self.health))
            self.health += healing_amount
            print(f"You have healed yourself by {healing_amount} and your current health level is {self.health}")
            self.healing_turns -= 1
            print(f"** You now have {self.healing_turns} healing packs remaining. Use them wisely! **\n")
        else:
            print("You are out of healing turns. Returning to the main menu...\n")

    # Special Attack Power Random Multiplier Helper Method
    # Randomly select a multiplier for the attack_power between 1-3x
    def special_attack_multiplier(self):
        multiplier = math.ceil(random.random() * random.randint(1,3))
        return multiplier
    
    # Display Stats Method - Show the current stats for both the player and their opponent
    # so that the player can make decisions about their next action
    def display_stats(self, opponent):
        print("\n************")
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        print(f"{opponent.name}'s Stats - Health: {opponent.health}/{opponent.max_health}, Attack Power: {opponent.attack_power}")
        print("************\n")
        

## CHARACTER CHILD CLASSES ##
# Warrior class (Inherited from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Special Abilities Method - Allow the player to select the special ability
    # they want to use if they have special attacks available and run the matching method
    def special_abilities(self, opponent):
        if self.special_attack_turns > 0:
            ability_choice = input("Which ability would you like to use? 1 - Power Attack | 2 - Duck Defense  ")
            if (ability_choice == "1"):
                self.power_attack(opponent)
                self.special_attack_turns -= 1
                print(f"** You now have {self.special_attack_turns} special attacks remaining. Use them wisely! **\n")

            elif (ability_choice == "2"):
                self.duck_defense()
                self.special_attack_turns -= 1
                print(f"** You now have {self.special_attack_turns} special attacks remaining. Use them wisely! **\n")
            else:
                print("Invalid choice. Returning to the main menu...")
        else:
            print("You are out of special attack turns. Returning to main menu...\n")
    
    # Power Attack Special Ability Method - Offensive
    def power_attack(self, opponent):
        special_attack_damage = self.attack_power * self.special_attack_multiplier()
        opponent.health -=  special_attack_damage
        print(f"{self.name} uses the Power Attack against {opponent.name} for {special_attack_damage} damage!")

    # Duck Defense Special Ability Method - Defensive
    def duck_defense(self):
        if (self.attack_occurred):
            self.health += self.health_lost
            self.attack_occurred = False

# Mage class (Inherited from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    # Special Abilities Method - Allow the player to select the special ability
    # they want to use if they have special attacks available and run the matching method
    def special_abilities(self, opponent):
        if self.special_attack_turns > 0:
            ability_choice = input("Which ability would you like to use? 1 - Cast Spell | 2 - Restore Spell  ")
            if (ability_choice == "1"):
                self.cast_spell(opponent)
                self.special_attack_turns -= 1
            elif (ability_choice == "2"):
                self.restore_spell()
                self.special_attack_turns -= 1
            else:
                print("Invalid choice. Returning to the main menu...\n")
            
            print(f"** You now have {self.special_attack_turns} special attacks remaining. Use them wisely! **\n")
        else:
            print("You are out of special attack turns. Returning to main menu...\n")
            
    # Cast Spell Special Ability Method - Offensive
    def cast_spell(self, opponent):
        special_attack_damage = self.attack_power * self.special_attack_multiplier()
        opponent.health -=  special_attack_damage
        print(f"{self.name} uses the Cast Spell against {opponent.name} for {special_attack_damage} damage!")
    
    # Restore Spell Special Ability Method - Defensive  
    def restore_spell(self):
        if (self.attack_occurred):
            self.health += self.health_lost
            self.attack_occurred = False

# Archer class (Inherited from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=40)  # Boost attack power

    # Special Abilities Method - Allow the player to select the special ability
    # they want to use if they have special attacks available and run the matching method
    def special_abilities(self, opponent):
        if self.special_attack_turns > 0:
            ability_choice = input("Which ability would you like to use? 1 - Quick Shot | 2 - Evade Attack  ")
            if (ability_choice == "1"):
                self.quick_shot(opponent)
                self.special_attack_turns -= 1
            elif (ability_choice == "2"):
                self.evade_attack()
                self.special_attack_turns -= 1
            else:
                print("Invalid choice. Returning to the main menu...")
            
            print(f"** You now have {self.special_attack_turns} special attacks remaining. Use them wisely! **\n")
        
        else:
            print("You are out of special attack turns. Returning to main menu...\n")

    # Quick Shot Special Ability Method - Offensive
    def quick_shot(self, opponent):
        special_attack_damage = self.attack_power * self.special_attack_multiplier()
        opponent.health -=  special_attack_damage
        print(f"{self.name} uses the Quick Shot against {opponent.name} for {special_attack_damage} damage!\n")

    # Evade Special Ability Method - Defensive
    def evade_attack(self):
        if (self.attack_occurred):
            self.health += self.health_lost
            self.attack_occurred = False

# Paladin class (Inherited from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=25)

    # Special Abilities Method - Allow the player to select the special ability
    # they want to use if they have special attacks available and run the matching method
    def special_abilities(self, opponent):
        if self.special_attack_turns > 0:
            ability_choice = input("Which ability would you like to use? 1 - Holy Strike | 2 - Divine Shield  ")
            if (ability_choice == "1"):
                self.holy_strike(opponent)
                self.special_attack_turns -= 1
            elif (ability_choice == "2"):
                self.divine_shield()
                self.special_attack_turns -= 1
            else:
                print("Invalid choice. Returning to the main menu...\n")
            print(f"** You now have {self.special_attack_turns} special attacks remaining. Use them wisely! **\n")
        else:
            print("You are out of special attack turns. Returning to main menu...\n")        

    # Holy Strike Special Ability Method - Offensive
    def holy_strike(self, opponent):
        special_attack_damage = self.attack_power * self.special_attack_multiplier()
        opponent.health -=  special_attack_damage
        print(f"{self.name} uses the Holy Strike against {opponent.name} for {special_attack_damage} damage!")

    # Divine Shield Special Ability Method - Defensive
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
        if self.health <= self.max_health - 5:
            self.health += 5  # Lower regeneration amount
            print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        else:
            print(f"{self.name} is at their max health of {self.max_health}. Here they come... \n")

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
            player.display_stats(wizard)
            continue
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

    # End Game Messages - Displays the appropriate message for the player
    # win or opponent win with ASCII art and a message set
    if wizard.health <= 0 or player.health <= 0:
        print("\n*********************")
        if (wizard.health <= 0):
            print(win_ascii)
            print(f"{wizard.name} has been defeated by {player.name}!")
        else:
            print(loss_ascii)
            print(f"OH NO! {player.name} has been defeated by {wizard.name}!")
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
