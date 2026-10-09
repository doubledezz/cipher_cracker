# Caesar Cipher Cracker 🔓

A Python-based tool designed to decrypt and automatically crack Caesar ciphers using custom character-shifting logic and an advanced hybrid text-scoring system.

---

## 🚀 Features

- **Custom ASCII Decryption Engine**: Performs modular arithmetic on ASCII character codes for both uppercase (`A-Z`) and lowercase (`a-z`) letters.
- **Punctuation & Space Preservation**: Keeps non-alphabetic characters (spaces, numbers, special symbols) completely intact during decryption.
- **Automated Key Discovery**: Tests all 25 possible key shifts using a brute-force approach.
- **Hybrid Scoring Engine**: Evaluates candidate texts using two complementary techniques:
  - **Statistical Frequency Analysis**: Awards points for common English letters (`E, T, A, O, I, N, S, H, R, D`) and penalizes rare letters (`J, K, Q, X, Z`).
  - **Dictionary Word Validation**: Performs fast $O(1)$ set lookups against a common English word database (`COMMON_WORDS`) to give a +50 point bonus per valid word.
- **Short & Long Text Precision**: Reliably cracks full paragraphs as well as short phrases or single encrypted words.
- **Automatic Punctuation Stripping**: Uses `str.translate()` with `string.punctuation` to clean words before dictionary comparison.
- **Modular Design**: Separates character shifting, text construction, string cleaning, dictionary lookup, and key discovery into distinct, readable functions.

---

## 📂 Code Overview

| Function / Data | Description |
| :--- | :--- |
| `COMMON_WORDS` | A Python `set` storing common English words for $O(1)$ fast dictionary validation. |
| `decrypt_upper_char(char, key)` | Handles ASCII conversion and modular shift math for uppercase letters. |
| `decrypt_lower_char(char, key)` | Handles ASCII conversion and modular shift math for lowercase letters. |
| `add_char(text, char)` | Helper function to append decrypted characters to a message string. |
| `decrypt_text(cipher, key)` | Iterates through ciphertext and applies character-level decryption. |
| `score_text(text)` | Evaluates candidate text using letter frequency analysis and clean word dictionary matching. |
| `crack_caesar(ciphertext)` | Tests all 25 shift keys against `score_text()` and returns the winning key and plaintext. |

---

## 🛠️ How to Run

1. Open your terminal in the project directory.
2. Run the main script:

```bash
python3 crack.py
