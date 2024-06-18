# Lab 1 - Get started

## Introduction

In this lab,xx

*Estimated Time:* 30 minutes

### Objectives

In this lab, you will:
* Create a VCN and configure the ports
* Create an OCI OpenSearch Cluster
* Create an Oracle Notification Service (ONS) topic
* Create a jumphost to access the dashboards


## Task 1: Create a VCN and configure the ports

1.	From the Oracle Cloud homepage, click on the hamburger icon, click on **Networking** and following click on **Virtual Cloud Networks**.

2.	Click on **Start VCN Wizard**, choose the **Create VCN with Internet Connectivity** option and click on **Start VCN Wizard** again.
   
    ![lab_vcn_1](images/vcn_1.png)
  	
  	![lab_vcn_2](images/vcn_2.png)

3. Add a logical name in the **VCN Name** box. Following, click on **Next** and then click on **Create**. This will create a VCN with a public and a private subnet. When all items are completed, click on **View VCN**.
    ![lab_vcn_3](images/vcn_3.png)
    ![lab_vcn_4](images/vcn_4.png)
   
4. To make sure you can access the OCI OpenSearch cluster and dashboard, we have to open two ports. On the left side, click on **Security Lists** and following click on **Security list for private_subnet-[name of VCN]**
    ![lab_vcn_5](images/vcn_5.png)

5. In the security list, click on "Add Ingress Rules**. Add "0.0.0.0/0" to the **Source CIDR** box and add "9200,5601" to the **Destination Port Range**. Leave the other boxes empty or default. Click on**Add Ingress Rules**.
    ![lab_vcn_6](images/vcn_6.png)


## Task 2: Create an OCI OpenSearch Cluster



1. Create OCI OpenSearch in private subnet
2. 

## Task 3: Create an Oracle Notification Service (ONS) topic

In this task, you will create an ONS topic and add your personal or work-related e-mail to the service. At the end of the workshop, the ONS topic will be invoked to report detected anomalies directly in your e-mail.

1. Go to the Oracle Cloud homepage and click on the hamburger menu. Following, click on **Developer Services** and click next on **Notifications**
2. On the next page, click on **Create Topic**. Add a name to the **Name** box and click on **Create**.
3. Click on the newly created topic to open the topic. When the topic is not directly visible, refresh the page.
4. Click on **Create Subscription**. Use **E-mail** as protocol and add your work or personal e-mail to the **Email" box. Click on **Create**.
   
   ![lab_1_ons_1](images/ons_1.png)
   
   ![lab_1_ons_2](images/ons_2.png)
   
   ![lab_1_ons_3](images/ons_3.png)

6. The notification service has sent you an e-mail. Please go to your personal or work-related inbox and click on **Confirm Subscription**.
7. Return to your created topic and copy the Topic's OCID. You will need this OCID later.
   
   ![lab_1_ons_4](images/ons_4.png)

## Task 4: Create a jumphost to access the dashboards

1.	Create jumphost in the public subnet


You may now **proceed to the next lab.**

## Acknowledgements
* **Authors**:
    * x
    * x
* **Last Updated By/Date** -xa, July 2024
