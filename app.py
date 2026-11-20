from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory book data.
# Data resets when the server restarts.
books = [
    {"id": 1, "title": "Python Basics", "author": "John"},
    {"id": 2, "title": "Java Programming", "author": "David"}
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to SWYNEX Book Management API",
        "endpoints": {
            "list_books": "GET /books",
            "add_book": "POST /books",
            "get_book": "GET /books/<book_id>",
            "update_book": "PUT /books/<book_id>",
            "delete_book": "DELETE /books/<book_id>"
        }
    }), 200


@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books), 200


@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be valid JSON"}), 400

    title = data.get("title")
    author = data.get("author")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A non-empty title is required"}), 400

    if not isinstance(author, str) or not author.strip():
        return jsonify({"error": "A non-empty author is required"}), 400

    new_book = {
        "id": max((book["id"] for book in books), default=0) + 1,
        "title": title.strip(),
        "author": author.strip()
    }
    books.append(new_book)
    return jsonify(new_book), 201


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404


@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be valid JSON"}), 400

    for book in books:
        if book["id"] == book_id:
            title = data.get("title", book["title"])
            author = data.get("author", book["author"])

            if not isinstance(title, str) or not title.strip():
                return jsonify({"error": "A non-empty title is required"}), 400
            if not isinstance(author, str) or not author.strip():
                return jsonify({"error": "A non-empty author is required"}), 400

            book["title"] = title.strip()
            book["author"] = author.strip()
            return jsonify(book), 200

    return jsonify({"error": "Book not found"}), 404


@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)
            return jsonify({
                "message": "Book deleted successfully",
                "book": deleted_book
            }), 200
    return jsonify({"error": "Book not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
