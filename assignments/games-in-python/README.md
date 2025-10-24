
# 📘 Assignment: Games in Python — Hangman

## 🎯 Objetivo

Build a Hangman word-guessing game that uses Python strings, loops and user input. Students will practice string manipulation, conditionals, loops and simple I/O.

## 📝 Tarefas

### 🛠️	Hangman Game

#### Description
Implement the classic Hangman game. The program should choose a secret word and let the player guess letters until the word is revealed or the player runs out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses and display current progress using underscores and revealed letters (for example: `_ a _ _ m a n`)
- Show letters already guessed and the number of incorrect attempts remaining
- End the game when the word is fully guessed or when attempts are exhausted
- Display a clear win or lose message and reveal the secret word when the player loses

#### Example session
```
Secret word: _ a _ _ m a n
Guess a letter: g
Wrong! Attempts remaining: 5
Guess a letter: h
Correct! _ a _ _ m a n
...
You won! The word was: hangman
```
