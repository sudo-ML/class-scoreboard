import pygame
from pygame import mixer
import customtkinter as ctk
from tkinter import simpledialog, filedialog, messagebox
import os

class ScoreboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Classroom Scoreboard By Matt L V2.0")
        ctk.set_appearance_mode("dark")

        # Set width and height of the window
        window_width = 1920
        window_height = 60

        # Set the window to be topmost
        self.root.attributes("-topmost", True)
        self.root.attributes("-fullscreen", False)

        # Calculate the x coordinate to center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        x_position = (screen_width - window_width) // 2

        # Set the window geometry to align it at the top of the screen
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+0")
        ctk.set_appearance_mode("dark")

        # Initialize sound and scores
        mixer.init()
        self.selected_student = None
        self.scores = {}
        self.name_labels = {}
        
        # Load student names and create the UI
        self.student_names = self.load_student_names()
        self.create_ui()
        
        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def load_student_names(self):
        option = messagebox.askquestion("Load Students", "Would you like to load student names from a .txt file?")
        if option == 'yes':
            return self.load_names_from_file()
        else:
            return self.get_student_names_from_user()

    def load_names_from_file(self):
        file_path = filedialog.askopenfilename(title="Select a .txt file", filetypes=[("Text Files", "*.txt")])
        try:
            with open(file_path, "r") as file:
                return [line.strip() for line in file.readlines()]
        except Exception as e:
            messagebox.showerror("Error", f"Could not read file: {e}")
            return []

    def get_student_names_from_user(self):
        names = simpledialog.askstring("Load Students", "Enter names separated by commas:")
        return [name.strip() for name in names.split(",")]

    def create_ui(self):
        for i, name in enumerate(self.student_names):
            self.scores[name] = ctk.IntVar(value=10)
            self.root.grid_columnconfigure(i, weight=1, uniform="equal")

            # Name label
            name_label = ctk.CTkLabel(self.root, text=name, font=("Arial", 14, "bold"), fg_color="transparent")
            name_label.grid(row=0, column=i, padx=2, pady=0, sticky="nsew")
            name_label.bind("<Button-1>", lambda e, n=name, lbl=name_label: self.select_student(n, lbl))
            self.name_labels[name] = name_label

            # Score label
            score_label = ctk.CTkLabel(self.root, textvariable=self.scores[name], font=("Arial", 16, "bold"))
            score_label.grid(row=1, column=i, padx=2, pady=0, sticky="nsew")

        # buttons
        add_button = ctk.CTkButton(self.root, text="Good", command=lambda: self.update_score(5, "magic.wav"), width=80, fg_color="green")
        add_button.grid(row=0, column=len(self.student_names), padx=2, pady=1, sticky="nsew")

        subtract_button = ctk.CTkButton(self.root, text="Bad", command=lambda: self.update_score(-2, "bad.mp3"), width=80, fg_color="red")
        subtract_button.grid(row=1, column=len(self.student_names), padx=2, pady=1, sticky="nsew")

    def select_student(self, student_name, label):
        if self.selected_student is not None:
            self.name_labels[self.selected_student].configure(fg_color="transparent")

        self.selected_student = student_name
        label.configure(fg_color="grey")

    def update_score(self, change, sound_file):
        if self.selected_student is not None:
            current_score = self.scores[self.selected_student].get()
            self.scores[self.selected_student].set(current_score + change)
        self.play_sound(sound_file)

    def play_sound(self, sound_file):
        try:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except pygame.error as e:
            messagebox.showerror("Sound Error", f"Could not play sound: {e}")

    def save_scores(self):
        file_path = "scores.txt"
        try:
            with open(file_path, "w") as file:
                for student, score_var in self.scores.items():
                    file.write(f"{student}: {score_var.get()}\n")
            print("Scores saved successfully to scores.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save scores: {e}")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to exit?"):
            self.save_scores()
            self.root.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    app = ScoreboardApp(root)
    root.mainloop()
