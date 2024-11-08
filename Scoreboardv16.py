import customtkinter as ctk
from tkinter import simpledialog, filedialog, messagebox

# Initialize main app window
root = ctk.CTk()
root.title("Classroom Scoreboard By Matt L V1.6")
root.geometry("1920x60")
root.attributes("-topmost", True)  
ctk.set_appearance_mode("dark")  

# Variable to keep track of the selected student
selected_student = None

# Dictionary to hold scores
scores = {}

# Function to update the score of the selected student
def update_score(change):
    global selected_student
    if selected_student is not None:
        current_score = scores[selected_student].get()
        new_score = current_score + change
        scores[selected_student].set(new_score)

# Function to handle selection of a student
def select_student(student_name, label):
    global selected_student

    # Reset background of previously selected student (if any)
    if selected_student is not None:
        name_labels[selected_student].configure(fg_color="transparent")

    # Set new selected student and highlight their label
    selected_student = student_name
    label.configure(fg_color="grey")  # Highlight selected student

# Function to load student names from a file
def load_names_from_file():
    file_path = filedialog.askopenfilename(title="Select a .txt file", filetypes=[("Text Files", "*.txt")])
    try:
        with open(file_path, "r") as file:
            names = [line.strip() for line in file.readlines()]
        return names
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {e}")
        return []

# Prompt for manual entry or file import
option = messagebox.askquestion("Load Students", "Would you like to load student names from a .txt file?")

if option == 'yes':
    student_names = load_names_from_file()
else:
    student_names = simpledialog.askstring("Load Students", "Enter names separated by commas:")
    student_names = [name.strip() for name in student_names.split(",")]

# Dictionary to hold labels for each student's name for highlighting
name_labels = {}

# Set the number of columns and configure each column to expand equally
for i in range(len(student_names)):
    root.grid_columnconfigure(i, weight=1, uniform="equal")  # Make columns expand equally

# Center the student name and score
for i, name in enumerate(student_names):
    # Create a variable to track each student's score
    scores[name] = ctk.IntVar(value=0)

    # Display student name (clickable to select student)
    name_label = ctk.CTkLabel(root, text=name, font=("Arial", 14, "bold"), fg_color="transparent")
    name_label.grid(row=0, column=i, padx=2, pady=0, sticky="nsew")
    name_label.bind("<Button-1>", lambda e, n=name, lbl=name_label: select_student(n, lbl))

    # Save the label to name_labels for highlighting
    name_labels[name] = name_label

    # Display score
    score_label = ctk.CTkLabel(root, textvariable=scores[name], font=("Arial", 16, "bold"))
    score_label.grid(row=1, column=i, padx=2, pady=0, sticky="nsew")

#"Good" and "Bad" buttons
add_button = ctk.CTkButton(root, text="Good", command=lambda: update_score(5), width=80, fg_color="green")
add_button.grid(row=0, column=i+1, padx=2, pady=1, sticky="nsew")

subtract_button = ctk.CTkButton(root, text="Bad", command=lambda: update_score(-2), width=80, fg_color="red")
subtract_button.grid(row=1, column=i+1, padx=2, pady=1, sticky="nsew")

# Run the app
root.mainloop()
