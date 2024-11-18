File Uploader and Question Answering Tool

This project is a GUI-based application built with Python’s tkinter framework. It allows users to upload a text file, index its content, and ask questions based on the indexed file using the LlamaIndex library for natural language query processing.

Features

	•	File Upload: Browse and select a .txt file from your system.
	•	File Indexing: Automatically indexes the uploaded file for querying.
	•	Question Answering: Submit questions related to the content of the file, and get AI-generated answers.
	•	User-Friendly Interface: Simple GUI with tkinter for ease of use.

Prerequisites

	1.	Python 3.x: Ensure you have Python 3 installed on your machine.
	2.	Required Libraries:
	•	tkinter (comes pre-installed with Python)
	•	llama_index (install using pip install llama-index)
	3.	OpenAI API Key:
	•	Obtain an API key from OpenAI.
	•	Set the API key in the script:

os.environ["OPENAI_API_KEY"] = 'your_api_key_here'



Installation

	1.	Clone this repository:

git clone https://github.com/your-username/file-uploader-qa.git
cd file-uploader-qa


	2.	Install dependencies:

pip install llama-index


	3.	Run the application:

python app.py



Usage

	1.	Launch the application.
	2.	Click Browse to upload a .txt file.
	3.	Enter your question in the provided text box.
	4.	Click Submit to get an AI-generated answer.

Code Overview

	•	File Selection: Uses filedialog to allow users to upload a .txt file.
	•	File Indexing: Reads and indexes the file using SimpleDirectoryReader from LlamaIndex.
	•	Querying: Allows users to ask questions based on the indexed file content.
	•	GUI: Built with tkinter for an interactive experience.

Example

	1.	Select a text file:

	2.	Ask a question and receive an answer:

Contributing

Feel free to fork this repository and submit pull requests for new features or improvements.


Happy coding! 😊
