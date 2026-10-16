import json
import os
import tempfile
import unittest

import app as codecrafthub


class CodeCraftHubApiTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_data_file = codecrafthub.DATA_FILE
        codecrafthub.DATA_FILE = os.path.join(self.temp_dir.name, "courses.json")
        with open(codecrafthub.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)
        codecrafthub.app.config["TESTING"] = True
        self.client = codecrafthub.app.test_client()

    def tearDown(self):
        codecrafthub.DATA_FILE = self.original_data_file
        self.temp_dir.cleanup()

    @staticmethod
    def sample_course():
        return {
            "name": "Python Basics",
            "description": "Learn Python fundamentals",
            "target_date": "2026-12-31",
            "status": "Not Started"
        }

    def test_get_empty_courses(self):
        response = self.client.get("/api/courses")
        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertTrue(payload["success"])
        self.assertEqual(payload["count"], 0)
        self.assertEqual(payload["courses"], [])

    def test_create_and_get_course(self):
        create = self.client.post("/api/courses", json=self.sample_course())
        self.assertEqual(create.status_code, 201)
        course_id = create.get_json()["course"]["id"]
        read = self.client.get(f"/api/courses/{course_id}")
        self.assertEqual(read.status_code, 200)
        self.assertEqual(read.get_json()["course"]["name"], "Python Basics")

    def test_update_course(self):
        create = self.client.post("/api/courses", json=self.sample_course())
        course_id = create.get_json()["course"]["id"]
        update = self.client.put(f"/api/courses/{course_id}", json={"status": "In Progress"})
        self.assertEqual(update.status_code, 200)
        self.assertEqual(update.get_json()["course"]["status"], "In Progress")

    def test_delete_course(self):
        create = self.client.post("/api/courses", json=self.sample_course())
        course_id = create.get_json()["course"]["id"]
        delete = self.client.delete(f"/api/courses/{course_id}")
        self.assertEqual(delete.status_code, 200)
        read = self.client.get(f"/api/courses/{course_id}")
        self.assertEqual(read.status_code, 404)

    def test_missing_required_field(self):
        response = self.client.post("/api/courses", json={"name": "Incomplete"})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing required field", response.get_json()["error"])

    def test_invalid_status(self):
        payload = self.sample_course()
        payload["status"] = "Paused"
        response = self.client.post("/api/courses", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Status must be one of", response.get_json()["error"])

    def test_invalid_date(self):
        payload = self.sample_course()
        payload["target_date"] = "12/31/2026"
        response = self.client.post("/api/courses", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("YYYY-MM-DD", response.get_json()["error"])

    def test_course_not_found(self):
        response = self.client.get("/api/courses/999")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()["error"], "Course not found")


if __name__ == "__main__":
    unittest.main(verbosity=2)
