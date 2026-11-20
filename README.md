# SWYNEX Python API Project – Book Management REST API

A beginner-friendly REST API built with Python and Flask. It supports creating,
viewing, searching, updating, and deleting book records.

## Features

- List all books (`GET /books`)
- Add a book (`POST /books`)
- Get one book (`GET /books/<book_id>`)
- Update a book (`PUT /books/<book_id>`)
- Delete a book (`DELETE /books/<book_id>`)
- JSON input validation and useful error responses

## Requirements

- Python 3.9 or later
- Flask

## Setup

1. Open this folder in Visual Studio Code.
2. Open the terminal in this folder.
3. (Recommended) Create and activate a virtual environment:

   Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Start the API:

   ```bash
   python app.py
   ```

6. Open http://127.0.0.1:5000/ in your browser.

## Test the endpoints

Use Postman or another REST API client. Keep the server running while testing.

### 1. List books

- Method: `GET`
- URL: `http://127.0.0.1:5000/books`

### 2. Add a book

- Method: `POST`
- URL: `http://127.0.0.1:5000/books`
- Body type: raw JSON

```json
{
  "title": "Data Structures",
  "author": "Anita"
}
```

### 3. Get one book

- Method: `GET`
- URL: `http://127.0.0.1:5000/books/1`

### 4. Update a book

- Method: `PUT`
- URL: `http://127.0.0.1:5000/books/1`
- Body type: raw JSON

```json
{
  "title": "Advanced Python",
  "author": "John"
}
```

### 5. Delete a book

- Method: `DELETE`
- URL: `http://127.0.0.1:5000/books/1`

## Important note

This starter project stores book records in memory, so changes reset when the
Flask server is restarted. It is suitable as a learning/demo project. Test each
endpoint before submitting your repository.

## Technologies

Python, Flask, REST API, JSON, GitHub
