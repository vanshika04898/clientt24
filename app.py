from flask import Flask, request, jsonify
from flask_cors import CORS
from models import visits_collection
from plate_ocr import extract_plate_from_base64
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)
CORS(app)

@app.route("/api/visits", methods=["POST"])
def create_visit():
    data = request.json or {}
    
    # Trigger OCR if a photo exists
    image_b64 = data.get("vehicleNoPhoto")
    if image_b64:
        data["vehiclePlateDetails"] = extract_plate_from_base64(image_b64)

    data["status"] = "approved"
    data["submittedAt"] = datetime.utcnow()

    # Save to AWS MongoDB
    result = visits_collection.insert_one(data)
    return jsonify({"message": "Success", "id": str(result.inserted_id)}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=False)