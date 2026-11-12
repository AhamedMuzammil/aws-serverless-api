AWS Serverless API using Lambda and API Gateway

## Project Overview

This project demonstrates how to build a simple Serverless API using AWS Lambda and Amazon API Gateway.

The application accepts a user's name through an HTTP GET request and returns a JSON response.

The project helps understand serverless computing and how AWS services work together without managing servers.

## Technologies Used

- AWS Lambda
- Amazon API Gateway
- Python
- AWS Management Console

## Architecture

**User → Amazon API Gateway → AWS Lambda → JSON Response**

## Project Objectives

- Understand serverless computing.
- Learn AWS Lambda fundamentals.
- Create and test a Lambda function.
- Understand Amazon API Gateway.
- Integrate API Gateway with Lambda.
- Build a simple serverless HTTP API.

## Implementation Steps

### 1. Create AWS Lambda Function

Created a Lambda function named `serverless-hello-api` using Python.

### 2. Write Python Code

Added Python code to process the incoming request and return a JSON response.

### 3. Test Lambda Function

Tested the Lambda function using a test event with a sample name.

### 4. Create API Gateway

Created an HTTP API using Amazon API Gateway.

### 5. Integrate Lambda

Connected the API Gateway HTTP API to the Lambda function.

### 6. Configure API Route

Configured the GET method with the `/hello` route.

### 7. Test API

Used the API Gateway Invoke URL to send requests and receive JSON responses.

## Python Code

```python
import json

def lambda_handler(event, context):

    params = event.get("queryStringParameters") or {}
    name = params.get("name", "Student")

    response = {
        "message": f"Hello {name}!",
        "service": "AWS Lambda Serverless API",
        "status": "Success"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }
```

## Sample API Request

**Method:** GET

**Route:** `/hello`

**Query Parameter:** `name=Ahamed`

## Expected JSON Response

```json
{
  "message": "Hello Ahamed!",
  "service": "AWS Lambda Serverless API",
  "status": "Success"
}
```

## Key Learnings

- Understanding serverless architecture.
- Creating and testing AWS Lambda functions.
- Working with Python in AWS Lambda.
- Integrating API Gateway with Lambda.
- Configuring HTTP API routes.
- Testing API requests and responses.

## Project Outcome

Successfully learned how AWS Lambda and Amazon API Gateway can be integrated to build a simple serverless API.

## Author

**Ahamed Muzammil**

BCA Graduate | Aspiring Cloud Engineer

**Learning Platform:** Softlogic Academy

---

#AWS #AWSLambda #APIGateway #Serverless #CloudComputing #Python
