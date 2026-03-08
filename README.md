<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1a2e,100:16213e&height=220&section=header&text=Slot%20Machine&fontSize=52&fontColor=FFD700&fontAlignY=38&desc=Casino-Style%20Terminal%20Game%20in%20Python&descAlignY=58&descAlign=50" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Module](https://img.shields.io/badge/Module-random-gold?style=for-the-badge)](.)
[![Type](https://img.shields.io/badge/Type-Terminal%20Game-blueviolet?style=for-the-badge)](.)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)](.)

<br/>

> *A fully functional casino-style Slot Machine built in pure Python — featuring multi-line betting, randomized symbol generation, dynamic payout logic, and bulletproof input validation. All in your terminal.*

<br/>

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Game Flow](#-game-flow)
- [Symbols & Payout Rules](#-symbols--payout-rules)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Implementation Highlights](#-implementation-highlights)
- [Screenshots](#-screenshots)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## 🎯 Overview

**Slot Machine** is a Python terminal game that replicates the core mechanics of a real casino slot machine. From depositing your balance to spinning reels and calculating per-line payouts — every interaction is handled with clean, modular code and validated input.

Built as a deep-dive into **Python fundamentals through game logic** — randomization, control flow, data structures, and function composition all in one project.

---

## ✨ Features

| Feature | Description |
|---|---|
| 💰 **Balance System** | Deposit funds and track balance across every spin |
| 🎯 **Multi-Line Betting** | Bet on 1 to 3 lines simultaneously |
| 🔁 **Randomized Spins** | Column-based symbol generation with realistic distribution |
| 🧮 **Per-Line Payouts** | Winnings calculated independently per winning line |
| 🛑 **Bet Protection** | Prevents bets that exceed current balance |
| ✅ **Input Validation** | Every input is sanitized — no crashes on bad input |
| 🖥️ **Clean Terminal UI** | Readable grid display with instant feedback |

---

## 🎮 Game Flow

```
┌─────────────────────────────────────────┐
│           🎰 SLOT MACHINE               │
├─────────────────────────────────────────┤
│  1. Deposit initial balance             │
│  2. Choose betting lines (1–3)          │
│  3. Set bet amount per line             │
│  4. Spin the reels                      │
│  5. Symbols generated per column        │
│  6. Matching rows = winnings            │
│  7. Balance updated — spin again or quit│
└─────────────────────────────────────────┘
```

---

## 🎰 Symbols & Payout Rules

| Symbol | Frequency | Payout Multiplier | Rarity |
|---|---|---|---|
| **A** | Very Low | **5×** | 🟥 Rare |
| **B** | Low | **4×** | 🟧 Uncommon |
| **C** | Medium | **3×** | 🟨 Common |
| **D** | High | **2×** | 🟩 Very Common |

> Higher-value symbols appear less frequently — maintaining authentic casino-style balance and excitement.

**Payout Formula:**
```
Winnings = Bet per line × Symbol Multiplier × Winning Lines
```

---

## 🛠 Tech Stack

| Component | Detail |
|---|---|
| **Language** | Python 3.x |
| **Modules** | `random` (stdlib — no installs needed) |
| **Concepts** | Functions, Dictionaries, Lists, Randomization, Modular Design |

---

## 🚀 Getting Started

**Prerequisites:** Python 3.x — [Download here](https://python.org/downloads)

```bash
# Clone the repository
git clone https://github.com/loisekk/slot-machine-python.git
cd slot-machine-python

# Run the game
python slot_machine.py
```

No dependencies. No setup. Just run and play.

---

## 📂 Project Structure

```
slot-machine-python/
│
├── slot_machine.py    # Core game logic — all mechanics in one clean file
└── README.md          # Project documentation
```

---

## 🧠 Implementation Highlights

- **Column-based generation** — symbols are drawn per column and removed after selection, preventing duplicates within a column and ensuring realistic spin behavior
- **Weighted symbol distribution** — symbol frequency is controlled via count configuration, not hardcoded probability, making it easy to tune
- **Per-line win detection** — each row is evaluated independently, so multi-line bets can yield multiple simultaneous wins
- **Modular function design** — `deposit()`, `get_bet()`, `spin()`, `check_winnings()` are fully separated, making the codebase easy to extend or test
- **Graceful exit** — player can quit at any time without errors; final balance is displayed on exit

---

## 📸 Screenshot

<div align="center">

<img width="979" height="756" alt="Slot Machine Terminal Screenshot" src="https://github.com/user-attachments/assets/2eb96a6d-8c8f-4512-af13-e4e5ab1ee0b4" />

*Terminal gameplay — deposit, spin, win.*

</div>

---

## 📈 Future Enhancements

- [ ] 🎨 GUI version (Tkinter or PyGame) with animated reels
- [ ] 🔊 Sound effects and win animations
- [ ] 💾 Persistent balance using local file / SQLite
- [ ] 🎚️ Difficulty modes (conservative / high-roller)
- [ ] 📊 Session stats — spins, wins, losses, net profit
- [ ] 🧪 Automated unit tests for game logic

---

## 👨‍💻 Author

<div align="center">

**Yash Brahmankar**

*Aspiring Software Developer · Python Enthusiast · Builder*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-loisekk-181717?style=for-the-badge&logo=github)](https://github.com/loisekk)
[![Email](https://img.shields.io/badge/Email-yashbrahmankar95%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:yashbrahmankar95@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/)

<br/>

⭐ **If this project was useful or fun, drop a star — it genuinely helps!**

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:16213e,50:1a1a2e,100:0d1117&height=120&section=footer" width="100%"/>

*Built with 🎰 and Python by Yash Brahmankar*

</div>
