```markdown
# 🃏 Blackjack Game with Credit System

A Python-based Blackjack game where you play against the computer while managing virtual credits. The game uses the `colorama` library for colorful terminal output.

## 🎯 Features
- Play Blackjack against the computer.
- Earn or lose credits based on the game result.
- Color-coded text for better readability.
- Automatic credit tracking between rounds.

## 📦 Installation
Make sure you have Python 3 installed.

Install the required library:
```bash
pip install colorama
```

## 🚀 How to Run
```bash
python blackjack.py
```

## 🖥 Example Gameplay
```
Welcome to Blackjack!
Credits: $1000
Your cards: [10, 7], current score: 17
Dealer's first card: 9

Do you want to draw another card? (y/n): y
Your cards: [10, 7, 4], current score: 21
Dealer's cards: [9, 8], score: 17

You win! 🎉
Credits: $1200
```

## 📜 Rules
1. Cards are worth their face value, with face cards worth 10 and Aces worth 11 or 1.
2. Try to get as close to 21 as possible without going over.
3. The dealer draws until their score is 17 or higher.
4. You start with $1000 credits.
5. Win → +$200 credits, Lose → -$200 credits.

## 🛠 Dependencies
- Python 3
- colorama (`pip install colorama`)

## 📄 License
This project is open-source and free to use.
```
