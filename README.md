
# Multiplication Table Generator — Day 6

## 📌 Project Overview
This is a beginner-friendly Python program that generates a multiplication table based on a number and a limit entered by the user.

## 🎯 Objectives
- Practice Python `for` loops.
- Understand the `range()` function.
- Accept user input and convert it into integers.
- Display multiplication results using f-strings.

## 🛠️ Technologies Used
- Python 3
- Visual Studio Code

## 📂 Project Structure
```text
Day6-Multiplication-Table/
├── multiplication_table.py
└── README.md
```

## 💻 Source Code
```python
user_input = int(input("Enter a number: "))

user_limit = int(input("Enter number till where you need: "))

for i in range(1, user_limit + 1):
    print(f"{user_input} * {i} = {user_input * i}")
```

## ⚙️ How It Works
1. The program asks the user to enter a number.
2. It asks for the multiplication table limit.
3. The `int()` function converts both inputs into integers.
4. The `for` loop repeats from 1 up to the specified limit.
5. The `range(1, user_limit + 1)` expression includes the final limit.
6. The program multiplies the entered number by each loop value.
7. An f-string displays each multiplication equation clearly.

## ▶️ How to Run
1. Install Python 3.
2. Save the code in `multiplication_table.py`.
3. Open the terminal in the project folder.
4. Run the command:

```bash
python multiplication_table.py
```

On Windows, you can also use:

```bash
py multiplication_table.py
```

## 🧪 Sample Output
Example input: Number = 5, Limit = 10

```text
Enter a number: 5
Enter number till where you need: 10
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
```

## ✅ Test Cases

| Number | Limit | Expected Result |
|---|---:|---|
| 5 | 10 | Table of 5 from 5 × 1 to 5 × 10 |
| 7 | 5 | Table of 7 from 7 × 1 to 7 × 5 |
| 12 | 3 | Results: 12, 24, 36 |

## 📚 Concepts Learned
- Variables
- User input using `input()`
- Type conversion using `int()`
- `for` loops
- `range()` function
- Multiplication operator (`*`)
- Formatted strings (f-strings)

## ⚠️ Limitations
- The program expects integer inputs.
- Non-numeric input causes a `ValueError`.
- A zero or negative limit produces no multiplication table rows.

## 🚀 Future Improvements
- Validate the table limit.
- Handle invalid input.
- Allow the user to choose a starting multiplier.

## 👨‍💻 Author
**Akash Adepu**

Python Programming Internship — Day 6 of 45

---
⭐ Created to practice Python fundamentals through hands-on coding.
