# CodeCraftHub Learning Management System

CodeCraftHub is a beginner-friendly personalized learning platform backend for developers to track courses they want to learn. Part 1 uses Python and Flask, persists course data in a JSON file, and intentionally uses no database or authentication.

## Features

- Create courses
- Read all courses
- Read one course by ID
- Update course details or status
- Delete courses
- Track target completion dates
- Status validation: `Not Started`, `In Progress`, `Completed`
- Auto-generated numeric IDs
- Auto-generated creation timestamps
- JSON file persistence
- Validation and useful error responses
- cURL test cases and automated Flask tests
- CORS headers included for the Part 2 dashboard

## Project structure

```text
codecrafthub/
├── app.py
├── courses.json
├── requirements.txt
├── test_app.py
├── tests.sh
├── TESTING.md
├── PROMPTS.md
├── PART1_DELIVERABLES.md
├── PART1_COPY_PASTE.txt
├── README.md
└── .gitignore
```

## Install

```bash
python3 -m pip install -r requirements.txt
```

## Run

```bash
python3 app.py
```

API base URL:

```text
http://localhost:5000/api/courses
```

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/courses` | Add a new course |
| GET | `/api/courses` | Get all courses |
| GET | `/api/courses/<id>` | Get a specific course |
| PUT | `/api/courses/<id>` | Update a course |
| DELETE | `/api/courses/<id>` | Delete a course |

## Course fields

```json
{
  "id": 1,
  "name": "Python Basics",
  "description": "Learn Python fundamentals",
  "target_date": "2026-12-31",
  "status": "Not Started",
  "created_at": "2026-10-16 20:00:00"
}
```

## Testing

Manual cURL tests are in `TESTING.md` and `tests.sh`.

Automated tests:

```bash
python3 -m unittest -v test_app.py
```

## Troubleshooting

If Flask is missing:

```bash
python3 -m pip install -r requirements.txt
```

If port 5000 is already in use:

```bash
lsof -i :5000
```

Reset sample data:

```bash
printf '[]\n' > courses.json
```

## Part 2 readiness

Part 2 can add its generated `index.html` to this same folder. The Flask root route is already able to serve it when present, and CORS headers allow IBM Live Server testing.

## Project context

Created for the IBM Generative AI software development final project, Part 1 (Python/Flask).
