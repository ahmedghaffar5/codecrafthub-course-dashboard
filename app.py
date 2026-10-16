from flask import Flask, jsonify, request, send_from_directory
import json
import os
from datetime import datetime

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "courses.json")
VALID_STATUSES = ("Not Started", "In Progress", "Completed")


def ensure_data_file():
    """Create courses.json with an empty list if it does not exist."""
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as file:
                json.dump([], file, indent=2)
        except OSError as exc:
            raise RuntimeError(f"Unable to create data file: {exc}") from exc


def load_courses():
    """Load and return all courses from courses.json."""
    ensure_data_file()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Unable to read course data: {exc}") from exc

    if not isinstance(data, list):
        raise RuntimeError("Unable to read course data: courses.json must contain a JSON list")
    return data


def save_courses(courses):
    """Write the complete course list to courses.json."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(courses, file, indent=2, ensure_ascii=False)
    except OSError as exc:
        raise RuntimeError(f"Unable to save course data: {exc}") from exc


def get_next_id(courses):
    """Generate the next course ID, starting at 1."""
    if not courses:
        return 1
    return max(course["id"] for course in courses) + 1


def is_valid_date(value):
    """Return True only when value is a real date in YYYY-MM-DD format."""
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except (TypeError, ValueError):
        return False


def validate_payload(data, require_all=True):
    """Validate create/update request payloads."""
    if not isinstance(data, dict):
        return "Request body must be valid JSON."

    required_fields = ("name", "description", "target_date", "status")
    if require_all:
        for field in required_fields:
            if field not in data or str(data[field]).strip() == "":
                return f"Missing required field: {field}"

    for field in ("name", "description"):
        if field in data and str(data[field]).strip() == "":
            return f"{field} cannot be empty"

    if "target_date" in data and not is_valid_date(data["target_date"]):
        return "target_date must use YYYY-MM-DD format"

    if "status" in data and data["status"] not in VALID_STATUSES:
        return "Status must be one of: " + ", ".join(VALID_STATUSES)

    return None


@app.after_request
def add_cors_headers(response):
    """Allow Part 2 to call this API from IBM Live Server on another port."""
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return response


@app.route("/", methods=["GET"])
def home():
    """Health response; Part 2 can later add index.html in this folder."""
    index_path = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(index_path):
        return send_from_directory(BASE_DIR, "index.html")
    return jsonify({"success": True, "message": "CodeCraftHub API is running"}), 200


@app.route("/api/courses", methods=["GET"])
def get_all_courses():
    try:
        courses = load_courses()
        return jsonify({"success": True, "count": len(courses), "courses": courses}), 200
    except RuntimeError as exc:
        return jsonify({"success": False, "error": str(exc)}), 500


@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    try:
        courses = load_courses()
        course = next((item for item in courses if item.get("id") == course_id), None)
        if course is None:
            return jsonify({"success": False, "error": "Course not found"}), 404
        return jsonify({"success": True, "course": course}), 200
    except RuntimeError as exc:
        return jsonify({"success": False, "error": str(exc)}), 500


@app.route("/api/courses", methods=["POST"])
def add_course():
    data = request.get_json(silent=True)
    error = validate_payload(data, require_all=True)
    if error:
        return jsonify({"success": False, "error": error}), 400

    try:
        courses = load_courses()
        new_course = {
            "id": get_next_id(courses),
            "name": data["name"].strip(),
            "description": data["description"].strip(),
            "target_date": data["target_date"],
            "status": data["status"],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        courses.append(new_course)
        save_courses(courses)
        return jsonify({
            "success": True,
            "message": "Course added successfully",
            "course": new_course
        }), 201
    except RuntimeError as exc:
        return jsonify({"success": False, "error": str(exc)}), 500


@app.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    data = request.get_json(silent=True)
    error = validate_payload(data, require_all=False)
    if error:
        return jsonify({"success": False, "error": error}), 400
    if not data:
        return jsonify({"success": False, "error": "No fields supplied for update"}), 400

    try:
        courses = load_courses()
        course = next((item for item in courses if item.get("id") == course_id), None)
        if course is None:
            return jsonify({"success": False, "error": "Course not found"}), 404

        for field in ("name", "description", "target_date", "status"):
            if field in data:
                value = data[field]
                if isinstance(value, str):
                    value = value.strip()
                course[field] = value

        save_courses(courses)
        return jsonify({
            "success": True,
            "message": "Course updated successfully",
            "course": course
        }), 200
    except RuntimeError as exc:
        return jsonify({"success": False, "error": str(exc)}), 500


@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    try:
        courses = load_courses()
        course = next((item for item in courses if item.get("id") == course_id), None)
        if course is None:
            return jsonify({"success": False, "error": "Course not found"}), 404

        courses.remove(course)
        save_courses(courses)
        return jsonify({
            "success": True,
            "message": "Course deleted successfully",
            "deleted_course": course
        }), 200
    except RuntimeError as exc:
        return jsonify({"success": False, "error": str(exc)}), 500


@app.errorhandler(404)
def api_not_found(_error):
    return jsonify({"success": False, "error": "API endpoint not found"}), 404


if __name__ == "__main__":
    ensure_data_file()
    print("CodeCraftHub API is starting...")
    print(f"Data will be stored in: {DATA_FILE}")
    print("API will be available at: http://localhost:5000/api/courses")
    app.run(host="0.0.0.0", port=5000, debug=False)
