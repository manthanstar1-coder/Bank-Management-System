# Bank Management System

A simple **command-line Bank Management System** built with Python. The project demonstrates object-oriented programming, JSON-based data persistence, user input handling, account authentication using an account number and PIN, bcrypt-based PIN hashing, and basic banking operations.

> **Project type:** Console / CLI application  
> **Language:** Python  
> **Data storage:** JSON file  
> **Entry point:** `main.py`  
> **Authentication:** Account number + bcrypt-verified PIN

---

## 📌 Project Overview

This project simulates a basic banking workflow through an interactive terminal menu. A customer can open a bank account, deposit money, withdraw money, view account details, update selected information, or close an account.

The application keeps customer records in `data.json`, so changes made through the program are written back to the local JSON file.

The implementation is intentionally lightweight and is suitable for learning **Python classes, file handling, JSON serialization, exception handling, list/dictionary operations, random number generation, authentication, and basic CRUD-style workflows**.

> **Note:** This is an educational CLI project and is not suitable for production banking use.

---

## ✨ Features

### 1. Open New Account

The application collects:

- Full name
- Date of birth
- Gender
- Email address
- 4-digit PIN

It then automatically generates a 15-digit account number and creates an initial balance of `0`.

The current implementation checks:

- Customer age must be **18 or above**
- PIN must contain **exactly 4 digits**
- PIN is hashed using **bcrypt** before being stored

When the checks pass, the account is added to `data.json`.

### 2. Deposit Money

A customer authenticates using:

- Account number
- PIN

After successful authentication, a positive integer amount can be deposited and the updated balance is saved to the JSON file.

### 3. Withdraw Money

The withdrawal workflow also requires the account number and PIN.

The application checks the available balance before deducting the requested amount.

> **Current limitation:** Negative withdrawal amounts are not explicitly rejected and can produce incorrect balance behavior. This remains part of the validation work tracked in GitHub Issues.

### 4. View Passbook / Account Details

The menu option labelled **View Passbook** displays the stored account information after account number and PIN verification.

The current implementation displays account details and balance. It does **not** provide a transaction-history statement.

### 5. Update Account Details

A verified customer can update:

- Name
- Email
- PIN

The application preserves:

- Date of birth
- Age
- Gender
- Account number
- Balance

The updated record is persisted back to `data.json`.

### 6. Close Account

A customer can locate the account using account number and PIN, review the stored details, and confirm the closure.

When confirmed with `y`, the account record is removed from the in-memory list and the updated data is written to `data.json`.

The main menu correctly maps option **6** to `closeAccount()`.

### 7. Continuous Main Menu

The application runs inside a continuous `while` loop.

After completing an operation, the menu is displayed again until the user selects:

```text
0. Exit
```

This functionality is already implemented and tracked issue **#1 is closed**.

---

## 🖥️ Application Menu

The current terminal menu is:

```text
1. Open Account
2. Deposit Money
3. Whidhraw Money
4. View Passbook
5. Update Details
6. Close Account
0. Exit
```

The displayed withdrawal label contains the existing spelling **`Whidhraw Money`** from the source code.

---

## 🏗️ Project Structure

```text
Bank-Management-System/
├── main.py      # Main application logic and CLI
├── data.json    # Local JSON database containing account records
└── README.md    # Project documentation
```

---

## 🔧 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application language |
| JSON | Local data persistence |
| bcrypt | PIN hashing and verification |
| `pathlib.Path` | Checking whether the database file exists |
| `datetime` | Date-of-birth and age calculation |
| `random` | Account number generation |
| `string` | Numeric character generation |
| OOP / Classes | Organizing user and banking operations |

### Python Dependency

The current implementation requires the external package:

```bash
pip install bcrypt
```

---

## 🧩 Code Architecture

### `userInfo` Class

The `userInfo` class is responsible for collecting customer information through terminal input.

Implemented methods:

- `Name()` — reads and uppercases the full name
- `dob()` — collects day, month, and year
- `Age()` — calculates age from the stored date of birth
- `Gender()` — accepts `M` / `F` input
- `Email()` — reads the email address
- `Pin()` — validates a 4-digit PIN and hashes it using bcrypt

### `Bank` Class

The `Bank` class manages the application and account data.

Important class members:

- `database = 'data.json'` — JSON database filename
- `data = []` — in-memory collection of account records

Important methods:

| Method | Responsibility |
|---|---|
| `loadDatabase()` | Loads JSON records into memory when the application starts |
| `__update()` | Writes the current account list back to `data.json` |
| `__accountGenerate()` | Generates a 15-digit account number |
| `creatAcc()` | Creates a new customer account |
| `moneyDeposit()` | Deposits funds into an authenticated account |
| `moneyWhidhraw()` | Withdraws funds after authentication |
| `showDetails()` | Displays authenticated account details |
| `userUpdate()` | Updates editable customer information |
| `closeAccount()` | Removes an account after confirmation |

---

## 💾 Data Storage

The project uses a local JSON file instead of a relational database.

Each account is represented as an object containing fields such as:

```json
{
  "Name": "CUSTOMER NAME",
  "DOB": "DD/MM/YYYY",
  "Age": 20,
  "Gender": "MALE",
  "Email": "customer@example.com",
  "Account No.": "123456789012345",
  "PIN": "<bcrypt-hash>",
  "Balance": 0
}
```

The program loads this list at startup and rewrites the complete list whenever account data changes.

### Persistence Flow

```text
Terminal Input
      ↓
Bank Class / Business Logic
      ↓
In-Memory Bank.data
      ↓
JSON Serialization
      ↓
data.json
```

### Current Data Format

The repository's current demo record stores the PIN as a bcrypt hash rather than a plain-text four-digit PIN.

---

## ▶️ How to Run

### Prerequisites

Install **Python 3** on your system.

Check your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

### Clone the Repository

```bash
git clone https://github.com/vishwas0229/Bank-Management-System.git
cd Bank-Management-System
```

### Install bcrypt

```bash
pip install bcrypt
```

or:

```bash
pip3 install bcrypt
```

### Run the Application

On systems where `python` maps to Python 3:

```bash
python main.py
```

Otherwise:

```bash
python3 main.py
```

The program will display the banking menu and continue running until the user selects **0. Exit**.

> Run the application from the repository directory because the program uses the relative path `data.json`.

---

## 🔐 Authentication & PIN Security

For account-level actions, the current implementation uses:

```text
Account Number + PIN
        ↓
bcrypt.checkpw()
        ↓
Authenticated Account
```

New PINs are:

1. Checked to ensure they contain exactly 4 digits.
2. Encoded as UTF-8.
3. Hashed with `bcrypt.hashpw()`.
4. Stored as a bcrypt hash string.
5. Verified later using `bcrypt.checkpw()`.

The current `data.json` also contains a bcrypt-format PIN hash.

### Important Security Notes

- The original PIN is not stored in plain text.
- The stored bcrypt hash should still be treated as sensitive information.
- The current application prints the stored account record in some workflows, including the PIN hash.
- The project is still an educational CLI application and is not suitable for real banking credentials.

---

## 🧠 Concepts Demonstrated

This project is useful for practicing several Python concepts:

- Object-oriented programming
- Classes and methods
- Class variables
- Class methods
- Private / name-mangled helper methods
- Lists and dictionaries
- List comprehensions
- File handling
- JSON serialization/deserialization
- Exception handling with `try` / `except`
- Date and time calculations
- Random number generation
- Conditional statements
- User input validation
- Password/PIN hashing
- CRUD-style data operations
- Basic authentication

---

## 🔄 Typical Workflow

### Account Creation

```text
Start Application
      ↓
Select "Open Account"
      ↓
Enter Customer Information
      ↓
Validate 4-digit PIN
      ↓
Hash PIN with bcrypt
      ↓
Generate Account Number
      ↓
Validate Age
      ↓
Create Account
      ↓
Save to data.json
```

### Deposit / Withdrawal / View / Update

```text
Start Application
      ↓
Select an Operation
      ↓
Enter Account Number + PIN
      ↓
Verify PIN with bcrypt
      ↓
Find Matching Account
      ↓
Perform Requested Operation
      ↓
Save Changes to data.json
```

### Account Closure

```text
Account Number + PIN
      ↓
Verify PIN with bcrypt
      ↓
Find Account
      ↓
Show Account Details
      ↓
Confirm Closure
      ↓
Remove Record
      ↓
Save data.json
```

---

## 📋 Project Issues & Feature Roadmap

GitHub Issues are being used to track planned improvements and identified bugs separately from the current implementation.

### 📊 Current Issue Status

| Issue | Feature / Bug | Status |
|---|---|---|
| [#1](https://github.com/vishwas0229/Bank-Management-System/issues/1) | Continuous Main Menu | ✅ **Closed** — continuous loop and exit option implemented |
| [#2](https://github.com/vishwas0229/Bank-Management-System/issues/2) | Transaction History | 🔴 **Open** — no transaction ledger or mini statement |
| [#3](https://github.com/vishwas0229/Bank-Management-System/issues/3) | Fund Transfer | 🔴 **Open** — no account-to-account transfer |
| [#4](https://github.com/vishwas0229/Bank-Management-System/issues/4) | Strong Input Validation | 🔴 **Open** — PIN validation exists, but comprehensive validation is incomplete |
| [#5](https://github.com/vishwas0229/Bank-Management-System/issues/5) | Secure PIN Storage | ✅ **Closed** — bcrypt hashing and verification implemented |
| [#6](https://github.com/vishwas0229/Bank-Management-System/issues/6) | Database Backend | 🔴 **Open** — application still uses JSON storage |
| [#7](https://github.com/vishwas0229/Bank-Management-System/issues/7) | Account Number Uniqueness | 🔴 **Open** — generated account numbers are not checked for collisions |
| [#8](https://github.com/vishwas0229/Bank-Management-System/issues/8) | Close Account Menu Mapping | ✅ **Closed** — option 6 correctly calls `closeAccount()` |

**Progress: 3 / 8 issues completed; 5 remain open.**

### 🚀 Planned Features

The remaining planned development includes:

- Transaction history and mini statement
- Account-to-account fund transfer
- Comprehensive input validation
- Database backend using SQLite/MySQL
- Account-number uniqueness verification

---

## ⚠️ Current Implementation Notes

This README documents the repository as it currently exists. Some behaviors should be considered when using or extending the project:

1. **Local JSON storage**  
   `data.json` is a local file rather than a relational banking database.

2. **Secure PIN storage**  
   PINs are now stored as bcrypt hashes and verified with `bcrypt.checkpw()`.

3. **Account number generation**  
   Account numbers are generated randomly from digits, but the current code does not check existing records for duplicate account numbers.

4. **Input validation**  
   Four-digit PIN validation is implemented, but date, email, account-number, menu and other input validation remains incomplete.

5. **Withdrawal validation**  
   The code checks insufficient balance, but negative withdrawal amounts are not explicitly rejected.

6. **Authentication lookup handling**  
   Some account lookups test `if userData == False` instead of checking whether the list is empty. Invalid credentials can therefore cause an `IndexError` in some workflows.

7. **Menu flow**  
   The application now uses a continuous `while` loop with an explicit `0. Exit` option. Issue #1 is therefore complete.

8. **Close-account menu behavior**  
   Option 6 correctly calls `user.closeAccount()`. Issue #8 is therefore complete.

9. **Transaction history**  
   Deposits and withdrawals update balances only. There is currently no transaction ledger.

10. **Fund transfer**  
    The application does not currently support transferring money between two accounts.

11. **PIN update behavior**  
    `userUpdate()` invokes the PIN input method when updating details, so PIN handling during profile updates still has edge cases.

12. **Sensitive information display**  
    Some workflows print the stored account record, including the bcrypt PIN hash. Hashes should not be exposed unnecessarily.

13. **Account closure**  
    The current close-account workflow does not require the balance to be zero before deleting an account.

14. **Sample data**  
    The repository's `data.json` contains demo account data and should not be treated as real banking data.

---

## 🔒 Source Protection

For documentation and project-tracking updates, the application source and demo data remain untouched.

| File | Maintenance Policy |
|---|---|
| `main.py` | **Do not modify** during README/Issue updates |
| `data.json` | **Do not modify** during README/Issue updates |
| `README.md` | Documentation and roadmap updates allowed |
| GitHub Issues | Feature planning and bug tracking allowed |

> **Current documentation update:** README format has been restored to the detailed project-documentation structure while keeping the implementation details synchronized with the current source.

---

## 🚀 Possible Future Improvements

The current project can be extended into a more complete banking application by adding:

- Stronger input validation
- Unique account-number verification
- Transaction history
- Mini statement
- Fund transfer between accounts
- Customer search
- Admin functionality
- Account types such as savings/current
- Interest calculation
- Proper database integration such as SQLite or MySQL
- Logging and audit trails
- Unit tests
- Better separation of UI, business logic, and data-access layers
- Safer handling of sensitive customer information
- Improved authentication error handling
- Account closure balance validation

---

## 🎯 Learning Objective

The primary value of this project is educational: it shows how a small Python program can combine **OOP + file handling + JSON storage + authentication + bcrypt + CRUD operations** into a practical application.

It can serve as a foundation for learning software design before moving from a local CLI prototype to a database-backed application with stronger security, validation, testing, and maintainability.

---

## 📄 License

No explicit license file is currently present in the repository. Until a license is added, the project's reuse and redistribution terms should be considered unspecified.

---

## 👨‍💻 Repository

**GitHub:** https://github.com/vishwas0229/Bank-Management-System
