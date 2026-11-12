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