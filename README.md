## Translation
[English](README.md) | [Bahasa Indonesia](README-id.md)

## 🚀 Welcome to the Event-Driven Microservices workshop with AWS

In this workshop, you will build and deploy a series of simple microservices with an event-driven architecture approach.

The main objective of this workshop is to build a foundation of extending and scaling microservices architecture by leveraging synchronous and asynchronous communication — with choreography and orchestration patterns.

The content of this workshop will be updated regularly and if you have questions or find issues in this workshop, please file them as an Issue.

## Feedback is Welcome
Please help us to provide your feedback. Participants who complete the surveys from AWS Innovate Online Conference - Modern Applications Edition will receive a gift code for USD25 in AWS credits. AWS credits will be sent via email by 30 November, 2021. [Feedback link is here](https://amazonmr.au1.qualtrics.com/jfe/form/SV_6x7UgBL9FHn59dA?Session=HOL7).

## Workshop Structure
This repo consists of 3 workshops:

#### **Lab 1: Basic Dispatch and Consume**
In this workshop, you will build 2 AWS Lambda Functions. One AWS Lambda Function (as the Producer) will dispatch events, and one AWS Lambda Function (as the Consumer) to receive events. In addition to receiving events, the Consumer will also print logs to AWS CloudWatch Logs to ensure the flow is going well.

[💻 Start This Workshop](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/1-lab-basicDispatchConsumeEvent)

#### **Lab 2: Building Choreographed Microservices**
As a continuation of the previous workshop, in this workshop, you will do a more complex system that uses multiple microservices. You will learn how to combine synchronous and asynchronous communication as it's a commonly used pattern in building microservices.

You will build an HTTP API with Amazon API Gateway and AWS Lambda Function. In the background, the HTTP API will dispatch events to Amazon EventBridge for backend processing. The event will be consumed by 4 other microservices represented by AWS Lambda Functions. Communication between microservices on the backend will run asynchronously by applying a choreographed approach using Amazon EventBridge.

[💻 Start This Workshop](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/2-lab-choreographMicroservices)

#### **Lab 3: Orchestrating Microservices**
Besides choreography, we also need to understand another approach, widely known as orchestration. In this lab, you will build a state machine to manage orchestration between microservices.

In this workshop, you will build a simple banking system that has 4 domains. This system aims to perform assessment and validation before opening an account at a bank.

You will learn how to use AWS Step Functions to build a state machine for orchestration. Apart from that, you can also use several state types provided by AWS Step Functions.

[💻 Start This Workshop](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/3-lab-orchestrateMicroservices)

---
## Workshop Level
This workshop welcomes developers of all levels. 

This workshop is structured as puzzles in which you need to complete a set of partial codes into a complete code. It is an intended design to help build an understanding of a specific concept. Also, to help you get familiar with common resources needed to develop with AWS services.

---
## 🛑 First Thing First
If this is your first time using this workshop, this section is an important piece that you need to read before moving on.

⚠️
>  Please make sure that your development environment meets the requirements below and properly configured before starting any of the workshops.

**Workshop Requirements**

Requirement | More Information | Notes  
---|---|---   
Active AWS Account | [Link](https://aws.amazon.com/) |  Mandatory requirement   
AWS CDK | [Link](https://aws.amazon.com/cdk/) |Require Node JS   
AWS CLI | [Link](https://aws.amazon.com/cli/) |Require active    AWS account. Please configure your account as described on this    [page](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) 
Python 3.8 | [Link](https://www.python.org/downloads/release/python-380/) |Most of the workshop will be using Python 3.8   
Boto3 | [Link](https://aws.amazon.com/sdk-for-python/) | Amazon Web Services (AWS) Software Development Kit (SDK) for Python
Node JS 10.30 or later | [Link](https://nodejs.org/en/download/current/) |Node.js versions 13.0.0 through 13.6.0 are not compatible with the AWS CDK


⚠️
> Since we will be using AWS CDK extensively in this workshop, please properly configure AWS CDK for your development environment. 

**If you haven't done that, please follow the instruction [here](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html).**

In summary, here's a quick checklist to complete the required checking.  
- [ ] Installed AWS CLI  
- [ ] Configured AWS CLI with `aws configure`  
- [ ] Installed Node JS  
- [ ] Installed AWS CDK with `npm install -g aws-cdk`  
- [ ] Configured AWS CDK with `cdk bootstrap`  

## Navigating The Workshop
Lab Name | Level | Duration
------------ | ------------- | -------------
[Lab 0 - Requirements Checking](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/0-requirements-checking) | All Levels | 15 mins
[Lab 1 - Basic Dispatch Consume](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/1-lab-basicDispatchConsumeEvent) | Beginner | 15 mins
[Lab 2 - Building Choreographed Microservices](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/2-lab-choreographMicroservices) | Intermediate | 30 mins
[Lab 3 - Orchestrating Microservices](https://github.com/donnieprakoso/workshop-eventDrivenMicroservices/tree/master/3-lab-orchestrateMicroservices) | Intermediate | 15 mins

### **💡 HINT** and **😕 Are you stuck?**
For the more complex tasks that you need to complete, there will be a **💡 HINT** to guide you on how to solve it. Most of the time, it will also include link(s) for further reading. 

Please remember that if you are stuck and can't move to the next step, you can always see the main reference file to see the solution. For easy access, **😕 Are you stuck?** will guide you directly to the solution.

## AWS Services
Some of the services from AWS that are used in this workshop are as follows:  
- [AWS CDK](https://aws.amazon.com/cdk/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

## ⚠️  Cleaning Up
This workshop uses AWS services that are mostly covered by the Free Tier allowance - ONLY if your account is less than 12 months old. For accounts passed the free tier eligibility, it may incur some costs. To minimize the cost, make sure you **delete resources used in this workshop when you are finished**.

All of the labs in this workshop use a standardized cleaning method with AWS CDK.
1. Go to each lab
2. Change the directory to `cdk /`
3. Run `cdk destroy`
4. If in some cases it fails, you need to go to [AWS CloudFormation](https://console.aws.amazon.com/cloudformation/) to manually delete the stack.


## Feedback is Welcome
Please help us to provide your feedback. Participants who complete the surveys from AWS Innovate Online Conference - Modern Applications Edition will receive a gift code for USD25 in AWS credits. AWS credits will be sent via email by 30 November, 2021. [Feedback link is here](https://amazonmr.au1.qualtrics.com/jfe/form/SV_6x7UgBL9FHn59dA?Session=HOL7).

