# 3.1 EBS - Elastic Block Store
<p aligne="center">
  <img src="https://docs.rightscale.com/img/cm-ebs-lifecycle-diagram.gif" alt="EBS Architecture" width="600px" height="500px">

* EBS is a service which provides block storage.
  * **Block Storage** - **raw** disk allocations(**volume**) - Can be **encrypted** using **KMS**.

  * When you attach an EBS volume to an EC2 instance, it appears as a **block device**, which EC2 can use to create a **file system**. (e.g. NTFS, ext4, ext3 etc.)
* Storage is provisioned in **ONE AZ** (Resilient **in that AZ**).
* <span style="color:red">EBS in one AZ is different from an EBS in another AZ.</span>
* **EBS is an availability zone specific service**.
* Generally EBS is attached to ***one*** EC2 instance ( or other service) over a storage network.
  * Some storage types allow you use a feature called **Multi-Attach** which allows you to attach a single EBS volume to multiple EC2 instances. Often used for clusters.
* EBS volumes can be **detached** and **reattached**, not linked to EC2 lifecycle...***persistent***.
* ***Snapshot***(*backup*) - EBS volumes can be backed up to S3 using snapshots.
  * Snapshots are regionally resilient.
    * The data is replicate across multiple AZs in the region. And accessible from all AZ's in the region.

<details>
  <summary>Example</summary>
  <p> You can take a snapshot of an EBS volume in AZ-A and EBS stores that data in S3. Which you can then use to create a new volume in a different AZ  </p>
</details>

#### AWS Documents

* [EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
