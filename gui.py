import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_path_var.set(file_path)
    file_path_label.config(text=file_path)

def submit_question():
    try:
        question = question_text.get("1.0", "end-1c")
        question_var.set(question)
        answer_text.delete("1.0", tk.END)  # Clear previous answer

        # Retrieve the stored document using the file_path_var
        file_path = file_path_var.get()
        if file_path:
            with open(file_path, "r", encoding="latin-1") as file:
                content = file.read()
                answer_text.insert(tk.END, content)
        else:
            answer_text.insert(tk.END, "Please select a file.")
    except Exception as e:
        answer_text.insert(tk.END, "An error occurred: " + str(e))

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
