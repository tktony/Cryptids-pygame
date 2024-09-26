# Cryptids

## Demo:
https://github.com/user-attachments/assets/1036e72d-b9f0-43c8-ab01-fc118ecd1693


# Pygame RPG Project - Cryptids
#### Don't ask me why I named it Cryptids 😅

## Overview
This project is a 2D RPG game developed using Pygame, featuring player control, combat mechanics, and an upgrade system. Players can navigate through a world, interact with enemies, cast spells, and upgrade their stats.

## Features
- **Player Movement**: Control the player using keyboard inputs for directional movement.
- **Combat System**: Engage in melee attacks and cast spells with cooldowns.
- **Magic and Weapons**: Switch between various weapons and magic spells.
- **Stat Management**: Upgrade player stats such as health, energy, attack, magic, and speed.
- **User Interface**: Display health, energy, experience, and selected weapon/magic in the UI.

## Usage
To run the game, simply execute the `.exe` file.

### Controls
- **Movement**: Use the arrow keys to move the player.
- **Attack**: Press `Space` to perform a melee attack.
- **Magic**: Press `Ctrl` to cast the currently selected spell.
- **Switch Weapons**: Press `Q` to cycle through available weapons.
- **Switch Magic**: Press `E` to cycle through available magic spells.

## Game Mechanics

### Player Class
The `Player` class handles the player's stats, movements, and actions. Key attributes include:
- **Stats**: Health, energy, attack, magic, speed.
- **Magic**: Different types of magic spells with varying strengths and costs.
- **Weapons**: Various weapons with different cooldowns and damage.

### UI Class
The `UI` class is responsible for displaying player stats, experience, and the currently selected weapon/magic on the screen.

### Upgrade System
Players can upgrade their stats using experience points, enhancing their combat capabilities.

## Assets
- Graphics and audio assets are stored in the `graphics` and `audio` directories, respectively.
- CSV files for level layouts can be found in the `map` directory.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
