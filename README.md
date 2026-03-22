# Basic Naive Bayes Spam Filter

This is a very basic, ground-up implementation of a Naive Bayes classifier without any machine learning libraries. It is built purely in standard Python to demonstrate the foundational concepts of the algorithm.

## Features
- **From Scratch**: Implemented using only `math`, `re`, and `collections` from the Python standard library.
- **Laplace Smoothing**: Implements Add-1 smoothing to prevent zero-probability errors when evaluating unseen words.
- **Log Probabilities**: Uses log addition instead of probability multiplication to avoid numerical underflow.

## How it works
1. **Tokenization**: It splits sentences into words and converts them to lowercase.
2. **Training Phase**: It calculates word counts and vocabulary size based on classified dummy data (Spam vs. Ham).
3. **Prediction Phase**: When given a new message, it calculates the probability that the message is Spam versus Ham, and returns the more probable label.

## How to Run
Navigate to this directory and simply run the python script:

```bash
python spam_filter.py
```
