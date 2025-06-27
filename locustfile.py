from locust import HttpUser, task, between

class FitnessAppUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def login(self):
        self.client.post("/api/login", json={"username": "user", "password": "pass"})
