import tkinter as tk
from tkinter import filedialog
from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os

os.environ["OPENAI_API_KEY"] = ''

index = None

def browse_file():
    global index
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        print("Selected file:", file_path)  # Debug line
        file_path_var.set(file_path)
        file_path_label.config(text=file_path)

def submit_question():
    try:
        global index
        question = question_text.get("1.0", "end-1c")
        question_var.set(question)
        answer_text.delete("1.0", tk.END)

        if index is None and file_path_var.get():
            file_path = file_path_var.get()
            print("File path from variable:", file_path)  # Debug line
            if os.path.exists(file_path):
                print("File exists:", file_path)  # Debug line
                documents = SimpleDirectoryReader(file_path).load_data()
                index = VectorStoreIndex.from_documents(documents)
                answer_text.insert(tk.END, "File indexed successfully.\n\n")
            else:
                answer_text.insert(tk.END, "Selected file does not exist.\n\n")
        
        if index is not None:
            query_engine = index.as_query_engine()
            print("Query:", question)  # Debug line
            response = query_engine.query(question)
            print("Response:", response)  # Debug line
            answer_text.insert(tk.END, response)
        else:
            answer_text.insert(tk.END, "Please select a file and submit the question.")
    except Exception as e:
        answer_text.insert(tk.END, "An error occurred: " + str(e))

root = tk.Tk()
root.title("File Uploader and Question")

file_path_var = tk.StringVar()
question_var = tk.StringVar()

file_frame = tk.Frame(root)
file_frame.pack(pady=10)

file_label = tk.Label(file_frame, text="Select a text file:")
file_label.pack(side=tk.LEFT)

browse_button = tk.Button(file_frame, text="Browse", command=browse_file)
browse_button.pack(side=tk.LEFT)

file_path_label = tk.Label(root, text="", wraplength=300)
file_path_label.pack()

question_frame = tk.Frame(root)
question_frame.pack(pady=10)

question_label = tk.Label(question_frame, text="Enter your question:")
question_label.pack()

question_text = tk.Text(question_frame, height=4, width=50)
question_text.pack()

submit_button = tk.Button(root, text="Submit", command=submit_question)
submit_button.pack()

answer_frame = tk.Frame(root)
answer_frame.pack(pady=10)

answer_label = tk.Label(answer_frame, text="Generated Answer:")
answer_label.pack()

answer_text = tk.Text(answer_frame, height=4, width=50)
answer_text.pack()

root.mainloop()
