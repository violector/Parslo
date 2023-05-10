import os
import math
from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape

url = "http://172.16.101.165:30001/"

class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get(url)

class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    tasks = [UserTasks]


class StepLoadShape(LoadTestShape):
    """
    A step load shape


    Keyword arguments:

        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds

    """

    step_time = 30
    step_load = 1
    spawn_rate = 1
    time_limit = 51000

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)
            

        
if __name__ == "__main__":
    cmd = ("locust -f locusttest.py --host=http://172.16.101.165:30001/ --headless  --csv=LLPdata")
    os.system(cmd)