**Objective:** Understand different AWS storage options and their use cases.

**Tasks:**

1. **S3 Storage:**
    - Create an S3 bucket with proper security settings
    ![alt text](image.png)

    - Upload different file types
    ![alt text](image-1.png)

    ![alt text](image-2.png)
    ![alt text](image-3.png)
    ![alt text](image-4.png)
    ![alt text](image-5.png)
    ![alt text](image-6.png)

    - Configure one lifecycle policy (move to cheaper storage after 30 days)

    ![alt text](image-7.png)
    ![alt text](image-8.png)
    - Create a simple static website

    ![alt text](image-9.png)
    ![alt text](image-11.png)
    ![alt text](image-12.png)

2. **EC2 Storage:**
    - Launch EC2 instance with default EBS volume
    ![alt text](image-13.png)
    ![alt text](image-14.png)
    - Create and attach one additional EBS volume
    ![alt text](image-15.png)
    ![alt text](image-16.png)
    - Test basic file operations and performance
    ![alt text](image-17.png)
3. **File Sharing:**
    - Create an EFS file system
    ![alt text](image-18.png)
    ![alt text](image-19.png)
    - Mount it to 2 EC2 instances
    ![alt text](image-20.png)
    ![alt text](image-21.png)
    ![alt text](image-22.png)
    ![alt text](image-23.png)
    - Test concurrent file access
    ![alt text](image-24.png)
    ![alt text](image-25.png)
    ![alt text](image-26.png)
    ![alt text](image-27.png)
    ![alt text](image-28.png)
    ![alt text](image-29.png)


**Use S3 When:**
- Storing backups and archives
- Hosting static websites
- Storing large datasets for analytics
- Need unlimited scalability
- Cost is primary concern
- Infrequent access patterns

**Use EBS When:**
- Running databases (MySQL, PostgreSQL)
- Need high performance for single instance
- Require persistent block storage
- Need low latency (<2ms)
- Running file systems (ext4, NTFS)
- Performance is critical

**Use EFS When:**
- Multiple instances need shared storage
- Running collaborative applications
- Need NFS file system
- Require concurrent access
- Building content repositories
- Running containerized applications
