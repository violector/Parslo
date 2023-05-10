import pandas as pd
import os
from locust import HttpUser, task, between
import numpy as np
from numpy import random
import time


url = "http://172.16.101.165:30001/basket.html"

class get_par_first(HttpUser):

    wait_time = between(1, 5)

    @task(1)
    def get_first_page(self):
        self.client.get(url)
        
        
if __name__ == "__main__":
    for i in range(10,1000,10):
        cmd = ("locust -f locustfile.py --host=http://172.16.101.165:30001/basket.html --headless -u %d -r 10 -t 210s --csv=LLP_3_data_%d" %(i, i) )
        os.system(cmd)
        time.sleep(60)
    