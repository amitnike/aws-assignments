## Assignment 2: Simple Serverless Application

**Objective:** Build a basic serverless web application using AWS services.

**Tasks:**

1. **Frontend:**
    **This is already covered**
    - Create a simple “Hello World” HTML/CSS web page
    - Host it on S3 as a static website
    - Enable public access for website hosting
2. **Backend API:**
    - Create a simple DynamoDB table
    ![alt text](image.png)
    ![alt text](image-1.png)
    ![alt text](image-2.png)
    Created role -:
    ![alt text](image-3.png)
    - Create 2 API Gateway endpoints (GET and POST)
    - Create 2 Lambda functions in Python:
        - One to retrieve data from DynamoDB
        - One to store data in DynamoDB
    ![alt text](image-4.png)
    ![alt text](image-5.png)

    Test-:
    ![alt text](image-6.png)
    ![alt text](image-7.png)

    API Gateway-:
    ![alt text](image-8.png)
    ![alt text](image-9.png)

    Testing-:

    ![alt text](image-10.png)

    
3. **Basic Monitoring:**
    - Enable CloudWatch logs for Lambda functions
    ![alt text](image-11.png)
    - Create one CloudWatch alarm for Lambda errors
    ![alt text](image-12.png)
    ![alt text](image-13.png)
    ![alt text](image-14.png)
    ![alt text](image-15.png)

**Deliverables:**

- Working web application
- Lambda function code
- Screenshots of API testing