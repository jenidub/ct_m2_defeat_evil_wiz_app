# Defeat the Evil Wizard

Welcome to **Defeat the Evil Wizard**
A text-based RPG game where players battle against the formidable Dark Wizard in a turn-based combat system. Choose your character, strategize your moves, and unleash powerful abilities to emerge victorious!

## Features
- **Four unique classes**: Warrior, Mage, Archer, and Paladin.
- Turn-based combat with options to attack, heal, or use special abilities.
- Dynamic gameplay with randomized damage and healing effects.
- ASCII art for victory and defeat.

## How to Play
1. Clone or download this repository.
2. Ensure you have Python installed on your system (Python 3.6 or higher is recommended).
3. Run the game using the command:
   ```bash
   python3 defeat_evil_wizard_jw.py
   ```

4. Follow the on-screen instructions to:
   - Choose your character class.
   - Name your character.
   - Battle the Evil Wizard by selecting from various actions in each turn.

## Game Mechanics
### Character Classes
Each class has unique stats and abilities:
- **Warrior**: High health and balanced attack power.
  - Special abilities: Power Attack (offensive), Duck Defense (defensive).
- **Mage**: Low health but high attack power.
  - Special abilities: Cast Spell (offensive), Restore Spell (defensive).
- **Archer**: High health and attack power.
  - Special abilities: Quick Shot (offensive), Evade Attack (defensive).
- **Paladin**: Balanced health and attack power with holy-themed abilities.
  - Special abilities: Holy Strike (offensive), Divine Shield (defensive).

### Combat Options
During each turn, players can:
1. **Attack**: Deal randomized damage to the opponent.
2. **Use Special Ability**: Leverage unique class-based powers (limited turns).
3. **Heal**: Restore health (limited turns).
4. **View Stats**: Check the health and attack power of both characters.

### Victory & Defeat
- Defeat the Evil Wizard by reducing its health to zero or lose if your character's health drops to zero.

## Development Notes
### Code Structure
The game includes:
- **Classes**:
  - `Character`: Base class for all characters.
  - `Warrior`, `Mage`, `Archer`, `Paladin`: Player classes with specialized methods.
  - `EvilWizard`: The final boss with its own abilities.

- **Functions**:
  - `create_character()`: Handles player character creation.
  - `battle()`: Core turn-based combat loop.
  - `main()`: Game entry point.

### Randomization
- Randomized damage and healing values create replayability.
- Special attack multipliers enhance strategic decisions.

## Credits
- Created by **JeniDub** as the Module 2 project for **Coding Temple**
- README file created using **ChatGPT** with edits by **JeniDub**

## License
This project is licensed under the MIT License. Feel free to modify and distribute the game.

Enjoy the adventure and defeat the Evil Wizard!
