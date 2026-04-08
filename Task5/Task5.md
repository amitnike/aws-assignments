**Objective:** Implement basic security controls in AWS.

**Tasks:**

1. **Identity Management:**
    - Create IAM users with MFA enabled
    ![alt text](image.png)
    ![alt text](image-1.png)
    - Create IAM groups with appropriate permissions
    ![alt text](image-2.png)
    ![alt text](image-3.png)
    - Create IAM roles for EC2 instances
    ![alt text](image-4.png)
    ![alt text](image-5.png)
    ![alt text](image-6.png)
    - Follow least privilege principle
    ![alt text](image-7.png)
    ![alt text](image-8.png)
    ![alt text](image-9.png)
    ![alt text](image-10.png)
2. **Network Security:**
    - Create VPC with public and private subnets
    ![alt text](image-11.png)
    - Configure security groups with minimal required access
    ![alt text](image-12.png)
    ![alt text](image-13.png)
    ![alt text](image-14.png)
    - Set up VPC Flow Logs
    ![alt text](image-16.png)
    ![alt text](image-15.png)
    ![alt text](image-17.png)
    - Create a bastion host for secure access
    ![alt text](image-18.png)
    ![alt text](image-19.png)
    ![alt text](image-20.png)
3. **Data Protection:**
    - Enable encryption for:
        - S3 bucket
        ![alt text](image-21.png)
        - EBS volumes
        ![alt text](image-22.png)
        ![alt text](image-23.png)
        - RDS database
    - Configure HTTPS using AWS Certificate Manager
4. **Security Monitoring:**
    - Enable AWS Config for basic compliance checking
    - Set up GuardDuty for threat detection
    - Review and document security findings

**Deliverables:**

- Security architecture diagram
- Screenshots of security configurations
- Brief security assessment report