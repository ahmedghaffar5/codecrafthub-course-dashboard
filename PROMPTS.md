# Part 1 — IBM GenAI Classroom Prompts

Paste these prompts into the IBM GenAI Classroom when the Part 1 lab asks for them.

## Prompt 1 — Requirements / architecture

```text
I want to create a simple personalized learning platform called CodeCraftHub where developers can track courses they want to learn.

Requirements:
- Use Python with Flask framework
- Store course data in a simple JSON text file (NO database needed)
- No authentication or user management needed
- Focus on learning REST API basics

Each course should track the following:
- Course name
- Description
- Target completion date
- Current status (Not Started, In Progress, Completed)

Recommend:
1. A simple project structure for beginners
2. The REST API endpoints to be created
3. How to store and retrieve data from a JSON file
```

## Prompt 2 — Generate app.py

```text
Now create the complete Python Flask code for app.py with these requirements:

1. Create a Flask REST API with all CRUD operations for courses
2. Store data in a JSON file called "courses.json"
3. Include these endpoints:
   - POST /api/courses - Add a new course
   - GET /api/courses - Get all courses
   - GET /api/courses/<id> - Get a specific course
   - PUT /api/courses/<id> - Update a course
   - DELETE /api/courses/<id> - Delete a course

4. Each course must have:
   - id (auto-generated, starting from 1)
   - name (required)
   - description (required)
   - target_date (required, format YYYY-MM-DD)
   - status (required, must be: "Not Started", "In Progress", or "Completed")
   - created_at (auto-generated timestamp)

5. Include proper error handling for:
   - Missing required fields
   - Course not found
   - Invalid status values
   - File read/write errors

6. Add helpful comments throughout the code for beginners
7. Make sure the app creates courses.json automatically if it doesn't exist
```

## Prompt 3 — Generate test cases

```text
Create comprehensive test cases for the CodeCraftHub API. Provide:

1. curl commands to test each endpoint
2. Example JSON payloads for POST and PUT requests
3. Expected responses for successful operations
4. Test cases for error scenarios (missing fields, invalid data, course not found)

Make the tests easy to copy and paste for beginners.
```

## Prompt 4 — Generate README

```text
Create a complete README.md file for the CodeCraftHub project that includes:

1. Project overview and description
2. Features list
3. Installation instructions (step-by-step)
4. How to run the application
5. API endpoints documentation with examples
6. Testing instructions
7. Troubleshooting common issues
8. Project structure explanation

Write it for beginners who are learning REST APIs for the first time.
```

## Optional challenge prompt

```text
Add a new endpoint GET /api/courses/stats that returns statistics about courses:
- Total number of courses
- Number of courses by status (Not Started, In Progress, Completed)
```

The optional challenge is not included in the baseline project because it is not required for Part 1 completion.
