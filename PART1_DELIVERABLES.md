# CodeCraftHub Part 1 — Ready Deliverables

## Project deliverables

- `app.py` — complete Python Flask CRUD API
- `courses.json` — JSON data store initialized as an empty list
- `requirements.txt` — Flask/Werkzeug dependencies
- `README.md` — project documentation
- `.gitignore` — excludes local/secret/dev-only files

## Testing deliverables

- `TESTING.md` — cURL commands, payloads, expected results, and error scenarios
- `tests.sh` — fast cURL runner after the server is started
- `test_app.py` — automated Flask test-client suite

## GenAI deliverables

- `PROMPTS.md` — Part 1 IBM GenAI Classroom prompts
- `PART1_COPY_PASTE.txt` — compact checklist/reference

## Implemented REST endpoints

- `POST /api/courses`
- `GET /api/courses`
- `GET /api/courses/<id>`
- `PUT /api/courses/<id>`
- `DELETE /api/courses/<id>`

## Implemented fields

- `id`
- `name`
- `description`
- `target_date`
- `status`
- `created_at`

## Implemented validation/error handling

- Missing required fields
- Invalid/missing JSON body
- Invalid target date format
- Invalid status value
- Course not found
- JSON file creation/read/write errors

## Verification commands for IBM/Theia later

```bash
python3 -m pip install -r requirements.txt
python3 -m py_compile app.py
python3 -m unittest -v test_app.py
python3 app.py
```

Then from a second terminal:

```bash
bash tests.sh
```

## Expected final Part 1 state

- Flask API runs on port 5000
- CRUD operations work
- Data persists in `courses.json`
- Error handling works
- Documentation and tests exist
- Files are ready for GitHub and for cloning into the Part 2 IBM/Theia environment
