from locust import HttpUser, task, between

class FitnessAppUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def login(self):
        with self.client.post("/api/login", json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }, catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Login failed")
            elif response.elapsed.total_seconds() > 2:
                response.failure("Response time exceeded 2 seconds")
