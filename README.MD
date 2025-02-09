# AmericaLocker

[Project Description](#project-description) - [Key Features](#key-features) - [Tech Stack](#technology-stack) - [Installation Instructions](#installation-instructions) - [Credits](#credits)

![Screenshot](image.png)

## Project Description

This is a program that locks a user's computer and displays a joke message about election interference. The project was created for humorous purposes and is not intended for actual malicious use. The program displays text that accuses the user of participating in the 2024 US election and requires the user to fulfill mock conditions to unlock the computer.

## Key Features

- **Displays a funny message about locking your computer.**
- **Mentions fictional offences, such as voting multiple times for different candidates and attempted hacking via Minecraft.**
- **Requires the user to fulfill humorous conditions for unlocking (write to Telegram, send a mug photo, etc.).**

## Tech Stack

**Programming Language:** Python 3

**Libraries:**

- pygame or other libraries for displaying text (if applicable)
- os or sys for system-level operations

**Tools:**

- **IDE/Editor:** PyCharm
- **Version Control:** Git

**Platform:** Windows

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/pie-with-jam/AmericaLocker.git
   ```

2. Navigate into the project directory:
   ```bash
   cd AmericaLocker
   ```

3. Activate a virtual environment:
   ```bash
   .venv\Scripts\activate
   ```

4. Build the executable using PyInstaller:
   ```bash
   pyinstaller .\AmericaLocker.spec
   ```

   This will create a standalone executable that you can run without needing to install Python.

## Credits

Special thanks to [EZIKALEXANDR](https://github.com/EZIKALEXANDR), the foundational inspiration behind this project. Without their pioneering work and ideas, this project would not have been possible.