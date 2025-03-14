from flask import Flask, request, jsonify
from storage.azure_blob_storage import AzureBlobStorage

app = Flask(__name__)

# Configure your Azure Blob Storage
connection_string = "your_connection_string"
container_name = "your_container_name"
blob_storage = AzureBlobStorage(connection_string, container_name)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Process the message with your chatbot logic
    bot_response = f"Bot response to: {user_message}"

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)