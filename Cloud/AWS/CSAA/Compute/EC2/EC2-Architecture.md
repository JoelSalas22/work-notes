## EC2 Architecture

* EC2 Instances are virtual machines (OS+Resources)
* EC2 instances run on EC2 Hosts (which is physical hardware aka Servers that AWS owns)
* They can be Shared Hosts or Dedicated Hosts
* Hosts = 1 AZ - If AZ Fails, Host Fails, Instances Fail
  * Reources include virtual CPU, memory, _local_ storage, network storage and access to other hardware such as networking and GPUs.
* EC2 Hosts have local hardware:
  * CPU & Memory
  * Local Storage: Instant Store - Which is Temporary

### Two Types of Networking

* Storage Networking
* Data Networking

> What Happens when provisioning an EC2 into a subnet?
> When instances are provisioned into a specific subnet w/in a VPC, a primary elastic network interface is provisioned into that subnet which is mapped to the physical hardware on that EC2 host.


### EBS Remote Storage

* EC2 can make use of remote storage called Elastic Block Storage (EBS).
  * EBS also runs inside a specific Availability Zone

> Example
> An EBS running inside AZ-A is ***different*** than an EBS running inside AZ-B.
> You CAN NOT access themn cross AZs.


* EBS lets you allocate volumes & volumes of portions of persistent storage. Which can be allocated to instances in the SAME AZ.

* Instances can have multiple Network Interfaces even in different subnets...as long as they are in the SAME AZ
* EC2 Instances run on **EC2 Hosts**.
  * EC2 Hosts are physical machines in AWS data centers.
  * EC2 Hosts run a **hypervisor** which allows them to run multiple EC2 instances.
* **Shared** Hosts or **Dedicated** Hosts.
  * Shared Hosts are used by multiple AWS customers.
    * Customers are isolated from each other.
  * Dedicated Hosts are used by a single AWS customer.
