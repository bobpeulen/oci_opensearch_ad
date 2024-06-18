# Introduction

## About this Workshop

This workshop runs through the steps to create and start an Anomaly Detection detector in [OCI OpenSearch](https://www.oracle.com/uk/cloud/search/). You will start by provisioning an OCI OpenSearch cluster and set up a topic in the [OCI Notification Service](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm). Afterwards, you will create a new index, add sample data to the index, and create an Anomaly Detection detector. Once implemented, using the [Oracle Cloud Shell](https://www.oracle.com/devops/cloud-shell/), you will run a script to feed new data every couple of seconds to your Anomaly Detection detector. Lastly, you will set up a trigger to receive automated e-mail notifications, using Oracle Notification Service, when anomalous behaviour in your data is detected. 

Estimated Workshop Time: 1 hour 30 minutes

*The video below is an example of the final result when all steps have been performed*

---- ADD VIDEO

## Objectives

In this workshop, you will follow multiple labs. For each lab, the individual steps are outlines below.

**Lab 1 - Get started**
* Create a VCN and configure the ports
* Create an OCI OpenSearch Cluster
* Create an Oracle Notification Service (ONS) topic
* Create a jumphost to access the dashboards
  
**Lab 2 - Access the Dashboard and index creation**
* Access the OpenSearch Dashboard
* Create a new index and add data to to the index using Oracle Cloud Shell
  
**Lab 3 - Create an Anomaly Detection detector**
* Create an Anomaly Detection Detector in OCI OpenSearch
* Set up automated e-mail notification using ONS
  
**Lab 4 - Start near real-time Anomaly Detection**
* Start the real-time Anomaly Detection Detector using Oracle Cloud Shell
* Review automatic e-mail notifaction


## Prerequisites
* An Oracle Cloud Account - Please view this workshop's LiveLabs landing page to see which environments are supported
* Please run the workshop in your home region. You will use Oracle Cloud Shell to access the OCI OpenSearch cluster, which is limited to your home region because of networking requirements.
* Please add the appropriate policies for [Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cloudshellintro.htm), [OCI OpenSearch](https://docs.oracle.com/en-us/iaas/Content/search-opensearch/Concepts/ocisearchpermissions.htm), and [Oracle Notification Service](https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm).
* Please add policies where OCI OpenSearch is allowed to invoke ONS.

## Acknowledgements
* **Authors**:
    * [xx](https://www.linkedin.com/in/bx), 
    * [xx](https://www.linkedin.com/in/pxx/), 
* **Last Updated By/Date** - xx, July 2024
