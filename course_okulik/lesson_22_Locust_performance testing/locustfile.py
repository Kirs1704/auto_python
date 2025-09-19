from locust import task, HttpUser, between

class MyUser(HttpUser):
    token = None

    def on_start(self):
        response = self.client.post('/authorize', json = {"name": "Eugeny"})
        self.token = response.json()['token']

    @task
    def get_the_habr_page(self):
        self.client.get('/meme', headers=self.token)

