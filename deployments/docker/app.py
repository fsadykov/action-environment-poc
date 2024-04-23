from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/submit', methods=['POST'])
def submit():
    # Ensure the request has JSON content
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    data = request.get_json()
    
    # Check for required keys
    aws_secret_manager = data.get('AWS_SECRET_MANAGER')
    environment = data.get('ENVIRONMENT')
    
    if not aws_secret_manager or not environment:
        return jsonify({"error": "Missing data in request"}), 400
    
    # Process the data (example here just echos it back)
    response_data = {
        "Received AWS Secret Manager": aws_secret_manager,
        "Received Environment": environment
    }
    
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)
