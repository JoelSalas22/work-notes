## EC2 Architecture

* EC2 instances are **virtual machines** (OS + Resources).
  * Reources include virtual CPU, memory, _local_ storage, network storage and access to other hardware such as networking and GPUs.

* EC2 Instances run on **EC2 Hosts**.
  * EC2 Hosts are physical machines in AWS data centers.
  * EC2 Hosts run a **hypervisor** which allows them to run multiple EC2 instances.
* **Shared** Hosts or **Dedicated** Hosts.
  * Shared Hosts are used by multiple AWS customers.
    * Customers are isolated from each other.
  * Dedicated Hosts are used by a single AWS customer.
