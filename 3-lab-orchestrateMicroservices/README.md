# Lab 3: Orchestrating Microservices
[English](README.md) | [Bahasa Indonesia](README-id.md)

Besides choreography, we also need to understand another approach, widely known as orchestration. In this lab, you will build a state machine to manage orchestration between microservices.

In this workshop, you will build a simple banking system that has 4 domains. This system aims to perform assessment and validation before opening an account at a bank.

You will learn how to use AWS Step Functions to build a state machine for orchestration. Apart from that, you can also use several state types provided by AWS Step Functions.

## Diagram
![Lab 3 Diagram](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/3-lab-orchestrateMicroservices/lab3-diagram.png)

## Tasks
These are the tasks that you need to complete. If at some point you are stuck, please refer to the primary reference located at `source/` folder. 

### Step 0: Prepare work folder and boto3
#### Install boto3 library
- Open your terminal
- Run this command
```bash
pip install boto3 
```

#### Preparing work folder
- Navigate to `work/` folder
- You will find 2 sub-directories named `cdk` and `lambda-functions`
- Navigate to `work/lambda-functions/` 
- You will find 3 sub-directories of AWS Lambda Functions. In this workshop, you don't need to work on AWS Lambda Functions.

### Step 1: Building AWS CDK App
#### Navigate to work folder
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

### Step 2: Create two tasks
- You need to create 2 tasks for `check-address` and also `approve-reject` services. 
- You will find there's a task defined for `verify-identity`, use this sample to build other 2 tasks.

> **💡 HINT**   
> - Use LambdaInvoke construct to create a task. Here's the [API reference](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_stepfunctions_tasks/LambdaInvoke.html).
> - If you're not using AWS Lambda function, you can use other available constructs to build a task.

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/3-lab-orchestrateMicroservices/source/cdk/app.py)

### Step 3: Create two states
- You need to create two states and oth categorized as `Succeed` for `approved` and `rejected`. 

> **💡 HINT**
> - Use `Succeed` construct to define the state. Here's the [API reference](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_stepfunctions/Succeed.html).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/3-lab-orchestrateMicroservices/source/cdk/app.py)

### Step 4: Create a parallel
- Create a parallel to run 2 tasks at the same time: `verify-identity` and `check-address`. 
- Use `$.Payload` as the `output_path` to select part of the state to be the output. 

> **💡 HINT**
> - Use `Parallel` construct to run one or more tasks at the same time. Here's the [API reference](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_stepfunctions/Parallel.html).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/3-lab-orchestrateMicroservices/source/cdk/app.py)

### Step 5: Last piece, you need to create a state machine. 
- Use `StateMachine` construct to complete this task. 
- Noticed that the `definition` is already defined, started by `s_verification` and the next destination is `c_human_review`. 

>**💡 HINT**
> - Here's the [API reference](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_stepfunctions/StateMachine.html).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/blob/master/3-lab-orchestrateMicroservices/source/cdk/app.py)

### Step 6: Install all required libraries to build and run CDK app
- Open your terminal
- Navigate to `work/cdk/`
- Create a file named `requirements.txt`. This is a standard method to install any dependencies for Python applications. 
- Add these lines:
```
aws-cdk.core==1.70.0
aws-cdk.aws-iam==1.70.0 
aws-cdk.aws-lambda==1.70.0
aws-cdk.aws-stepfunctions==1.70.0
aws-cdk.aws-stepfunctions-tasks==1.70.0
```

- Install the libraries by executing:
```bash
pip3 install -r requirements.txt
```

### Step 7: Deploy
- Open your terminal
- Navigate to `work/cdk/`
- Deploy the app by executing:
```bash
cdk deploy
```
- At this point, you have your state machine created. Go to the [AWS StepFunctions dashboard](https://ap-southeast-1.console.aws.amazon.com/states/home?) to view your state machines.

### Step 8: Testing
- From AWS StepFunctions dashboard, filter the state machine by typing `lab3`. 
- Click the link to open the state machine.
- Review the definition in visual representation by clicking on the `Definition` tab. It must be look like the diagram above.
- We are going to do 3 scenarios to test the state machine.

![Lab 3: State Machine Visual Definition](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/3-lab-orchestrateMicroservices/lab3-definition.png)
 
#### Testing Scenario 1: Auto Approved
- Click `Start Execution` button on the upper right. 
- On the input, copy and paste JSON below:
```json
{
  "name": "Scenario 1",
  "document": true,
  "address": true,
  "amount": 1000
}
```
- Click `Start Execution` and wait until it's finished.
- Your state machine should automatically approve the application.

![Lab 3: Scenario 1](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/3-lab-orchestrateMicroservices/lab3-scenario1.png)

#### Testing Scenario 2: Approved with Human Review Checking
- Click `New Execution` button on the upper right. 
- On the input, copy and paste JSON below:
```json
{
  "name": "Scenario 2",
  "document": false,
  "address": true,
  "amount": 5000
}
```
- Click `Start Execution` and wait until it's finished.
- Your state machine should went to `Human Review Required` before it went to `Approve Application`

![Lab3: Scenario 2](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/3-lab-orchestrateMicroservices/lab3-scenario2.png)

#### Testing Scenario 3: Rejected with Human Review Checking
- Click `New Execution` button on the upper right. 
- On the input, copy and paste JSON below:
```json
{
  "name": "Scenario 3",
  "document": false,
  "address": false,
  "amount": 10000
}
```
- Click `Start Execution` and wait until it's finished.
- Your state machine should went to `Human Review Required` before it went to `Reject Application`

![Lab3: Scenario 3](https://raw.githubusercontent.com/donnieprakoso/workshop-eventDrivenMicroservices/master/3-lab-orchestrateMicroservices/lab3-scenario3.png)

---

# 🤘🏻Congrats! 
You've just finished the Lab 3.

## Cleaning Up
To clean up all resources, follow these instructions below:
1. Go to `work/cdk/`
2. Run `cdk destroy` command
```bash
cdk destroy
```