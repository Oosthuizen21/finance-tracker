# finance-tracker
# 💰 Personal Finance Tracker

A command-line Personal Finance Tracker built in Python to help users record income and expenses, calculate balances, and generate spending reports.

This project is designed as a learning experience in object-oriented programming, file handling, data persistence, and clean software architecture while producing a practical application.

---

## 📌 Features

### Current Features
- Add income transactions
- Add expense transactions
- View current balance
- Categorize transactions
- Save transaction history

### Planned Features
- Load saved transactions automatically
- Monthly spending summaries
- Spending by category
- Export data to CSV
- Search transactions
- Delete transactions
- Data visualization with Matplotlib
- SQLite database support
- Desktop GUI version

---

## 🎯 Project Goals

The purpose of this project is to practice:

- Object-Oriented Programming (OOP)
- Python classes and objects
- File handling
- JSON serialization
- Error handling
- Modular programming
- Git and GitHub workflow
- Clean code practices

---

## 📁 Project Structure

```
finance-tracker/
│
├── main.py
│
├── models/
│   ├── finance.py
│   └── transaction.py
│
├── utils/
│   ├── file_handler.py
│   └── report.py
│
├── data/
│   └── transactions.json
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone git@github.com:YOUR_USERNAME/finance-tracker.git
cd finance-tracker
```

### Create a virtual environment

```bash
python3 -m venv .venv
```

### Activate the virtual environment

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python main.py
```

---

## 🧠 Development Roadmap

### Version 1
- [ ] Create Transaction class
- [ ] Create Finance class
- [ ] Add income
- [ ] Add expenses
- [ ] Calculate balance

### Version 2
- [ ] Save transactions to JSON
- [ ] Load transactions from JSON

### Version 3
- [ ] Spending reports
- [ ] Income reports
- [ ] Category summaries

### Version 4
- [ ] Search transactions
- [ ] Delete transactions
- [ ] Monthly reports

### Version 5
- [ ] Export to CSV
- [ ] Generate graphs using Matplotlib

### Version 6
- [ ] SQLite database integration

### Version 7
- [ ] Desktop GUI

---

## 🏗️ Class Design

### Transaction

Responsible for storing information about a single transaction.

Attributes:

- amount
- category
- transaction_type
- date

---

### Finance

Responsible for managing all transactions.

Methods:

- Add transaction
- Remove transaction
- Calculate balance
- Generate reports
- Save data
- Load data

---

## 📚 Skills Demonstrated

- Python
- Object-Oriented Programming
- Git
- GitHub
- JSON
- File Handling
- Modular Design
- Command Line Applications

---

## 📈 Future Improvements

- User accounts
- Password protection
- Cloud synchronization
- Web application using Flask
- REST API
- Budget planning
- Expense forecasting

---

## 📄 License

This project is intended for educational and portfolio purposes.
