from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='build', static_url_path='')
CORS(app)  # Enable CORS for frontend communication

@app.route('/drive', methods=['POST'])
def drive():
    data = request.json
    sensors = data.get("sensors", [])
    
    # Dummy logic: steer right if left sensor is closer
    if not sensors or len(sensors) < 2:
        return jsonify({"steering": 0.0})
    
    steering = 0.5 if sensors[0] < sensors[1] else -0.5
    return jsonify({"steering": steering})

# Serve React build files
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
