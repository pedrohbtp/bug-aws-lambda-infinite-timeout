try:
  import unzip_requirements
except ImportError:
  pass
import time
import boto3
import json

def handler(event, context):
    time.sleep(2)
    return 'finished'


if __name__ == '__main__':
    lambda_client = boto3.client('lambda')
    while True:
        lambda_request = lambda_client.invoke(
            FunctionName='bug-lambda-timeout-dev-bug-lambda-event-function'
        )
        print('published: ', time.time())
        print(lambda_request['Payload'].read())
        time.sleep(0.5)