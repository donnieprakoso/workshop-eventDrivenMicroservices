#!/usr/bin/env python3

from aws_cdk import aws_events as _eb
from aws_cdk import aws_events_targets as _ebt
from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import core


class CdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Model all required resources
        
        '''
        Define IAM role that will be used for AWS Lambda Functions
        '''
        lambda_role = _iam.Role(
            self,
            id='lab1-bdc-lambda-role',
            assumed_by=_iam.ServicePrincipal('lambda.amazonaws.com'))


        '''
        Define Amazon EventBridge Construct and also pattern to be included later. 
        '''
        eb = _eb.EventBus(
            self, id="lab1-bdc-eventbus", event_bus_name="lab1-bdc-eventbus")
        eb_pattern = _eb.EventPattern(
            detail_type=["message-received"],
        )

        '''
        These lines below define construct for our AWS Lambda Functions. There are 2 Lambda functions that we need to create: dispatch and consume.
        As the dispatch function need to add environment variable, noticed that we add an env_var into AWS Lambda Function that later could be retrieved within the function. 
        '''
        fnLambda_dispatch = _lambda.Function(
            self, 
            "lab1-bdc-function-dispatch",
            code=_lambda.AssetCode("../lambda-functions/dispatch-function"),
            handler="app.handler",
            timeout=core.Duration.seconds(60),
            role=lambda_role,
            runtime=_lambda.Runtime.PYTHON_3_8)
        fnLambda_dispatch.add_environment("EVENT_BUS_NAME", eb.event_bus_name)


        fnLambda_consume = _lambda.Function(
            self, 
            "lab1-bdc-function-consume",
            code=_lambda.AssetCode("../lambda-functions/consume-function"),
            handler="app.handler",
            role=lambda_role,
            timeout=core.Duration.seconds(60),
            runtime=_lambda.Runtime.PYTHON_3_8)

        cw_policy_statement = _iam.PolicyStatement(effect=_iam.Effect.ALLOW)
        cw_policy_statement.add_actions("logs:CreateLogGroup")
        cw_policy_statement.add_actions("logs:CreateLogStream")
        cw_policy_statement.add_actions("logs:PutLogEvents")
        cw_policy_statement.add_actions("logs:DescribeLogStreams")
        cw_policy_statement.add_resources("*")
        lambda_role.add_to_policy(cw_policy_statement)
        
        eb_policy_statement = _iam.PolicyStatement(effect=_iam.Effect.ALLOW)
        eb_policy_statement.add_actions("events:PutEvents")
        eb_policy_statement.add_resources(eb.event_bus_arn)
        lambda_role.add_to_policy(eb_policy_statement)

        '''
        [TASK] Define Amazon EventBridge Rule
        '''


'''
[TASK] Tag your AWS CDK App
'''
