#!/usr/bin/env python3

from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda, core
from aws_cdk import aws_stepfunctions as _sfn
from aws_cdk import aws_stepfunctions_tasks as _tasks


class CdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_role = _iam.Role(
            self,
            id='lab3-om-role',
            assumed_by=_iam.ServicePrincipal('lambda.amazonaws.com'))

        cloudwatch_policy_statement = _iam.PolicyStatement(
            effect=_iam.Effect.ALLOW)
        cloudwatch_policy_statement.add_actions("logs:CreateLogGroup")
        cloudwatch_policy_statement.add_actions("logs:CreateLogStream")
        cloudwatch_policy_statement.add_actions("logs:PutLogEvents")
        cloudwatch_policy_statement.add_actions("logs:DescribeLogStreams")
        cloudwatch_policy_statement.add_resources("*")
        lambda_role.add_to_policy(cloudwatch_policy_statement)

        fn_lambda_approve_reject = aws_lambda.Function(
            self,
            "lab3-om-approve-reject",
            code=aws_lambda.AssetCode(
                "../lambda-functions/approve-reject-application/"),
            handler="app.handler",
            tracing=aws_lambda.Tracing.ACTIVE,
            timeout=core.Duration.seconds(30),
            role=lambda_role,
            runtime=aws_lambda.Runtime.PYTHON_3_8)

        fn_lambda_verify_identity = aws_lambda.Function(
            self,
            "lab3-om-verify-identity",
            code=aws_lambda.AssetCode("../lambda-functions/verify-identity/"),
            handler="app.handler",
            tracing=aws_lambda.Tracing.ACTIVE,
            timeout=core.Duration.seconds(30),
            role=lambda_role,
            runtime=aws_lambda.Runtime.PYTHON_3_8)

        fn_lambda_check_address = aws_lambda.Function(
            self,
            "lab3-om-check-address",
            code=aws_lambda.AssetCode("../lambda-functions/check-address/"),
            handler="app.handler",
            tracing=aws_lambda.Tracing.ACTIVE,
            timeout=core.Duration.seconds(30),
            role=lambda_role,
            runtime=aws_lambda.Runtime.PYTHON_3_8)

        '''
        [INFO] This is a sample how to define the task and integrate with Lambda Functions. You need to create another 2 tasks for respective Lambda functions
        '''
        task_verify_identity = _tasks.LambdaInvoke(
            self,
            "Verify Identity Document",
            lambda_function=fn_lambda_verify_identity,
            output_path="$.Payload"
        )

        '''
        [TASK] Create task and integrate with check address service
        '''

        '''
        [TASK] Create task and integrate with approve/reject service
        '''

        '''
        [TASK] Create two states for approved and rejected. There states need to use Success type and named "Approve Application" and "Reject Application"
        '''

        '''
        [TASK] Create a parallel for task_verify_identity and task_check_address
        '''

        # Next, we add a choice state
        c_human_review = _sfn.Choice(self, "Human review required?")
        c_human_review.when(
            _sfn.Condition.and_(
                _sfn.Condition.boolean_equals("$[0].humanReviewRequired",
                                              False),
                _sfn.Condition.boolean_equals("$[1].humanReviewRequired",
                                              False)), state_approve)
        c_human_review.when(
            _sfn.Condition.or_(
                _sfn.Condition.boolean_equals("$[0].humanReviewRequired",
                                              True),
                _sfn.Condition.boolean_equals("$[1].humanReviewRequired",
                                              True)), task_wait_review)

        # Another choice state to check if the application passed the review
        c_review_approved = _sfn.Choice(self, "Review approved?")
        c_review_approved.when(
            _sfn.Condition.boolean_equals("$.reviewApproved", True),
            state_approve)
        c_review_approved.when(
            _sfn.Condition.boolean_equals("$.reviewApproved", False),
            state_reject)

        task_wait_review.next(c_review_approved)

        definition = s_verification.next(c_human_review)

        '''
        [TASK] Create a state machine and use the definition and timeout of 5 mins. 
        '''


app = core.App()
stack = CdkStack(app, "Lab3-OrchestratingMicroservices")
core.Tags.of(stack).add('Name', 'Lab3-OrchestratingMicroservices')

app.synth()
