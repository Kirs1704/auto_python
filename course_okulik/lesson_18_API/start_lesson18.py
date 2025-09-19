import requests

def all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    print(response)

def one_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/42').json()
    print(response)

def post_request():
    body = {
        'userId': 5,
        'id': 42,
        'title': 'commodi ullam sint et excepturi error explicabo praesentium voluptas',
        'body': 'odio fugit voluptatum'
    }
    headers = {

        'Content - Type' : 'application/json'
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts',
                             json = body,
                             headers=headers).json()
    print(response)

post_request()