import boto3

client = boto3.client('sqs')

response = client.send_message(
    QueueUrl='https://sqs.us-east-2.amazonaws.com/079385551353/test-queue.fifo',
    MessageBody='This is Python !',
    MessageGroupId='1212001'
)

print(response)