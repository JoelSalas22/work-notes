# 1. EC2 Storage

## 1.1. Storage Refresher

* **Direct (local) Attached Storage** - Storage on the EC2 Host _Instance Store_.
  * Instance Store Volumes - Ephemeral Storage.
  * **Instance Store Pros**:
    * High I/O performance.
    * Good for temporary storage.
  * **Instance Store Cons**:
    * Data is lost when the EC2 instance is stopped.
  * Cannot be resized.
    * Backups are not possible.
    * Not suitable for long-term storage.
* **Network Attached Storage** - Volumes delieverd on/over the network and attached to the device.
  * Generally Highly Resilient.
  * In on-premises environments, this uses protocols such as iSCSI. In AWS, it uses a service called EBS.
  * **EBS** - Elastic Block Store.
  * **EFS** - Elastic File System.
* **Ephemeral Storage** - Temporary Storage that is lost when the EC2 instance is stopped.
  * *Instance Store Volumes.*
* **Persistent Storage** - Storage that persists even when the EC2 instance is stopped.
  * **EBS** - Elastic Block Store.
  * **EFS** - Elastic File System.

## 1.2 Three Main Categories of Storage in AWS

* **Block** **Storage** - **Volume** presented to the **OS** as a collection of blocks...no structure provided. _**Mountable**_. _**Bootable**_.
  * **EBS** - Elastic Block Store.
  * Has a number of addressable blocks.
  * The OS creates a file system on the volume from these blocks. (e.g. NTFS, ext3 etc.)
  * The mounts the volume (e.g. C drive for Windows or Root Volume for Linux).
  * **Key Points**:
    * Block Storage has ***no in-built structure.***
    * Most EC2 Instaces use EBS as the boot volume.

---

* **File** **Storage** - **File** **System** presented to the **OS** as a collection of files and directories. _**Mountable**_. _**Not Bootable**_.
  * **EFS** - Elastic File System.
  * **Key Points**:
    * File Storage has ***in-built structure.***
    * Can be shared across multiple EC2 instances.
    * Can be accessed by multiple EC2 instances at the same time.
