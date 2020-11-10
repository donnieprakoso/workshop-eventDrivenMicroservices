#!/usr/bin/env python3

from aws_cdk import aws_apigateway as _ag
from aws_cdk import aws_dynamodb as _ddb
from aws_cdk import aws_events as _eb
from aws_cdk import aws_events_targets as _ebt
from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda, core
from aws_cdk.aws_dynamodb import Attribute, AttributeType


class CdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        dynamodb_table = _ddb.Table(
            self,
            id="lab2-cm-ddb",
            table_name="lab2-cm-order-status",
            partition_key=Attribute(name='ID', type=AttributeType.STRING),
            removal_policy=core.RemovalPolicy.DESTROY  # NOT for production
        )

        eb = _eb.EventBus(
            self, id="lab2-cm-eventbus", event_bus_name="lab2-cm-eventbus")

        lambda_role = _iam.Role(
            self,
            id='lab2-cm-role',
            assumed_by=_iam.ServicePrincipal('lambda.amazonaws.com'))

        dynamodb_policy_statement = _iam.PolicyStatement(
            effect=_iam.Effect.ALLOW)
        dynamodb_policy_statement.add_actions("dynamodb:*")
        dynamodb_policy_statement.add_resources(dynamodb_table.table_arn)
        lambda_role.add_to_policy(dynamodb_policy_statement)

        eventbridge_policy_statement = _iam.PolicyStatement(
            effect=_iam.Effect.ALLOW)
        eventbridge_policy_statement.add_actions("events:*")
        eventbridge_policy_statement.add_resources(eb.event_bus_arn)
        lambda_role.add_to_policy(eventbridge_policy_statement)

        cloudwatch_policy_statement = _iam.PolicyStatement(
            effect=_iam.Effect.ALLOW)
        cloudwatch_policy_statement.add_actions("logs:CreateLogGroup")
        cloudwatch_policy_statement.add_actions("logs:CreateLogStream")
        cloudwatch_policy_statement.add_actions("logs:PutLogEvents")
        cloudwatch_policy_statement.add_actions("logs:DescribeLogStreams")
        cloudwatch_policy_statement.add_resources("*")
        lambda_role.add_to_policy(cloudwatch_policy_statement)

        fn_lambda_invoice_service = aws_lambda.Function(
            self,
            "lab2-cm-invoiceService",
            code=aws_lambda.AssetCode("../lambda-functions/invoice-service/"),
            handler="app.lambda_handler",
            tracing=aws_lambda.Tracing.ACTIVE,
            timeout=core.Duration.seconds(30),
            role=lambda_role,
            runtime=aws_lambda.Runtime.PYTHON_3_8)
        fn_lambda_invoice_service.add_environment("TABLE_NAME",
                                                  dynamodb_table.table_name)

        fn_lambda_fulfilment_service = aws_lambda.Function(
            self,
            "lab2-cm-fulfilmentService",
            code=aws_lambda.AssetCode(
                "../lambda-functions/fulfilment-service/"),
            handler="app.lambda_handler",
            tracing=aws_lambda.Tracing.ACTIVE,
            timeout=core.Duration.seconds(30),
            role=lambda_role,
            runtime=aws_lambda.Runtime.PYTHON_3_8)
        fn_lambda_fulfilment_service.add_environment(
            "TABLE_NAME", dynamodb_table.table_name)
        fn_lambda_fulfilment_service.add_environment("EVENTBUS_NAME",
                                                eb.event_bus_name)

        fn_lambda_forecasting_service = aws_lambda.Function(
            self,
            "lab2-cm-forecastingService",
            code=aws_lambda.AssetCode(
                "../lambda-functions/forecasting-service/"),
            handler="app.lambda_handler",
            tracing=aws_lambda.Tracing.ACTIVE,
            timeout=core.Duration.seconds(30),
            role=lambda_role,
            runtime=aws_lambda.Runtime.PYTHON_3_8)
        fn_lambda_forecasting_service.add_environment(
            "TABLE_NAME", dynamodb_table.table_name)

        fn_lambda_order_service = aws_lambda.Function(
            self,
            "lab2-cm-orderService",
            code=aws_lambda.AssetCode("../lambda-functions/order-service/"),
            handler="app.lambda_handler",
            timeout=core.Duration.seconds(30),
            tracing=aws_lambda.Tracing.ACTIVE,
            role=lambda_role,
            runtime=aws_lambda.Runtime.PYTHON_3_8)
        fn_lambda_order_service.add_environment("TABLE_NAME",
                                                dynamodb_table.table_name)
        fn_lambda_order_service.add_environment("EVENTBUS_NAME",
                                                eb.event_bus_name)

        fn_lambda_logistic_service = aws_lambda.Function(
            self,
            "lab2-cm-logisticService",
            code=aws_lambda.AssetCode("../lambda-functions/logistic-service/"),
            handler="app.lambda_handler",
            timeout=core.Duration.seconds(30),
            tracing=aws_lambda.Tracing.ACTIVE,
            role=lambda_role,
            runtime=aws_lambda.Runtime.PYTHON_3_8)
        fn_lambda_logistic_service.add_environment("TABLE_NAME",
                                                   dynamodb_table.table_name)

        '''
        [TASK] Create EventBridge pattern for order_created
        '''

        '''
        [TASK] Create EventBridge rule for order_created. Define 3 targets into this rule: invoice service, fulfilment service, forecasting service.
        '''

        '''
        [ADDITIONAL TASK] Create EventBridge pattern for fulfilment_completed
        '''
        
        '''
        [ADDITIONAL TASK] Create EventBridge rule for fulfilment completed. Define 1 target into this rule: invoice service, fulfilment service, forecasting service.
        '''
        
        
        api = _ag.RestApi(
            self,
            id='lab2-cm-api-gateway',
        )
        api_lambda_integration = _ag.LambdaIntegration(fn_lambda_order_service)
        api.root.add_resource('order').add_method('GET',
                                                  api_lambda_integration)


app = core.App()
stack = CdkStack(app, "Lab2-ChoreographyMicroservices")
core.Tags.of(stack).add('Name', 'Lab2-ChoreographyMicroservices')
app.synth()
