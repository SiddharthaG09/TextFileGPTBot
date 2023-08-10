import tkinter as tk
from tkinter import filedialog
import openai
openai.api_key="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"

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_path_var.set(file_path)
    file_path_label.config(text=file_path)

def submit_question():
    question = question_text.get("1.0", "end-1c")
    question_var.set(question)
    answer_text.delete("1.0", tk.END)  # Clear previous answer
    # Here, you can add code to generate the answer based on the question and file_path
    answer = "This is a sample answer."
    answer_text.insert(tk.END, answer)

# Create the main GUI window
root = tk.Tk()
root.title("File Uploader and Question")

# Variables to store file path and question
file_path_var = tk.StringVar()
question_var = tk.StringVar()

# File Upload Frame
file_frame = tk.Frame(root)
file_frame.pack(pady=10)

file_label = tk.Label(file_frame, text="Select a text file:")
file_label.pack(side=tk.LEFT)

browse_button = tk.Button(file_frame, text="Browse", command=browse_file)
browse_button.pack(side=tk.LEFT)

file_path_label = tk.Label(root, text="", wraplength=300)
file_path_label.pack()

# Question Frame
question_frame = tk.Frame(root)
question_frame.pack(pady=10)

question_label = tk.Label(question_frame, text="Enter your question:")
question_label.pack()

question_text = tk.Text(question_frame, height=4, width=50)
question_text.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_question)
submit_button.pack()

# Answer Frame
answer_frame = tk.Frame(root)
answer_frame.pack(pady=10)

answer_label = tk.Label(answer_frame, text="Generated Answer:")
answer_label.pack()

answer_text = tk.Text(answer_frame, height=4, width=50)
answer_text.pack()



# Start the GUI event loop
root.mainloop()

# Retrieve the stored variables after the GUI is closed
file_path = file_path_var.get()
question = question_var.get()

print("File Path:", file_path)
print("Question:", question)
