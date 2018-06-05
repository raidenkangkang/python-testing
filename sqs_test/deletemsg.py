#delete the message
import boto3

client = boto3.client('sqs')


response_to_delete = client.delete_message(
    QueueUrl='https://sqs.us-east-2.amazonaws.com/079385551353/test-queue.fifo',
    
    ReceiptHandle='AQEB0Elw34tEKZiapX8gxSZruqfd2v7VZmfPyu0cciJn7FlS7YMdyDLILruuYiDzIE2+LqmaPq0douqmO4FV9tNIk1FT4WSQ7gFSO6lkpo1ysoZOrdSiCgMNl1izI6ABfAuhwNxvsdUN44NM16jm9wcoidk1EV4KmhzpK/riWUwl0SKbHckT8MU2MrHDGuT/a/HBLuIYvyNhYXLx2/puX64+3ZcaQatbfGXr8GCpW8JuMiXZjHrnHLFA0JgBZb0guCzw7CLhtNovXTs0GRuuMQXPgw=='
    )
print(response_to_delete)