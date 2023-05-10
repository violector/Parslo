import pandas as pd
import os
from locust import HttpUser, task, between
import numpy as np
from numpy import random
import time
import base64
from random import randint, choice

url = "http://172.16.101.165:30001/"

class get_car_first(HttpUser):

    @task(1)
    def get_car_page(self):
        base64string = base64.encodestring('%s:%s' % ('user', 'password')).replace('\n', '')
        catalogue = self.client.get("/catalogue").json()
        category_item = choice(catalogue)
        item_id = category_item["id"]
        self.client.get(url)
        self.client.get("/")
        self.client.get("/login", headers={"Authorization":"Basic %s" % base64string})
        self.client.get("/category.html")
        self.client.get("/detail.html?id={}".format(item_id))
        self.client.delete("/cart")
        self.client.post("/cart", json={"id": item_id, "quantity": 1})
        self.client.get("/basket.html")
        
        
if __name__ == "__main__":
    for i in range(10,1000,10):
        cmd = ("locust -f locustfile_car.py --host=http://172.16.101.165:30001/ --headless -u %d -r 10 -t 210s --csv=LLP_3_data_%d" %(i, i) )
        os.system(cmd)
        time.sleep(60)
    