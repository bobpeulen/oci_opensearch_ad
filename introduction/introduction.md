# Introduction

## About this Workshop

This workshop runs through the steps to create and start an Anomaly Detection detector in [OCI OpenSearch](https://www.oracle.com/uk/cloud/search/). You will start by provisioning an OCI OpenSearch cluster and set up a topic in the [OCI Notification Service](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm). Afterwards, you will access the OpenSearch dashboards by using NGINX, create a new index in OpenSearch, and add sample data to the index. Then, you will create an Anomaly Detection detector using the OpenSearch dashboards. Once implemented, using the compute instance (also used for NGINX), you will run a script to feed new data every couple of seconds to your Anomaly Detection detector. Lastly, you will set up a trigger to receive automated e-mail notifications, using Oracle Notification Service. As a result, when anomalous behaviour in your data is detected, you will be notified automatically.

The workshop uses Anomaly Detection as defined by OpenSearch. See the full documentation on Anomaly Detection [here](https://opensearch.org/docs/latest/observing-your-data/ad/index/).

Estimated Workshop Time: 1 hour 45 minutes

*The video below is an example of the final result when all steps have been performed*

---- ADD VIDEO

## Objectives

In this workshop, you will follow multiple labs. For each lab, the individual steps are outlines below.

**Lab 1 - Get started**
* Create a VCN and configure the ports
* Create an OCI OpenSearch Cluster
* Create an Oracle Notification Service (ONS) topic
  
**Lab 2 - Access the Dashboard and index creation**
* Create a compute host with NGINX to access the dashboards
* Create a new index in the OCI OpenSearch dashboar
* Add historical data to the newly created index and set up a real-time feed
  
**Lab 3 - Create an Anomaly Detection detector**
* Create an Anomaly Detection Detector in OCI OpenSearch
* Set up automated e-mail notification using ONS
  

## Prerequisites
* An Oracle Cloud Account - Please view this workshop's LiveLabs landing page to see which environments are supported
* Please run the workshop in your home region. You will use Oracle Cloud Shell to access the OCI OpenSearch cluster, which is limited to your home region because of networking requirements.
* Please add the appropriate policies for [OCI OpenSearch](https://docs.oracle.com/en-us/iaas/Content/search-opensearch/Concepts/ocisearchpermissions.htm) and [Oracle Notification Service](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm).
* Please add policies where OCI OpenSearch is allowed to invoke ONS.

## Acknowledgements
* **Authors**:
    * [Bob Peulen](https://www.linkedin.com/in/bobpeulen/)
    * [Robert de Laat](https://www.linkedin.com/in/rdelaat/) 
* **Last Updated By/Date** - Bob Peulen, September 2024
