# Lab 2 - Access the Dashboard and index creation

## Introduction

In this lab, you will access the OCI OpenSearch Dashboard.

*Estimated Time:* 20 minutes

### Objectives

In this lab, you will:
* Create a compute host with NGINX to access the dashboards
* Create a new index and add data to to the index using the compute


## Task 1: Create a compute host with NGINX to access the dashboards

In this example we choose Oracle Linux, you can choose any O.S., please note that pahts may be slightly different on specific opereating systems.

1.	Click on the hamburger menu, go to **Compute** and click on **Instances**. Click on **Create Instance**.

   ![lab_1_compute_1](images/compute_1.png)
   
2.	Change the **Name** to NGINX-host. All default settings are fine, however, feel free to change the Instance Shape. In this example, we are using Oracle Linux 8 as image.
3.	In the **networking options**, make sure to select the same VCN as you just created. Select the **Public Subnet**.

   ![lab_1_compute_2](images/compute_2.png)

4. In the **Add SSH Keys** box, make sure to either **Save private key** or upload your public key. For more information on the different options to connect to the instance, visit this [Connect to your instance](https://docs.oracle.com/en-us/iaas/Content/GSG/Tasks/testingconnection.htm) page.
5. When you completed the steps, click on **Create instance**. This will take 10 - 20 seconds before the instance is active.
6. When the instance is **Active**, use the Public IP address and Username to SSH into the instance. See [here](https://docs.oracle.com/en-us/iaas/Content/GSG/Tasks/testingconnection.htm) for more details on how to SSH into your instance.

   ![lab_1_compute_3](images/compute_3.png)

7. In your terminal of choice, run the following two commands. When prompted, hit **"Y"** and hit **Enter**. The below will install NGINX on your instance. When finished, the terminal should state **Complete!**.
    ```
    sudo su
    yum install nginx
    ```

   ![lab_1_compute_4](images/compute_4.png)
    
8. In Oracle Cloud, in the overview page of your OpenSearch cluster. You will find the **OpenSearch Dashboard Private IP**. NGINX will use this private IP to forward the HTTP traffic towards. Find the Private IP and use the private IP in the next step.

   ![lab_1_compute_5](images/compute_5.png)

9. Copy the below statement and replace the **[ADD_YOUR_DASHBOARD_PRIVATE_IP_HERE]** with your dashboard's private IP. 
   ```
    upstream backend {
           server [ADD_YOUR_DASHBOARD_PRIVATE_IP_HERE]:5601;}
   ```

10. Go back to your terminal and run the below. This will open the config file for the NGINX. In this config file, we can add the routing: from https traffic towards the OpenSearch dashboards using the public IP of the instance you are working on.
    ```
    nano /etc/nginx/nginx.conf
    ```

11. The previous command opens the file, you can now edit the file. Use the arrows to go down to **http** section. Add between **access_log** and **sendfile** a new line, being the statement from step 9. Make sure you changed the Dashboard's private IP.

   ![lab_1_compute_6](images/compute_6.png)

12. When you added the statement, scroll down until you see **location**. Similar to the previous step, change the file using the below statement. When done, hit **CRTL + X** to close the file, select **Y** to save the changes made and following hit enter to overwrite the current file.

    ```
    location / {
          proxy_pass https://backend;
        }
    ```

   ![lab_1_compute_7](images/compute_7.png)

13. When you closed and saves the config file. Run the below statement in the terminal to open the instance's firewall so it can accept and process http traffic towards the OpenSearch dashboards. The result should **success**.

    ```
    firewall-cmd --add-service=http --permanent
    firewall-cmd --reload
    ```


## Task 2: Create a new index and add data to to the index using the compute





You may now **proceed to the next lab.**

## Acknowledgements
* **Authors**:
    * x
    * x
* **Last Updated By/Date** -xa, July 2024
