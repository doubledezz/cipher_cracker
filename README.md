# Caesar Cipher Cracker 🔓

A Python-based tool designed to decrypt and automatically crack Caesar ciphers using custom character-shifting logic and a statistical text-scoring system.

---

## 🚀 Features

- **Custom ASCII Decryption Engine**: Performs modular arithmetic on ASCII character codes for both uppercase (`A-Z`) and lowercase (`a-z`) letters.
- **Punctuation & Space Preservation**: Keeps non-alphabetic characters (spaces, numbers, special symbols) completely intact.
- **Automated Key Discovery**: Tests all 25 possible key shifts using a brute-force approach.
- **English Text Scoring Engine**: Evaluates decrypted attempts using a point-scoring system based on common (`E, T, A, O, I, N, S, H, R, D`) vs. rare (`J, K, Q, X, Z`) English letter frequencies to determine the correct key without human intervention.
- **Modular Design**: Separates character shifting, text construction, letter evaluation, and automated key selection into distinct, readable functions.

---

## 📂 Code Overview

| Function | Description |
| :--- | :--- |
| `decrypt_upper_char(char, key)` | Handles ASCII conversion and shift math for uppercase letters. |
| `decrypt_lower_char(char, key)` | Handles ASCII conversion and shift math for lowercase letters. |
| `add_char(text, char)` | Helper function to append characters to a message string. |
| `decrypt_text(cipher, key)` | Iterates through a ciphertext and decrypts it character by character. |
| `score_text(text)` | Inspects text frequency to award or penalize points based on English character habits. |
| `crack_caesar(ciphertext)` | Evaluates all 25 shift attempts against `score_text()` and returns the winning key and plaintext. |

---

## 🛠️ How to Run

1. Open your terminal in the project directory.
2. Run the main script:

```bash
python3 crack.py
