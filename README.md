# Study enhancer API

## Description
This project is an API built with FastAPI to manage a database of questions. It allows you to create, update, delete, and retrieve questions through RESTful endpoints — making it ideal for educational platforms, quizzes, or any system that needs dynamic question management.

## Technologies used
- Python
- FastAPI
- SQLite

## Features
✏️ Create and Edit Questions
- Easily add new questions or update existing ones via API requests

🗑️ Delete Questions
- Remove questions from the database

📄 Retrieve Questions
- Get individual questions or list all stored questions

🔍 Search and Filtering
- Search by keywords, categories, or difficulty levels

🚀 FastAPI Integration
- Includes automatic interactive API docs via Swagger UI (/docs)

## Installing
To run this project, you'll need firstly to copy it. Open the terminal in the folder you want to install the project an then run this line of code to copy it from github

    git clone https://github.com/lucabattesini/study-enhancer.git

Now, with the terminal open in the project folder, install the main requirements running this line of code

    pip install requirements.txt

## Running the project
Now you've already intalled all the requirements, you just need to run this code in your terminal to run it

    uvicorn app:app --reload   

## Documentation
As the project was made with FastAPI, all the documentation can be accessed by following the following steps

- Run the project
- Open the HTTP adress in your browser (It'll appear in your terminal)
- Add to address a "/docs"

It'll look like this

    http://127.0.0.1:8000/docs
