import boto3
import json

brt = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1',
    aws_access_key_id='ASIA4MTWHZPHBRQ4GQCB',
    aws_secret_access_key='INuPCUsYPtTTZ+OezROL5JFzMNNoaJV3csUVNVft',
    aws_session_token='IQoJb3JpZ2luX2VjEOr//////////wEaCXVzLWVhc3QtMSJHMEUCIQDYBACE395SebzaO31EJqTKdfA4dns06oGGq0o6/jUlSQIgMRSg31QlHqOEhwne8L4hirSgx5DiR2Qpygd1/eUXD5oqiwMIMxAAGgw4NTE3MjUyNDEyOTQiDIDI2bt1SDwTAGLyoyroAnGrk9Iooa/RTWaTpPtT1H6EJwa5CT8HMgMud0zYKwFazya77lNRmD/9KJe43ugbpYQUmpfE9Ird1qBBG0NzgxXptad8BjCl/weLLZZfrXQwhKT8SdaY+RBXRrm4UHq/j6WQfMdfyPKoa/pz20strq9EH+wYpXkKDTAbjGfUqWz6beGlND647qjZxB4THum6GHQNgxNMgKRyuELEFGWAAex2cjIhFkij8ZFAXPD8E+6qr0TiIZ+VnPh9hKPFIpHcHUJQq7smWIvY0ws+e+dtk2Bd37WDcq4tZ3q7TqjJ5p1IBb4sod/goKH0dn60Hlq/QlGI3zmd+QcDfe5PrTCwb3lOlfFxvr9UpSZY/KBqHmtgvUostJcSr7XK8deOZ7D2sQ8TO8dcFBqKFMnbUM7r9oMMMSo5BZfLCXRLoYf83CDDZgMb7ZzYdDxq9uPZMvkPm9OclG41LMzMh5MT8QjUheAiDJZL6oBtqzC984+xBjqmAaN0C2uPH7XnDncOccZIQdp244fkllRJLFaYIEHJfNvhubjo0AZZeddTJ6cVa+TOPVt3jZwqnbGApjmS6i2Yx5PyIRY/tNmUPZ41NuIXYwDaZSTNdf6mLfe6wWg8DNSJ4v40Wp2kraC267bW9Sl7CMvDsBzLW/+Tbzkbyx+i3rDpLJAiYO2fC6pwKu1HEygF+Vb1gbS8Ds2z1y/UBC/bIgfV6CLXPAo=',
    endpoint_url='https://bedrock-runtime.us-east-1.amazonaws.com'
)

body = json.dumps({
    "prompt": "\n\nHuman: explain black holes to 8th graders\n\nAssistant:",
    "max_tokens_to_sample": 300,
    "temperature": 0.1,
    "top_p": 0.9,
})

modelId = 'anthropic.claude-v2'
accept = 'application/json'
contentType = 'application/json'

response = brt.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

response_body = json.loads(response.get('body').read())

# text
print(response_body.get('completion'))
