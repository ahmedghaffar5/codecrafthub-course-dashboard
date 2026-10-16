# CodeCraftHub API Test Cases

Start the server first:

```bash
python3 app.py
```

Use another terminal for the cURL tests.

## 1. Create course

```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Python Basics","description":"Learn Python fundamentals","target_date":"2026-12-31","status":"Not Started"}'
```

Expected: HTTP 201 and JSON with `success: true`, a message, and an auto-generated course ID.

## 2. Get all courses

```bash
curl http://localhost:5000/api/courses
```

Expected: HTTP 200, a `count`, and a `courses` array.

## 3. Get a specific course

```bash
curl http://localhost:5000/api/courses/1
```

Expected: HTTP 200 and the course object.

## 4. Update a course

```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"In Progress"}'
```

Expected: HTTP 200 and `Course updated successfully`.

## 5. Delete a course

```bash
curl -X DELETE http://localhost:5000/api/courses/1
```

Expected: HTTP 200 and `Course deleted successfully`.

## Error: missing required fields

```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Incomplete Course"}'
```

Expected: HTTP 400 with a missing-required-field error.

## Error: invalid status

```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Course","description":"Test","target_date":"2026-12-31","status":"Invalid Status"}'
```

Expected: HTTP 400 with a valid-status error.

## Error: invalid date format

```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Course","description":"Test","target_date":"12/31/2026","status":"Not Started"}'
```

Expected: HTTP 400 mentioning `YYYY-MM-DD`.

## Error: course not found

```bash
curl http://localhost:5000/api/courses/999
```

Expected: HTTP 404 and `Course not found`.

## Automated tests

```bash
python3 -m unittest -v test_app.py
```
