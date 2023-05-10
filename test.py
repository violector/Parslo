import pandas as pd
import os
from locust import HttpUser, task, between
import numpy as np
from numpy import random
import time


url = "http://172.16.101.165:30001/customer-orders.html"

class get_par_first(HttpUser):

    wait_time = between(1, 5)

    @task(1)
    def get_first_page(self):
        self.client.get(url)
        
        
if __name__ == "__main__":
    cmd = ("locust -f test.py --host=http://172.16.101.165:30001")
    os.system(cmd)