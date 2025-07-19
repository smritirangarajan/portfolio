# tests/test_app.pу
import unittest 
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        
        # Check the title
        assert "<title>Smriti Rangaragajan</title>" in html
        
        # Check if section about exists
        assert '<section class="about">' in html, "Missing <section class='about'>"

        # Check if about-title exists inside the HTML
        assert '<h2 class="about-title">About Me</h2>' in html, "Missing <h2 class='about-title'>"

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) != 0
    
    # --------------- Timeline Post ----------------
    # 1. test with correct data
    def test_post_timeline(self):
        # Data will test post.
        name = 'Nada Feteiha'
        email = 'nada@gmail.com'
        content = 'Amazing portfolio Smriti!'
        
        # call the post endpoint
        response = self.client.post("/api/timeline_post", data={
            'name': name,
            'email': email,
            'content': content
        })
        
        # Check response is success and data sent correctly
        assert response.status_code == 200
        json = response.get_json()
        assert "id" in json
        assert json["id"] == 1
        assert json["name"] == name
        assert json["email"] == email
        assert json["content"] == content
        assert "created_at" in json

    # 2. test with missing data
    def test_post_timeline_missing_data(self):
        # Call the post endpoint with missing data
        response = self.client.post("/api/timeline_post", data={
            'name': 'Nada Feteiha',
            'email': '  ', 
            'content': 'Amazing portfolio Smriti!'
        })

        # Check response is error
        assert response.status_code == 400

    # 3. test with invalid data
    def test_post_timeline_invalid_data(self):
        # Call the post endpoint with invalid data
        response = self.client.post("/api/timeline_post", data={
            'name': 'Nada Feteiha',
            'email': 'nadaFeteiha', 
            'content': 'Amazing portfolio Smriti!'
        })

        # Check response has error
        assert response.status_code == 400
        json = response.get_json()
        assert "error" in json
        assert json["error"] == "Invalid email format"
    
    # --------------- Timeline get ----------------
    def test_get_timeline_posts(self):
        # Call get endpoint
        response = self.client.get("/api/timeline_post")
        
        # Check response is success and return array
        assert response.status_code == 200
        json = response.get_json()
        assert "timeline_posts" in json
        assert isinstance(json["timeline_posts"], list)
    
        # --------------- Timeline delete ----------------
    # 1. test delete with valid ID
    def test_delete_timeline_post(self):
        # post to get valid post ID
        postResponse = self.client.post("/api/timeline_post", data={
            'name': 'Test User',
            'email': 'test@example.com',
            'content': 'This is a test post.'
        })

        # Get the post ID from the response
        post_id = postResponse.get_json().get("id")

        # Call delete endpoint
        response = self.client.delete(f"/api/timeline_post/{post_id}")

        # Check response is success
        assert response.status_code == 200

        # Call get endpoint to ensure post is deleted
        get_response = self.client.get(f"/api/timeline_post")
        json = get_response.get_json()
        assert "timeline_posts" in json
        assert all(post["id"] != post_id for post in json["timeline_posts"])

    # 2. test delete with invalid ID
    def test_delete_timeline_post_invalid_id(self): 
        # Call delete endpoint with invalid ID
        response = self.client.delete("/api/timeline_post/9999")
        # Check response is error
        assert response.status_code == 404
        json = response.get_json()
        assert "error" in json
        assert json["error"] == "Post with ID 9999 does not exist"

    
