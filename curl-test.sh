#!/bin/bash

# Start Flask in the background
echo "Starting Flask..."
flask run > flask.log 2>&1 &
FLASK_PID=$!

# Wait for Flask to fully start up
echo "Waiting for Flask to start..."
sleep 2

# POST to create a test timeline post
echo "Sending POST request..."
RESPONSE=$(curl -s -X POST http://127.0.0.1:5000/api/timeline_post \
-d "name=Smriti&email=smriti@example.com&content=This is a test post!")

echo "POST response:"
echo "$RESPONSE"

# Extract the ID of the new post
POST_ID=$(echo "$RESPONSE" | grep -o '"id":[0-9]*' | grep -o '[0-9]*')

# GET to confirm post is in the timeline
echo "Sending GET request..."
curl -s http://127.0.0.1:5000/api/timeline_post

# DELETE the post if ID was extracted successfully
if [[ -n "$POST_ID" ]]; then
  echo "Sending DELETE request for post ID $POST_ID..."
  curl -s -X DELETE http://127.0.0.1:5000/api/timeline_post/$POST_ID
else
  echo "Could not extract ID from POST response. Skipping DELETE."
fi

# Kill the Flask process
echo "Stopping Flask..."
kill $FLASK_PID
