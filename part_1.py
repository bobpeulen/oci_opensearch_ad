import os
os.system("pip install --target ./ pandas opensearch-py datetime")

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


def create_a_new_index(client, index_name):
    
    
    #delete index if exists
    print(f"Delete the index, if exists, with name {index_name}")
    client.indices.delete(index=index_name, ignore=[400, 404])
    
    request_body = {
            "settings":{
              "number_of_shards":1,
              "number_of_replicas": 1, 
              "translog.durability":"async", 
              "refresh_interval":-1,
           },
           "mappings":{
              "properties":{
                 "@timestamp":{
                    "type":"date"
                 },
                 "latency_min":{
                    "type":"double"
                 },
                 "latency_max":{
                    "type":"double"
                 },
                 "latency_diff":{
                    "type":"double"
                 }
              }
           }
        }

    print(f"Create the index with name {index_name}")
    client.indices.create(index=index_name, body=request_body)
    


def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta



def add_ad_data(index_name, client):
    
    loop = 0
    
    ##List of 7 days (5 min apart)
    list_of_dates = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in 
                     datetime_range(datetime.now() - timedelta(days=7), datetime.now(), timedelta(minutes=5))]
    
    for date in list_of_dates:
        
        #convert string time to datetime object
        timestamp = datetime_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

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
        
    return list_of_dates


def main():
    
    #create client
    client = create_opensearch_client(api_endpoint, username, password)

    #create index
    create_a_new_index(client, index_name)

    #add the data row ty row to the index
    list_of_dates = add_ad_data(index_name, client)
    
    return list_of_dates

if __name__ == '__main__':
    main()
