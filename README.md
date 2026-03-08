<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=240&section=header&text=Python%20Mini%20Games&fontSize=52&fontColor=ffffff&fontAlignY=36&desc=A%20Collection%20of%20Interactive%20CLI%20%26%20Pygame%20Experiences&descAlignY=56&descAlign=50" width="100%"/>


[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pygame](https://img.shields.io/badge/Pygame-2.x-00B140?style=for-the-badge&logo=python&logoColor=white)](https://pygame.org)
[![Projects](https://img.shields.io/badge/Projects-5-FF6B6B?style=for-the-badge)](.)
[![Type](https://img.shields.io/badge/Type-Game%20Dev-blueviolet?style=for-the-badge)](.)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-00FF88?style=for-the-badge)](.)

<br/>

```
█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀▀ █▀█ █░░ █░░ █▀▀ █▀▀ ▀█▀ █ █▀█ █▄░█
█▄█ █▀█ █░▀░█ ██▄   █▄▄ █▄█ █▄▄ █▄▄ ██▄ █▄▄ ░█░ █ █▄█ █░▀█
```

> *Five games. One repo. Infinite replayability.*
> A showcase of Python game development spanning CLI adventures to real-time Pygame action.

<br/>

</div>

---

## 📋 Table of Contents

- [About the Collection](#-about-the-collection)
- [Games at a Glance](#-games-at-a-glance)
- [Project Breakdowns](#-project-breakdowns)
  - [🐍 Snake Game](#-project-1--snake-game-pygame)
  - [✊ Snake-Water-Gun](#-project-2--snakewatergun)
  - [❓ Gaming Quiz](#-project-3--interactive-gaming-quiz)
  - [🔢 Number Guessing](#-project-4--number-guessing-game)
  - [🗺️ Choose Your Adventure](#-project-5--choose-your-own-adventure)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Skills Demonstrated](#-skills-demonstrated)
- [Roadmap](#-roadmap)
- [Author](#-author)

---

## 🌌 About the Collection

**Python Mini Games Collection** is a curated set of five interactive Python projects — from terminal-based logic games to a real-time graphical experience with Pygame.

Each game is independently runnable, purposefully minimal, and built to demonstrate a distinct set of Python programming concepts. Whether you're here to play, learn, or fork — there's something for every level.

| Dimension | Detail |
|---|---|
| 🎯 **Purpose** | Portfolio showcase & Python fundamentals demonstration |
| 🧱 **Architecture** | Standalone scripts — no cross-dependencies |
| 🎮 **Game Types** | Real-time (Pygame) + Interactive CLI |
| 👥 **Audience** | Beginners, learners, and Python enthusiasts |

---

## 🎮 Games at a Glance

| # | Game | Type | Engine | Core Concept |
|---|---|---|---|---|
| 1 | 🐍 Snake Game | Real-Time | Pygame | Game loop, collision, rendering |
| 2 | ✊ Snake-Water-Gun | CLI | stdlib | Randomization, game logic |
| 3 | ❓ Gaming Quiz | CLI | stdlib | Control flow, scoring |
| 4 | 🔢 Number Guessing | CLI | stdlib | Validation, binary search intuition |
| 5 | 🗺️ Adventure Game | CLI | stdlib | Branching narratives, conditionals |

---

## 🔍 Project Breakdowns

---

### 🐍 Project 1 — Snake Game (Pygame)

> *The classic — reimagined in Python with real-time rendering, collision detection, and smooth movement.*

```
┌──────────────────────────────────┐
│  🟩 🟩 🟩 ●                     │
│              🍎                  │
│                                  │
│         Score: 3                 │
└──────────────────────────────────┘
```

**Features:**
- Real-time snake movement with arrow key controls
- Randomized food generation on a bounded grid
- Live score display updated per food consumed
- Game-over on wall collision or self-intersection
- Instant replay / quit prompt on game end

**Tech:** `Python` · `Pygame`

```bash
pip install pygame
python snake_game.py
```

---

### ✊ Project 2 — Snake–Water–Gun

> *India's classic hand game — Snake beats Water, Water beats Gun, Gun beats Snake. You vs the machine.*

**Features:**
- Fully randomized computer choice each round
- Win / Lose / Draw outcome detection
- Lightweight — runs instantly with zero dependencies
- Easily extensible to multi-round scoring

**Tech:** `Python` · `random`

```bash
python snake_water_gun.py
```

---

### ❓ Project 3 — Interactive Gaming Quiz

> *Test your gamer knowledge. Multiple choice, score tracking, and emoji-packed feedback.*

**Features:**
- Curated gaming-themed multiple choice questions
- Per-question score accumulation
- Immediate right/wrong feedback with personality
- Final score summary with rating

**Tech:** `Python`

```bash
python quiz_game.py
```

---

### 🔢 Project 4 — Number Guessing Game

> *User-defined range. Hidden number. How many guesses will it take?*

**Features:**
- Player sets their own min/max range
- Input validation — no crashes on bad entries
- Guess counter tracked across the session
- Higher / Lower hints to guide each guess

**Tech:** `Python` · `random`

```bash
python number_guessing.py
```

---

### 🗺️ Project 5 — Choose Your Own Adventure

> *Marvel 🦸 or DC 🦇? Every choice splits the story. No two playthroughs are alike.*

**Features:**
- Fully branching narrative — choices have real consequences
- Multiple distinct endings based on decisions
- Fun, creative storytelling with conditionals as the engine
- Zero dependencies — pure Python storytelling

**Tech:** `Python`

```bash
python adventure_game.py
```

---

## 📂 Project Structure

```
python-mini-games/
│
├── snake_game.py          # 🐍 Real-time Pygame snake game
├── snake_water_gun.py     # ✊ CLI hand game vs computer
├── quiz_game.py           # ❓ Gamer-themed quiz with scoring
├── number_guessing.py     # 🔢 Range-based number guessing
├── adventure_game.py      # 🗺️ Branching Marvel vs DC adventure
│
└── README.md              # You are here
```

---

## ⚡ Quick Start

```bash
# Clone the collection
git clone https://github.com/loisekk/python-mini-games.git
cd python-mini-games

# For Pygame (Snake Game only)
pip install pygame

# Run any game directly
python snake_game.py
python snake_water_gun.py
python quiz_game.py
python number_guessing.py
python adventure_game.py
```

> All CLI games run with **zero dependencies** beyond Python 3.x.

---

## 🧠 Skills Demonstrated

```
Python Mini Games — Concepts Covered
│
├── 🔁 Game Loops & Real-Time Rendering     [Snake Game]
├── 🎲 Randomization & Probability Logic    [Snake-Water-Gun, Number Guess]
├── ✅ Input Validation & Error Handling    [Number Guessing, All CLI games]
├── 🌿 Branching Logic & Decision Trees     [Adventure Game]
├── 📊 Score Tracking & State Management   [Quiz, Snake Game]
├── 🖥️ Pygame: Events, Surface, Clock      [Snake Game]
└── 🧩 Modular Design & Clean Code         [All Projects]
```

---

## 🚀 Roadmap

| Enhancement | Target Project | Priority |
|---|---|---|
| 🔊 Sound effects & background music | Snake Game | High |
| 🏆 Persistent leaderboard (SQLite) | Snake Game, Quiz | High |
| 🖥️ GUI versions of CLI games | All CLI Projects | Medium |
| 🎚️ Difficulty levels (Easy / Hard) | Number Guessing, Quiz | Medium |
| 🌐 Multiplayer mode (socket-based) | Snake-Water-Gun | Low |
| 🤖 AI opponent using minimax | Snake-Water-Gun | Low |
| 🧪 Unit tests for game logic | All Projects | Medium |

---

## 👨‍💻 Author

<div align="center">

**Yash Brahmankar**

*Python Developer · Game Enthusiast · Builder*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-loisekk-181717?style=for-the-badge&logo=github)](https://github.com/loisekk)
[![Email](https://img.shields.io/badge/Email-yashbrahmankar95%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:yashbrahmankar95@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/)

<br/>

⭐ **If this collection taught you something or made you smile — drop a star. It means a lot.**

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,8,25,30&height=140&section=footer" width="100%"/>

*Built with 🎮 creativity and 🐍 Python by Yash Brahmankar*

</div>
