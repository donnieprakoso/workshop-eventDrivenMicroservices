from aws_cdk import core
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_apigateway as _ag
from aws_cdk import aws_iam as _iam
from aws_cdk import aws_dynamodb as _ddb
from aws_cdk.aws_dynamodb import (Attribute, AttributeType)
from aws_cdk import aws_events as _eb
from aws_cdk import aws_events_targets as _ebt


class CdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Model all required resources
        
        ## IAM Roles
        lambda_role = _iam.Role(
            self,
            id='bdc-lambda-role',
            assumed_by=_iam.ServicePrincipal('lambda.amazonaws.com'))


        ## EventBridge
        eb = _eb.EventBus(
            self, id="bdc-eventbus", event_bus_name="bdc-eventbus")
        eb_pattern = _eb.EventPattern(
            detail_type=["message-received"],
        )

        ## AWS Lambda Functions
        fnLambda_dispatch = _lambda.Function(
            self, 
            "bdc-function-dispatch",
            code=_lambda.AssetCode("../lambda-functions/dispatch-function"),
            handler="app.handler",
            timeout=core.Duration.seconds(60),
            role=lambda_role,
            runtime=_lambda.Runtime.PYTHON_3_8)
        fnLambda_dispatch.add_environment("EVENT_BUS_NAME", eb.event_bus_name)


        fnLambda_consume = _lambda.Function(
            self, 
            "bdc-function-consume",
            code=_lambda.AssetCode("../lambda-functions/consume-function"),
            handler="app.handler",
            role=lambda_role,
            timeout=core.Duration.seconds(60),
            runtime=_lambda.Runtime.PYTHON_3_8)

        policy_statement = _iam.PolicyStatement(effect=_iam.Effect.ALLOW)
        policy_statement.add_actions("logs:CreateLogGroup")
        policy_statement.add_actions("logs:CreateLogStream")
        policy_statement.add_actions("logs:PutLogEvents")
        policy_statement.add_actions("logs:DescribeLogStreams")
        policy_statement.add_actions("events:PutEvents")
        policy_statement.add_resources("*")
        lambda_role.add_to_policy(policy_statement)

        eb_rule = _eb.Rule(
            self,
            id="bdc-eventRule",
            description="A basic rule sample",
            enabled=True,
            event_bus=eb,
            event_pattern=eb_pattern,
            rule_name="BDC-BasicDispatchConsume",
            targets=[_ebt.LambdaFunction(handler=fnLambda_consume)])
