import json
import boto3
import time

gitOpsSource = 'codepipeline.amazonaws.com'
gitOpsPipeline = 'ecs-test'

def gitOpsCheck(source):
    if source != gitOpsSource:
        return False
    else:
        return True

def checkLastDeployment():
    client = boto3.client('codepipeline')
    response = client.list_pipeline_executions(
        pipelineName = gitOpsPipeline,
        maxResults=1)
    print(response)
    
def checkTimeDifference(X):
    pass

def beginPipelineExecution():
    client = boto3.client('codepipeline')
    response = client.start_pipeline_execution(
        name=gitOpsPipeline
    )
    print(response)

def lambda_handler(event, context):
    # TODO implement
    print(event)
    eventSource = event['detail']['sourceIPAddress']
    eventName = event['detail']['eventName']
    eventName = event['detail']['requestParameters']['service']
    print("In Execution")
    print("Event name;"+eventName)
    print("Event Source:"+eventSource)
    validation = gitOpsCheck(eventSource)
    if validation == False:
        checkLastDeployment()
        beginPipelineExecution()
    ##checkTimeDifference
    
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
