# Basketball Team Stats Tool 🏀

A Python-based data cleaning and analysis project that organizes raw player data into balanced basketball teams, computes descriptive statistics, and provides an interactive CLI for exploring results.

## 📌 Project Overview

This project demonstrates key **data science concepts** such as:

* **Data cleaning**: Transforming raw string-based attributes (height, experience, guardians) into structured data.
* **Feature engineering**: Creating new attributes (boolean experience, numeric height, list of guardians).
* **Data analysis**: Computing descriptive statistics per team (counts, averages, distributions).
* **Data presentation**: Delivering results through a user-friendly command-line menu.

The script reads player and team data from `constants.py`, cleans and transforms the data, assigns players fairly to teams, and displays descriptive team stats interactively.

---

## ⚙️ Features

* **Data Cleaning**

  * Converts height strings (e.g., `"42 inches"`) into integers.
  * Transforms experience flags ("YES"/"NO") into booleans.
  * Splits guardian strings into lists of names.
  * Creates a new cleaned player dataset without mutating the original data.

* **Team Balancing**

  * Players are distributed evenly across teams.
  * Equal balance of experienced vs. inexperienced players.
  * Teams are internally sorted by player height.

* **Descriptive Statistics**

  * Total number of players.
  * Number of experienced vs. inexperienced players.
  * Average player height.
  * Player roster (organized by height).
  * Guardians list.

* **Interactive CLI**

  * Main menu with options to:

    * Display team stats.
    * Quit the program.
  * Submenu prompts for team selection (Panthers, Bandits, Warriors).
  * User can explore stats repeatedly until they choose to exit.

---

## 🗂️ File Structure

```
project/
│── app.py          # Main program logic
│── constants.py    # Raw player and team data
│── README.md       # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed.
* Terminal or command prompt.

### Running the Program

1. Clone or download this repository.

2. Open a terminal in the project folder.

3. Run the script:

   ```bash
   python app.py
   ```

4. Use the interactive menu to explore team statistics.

---

## 📊 Example Output

```
BASKETBALL TEAM STATS TOOL

---- MENU----
Here are your choices:
 A) Display Team Stats
 B) Quit

Enter an option: A

A) Panthers
B) Bandits
C) Warriors

Enter an option: A

Team Panthers Stats
--------------------
Total players: 6
Total experienced: 3
Total inexperienced: 3
Average height: 42.7

Players on Team:
  Joe Smith, Jane Doe, ...

Guardians:
  Alice Smith, Bob Doe, ...
```

---

## 🔬 Data Science Connections

This project mirrors a real-world **data science workflow**:

1. **Data Acquisition**

   * Importing raw, inconsistent player data from `constants.py`.

2. **Data Cleaning**

   * Converting categorical and textual fields into structured formats.
   * Removing ambiguous formatting (e.g., splitting guardian strings).

3. **Feature Engineering**

   * Creating derived attributes (boolean experience, integer heights).

4. **Exploratory Data Analysis (EDA)**

   * Computing descriptive stats such as counts and averages.
   * Summarizing datasets by subgroups (teams).

5. **Data Presentation**

   * Displaying findings through an interactive, text-based dashboard.

---

## ✅ Rubric Checklist

* **Script filename**: `app.py` provided ✅
* **Use provided data**: Imports and cleans `constants.py` ✅
* **Script execution**: Handles exceptions gracefully ✅
* **Proper Dunder Main usage**: Execution logic inside `if __name__ == "__main__":` ✅
* **Clean up data**: Height → int, Experience → bool, Guardians → list ✅
* **Avoid altering imported data**: Uses `clean_players` structure ✅
* **Team balancing**: Ensures fairness and equal distribution ✅
* **Menu creation**: Interactive CLI with looping menu ✅
* **Display stats**: Full descriptive team statistics with readable formatting ✅

---

## 🧩 Possible Extensions

* Add data visualization with **matplotlib** or **seaborn**.
* Export cleaned data and stats to **CSV/JSON** for further analysis.
* Build a **dashboard** with Flask, Dash, or Streamlit for interactive exploration.
* Extend balancing logic to optimize by additional features (e.g., height distribution fairness).

---

## 📖 License

This project is provided for educational purposes as part of a data science–focused coding exercise.

---