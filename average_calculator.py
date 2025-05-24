from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/average', methods=['POST'])
def calculate_average():
    data = request.get_json()

    if not data or "numbers" not in data:
        return jsonify({"error": "Missing 'numbers' key"}), 400

    numbers = data["numbers"]

    if not isinstance(numbers, list):
        return jsonify({"error": "'numbers' must be a list"}), 400

    if not numbers:
        return jsonify({"error": "'numbers' list is empty"}), 400

    if not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({"error": "All items in 'numbers' must be numeric"}), 400

    average = sum(numbers) / len(numbers)
    return jsonify({"average": average})

if __name__ == '__main__':
    app.run(debug=True)
