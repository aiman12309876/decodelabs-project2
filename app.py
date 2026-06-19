from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Aiman Zahoor", "email": "aimanzahoor87@gmail.com", "role": "AI Engineer"},
    {"id": 2, "name": "Ali Hassan", "email": "ali@example.com", "role": "Developer"},
    {"id": 3, "name": "Sara Ahmed", "email": "sara@example.com", "role": "Designer"}
]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to DecodeLabs Full Stack API",
        "status": "running",
        "endpoints": {
            "GET /users": "Get all users",
            "GET /users/<id>": "Get user by ID",
            "POST /users": "Add a new user",
            "PUT /users/<id>": "Update a user",
            "DELETE /users/<id>": "Delete a user"
        }
    })

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        "status": "success",
        "data": users,
        "count": len(users)
    })

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify({"status": "success", "data": user})
    return jsonify({"status": "error", "message": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or not data.get('name') or not data.get('email'):
        return jsonify({
            "status": "error",
            "message": "Name and email are required"
        }), 400

    new_user = {
        "id": len(users) + 1,
        "name": data['name'],
        "email": data['email'],
        "role": data.get('role', 'User')
    }
    users.append(new_user)

    return jsonify({
        "status": "success",
        "message": "User added successfully",
        "data": new_user
    }), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404

    data = request.get_json()
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        user['email'] = data['email']
    if 'role' in data:
        user['role'] = data['role']

    return jsonify({
        "status": "success",
        "message": "User updated successfully",
        "data": user
    })

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404

    users = [u for u in users if u["id"] != user_id]
    return jsonify({
        "status": "success",
        "message": "User deleted successfully"
    })

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("   FULL STACK API - DECODELABS PROJECT 2")
    print("=" * 60)
    print("\n Server running at: http://127.0.0.1:5001")
    print(" Press Ctrl+C to stop")
    print("=" * 60 + "\n")
    app.run(debug=True, port=5001)