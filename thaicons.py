import tkinter as tk
from tkinter import font

# List of Thai consonants with their names
thai_consonants = [
    ("ก", "Gor Gai"),
    ("\u0E02", "Khor Khai"),
    ("\u0E04", "Khor Khuat"),
    ("\u0E06", "Khor Rakhang"),
    ("\u0E08", "Jor Jaan"),
    ("\u0E0A", "Chor Ching"),
    ("\u0E0C", "Chor Chang"),
    ("\u0E0E", "Sor So"),
]


class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.current_index = 0
        self.flipped = False

        self.custom_font = font.Font(family="Helvetica", size=50)
        self.label = tk.Label(root, text=thai_consonants[self.current_index][0], font=self.custom_font, width=10,
                              height=5, relief="ridge")
        self.label.pack(pady=20)

        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        self.prev_button = tk.Button(root, text="Previous", command=self.prev_card)
        self.prev_button.pack(side=tk.LEFT, padx=10)

    def flip_card(self):
        self.flipped = not self.flipped
        if self.flipped:
            self.label.config(text=thai_consonants[self.current_index][1])
        else:
            self.label.config(text=thai_consonants[self.current_index][0])

    def next_card(self):
        self.current_index = (self.current_index + 1) % len(thai_consonants)
        self.flipped = False
        self.label.config(text=thai_consonants[self.current_index][0])

    def prev_card(self):
        self.current_index = (self.current_index - 1) % len(thai_consonants)
        self.flipped = False
        self.label.config(text=thai_consonants[self.current_index][0])


# Run the application
root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
