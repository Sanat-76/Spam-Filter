import tkinter as tk
from tkinter import messagebox
import math
from collections import defaultdict
import re

class NaiveBayesClassifier:
    def __init__(self):
        self.spam_word_counts = defaultdict(int)
        self.ham_word_counts = defaultdict(int)
        self.spam_total_words = 0
        self.ham_total_words = 0
        self.spam_count = 0
        self.ham_count = 0
        self.vocabulary = set()

    def tokenize(self, text):
        # Convert to lowercase and extract words
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)
        return words

    def train(self, dataset):
        """
        Trains the classifier on a dataset.
        dataset is a list of tuples: (text, label)
        where label is either 'spam' or 'ham'.
        """
        for text, label in dataset:
            words = self.tokenize(text)
            
            if label == 'spam':
                self.spam_count += 1
                for word in words:
                    self.spam_word_counts[word] += 1
                    self.spam_total_words += 1
                    self.vocabulary.add(word)
            elif label == 'ham':
                self.ham_count += 1
                for word in words:
                    self.ham_word_counts[word] += 1
                    self.ham_total_words += 1
                    self.vocabulary.add(word)

    def predict(self, text):
        """
        Predicts whether a text is 'spam' or 'ham'.
        """
        words = self.tokenize(text)
        
        # Calculate prior probabilities
        total_messages = self.spam_count + self.ham_count
        if total_messages == 0:
            return "unknown"
            
        prob_spam = self.spam_count / total_messages
        prob_ham = self.ham_count / total_messages
        
        # Standard Naive Bayes Formula
        # P(Spam|Text) = (P(Word1|Spam) * P(Word2|Spam) * ...) * P(Spam)
        # P(Ham|Text) =  (P(Word1|Ham)  * P(Word2|Ham)  * ...) * P(Ham)
        
        prob_if_spam = prob_spam
        prob_if_ham = prob_ham
        
        vocab_size = len(self.vocabulary)
        
        for word in words:
            # P(Word | Class) with Laplace Smoothing (alpha = 1)
            # Formula: (count(word, class) + 1) / (total_words_in_class + |V|)
            # This prevents zero probabilities for unseen words
            word_spam_prob = (self.spam_word_counts[word] + 1) / (self.spam_total_words + vocab_size) if self.spam_total_words > 0 else 0
            word_ham_prob = (self.ham_word_counts[word] + 1) / (self.ham_total_words + vocab_size) if self.ham_total_words > 0 else 0
            
            # The core of Naive Bayes: Multiplying the probabilities together
            prob_if_spam *= word_spam_prob
            prob_if_ham *= word_ham_prob
            
        return 'spam' if prob_if_spam > prob_if_ham else 'ham'

def get_training_data():
    return [
        # Spam examples
        ("Win free cash now", "spam"),
        ("Get a free gift waiting for you", "spam"),
        ("Click here for free money", "spam"),
        ("Buy our product now cheap", "spam"),
        ("Congratulations! You won the lottery", "spam"),
        ("Urgent: Your account has been compromised, click here to verify", "spam"),
        ("Claim your $1000 Walmart gift card!", "spam"),
        ("You have been selected for a special exclusive offer", "spam"),
        ("Earn money working from home easy", "spam"),
        ("Limited time offer: get 50% off all purchases", "spam"),
        
        # Ham examples
        ("Hello friend how are you", "ham"),
        ("Meeting at 10 am tomorrow", "ham"),
        ("Can you send the report", "ham"),
        ("Let's grab lunch today", "ham"),
        ("Are we still on for the meeting?", "ham"),
        ("Don't forget to pick up groceries", "ham"),
        ("Here is the requested document for review", "ham"),
        ("Did you watch the game last night?", "ham"),
        ("Let me know when you are available for a quick chat", "ham"),
        ("The project deadline has been extended to Friday", "ham")
    ]

class SpamFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spam Filter AI")
        self.root.geometry("450x350")
        self.root.configure(padx=20, pady=20)
        
        # Initialize and train model
        self.classifier = NaiveBayesClassifier()
        self.classifier.train(get_training_data())
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(self.root, text="✉️ Naive Bayes Spam Filter", font=("Segoe UI", 16, "bold"))
        title_label.pack(pady=(0, 10))
        
        # Instructions
        instruction_label = tk.Label(self.root, text="Enter a message to classify:", font=("Segoe UI", 10))
        instruction_label.pack(anchor="w")
        
        # Text input area
        self.text_input = tk.Text(self.root, height=6, width=45, font=("Segoe UI", 11), relief="solid", bd=1)
        self.text_input.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Predict Button
        predict_button = tk.Button(
            self.root, 
            text="Classify Message", 
            command=self.classify_message, 
            bg="#0078D7", 
            fg="white", 
            font=("Segoe UI", 12, "bold"), 
            relief="flat", 
            cursor="hand2"
        )
        predict_button.pack(fill="x", pady=5)
        
        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Segoe UI", 15, "bold"))
        self.result_label.pack(pady=15)
        
    def classify_message(self):
        message = self.text_input.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Input Error", "Please enter a message to classify.")
            return
            
        # Call the existing predictor
        prediction = self.classifier.predict(message)
        
        # Update UI based on result
        if prediction == 'spam':
            self.result_label.config(text="Result: SPAM 🚨", fg="#D13438") # Red for spam
        else:
            self.result_label.config(text="Result: HAM ✅", fg="#107C10") # Green for ham

if __name__ == "__main__":
    root = tk.Tk()
    # Simple styling to make it look decent on Windows
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass
        
    app = SpamFilterApp(root)
    root.mainloop()
