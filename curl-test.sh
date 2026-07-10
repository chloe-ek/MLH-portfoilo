#!/bin/bash

# POST a random timeline post
echo "Testing POST /api/timeline_post..."
curl -X POST http://127.0.0.1:5000/api/timeline_post \
  -d "name=Chloe&email=chloe@test.com&content=Test post $(date)"

echo ""

# GET all timeline posts
echo "Testing GET /api/timeline_post..."
curl http://127.0.0.1:5000/api/timeline_post

echo ""
echo "Done!"
