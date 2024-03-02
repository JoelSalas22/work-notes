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

* **File** **Storage** - **File** **System** presented to the **OS** as a collection of files and directories. _**Mountable**_. _**Not Bootable**_.
  * **EFS** - Elastic File System.
  * **Key Points**:
    * File Storage has ***in-built structure.***
    * Can be shared across multiple EC2 instances.
    * Can be accessed by multiple EC2 instances at the same time.

* **Object Storage** - A collection of objects, flat. **NOT BOOTABLE**. **NOT MOUNTABLE**.
  * **S3** - Simple Storage Service.
  * **Key Points**:
    * Object Storage has ***no in-built structure.***
    * Very Scalable.
    * Not suitable for installing an OS or a file system.

* **Use Cases**:    
  * Generally in on premises and in AWS:
    * If you want to utilize storage to boot from, then use **Block Storage**.
    * If you want to utilize high performance storage inside an operating system, then use **Block Storage**.
    * If you want to share a file system across multiple different servers or clients, then can often be  **File Storage**. 
    * If you want large access to read & write data object data at scale, like a _web application_, storing _photos_, then use **Object Storage**. It is highly scalable and highly durable.

---

## Storage Performance

* ***IO (**block**) Size*** - Is the size of the blocks of data that you're writing to disk. Expressed as KB (kilobytes) or MB (megabytes). 
  * Can range from 16K, 64K to 1MB.
    * 
  * You can think of IO size as the size of of the wheels on the race car.
* ***IOPS*** (_Input/Output Operations Per Second_) - Measures number of IO operations the storage system can perform per second.
  * Certain media types are better at delivering high IOPS versus other media typees. Certain media types are better at delivering high throughput.
  * If you're using a NAS, the network can also impact how many IOPS can be delivered.
  * Think of IOPS as the speed at which the engine of a race car runs at, revoluting per second.
* ***Throughput*** (_MB/s_) - The amount of data than can be transferred in a given second.
  * As the end speed of the race ![image](/assets/image_argo7m47j.png)car.

> $$ IOSize * IOPS = Throughputs $$
> 16K x 100IOPS = 1.6MB/s
