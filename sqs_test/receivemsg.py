import boto3

client = boto3.client('sqs')

response = client.receive_message(
    QueueUrl='https://sqs.us-east-2.amazonaws.com/079385551353/test-queue.fifo',
    AttributeNames=["ALL"],
    MaxNumberOfMessages=10,
    VisibilityTimeout=30,
    WaitTimeSeconds=3
    )

print(response)