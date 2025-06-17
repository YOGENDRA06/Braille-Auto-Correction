import tkinter as tk
from tkinter import ttk
from braille_map import braille_char_map
from rapidfuzz import process

# -----------------------------
# Dictionary loading function
# -----------------------------
def load_dictionary(filepath):
    with open(filepath, 'r') as file:
        return [line.strip().lower() for line in file.readlines()]

# -----------------------------
# Convert Braille keys to text
# -----------------------------
def convert_braille_to_text(braille_input):
    valid_keys = set(['D', 'W', 'Q', 'K', 'O', 'P'])
    word = ""
    for key_combo in braille_input:
        filtered = ''.join(sorted([ch.upper() for ch in key_combo if ch.upper() in valid_keys]))
        letter = braille_char_map.get(filtered, '?')
        word += letter
    return word.lower()

# -----------------------------
# Suggest words using RapidFuzz
# -----------------------------
def suggest_word(decoded_word, word_list, max_suggestions=1, threshold=60):
    # results = process.extract(decoded_word, word_list, limit=max_suggestions, score_cutoff=threshold)
    # return [match for match, score, _ in results]
    # Step 1: Get all matches above the threshold
    all_matches = process.extract(decoded_word, word_list, score_cutoff=threshold, limit=None)

    # Step 2: Filter and sort by closeness in length
    sorted_matches = sorted(
        all_matches,
        key=lambda x: (abs(len(x[0]) - len(decoded_word)), -x[1])  # (length difference, score descending)
    )

    # Step 3: Return the top 'max_suggestions'
    return [match for match, score, _ in sorted_matches[:max_suggestions]]

# -----------------------------
# GUI Application
# -----------------------------
class BrailleAutoCorrectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Braille Auto-Correct System")

        self.word_list = load_dictionary("daily_conversation_words.txt")

        self.input_label = ttk.Label(root, text="Enter Braille Key Combos (comma separated):")
        self.input_label.pack(pady=5)

        self.input_field = ttk.Entry(root, width=50)
        self.input_field.pack(pady=5)
        self.input_field.bind("<KeyRelease>", self.on_input)

        self.decoded_label = ttk.Label(root, text="Decoded Word:")
        self.decoded_label.pack(pady=5)

        self.decoded_word_var = tk.StringVar()
        self.decoded_word_display = ttk.Label(root, textvariable=self.decoded_word_var, font=("Arial", 14))
        self.decoded_word_display.pack(pady=5)

        self.suggestion_label = ttk.Label(root, text="Suggestions:")
        self.suggestion_label.pack(pady=5)

        self.suggestion_var = tk.StringVar()
        self.suggestion_display = ttk.Label(root, textvariable=self.suggestion_var, font=("Arial", 12))
        self.suggestion_display.pack(pady=5)

    def on_input(self, event=None):
        raw_input = self.input_field.get()
        braille_keys = [chunk.strip() for chunk in raw_input.split(',') if chunk.strip()]

        if braille_keys:
            decoded = convert_braille_to_text(braille_keys)
            self.decoded_word_var.set(decoded)

            suggestions = suggest_word(decoded, self.word_list)
            self.suggestion_var.set(', '.join(suggestions) if suggestions else "No suggestions")
        else:
            self.decoded_word_var.set("")
            self.suggestion_var.set("")

# -----------------------------
# Run the GUI
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BrailleAutoCorrectApp(root)
    root.mainloop()
