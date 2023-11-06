from bin.requestsLib import Requests
import pytest


base_url = "https://jsonplaceholder.typicode.com"
requestObject = Requests(base_url)


def test_endpoint():
    get_response = requestObject.get_request("posts/1")
    assert get_response.status_code == 200


def test_post():
    post_data = {
        "userId": 1,
        "title": "More crazy content",
        "body": "This is an anticlimax."
    }
    post_response = requestObject.post_request("posts", post_data)
    assert (post_response.json()['title']) == post_data['title']

def test_put(): 
    put_data = {
        "id": 1,
        "title": "Lord Puttersly of API-shire"
    }
    put_response = requestObject.put_request("posts/1", put_data)
    assert (put_response.json()['title']) == put_data['title']

def test_delete():
    delete_response = requestObject.delete_request("posts/1")
    assert delete_response.status_code == 200
