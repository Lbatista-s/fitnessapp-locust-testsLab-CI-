from locust import HttpUser, task, between

class FitnessAppUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def login(self):
        response = self.client.post("/api/login", json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })
        if response.status_code != 200:
            response.failure(f"Failed with status code {response.status_code}")
