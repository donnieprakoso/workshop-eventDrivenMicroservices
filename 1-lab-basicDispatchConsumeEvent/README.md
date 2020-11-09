# Lab 1: Basic Dispatch Consume
In this workshop, you will build 2 AWS Lambda Functions. One AWS Lambda Function (as the producer) will dispatch events, and one AWS Lambda Function (as the consumer) to receive events. In addition to receiving events, Consumer will also print logs to AWS CloudWatch Logs to ensure the flow is going well.

## Diagram

## Tasks
These are the tasks that you need to complete. If at some point you are stuck, please refer to the primary reference located at `source/` folder. 

0. Create subfolders
- Navigate to `work/` folder
- Create 2 sub-directories named `cdk` and `lambda-functions`
- Navigate to `work/lambda-functions/` 
- Create 2 sub-directories named `consume-function` and `dispatch-function` 

1. Create Producer with AWS Lambda
- Navigate to `work/lambda-functions/dispatch-function`
- Create a file named `app.py`
- Create a basic AWS Lambda function that returns "Message dispatched" string.

```python
	def handler(event, context):
		return "Message dispatched"
```
- Send an event to Amazon EventBridge with this following info:
	- Source: bdc-function-dispatch
	- DetailType: message-received
	- Detail: < Need to be in JSON format >
		```json
		{"title":"This is a test message", "test": True} 
		```
	- EventBusName: < Need to obtain from environment variable named: "Event_BUS_NAME" >

**HINT**
- You need to create a client to connect to AWS resources. On Python, you need to use boto3 library. 
- Use put_events() API to send event to Amazon EventBridge. Here's the [link](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html).

2. Create Consumer with AWS Lambda
- Navigate to `work/lambda-functions/dispatch-function`
- Create a file named `app.py`
- Create a basic AWS Lambda function that print the event received to Amazon CloudWatch Logs.
**HINT**
- Python `print` command in AWS Lambda Functions will send the output to Amazon CloudWatch Logs. 

3. Create an AWS CDK app
- Navigate to `work/cdk/`
- Create a file named `cdk.json`
- Open `cdk.json` and write these lines. These lines are to give a set of instruction for AWS CDK on how to build this app.
```json
{
	"app":"python3 app.py",
	"context":{}
}
```
- Open `app.py`. In this file, you see that we are missing few things to make this as a complete code. Read the file thoroughly and go to the next steps below.
- Define Amazon EventBridge Construct and Pattern
This is already been provided in the `app.py` file.
- Define IAM Permissions
This is already been provided in the `app.py` file.
- Define AWS Lambda Construct for Producer
This is already been provided in the `app.py` file.
- Define AWS Lambda Construct for Consumer
This is already been provided in the `app.py` file.
- Define Amazon EventBridge Rule
You'll need to define the Amazon EventBridge rule and attaching to respective constructs. Here are the details that you need to include:
	- enabled: True — < If it's false, then this rule is disabled >
	- event_bus: eb — < Need to add reference to the `eb` variable >
	- event_pattern: eb_pattern — < Need to add a reference to `eb_pattern` >
	-targets: < Need to add reference to fnLambda_consume >
**HINT**
- Defining Amazon EventBridge rule is quite straightforward. Here's the API reference [link](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_events/Rule.html).
- Don't forget to add the target to this rule. Amazon EventBridge provides various integration for AWS services. Here's the API reference [link](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_events_targets/LambdaFunction.html) to attach to AWS Lambda Function.
- Tagging your AWS CDK App. You need to open `app.py` and add these following lines. It's pretty handy to keep these lines so you can tag your CDK app.
```python
app = core.App()
stack = CdkStack(app, "BasicDispatchConsume")
core.Tags.of(stack).add('Name','BasicDispatchConsume')
app.synth()
```
4. Install all required libraries to build and run CDK app
- Navigate to `work/cdk/`
- Create a file named `requirements.txt`. This is a standard method to install any dependencies for Python applications. 
- Add these lines:
```
-e .
aws-cdk.core==1.70.0
aws-cdk.aws-lambda==1.70.0
aws-cdk.aws-apigateway==1.70.0
aws-cdk.aws-iam==1.70.0
aws-cdk.aws-events==1.70.0
aws-cdk.aws-events-targets==1.70.0
```
- Install the libraries by executing:
```bash
pip3 install -r requirements.txt
```
5. Deploy
- Navigate to `work/cdk/`
- Deploy the app by executing:
```bash
cdk deploy
```
6. Testing
- Navigate to AWS Lambda Functions [dashboard](https://ap-southeast-1.console.aws.amazon.com/lambda/home). 
- Make sure that you're in the same AWS region as you deployed your application. 
- Find the **Producer** Lambda function. To filter based on the name, you can type "BasicDispatchConsume" on the filter text input. 
- Open the link which will navigate you to the AWS Lambda Function

> Now we are going to test the Producer function which will trigger an event to Amazon EventBridge and will be consumed by the Consumer function as well as print the logs into CloudWatch. 

- Create a test event by choosing **Test** in the upper right corner
- In the Configure test event page, choose **Create new test event** and in Event template, leave the default Hello World option. Enter an Event name and provide an empty template:
```json
{}
``` 
- Choose **Create** and then choose **Test**.
- Navigate to Amazon CloudWatch [dashboard](https://ap-southeast-1.console.aws.amazon.com/cloudwatch/home).
- Find the logs for the **Consumer** function. To filter based on the name, you can type "BasicDispatchConsume" on the filter text input. 
- Find and open the latest Log Stream.
- If you see there's a JSON with data from event passed by the **Producer** via Amazon EventBridge, then you've completed this workshop.

## Cleaning Up
To clean up all resources, run this command
```bash
cdk destroy
```
