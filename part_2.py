import os
os.system("pip install opensearch-py --user")

### imports
import oci
import random
from json import loads, dumps
from urllib.request import urlopen 
import subprocess
from random import Random
import argparse
from opensearchpy import OpenSearch, RequestsHttpConnection
from opensearchpy import helpers
import time
from datetime import datetime, timedelta

import warnings
warnings.filterwarnings('ignore')

#get arguments
parser = argparse.ArgumentParser()

parser.add_argument("-api_endpoint", "--api_endpoint", help="cluster endpoint without http:// and without port", required=True)
parser.add_argument("-username", "--username", help="Username used",required=True)
parser.add_argument("-password", "--password", help="Password used", required=True)
parser.add_argument("-index_name", "--index_name", help="Index name used", required=True)
args = parser.parse_args()
api_endpoint = args.api_endpoint
username = args.username
password = args.password
index_name = args.index_name



def create_opensearch_client(api_endpoint, username, password):
    #create client
    client = OpenSearch(
    hosts=[{'host': api_endpoint, 'port': 9200}],
    use_ssl=True,
    verify_certs=False,
    http_auth=(username, password),
    scheme="https",
    port=9200,
    connection_class=RequestsHttpConnection)
    
    return client


def start_ad_loop(index_name, client):
    
    #get the last date in the list of dates
    last_date_used = list_of_dates[-1]
    
    #convert last_date_used to timestamp
    timestamp = datetime_object = datetime.strptime(last_date_used, '%Y-%m-%d %H:%M:%S')
    
    #start with the next id.
    loop = 2018
 
    #create a range to loop through. 300 items.
    full_range = range(5)
    
    for idx in full_range:
        
        #for each loop, add 5 min to the timestamp
        timestamp = timestamp + timedelta(minutes=5)
    
        latency_min = round(random.uniform(300.1, 600.9),2)
        latency_max = round(random.uniform(700.1, 3100.9),2)
        latency_diff = latency_max - latency_min

        print(f"Loading latency with min {latency_min}, max {latency_max}, on timestamp {timestamp}")

        input_payload = {"@timestamp": timestamp,
                        "latency_min": latency_min,
                        "latency_max": latency_max,
                        "latency_diff": latency_diff}

        #add new row to the index
        response = client.index(index = index_name, body = input_payload, id = loop, refresh = True)

        #create next id
        loop+=1

         #wait 30 seconds for next iteration        
        time.sleep(30)


def main():
    
    start_ad_loop(index_name, client)

if __name__ == '__main__':
    main()
