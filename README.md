# 🎲 Robust Command-Line Dice Rolling Game in Python

This is a fun and interactive command-line dice rolling game built with Python. The player gets three chances to guess a number between 1 and 6.

This project is an excellent exercise for beginners and demonstrates several core programming concepts, including loops, conditional statements, random number generation, and robust **error handling**.

---

### ✨ Features

-   **Interactive Gameplay:** A simple and engaging command-line interface.
-   **Three Chances:** The player gets three attempts to guess the correct number.
-   **Random Dice Roll:** Powered by the **NumPy** library for efficient random number generation.
-   **"Rolling" Animation:** Uses the `time` and `sys` libraries to create a simple animation for a better user experience.
-   **Robust Error Handling:**
    -   Handles non-numeric inputs gracefully using a `try-except` block, preventing crashes.
    -   Validates that the user's input is within the valid range (1-6).

---

### 🛠️ Technologies Used

-   **Python 3**
-   **NumPy**

---

### 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Install the necessary dependencies:**
    Make sure you have Python 3 installed. Then, install NumPy using pip.
    ```bash
    pip install numpy
    ```

3.  **Execute the script:**
    Run the game from your terminal.
    ```bash
    python dice_game.py
    ```

---

### 🎮 Gameplay Example

```text
--- Welcome to Dice Rolling Game ---

--- You have 3 chances to guess the correct number between 1 and 6 ---

Chance 1: Enter your number between 1 & 6 : hello
Invalid input! Please enter a number.

Chance 2: Enter your number between 1 & 6 : 8
Number must be between 1 and 6. You lost a chance.

Chance 3: Enter your number between 1 & 6 : 4
--- Rolling the Dice ---
.....
Dice Shows: 4
Congratulations ! Aap jeet gaye !!
```# Python-Dice-Game-V2
