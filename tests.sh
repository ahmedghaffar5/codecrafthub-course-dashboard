#!/usr/bin/env bash
set -e
BASE="http://localhost:5000/api/courses"

echo "===== RESET DATA ====="
printf '[]\n' > courses.json

echo; echo "===== 1. CREATE COURSE ====="
curl -s -X POST "$BASE" -H "Content-Type: application/json" -d '{"name":"Python Basics","description":"Learn Python fundamentals","target_date":"2026-12-31","status":"Not Started"}'
echo

echo; echo "===== 2. GET ALL COURSES ====="
curl -s "$BASE"; echo

echo; echo "===== 3. GET COURSE 1 ====="
curl -s "$BASE/1"; echo

echo; echo "===== 4. UPDATE COURSE 1 ====="
curl -s -X PUT "$BASE/1" -H "Content-Type: application/json" -d '{"status":"In Progress"}'; echo

echo; echo "===== 5. MISSING REQUIRED FIELDS ====="
curl -s -X POST "$BASE" -H "Content-Type: application/json" -d '{"name":"Incomplete Course"}'; echo

echo; echo "===== 6. INVALID STATUS ====="
curl -s -X POST "$BASE" -H "Content-Type: application/json" -d '{"name":"Invalid Status Course","description":"Validation example","target_date":"2026-12-31","status":"Paused"}'; echo

echo; echo "===== 7. COURSE NOT FOUND ====="
curl -s "$BASE/999"; echo

echo; echo "===== 8. DELETE COURSE 1 ====="
curl -s -X DELETE "$BASE/1"; echo

echo; echo "===== COMPLETE ====="
