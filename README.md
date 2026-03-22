# Naive Bayes Spam Filter with UI

This is a ground-up implementation of a Naive Bayes classifier built entirely from scratch in standard Python, complete with a graphical user interface (GUI) using Tkinter. It demonstrates the foundational concepts of the machine learning algorithm without relying on external libraries.

## Features
- **From Scratch Implementation**: The classifier is built and trained internally using only standard Python libraries (`math`, `re`, `collections`, `tkinter`).
- **Interactive UI**: Includes a clean and simple graphical interface to type messages and instantly classify them as "Spam 🚨" or "Ham ✅".

## How it works
1. **Tokenization**: It splits input sentences into words and normalizes them to lowercase.
2. **Training Phase**: When launched, it reads an internal hardcoded dataset of diverse Spam and Ham examples, calculating word frequencies and total vocabulary size.
3. **Prediction Phase**: When given a new message in the UI, it calculates the statistical probability of the message being Spam versus Ham using the standard Naive Bayes probability formula, and returns the most probable label.

## How to Run
Ensure you have Python installed on your system. Navigate to this directory and run the following command:

```bash
python spam_filter.py
```
