CONFIG_RULES = {
    'ACCESS_KEYS_ROTATED': {
        'description': 'Checks if the active access keys are rotated within the number of days specified in maxAccessKeyAge. The rule is NON_COMPLIANT if the access keys have not been rotated for more than maxAccessKeyAge number of days.',
        'trigger_type': 'Periodic'
    },
    'ACCOUNT_PART_OF_ORGANIZATIONS': {
        'description': 'Checks if an AWS account is part of AWS Organizations. The rule is NON_COMPLIANT if an AWS account is not part of AWS Organizations or AWS Organizations master account ID does not match rule parameter MasterAccountId.',
        'trigger_type': 'Periodic'
    },
    'ACM_CERTIFICATE_EXPIRATION_CHECK': {
        'description': 'Checks if AWS Certificate Manager Certificates in your account are marked for expiration within the specified number of days. Certificates provided by ACM are automatically renewed. ACM does not automatically renew certificates that you import. The rule is NON_COMPLIANT if your certificates are about to expire.',
        'trigger_type': 'Configuration changes'
    },
    'ALB_DESYNC_MODE_CHECK': {
        'description': 'Checks if an Application Load Balancer (ALB) is configured with a user defined desync mitigation mode. The rule is NON_COMPLIANT if ALB desync mitigation mode does not match with the user defined desync mitigation mode.',
        'trigger_type': 'Configuration changes'
    },
    'ALB_HTTP_DROP_INVALID_HEADER_ENABLED': {
        'description': 'Checks if rule evaluates AWS Application Load Balancers (ALB) to ensure they are configured to drop http headers. The rule is NON_COMPLIANT if the value of routing.http.drop_invalid_header_fields.enabled is set to false.',
        'trigger_type': 'Configuration changes'
    },
    'ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK': {
        'description': 'Checks if HTTP to HTTPS redirection is configured on all HTTP listeners of Application Load Balancers. The rule is NON_COMPLIANT if one or more HTTP listeners of Application Load Balancer do not have HTTP to HTTPS redirection configured. The rule is also NON_COMPLIANT if one of more HTTP listeners have forwarding to an HTTP listener instead of redirection.',
        'trigger_type': 'Periodic'
    },
    'ALB_WAF_ENABLED': {
        'description': 'Checks if Web Application Firewall (WAF) is enabled on Application Load Balancers (ALBs). This rule is NON_COMPLIANT if key: waf.enabled is set to false.',
        'trigger_type': 'Configuration changes'
    },
    'API_GW_ASSOCIATED_WITH_WAF': {
        'description': 'Checks if an Amazon API Gateway API stage is using an AWS WAF Web ACL. This rule is NON_COMPLIANT if an AWS WAF Web ACL is not used or if a used AWS Web ACL does not match what is listed in the rule parameter.',
        'trigger_type': 'Configuration changes'
    },
    'API_GW_CACHE_ENABLED_AND_ENCRYPTED': {
        'description': 'Checks that all methods in Amazon API Gateway stages have cache enabled and cache encrypted. The rule is NON_COMPLIANT if any method in Amazon API Gateway stage is not configured to cache or the cache is not encrypted.',
        'trigger_type': 'Configuration changes',
    },
    'API_GW_ENDPOINT_TYPE_CHECK': {
        'description': 'Checks if Amazon API Gateway APIs are of the type specified in the rule parameter endpointConfigurationType. The rule returns NON_COMPLIANT if the REST API does not match the endpoint type configured in the rule parameter.',
        'trigger_type': 'Configuration changes'
    },
    'API_GW_EXECUTION_LOGGING_ENABLED': {
        'description': 'Checks that all methods in Amazon API Gateway stage has logging enabled. The rule is NON_COMPLIANT if logging is not enabled. The rule is NON_COMPLIANT if loggingLevel is neither ERROR nor INFO.',
        'trigger_type': 'Configuration changes'
    },
    'API_GW_SSL_ENABLED': {
        'description': 'Checks if a REST API stage uses an Secure Sockets Layer (SSL) certificate. This rule is NON_COMPLIANT if the REST API stage does not have an associated SSL certificate.',
        'trigger_type': 'Configuration changes'
    },
    'API_GW_XRAY_ENABLED': {
        'description': 'Checks if AWS X-Ray tracing is enabled on Amazon API Gateway REST APIs. The rule is COMPLIANT if X-Ray tracing is enabled and NON_COMPLIANT otherwise.',
        'trigger_type': 'Configuration changes'
    },
    'APPROVED_AMIS_BY_ID': {
        'description': 'Checks if running instances are using specified AMIs. Specify a list of approved AMI IDs. Running instances with AMIs that are not on this list are NON_COMPLIANT.',
        'trigger_type': 'Configuration changes'
    },
    'APPROVED_AMIS_BY_TAG': {
        'description': 'Configuration changes',
        'trigger_type': "Checks if running instances are using specified AMIs. Specify the tags that identify the AMIs. Running instances with AMIs that don't have at least one of the specified tags are NON_COMPLIANT."
    },
    'AURORA_LAST_BACKUP_RECOVERY_POINT_CREATED': {
        'description': 'Checks if a recovery point was created for Amazon Aurora DB clusters. The rule is NON_COMPLIANT if the Amazon Relational Database Service (Amazon RDS) DB Cluster does not have a corresponding recovery point created within the specified time period.',
        'trigger_type': 'Periodic'
    },
    'AURORA_MYSQL_BACKTRACKING_ENABLED': {
        'description': 'Checks if an Amazon Aurora MySQL cluster has backtracking enabled. This rule is NON_COMPLIANT if the Aurora cluster uses MySQL and it does not have backtracking enabled.',
        'trigger_type': 'Configuration changes'
    },
    'AURORA_RESOURCES_PROTECTED_BY_BACKUP_PLAN': {
        'description': 'Checks if Amazon Aurora DB clusters are protected by a backup plan. The rule is NON_COMPLIANT if the Amazon Relational Database Service (Amazon RDS) Database Cluster is not protected by a backup plan.',
        'trigger_type': 'Periodic'
    },
    'AUTOSCALING_CAPACITY_REBALANCING': {
        'description': 'Checks if Capacity Rebalancing is enabled for Amazon EC2 Auto Scaling groups that use multiple instance types. The rule is NON_COMPLIANT if capacity Rebalancing is not enabled.',
        'trigger_type': 'Configuration changes'
    },
    'AUTOSCALING_GROUP_ELB_HEALTHCHECK_REQUIRED': {
        'description': 'Checks if your Auto Scaling groups that are associated with a Classic Load Balancer are using Elastic Load Balancing health checks. The rule is NON_COMPLIANT if the Auto Scaling groups are not using Elastic Load Balancing health checks.',
        'trigger_type': 'Configuration changes'
    },
    'AUTOSCALING_LAUNCHCONFIG_REQUIRES_IMDSV2': {
        'description': 'Checks whether only IMDSv2 is enabled. This rule is NON_COMPLIANT if the Metadata version is not included in the launch configuration or if both Metadata V1 and V2 are enabled.',
        'trigger_type': 'Configuration changes'
    },
    'AUTOSCALING_LAUNCH_CONFIG_HOP_LIMIT': {
        'description': 'Checks the number of network hops that the metadata token can travel. This rule is NON_COMPLIANT if the Metadata response hop limit is greater than 1.',
        'trigger_type': 'Configuration changes'
    },
    'AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED': {
        'description': "Checks if Amazon EC2 Auto Scaling groups have public IP addresses enabled through Launch Configurations. This rule is NON_COMPLIANT if the Launch Configuration for an Auto Scaling group has AssociatePublicIpAddress set to 'true'.",
        'trigger_type': 'Configuration changes'
    },
    'AUTOSCALING_LAUNCH_TEMPLATE': {
        'description': 'Checks if an Amazon Elastic Compute Cloud (EC2) Auto Scaling group is created from an EC2 launch template. The rule is NON_COMPLIANT if the scaling group is not created from an EC2 launch template.',
        'trigger_type': 'Configuration changes'
    },
    'AUTOSCALING_MULTIPLE_AZ': {
        'description': 'Checks if the Auto Scaling group spans multiple Availability Zones. The rule is NON_COMPLIANT if the Auto Scaling group does not span multiple Availability Zones.',
        'trigger_type': 'Configuration changes'
    },
    'AUTOSCALING_MULTIPLE_INSTANCE_TYPES': {
        'description': 'Checks if an Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling group uses multiple instance types. This rule is NON_COMPLIANT if the Amazon EC2 Auto Scaling group has only one instance type defined.',
        'trigger_type': 'Configuration changes'
    },
    'BACKUP_PLAN_MIN_FREQUENCY_AND_MIN_RETENTION_CHECK': {
        'description': 'Checks if a backup plan has a backup rule that satisfies the required frequency and retention period. The rule is NON_COMPLIANT if recovery points are not created at least as often as the specified frequency or expire before the specified period.',
        'trigger_type': 'Configuration changes'
    },
    'BACKUP_RECOVERY_POINT_ENCRYPTED': {
        'description': 'Checks if a recovery point is encrypted. The rule is NON_COMPLIANT if the recovery point is not encrypted.',
        'trigger_type': 'Configuration changes'
    },
    'BACKUP_RECOVERY_POINT_MANUAL_DELETION_DISABLED': {
        'description': "Checks if a backup vault has an attached resource-based policy which prevents deletion of recovery points. The rule is NON_COMPLIANT if the Backup Vault does not have resource-based policies or has policies without a suitable 'Deny' statement (statement with backup:DeleteRecoveryPoint, backup:UpdateRecoveryPointLifecycle, and backup:PutBackupVaultAccessPolicy permissions).",
        'trigger_type': 'Configuration changes'
    },
    'BACKUP_RECOVERY_POINT_MINIMUM_RETENTION_CHECK': {
        'description': 'Checks if a recovery point expires no earlier than after the specified period. The rule is NON_COMPLIANT if the recovery point has a retention point that is less than the required retention period.',
        'trigger_type': 'Configuration changes'
    },
    'BEANSTALK_ENHANCED_HEALTH_REPORTING_ENABLED': {
        'description': 'Checks if an AWS Elastic Beanstalk environment is configured for enhanced health reporting. The rule is COMPLIANT if the environment is configured for enhanced health reporting. The rule is NON_COMPLIANT if the environment is configured for basic health reporting.',
        'trigger_type': 'Configuration changes'
    },
    'CLB_DESYNC_MODE_CHECK': {
        'description': 'Checks if Classic Load Balancers (CLB) are configured with a user defined Desync mitigation mode. The rule is NON_COMPLIANT if CLB Desync mitigation mode does not match with user defined Desync mitigation mode.',
        'trigger_type': 'Configuration changes'
    },
    'CLB_MULTIPLE_AZ': {
        'description': 'Checks if a Classic Load Balancer spans multiple Availability Zones (AZs). The rule is NON_COMPLIANT if a Classic Load Balancer spans less than 2 AZs or does not span number of AZs mentioned in the minAvailabilityZones parameter (if provided).',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK': {
        'description': 'Checks if the actual configuration of a Cloud Formation stack differs, or has drifted, from the expected configuration. A stack is considered to have drifted if one or more of its resources differ from their expected configuration. The rule and the stack are COMPLIANT when the stack drift status is IN_SYNC. The rule is NON_COMPLIANT if the stack drift status is DRIFTED.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFORMATION_STACK_NOTIFICATION_CHECK': {
        'description': 'Checks whether your CloudFormation stacks are sending event notifications to an SNS topic. Optionally checks whether specified SNS topics are used.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFRONT_ACCESSLOGS_ENABLED': {
        'description': 'Checks if Amazon CloudFront distributions are configured to capture information from Amazon Simple Storage Service (Amazon S3) server access logs. This rule is NON_COMPLIANT if a CloudFront distribution does not have logging configured.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFRONT_ASSOCIATED_WITH_WAF': {
        'description': 'Checks if Amazon CloudFront distributions are associated with either WAF or WAFv2 web access control lists (ACLs). This rule is NON_COMPLIANT if a CloudFront distribution is not associated with a web ACL.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFRONT_CUSTOM_SSL_CERTIFICATE': {
        'description': 'Checks if the certificate associated with an Amazon CloudFront distribution is the default Secure Sockets Layer (SSL) certificate. This rule is NON_COMPLIANT if a CloudFront distribution uses the default SSL certificate.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFRONT_DEFAULT_ROOT_OBJECT_CONFIGURED': {
        'description': 'Checks if an Amazon CloudFront distribution is configured to return a specific object that is the default root object. The rule is NON_COMPLIANT if Amazon CloudFront distribution does not have a default root object configured.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFRONT_NO_DEPRECATED_SSL_PROTOCOLS': {
        'description': 'Checks if CloudFront distributions are using deprecated SSL protocols for HTTPS communication between CloudFront edge locations and custom origins. This rule is NON_COMPLIANT for a CloudFront distribution if any ‘OriginSslProtocols’ includes ‘SSLv3’.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFRONT_ORIGIN_ACCESS_IDENTITY_ENABLED': {
        'description': 'Checks if Amazon CloudFront distribution with S3 Origin type has Origin Access Identity (OAI) configured. The rule is NON_COMPLIANT if the CloudFront distribution is backed by S3 and any of S3 Origin type is not OAI configured or if the origin is not an S3 bucket.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFRONT_ORIGIN_FAILOVER_ENABLED': {
        'description': 'Checks whether an origin group is configured for the distribution of at least 2 origins in the origin group for Amazon CloudFront. This rule is NON_COMPLIANT if there are no origin groups for the distribution.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFRONT_SNI_ENABLED': {
        'description': 'Checks if Amazon CloudFront distributions are using a custom SSL certificate and are configured to use SNI to serve HTTPS requests. This rule is NON_COMPLIANT if a custom SSL certificate is associated but the SSL support method is a dedicated IP address.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFRONT_TRAFFIC_TO_ORIGIN_ENCRYPTED': {
        'description': 'Checks if Amazon CloudFront distributions are encrypting traffic to custom origins. The rule is NON_COMPLIANT if ‘OriginProtocolPolicy’ is ‘http-only’ or if ‘OriginProtocolPolicy’ is ‘match-viewer’ and ‘ViewerProtocolPolicy’ is ‘allow-all’.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDFRONT_VIEWER_POLICY_HTTPS': {
        'description': "Checks whether your Amazon CloudFront distributions use HTTPS (directly or via a redirection). The rule is NON_COMPLIANT if the value of ViewerProtocolPolicy is set to 'allow-all' for the defaultCacheBehavior or for the cacheBehaviors.",
        'trigger_type': 'Configuration changes'
    },
    'CLOUDTRAIL_S3_DATAEVENTS_ENABLED': {
        'description': 'Checks whether at least one AWS CloudTrail trail is logging Amazon S3 data events for all S3 buckets. The rule is NON_COMPLIANT if trails log data events for S3 buckets is not configured.',
        'trigger_type': 'Periodic'
    },
    'CLOUDTRAIL_SECURITY_TRAIL_ENABLED': {
        'description': 'Checks that there is at least one AWS CloudTrail trail defined with security best practices. This rule is COMPLIANT if there is at least one trail that meets all of the following:',
        'trigger_type': 'Periodic'
    },
    'CLOUDWATCH_ALARM_ACTION_CHECK': {
        'description': 'Checks whether CloudWatch alarms have at least one alarm action, one INSUFFICIENT_DATA action, or one OK action enabled. Optionally, checks whether any of the actions matches one of the specified ARNs.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDWATCH_ALARM_ACTION_ENABLED_CHECK': {
        'description': 'Checks if Amazon CloudWatch alarms actions are in enabled state. The rule is NON_COMPLIANT if the CloudWatch alarms actions are not in enabled state.',
        'trigger_type': 'Configuration changes'
    },
    'CLOUDWATCH_ALARM_RESOURCE_CHECK': {
        'description': 'Checks whether the specified resource type has a CloudWatch alarm for the specified metric. For resource type, you can specify EBS volumes, EC2 instances, RDS clusters, or S3 buckets.',
        'trigger_type': 'Periodic'
    },
    'CLOUDWATCH_ALARM_SETTINGS_CHECK': {
        'description': 'Checks whether CloudWatch alarms with the given metric name have the specified settings.',
        'trigger_type': 'Configuration changes',
    },
    'CLOUDWATCH_LOG_GROUP_ENCRYPTED': {
        'description': 'Checks if a log group in Amazon CloudWatch Logs is encrypted with a AWS Key Management Service (KMS) managed Customer Master Keys (CMK). The rule is NON_COMPLIANT if no AWS KMS CMK is configured on the log groups.',
        'trigger_type': 'Periodic',
    },
    'CLOUD_TRAIL_CLOUD_WATCH_LOGS_ENABLED': {
        'description': 'Checks whether AWS CloudTrail trails are configured to send logs to Amazon CloudWatch logs. The trail is non-compliant if the CloudWatchLogsLogGroupArn property of the trail is empty.',
        'trigger_type': 'Periodic',
    },
    'CLOUD_TRAIL_ENABLED': {
        'description': 'Checks if an AWS CloudTrail trail is enabled in your AWS account. The rule is NON_COMPLIANT if a trail is not enabled. You can specify for the rule to check a specific S3 bucket, SNS topic, and Amazon CloudWatch log group.',
        'trigger_type': 'Periodic',
    },
    'CLOUD_TRAIL_ENCRYPTION_ENABLED': {
        'description': 'Checks if AWS CloudTrail is configured to use the server side encryption (SSE) AWS Key Management Service (AWS KMS) encryption. The rule is COMPLIANT if the KmsKeyId is defined.',
        'trigger_type': 'Periodic',
    },
    'CLOUD_TRAIL_LOG_FILE_VALIDATION_ENABLED': {
        'description': 'Checks whether AWS CloudTrail creates a signed digest file with logs. AWS recommends that the file validation must be enabled on all trails. The rule is noncompliant if the validation is not enabled.',
        'trigger_type': 'Periodic',
    },
    'CMK_BACKING_KEY_ROTATION_ENABLED': {
        'description': 'Checks if automatic key rotation is enabled for every AWS Key Management Service (AWS KMS) customer managed symmetric encryption key. The rule is NON_COMPLIANT if automatic key rotation is not enabled for an AWS KMS customer managed symmetric encryption key.',
        'trigger_type': 'Periodic',
    },
    'CODEBUILD_PROJECT_ARTIFACT_ENCRYPTION': {
        'description': "Checks if an AWS CodeBuild project has encryption enabled for all of its artifacts. The rule is NON_COMPLIANT if 'encryptionDisabled' is set to 'true' for any primary or secondary (if present) artifact configurations.'",
        'trigger_type': 'Configuration changes',
    },
    'CODEBUILD_PROJECT_ENVIRONMENT_PRIVILEGED_CHECK': {
        'description': 'Checks if an AWS CodeBuild project environment has privileged mode enabled. The rule is NON_COMPLIANT for a CodeBuild project if ‘privilegedMode’ is set to ‘true’.',
        'trigger_type': 'Configuration changes',
    },
    'CODEBUILD_PROJECT_ENVVAR_AWSCRED_CHECK': {
        'description': 'Checks whether the project contains environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The rule is NON_COMPLIANT when the project environment variables contains plaintext credentials.',
        'trigger_type': 'Configuration changes',
    },
    'CODEBUILD_PROJECT_LOGGING_ENABLED': {
        'description': "Checks if an AWS CodeBuild project environment has at least one log option enabled. The rule is NON_COMPLIANT if the status of all present log configurations is set to 'DISABLED'.",
        'trigger_type': 'Configuration changes',
    },
    'CODEBUILD_PROJECT_S3_LOGS_ENCRYPTED': {
        'description': 'Checks if a AWS CodeBuild project configured with Amazon S3 Logs has encryption enabled for its logs. The rule is NON_COMPLIANT if ‘encryptionDisabled’ is set to ‘true’ in a S3LogsConfig of a CodeBuild project.',
        'trigger_type': 'Configuration changes',
    },
    'CODEBUILD_PROJECT_SOURCE_REPO_URL_CHECK': {
        'description': 'Checks whether the GitHub or Bitbucket source repository URL contains either personal access tokens or user name and password. The rule is COMPLIANT with the usage of OAuth to grant authorization for accessing GitHub or Bitbucket repositories.',
        'trigger_type': 'Configuration changes',
    },
    'CODEDEPLOY_AUTO_ROLLBACK_MONITOR_ENABLED': {
        'description': 'Checks if the deployment group is configured with automatic deployment rollback and deployment monitoring with alarms attached. The rule is NON_COMPLIANT if AutoRollbackConfiguration or AlarmConfiguration has not been configured or is not enabled.',
        'trigger_type': 'Configuration changes',
    },
    'CODEDEPLOY_EC2_MINIMUM_HEALTHY_HOSTS_CONFIGURED': {
        'description': 'Checks if the deployment group for EC2/On-Premises Compute Platform is configured with a minimum healthy hosts fleet percentage or host count greater than or equal to the input threshold. The rule is NON_COMPLIANT if either is below the threshold.',
        'trigger_type': 'Configuration changes',
    },
    'CODEDEPLOY_LAMBDA_ALLATONCE_TRAFFIC_SHIFT_DISABLED': {
        'description': "Checks if the deployment group for Lambda Compute Platform is not using the default deployment configuration. The rule is NON_COMPLIANT if the deployment group is using the deployment configuration 'CodeDeployDefault.LambdaAllAtOnce'.",
        'trigger_type': 'Configuration changes',
    },
    'CODEPIPELINE_DEPLOYMENT_COUNT_CHECK': {
        'description': 'Checks whether the first deployment stage of the AWS Codepipeline performs more than one deployment. Optionally checks if each of the subsequent remaining stages deploy to more than the specified number of deployments (deploymentLimit).',
        'trigger_type': 'Configuration changes',
    },
    'CODEPIPELINE_REGION_FANOUT_CHECK': {
        'description': 'Checks if each stage in the AWS CodePipeline deploys to more than N times the number of the regions the AWS CodePipeline has deployed in all the previous combined stages, where N is the region fanout number. The first deployment stage can deploy to a maximum of one region and the second deployment stage can deploy to a maximum number specified in the regionFanoutFactor. If you do not provide a regionFanoutFactor, by default the value is three. For example: If 1st deployment stage deploys to one region and 2nd deployment stage deploys to three regions, 3rd deployment stage can deploy to 12 regions, that is, sum of previous stages multiplied by the region fanout (three) number. The rule is NON_COMPLIANT if the deployment is in more than one region in 1st stage or three regions in 2nd stage or 12 regions in 3rd stage.',
        'trigger_type': 'Configuration changes',
    },
    'CW_LOGGROUP_RETENTION_PERIOD_CHECK': {
        'description': 'Checks if Amazon CloudWatch LogGroup retention period is set to specific number of days. The rule is NON_COMPLIANT if the retention period for the log group is less than the MinRetentionTime parameter.',
        'trigger_type': 'Periodic',
    },
    'DAX_ENCRYPTION_ENABLED': {
        'description': 'Checks that Amazon DynamoDB Accelerator (DAX) clusters are encrypted. The rule is NON_COMPLIANT if a DAX cluster is not encrypted',
        'trigger_type': 'Periodic',
    },
    'DB_INSTANCE_BACKUP_ENABLED': {
        'description': 'Checks if RDS DB instances have backups enabled. Optionally, the rule checks the backup retention period and the backup window.',
        'trigger_type': 'Configuration changes',
    },
    'DESIRED_INSTANCE_TENANCY': {
        'description': 'Checks instances for specified tenancy. Specify AMI IDs to check instances that are launched from those AMIs or specify host IDs to check whether instances are launched on those Dedicated Hosts. Separate multiple ID values with commas.',
        'trigger_type': 'Configuration changes',
    },
    'DESIRED_INSTANCE_TYPE': {
        'description': 'Checks whether your EC2 instances are of the specified instance types. For a list of supported Amazon EC2 instance types, see Instance Types in the Amazon EC2 User Guide for Linux Instances.',
        'trigger_type': 'Configuration changes',
    },
    'DMS_REPLICATION_NOT_PUBLIC': {
        'description': 'Checks whether AWS Database Migration Service replication instances are public. The rule is NON_COMPLIANT if PubliclyAccessible field is True.',
        'trigger_type': 'Periodic',
    },
    'DYNAMODB_AUTOSCALING_ENABLED': {
        'description': 'Checks if Auto Scaling or On-Demand is enabled on your DynamoDB tables and/or global secondary indexes. Optionally you can set the read and write capacity units for the table or global secondary index.',
        'trigger_type': 'Periodic',
    },
    'DYNAMODB_IN_BACKUP_PLAN': {
        'description': 'Checks whether Amazon DynamoDB table is present in AWS Backup Plans. The rule is NON_COMPLIANT if Amazon DynamoDB tables are not present in any AWS Backup plan.',
        'trigger_type': 'Periodic',
    },
    'DYNAMODB_LAST_BACKUP_RECOVERY_POINT_CREATED': {
        'description': 'Checks if a recovery point was created for Amazon DynamoDB Tables within the specified period. The rule is NON_COMPLIANT if the DynamoDB Table does not have a corresponding recovery point created within the specified time period.',
        'trigger_type': 'Periodic',
    },
    'DYNAMODB_PITR_ENABLED': {
        'description': 'Checks that point in time recovery (PITR) is enabled for Amazon DynamoDB tables. The rule is NON_COMPLIANT if point in time recovery is not enabled for Amazon DynamoDB tables.',
        'trigger_type': 'Configuration changes',
    },
    'DYNAMODB_RESOURCES_PROTECTED_BY_BACKUP_PLAN': {
        'description': 'Checks if Amazon DynamoDB tables are protected by a backup plan. The rule is NON_COMPLIANT if the DynamoDB Table is not covered by a backup plan.',
        'trigger_type': 'Periodic',
    },
    'DYNAMODB_TABLE_ENCRYPTED_KMS': {
        'description': 'Checks if Amazon DynamoDB table is encrypted with AWS Key Management Service (KMS). The rule is NON_COMPLIANT if Amazon DynamoDB table is not encrypted with AWS KMS. The rule is also NON_COMPLIANT if the encrypted AWS KMS key is not present in kmsKeyArns input parameter.',
        'trigger_type': 'Configuration changes',
    },
    'DYNAMODB_TABLE_ENCRYPTION_ENABLED': {
        'description': 'Checks if the Amazon DynamoDB tables are encrypted and checks their status. The rule is COMPLIANT if the status is enabled or enabling.',
        'trigger_type': 'Configuration changes',
    },
    'DYNAMODB_THROUGHPUT_LIMIT_CHECK': {
        'description': 'Checks if provisioned DynamoDB throughput is approaching the maximum limit for your account. By default, the rule checks if provisioned throughput exceeds a threshold of 80 percent of your account limits.',
        'trigger_type': 'Periodic',
    },
    'EBS_IN_BACKUP_PLAN': {
        'description': 'Check if Amazon Elastic Block Store (Amazon EBS) volumes are added in backup plans of AWS Backup. The rule is NON_COMPLIANT if Amazon EBS volumes are not included in backup plans.',
        'trigger_type': 'Periodic',
    },
    'EBS_LAST_BACKUP_RECOVERY_POINT_CREATED': {
        'description': 'Checks if a recovery point was created for Amazon Elastic Block Store (Amazon EBS). The rule is NON_COMPLIANT if the Amazon EBS volume does not have a corresponding recovery point created within the specified time period.',
        'trigger_type': 'Periodic',
    },
    'EBS_OPTIMIZED_INSTANCE': {
        'description': 'Checks if EBS optimization is enabled for your EC2 instances that can be EBS-optimized. The rule is NON_COMPLIANT if EBS optimization is not enabled for an EC2 instance that can be EBS-optimized.',
        'trigger_type': 'Configuration changes',
    },
    'EBS_RESOURCES_PROTECTED_BY_BACKUP_PLAN': {
        'description': 'Checks if Amazon Elastic Block Store (Amazon EBS) volumes are protected by a backup plan. The rule is NON_COMPLIANT if the Amazon EBS volume is not covered by a backup plan.',
        'trigger_type': 'Periodic',
    },
    'EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK': {
        'description': 'Checks whether Amazon Elastic Block Store (Amazon EBS) snapshots are not publicly restorable. The rule is NON_COMPLIANT if one or more snapshots with RestorableByUserIds field are set to all, that is, Amazon EBS snapshots are public.',
        'trigger_type': 'Periodic',
    },
    'EC2_EBS_ENCRYPTION_BY_DEFAULT': {
        'description': 'Check that Amazon Elastic Block Store (EBS) encryption is enabled by default. The rule is NON_COMPLIANT if the encryption is not enabled.',
        'trigger_type': 'Periodic',
    },
    'EC2_IMDSV2_CHECK': {
        'description': 'Checks whether your Amazon Elastic Compute Cloud (Amazon EC2) instance metadata version is configured with Instance Metadata Service Version 2 (IMDSv2). The rule is NON_COMPLIANT if the HttpTokens is set to optional.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_INSTANCE_DETAILED_MONITORING_ENABLED': {
        'description': 'Checks if detailed monitoring is enabled for EC2 instances. The rule is NON_COMPLIANT if detailed monitoring is not enabled.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_INSTANCE_MANAGED_BY_SSM': {
        'description': 'Checks whether the Amazon EC2 instances in your account are managed by AWS Systems Manager.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_INSTANCE_MULTIPLE_ENI_CHECK': {
        'description': 'Checks if Amazon Elastic Compute Cloud (Amazon EC2) uses multiple ENIs (Elastic Network Interfaces) or Elastic Fabric Adapters (EFAs). This rule is NON_COMPLIANT an Amazon EC2 instance use multiple network interfaces.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_INSTANCE_NO_PUBLIC_IP': {
        'description': 'Checks whether Amazon Elastic Compute Cloud (Amazon EC2) instances have a public IP association. The rule is NON_COMPLIANT if the publicIp field is present in the Amazon EC2 instance configuration item. This rule applies only to IPv4.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_INSTANCE_PROFILE_ATTACHED': {
        'description': 'Checks if an Amazon Elastic Compute Cloud (Amazon EC2) instance has an Identity and Access Management (IAM) profile attached to it. This rule is NON_COMPLIANT if no IAM profile is attached to the Amazon EC2 instance.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_LAST_BACKUP_RECOVERY_POINT_CREATED': {
        'description': 'Checks if a recovery point was created for Amazon Elastic Compute Cloud (Amazon EC2) instances. The rule is NON_COMPLIANT if the Amazon EC2 instance does not have a corresponding recovery point created within the specified time period.',
        'trigger_type': 'Periodic',
    },
    'EC2_MANAGEDINSTANCE_APPLICATIONS_BLACKLISTED': {
        'description': 'Checks if none of the specified applications are installed on the instance. Optionally, specify the version. Newer versions will not be denylisted. Optionally, specify the platform to apply the rule only to instances running that platform.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_MANAGEDINSTANCE_APPLICATIONS_REQUIRED': {
        'description': 'Checks if all of the specified applications are installed on the instance. Optionally, specify the minimum acceptable version. You can also specify the platform to apply the rule only to instances running that platform.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_MANAGEDINSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK': {
        'description': 'Checks if the status of the AWS Systems Manager association compliance is COMPLIANT or NON_COMPLIANT after the association execution on the instance. The rule is compliant if the field status is COMPLIANT. For more information about associations, see What is an association?.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_MANAGEDINSTANCE_INVENTORY_BLACKLISTED': {
        'description': 'Checks whether instances managed by Amazon EC2 Systems Manager are configured to collect blacklisted inventory types.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_MANAGEDINSTANCE_PATCH_COMPLIANCE_STATUS_CHECK': {
        'description': 'Checks whether the compliance status of the AWS Systems Manager patch compliance is COMPLIANT or NON_COMPLIANT after the patch installation on the instance. The rule is compliant if the field status is COMPLIANT.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_MANAGEDINSTANCE_PLATFORM_CHECK': {
        'description': 'Checks whether EC2 managed instances have the desired configurations.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_NO_AMAZON_KEY_PAIR': {
        'description': 'Checks if running Amazon Elastic Compute Cloud (EC2) instances are launched using amazon key pairs. The rule is NON_COMPLIANT if a running EC2 instance is launched with a key pair.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_PARAVIRTUAL_INSTANCE_CHECK': {
        'description': "Checks if the virtualization type of an EC2 instance is paravirtual. This rule is NON_COMPLIANT for an EC2 instance if 'virtualizationType' is set to 'paravirtual'.",
        'trigger_type': 'Configuration changes',
    },
    'EC2_RESOURCES_PROTECTED_BY_BACKUP_PLAN': {
        'description': 'Checks if Amazon Elastic Compute Cloud (Amazon EC2) instances are protected by a backup plan. The rule is NON_COMPLIANT if the Amazon EC2 instance is not covered by a backup plan.',
        'trigger_type': 'Periodic',
    },
    'EC2_SECURITY_GROUP_ATTACHED_TO_ENI': {
        'description': 'Checks if non-default security groups are attached to Elastic network interfaces (ENIs). The rule is NON_COMPLIANT if the security group is not associated with an elastic network interface (ENI).',
        'trigger_type': 'Configuration changes',
    },
    'EC2_SECURITY_GROUP_ATTACHED_TO_ENI_PERIODIC': {
        'description': 'Checks if non-default security groups are attached to Elastic network interfaces (ENIs). The rule is NON_COMPLIANT if the security group is not associated with an elastic network interface (ENI).',
        'trigger_type': 'Periodic',
    },
    'EC2_STOPPED_INSTANCE': {
        'description': 'Checks if there are instances stopped for more than the allowed number of days. The instance is NON_COMPLIANT if the state of the ec2 instance has been stopped for longer than the allowed number of days.',
        'trigger_type': 'Periodic',
    },
    'EC2_TOKEN_HOP_LIMIT_CHECK': {
        'description': 'Checks if an Amazon Elastic Compute Cloud (EC2) instance metadata has a specified token hop limit that is below the desired limit. The rule is NON_COMPLIANT for an instance if it has a hop limit value above the intended limit.',
        'trigger_type': 'Configuration changes',
    },
    'EC2_TRANSIT_GATEWAY_AUTO_VPC_ATTACH_DISABLED': {
        'description': "Checks if Amazon Elastic Compute Cloud (Amazon EC2) Transit Gateways have 'AutoAcceptSharedAttachments' enabled. The rule is NON_COMPLIANT for a Transit Gateway if 'AutoAcceptSharedAttachments' is set to 'enable'.",
        'trigger_type': 'Configuration changes',
    },
    'EC2_VOLUME_INUSE_CHECK': {
        'description': 'Checks if EBS volumes are attached to EC2 instances. Optionally checks if EBS volumes are marked for deletion when an instance is terminated.',
        'trigger_type': 'Configuration changes',
    },
    'ECR_PRIVATE_IMAGE_SCANNING_ENABLED': {
        'description': 'Checks if a private Amazon Elastic Container Registry (ECR) repository has image scanning enabled. The rule is NON_COMPLIANT if image scanning is not enabled for the private ECR repository.',
        'trigger_type': 'Configuration changes',
    },
    'ECR_PRIVATE_LIFECYCLE_POLICY_CONFIGURED': {
        'description': 'Checks if a private Amazon Elastic Container Registry (ECR) repository has at least one lifecycle policy configured. The rule is NON_COMPLIANT if no lifecycle policy is configured for the ECR private repository',
        'trigger_type': 'Configuration changes',
    },
    'ECR_PRIVATE_TAG_IMMUTABILITY_ENABLED': {
        'description': 'Checks if a private Amazon Elastic Container Registry (ECR) repository has tag immutability enabled. This rule is NON_COMPLIANT if tag immutability is not enabled for the private ECR repository.',
        'trigger_type': 'Configuration changes',
    },
    'ECS_AWSVPC_NETWORKING_ENABLED': {
        'description': 'Checks if the networking mode for active ECSTaskDefinitions is set to ‘awsvpc’. This rule is NON_COMPLIANT if active ECSTaskDefinitions is not set to ‘awsvpc’.',
        'trigger_type': 'Configuration changes',
    },
    'ECS_CONTAINERS_NONPRIVILEGED': {
        'description': 'Checks if the privileged parameter in the container definition of ECSTaskDefinitions is set to ‘true’. The rule is NON_COMPLIANT if the privileged parameter is ‘true’.',
        'trigger_type': 'Configuration changes',
    },
    'ECS_CONTAINERS_READONLY_ACCESS': {
        'description': 'Checks if Amazon Elastic Container Service (Amazon ECS) Containers only have read-only access to its root filesystems. The rule is NON_COMPLIANT if the readonlyRootFilesystem parameter in the container definition of ECSTaskDefinitions is set to ‘false’.',
        'trigger_type': 'Configuration changes',
    },
    'ECS_CONTAINER_INSIGHTS_ENABLED': {
        'description': 'Checks if Amazon Elastic Container Service clusters have container insights enabled. The rule is NON_COMPLIANT if container insights are not enabled.',
        'trigger_type': 'Configuration changes',
    },
    'ECS_FARGATE_LATEST_PLATFORM_VERSION': {
        'description': 'Checks if Amazon Elastic Container Service (ECS) Fargate Services is running on the latest Fargate platform version. The rule is NON_COMPLIANT if ECS Service platformVersion not set to LATEST.',
        'trigger_type': 'Configuration changes',
    },
    'ECS_NO_ENVIRONMENT_SECRETS': {
        'description': "Checks if secrets are passed as container environment variables. The rule is NON_COMPLIANT if 1 or more environment variable key matches a key listed in the 'secretKeys' parameter (excluding environmental variables from other locations such as Amazon S3).",
        'trigger_type': 'Configuration changes',
    },
    'ECS_TASK_DEFINITION_LOG_CONFIGURATION': {
        'description': 'Checks if logConfiguration is set on active ECS Task Definitions. This rule is NON_COMPLIANT if an active ECSTaskDefinition does not have the logConfiguration resource defined or the value for logConfiguration is null in at least one container definition.',
        'trigger_type': 'Configuration changes',
    },
    'ECS_TASK_DEFINITION_MEMORY_HARD_LIMIT': {
        'description': 'Checks if Amazon Elastic Container Service (ECS) task definitions have a set memory limit for its container definitions. The rule is NON_COMPLIANT for a task definition if the ‘memory’ parameter is absent for one container definition.',
        'trigger_type': 'Configuration changes',
    },
    'ECS_TASK_DEFINITION_NONROOT_USER': {
        'description': 'Checks if ECSTaskDefinitions specify a user for Amazon Elastic Container Service (Amazon ECS) EC2 launch type containers to run on. The rule is NON_COMPLIANT if the ‘user’ parameter is not present or set to ‘root’.',
        'trigger_type': 'Configuration changes',
    },
    'ECS_TASK_DEFINITION_PID_MODE_CHECK': {
        'description': 'Checks if ECSTaskDefinitions are configured to share a host’s process namespace with its Amazon Elastic Container Service (Amazon ECS) containers. The rule is NON_COMPLIANT if the pidMode parameter is set to ‘host’.',
        'trigger_type': 'Configuration changes',
    },
    'ECS_TASK_DEFINITION_USER_FOR_HOST_MODE_CHECK': {
        'description': "Checks if an Amazon Elastic Container Service (Amazon ECS) task definition with host networking mode has 'privileged' or 'user' container definitions. The rule is NON_COMPLIANT for task definitions with host network mode and container definitions of privileged=false or empty and user=root or empty.",
        'trigger_type': 'Configuration changes',
    },
    'EFS_ACCESS_POINT_ENFORCE_ROOT_DIRECTORY': {
        'description': "Checks if Amazon Elastic File System (Amazon EFS) access points are configured to enforce a root directory. The rule is NON_COMPLIANT if the value of 'Path' is set to '/' (default root directory of the file system).",
        'trigger_type': 'Configuration changes',
    },
    'EFS_ACCESS_POINT_ENFORCE_USER_IDENTITY': {
        'description': "Checks if Amazon Elastic File System (Amazon EFS) access points are configured to enforce a user identity. The rule is NON_COMPLIANT if 'PosixUser' is not defined or if parameters are provided and there is no match in the corresponding parameter.",
        'trigger_type': 'Configuration changes',
    },
    'EFS_ENCRYPTED_CHECK': {
        'description': 'Checks if Amazon Elastic File System (Amazon EFS) is configured to encrypt the file data using AWS Key Management Service (AWS KMS). The rule is NON_COMPLIANT if the encrypted key is set to false on DescribeFileSystems or if the KmsKeyId key on DescribeFileSystems does not match the KmsKeyId parameter.',
        'trigger_type': 'Periodic',
    },
    'EFS_IN_BACKUP_PLAN': {
        'description': 'Checks whether Amazon Elastic File System (Amazon EFS) file systems are added in the backup plans of AWS Backup. The rule is NON_COMPLIANT if EFS file systems are not included in the backup plans.',
        'trigger_type': 'Periodic',
    },
    'EFS_LAST_BACKUP_RECOVERY_POINT_CREATED': {
        'description': 'Checks if a recovery point was created for Amazon Elastic File System (Amazon EFS) File Systems. The rule is NON_COMPLIANT if the Amazon EFS File System does not have a corresponding Recovery Point created within the specified time period.',
        'trigger_type': 'Periodic',
    },
    'EFS_RESOURCES_PROTECTED_BY_BACKUP_PLAN': {
        'description': 'Checks if Amazon Elastic File System (Amazon EFS) File Systems are protected by a backup plan. The rule is NON_COMPLIANT if the EFS File System is not covered by a backup plan.',
        'trigger_type': 'Periodic',
    },
    'EIP_ATTACHED': {
        'description': 'Checks if all Elastic IP addresses that are allocated to an AWS account are attached to EC2 instances or in-use elastic network interfaces (ENIs).',
        'trigger_type': 'Configuration changes',
    },
    'EKS_CLUSTER_OLDEST_SUPPORTED_VERSION': {
        'description': "Checks if an Amazon Elastic Kubernetes Service (EKS) cluster is running the oldest supported version. The rule is NON_COMPLIANT if an EKS cluster is running oldest supported version (equal to the parameter 'oldestVersionSupported').",
        'trigger_type': 'Configuration changes',
    },
    'EKS_CLUSTER_SUPPORTED_VERSION': {
        'description': "Checks if an Amazon Elastic Kubernetes Service (EKS) cluster is running a supported Kubernetes version. This rule is NON_COMPLIANT if an EKS cluster is running an unsupported version (less than the parameter 'oldestVersionSupported').",
        'trigger_type': 'Configuration changes',
    },
    'EKS_ENDPOINT_NO_PUBLIC_ACCESS': {
        'description': 'Checks whether Amazon Elastic Kubernetes Service (Amazon EKS) endpoint is not publicly accessible. The rule is NON_COMPLIANT if the endpoint is publicly accessible.',
        'trigger_type': 'Periodic',
    },
    'EKS_SECRETS_ENCRYPTED': {
        'description': 'Checks if Amazon Elastic Kubernetes Service clusters are configured to have Kubernetes secrets encrypted using AWS Key Management Service (KMS) keys.\n- This rule is COMPLIANT if an EKS cluster has an encryptionConfig with secrets as one of the resources.\n- This rule is also COMPLIANT if the key used to encrypt EKS secrets matches with the parameter.\n- This rule is NON_COMPLIANT if an EKS cluster does not have an encryptionConfig or if the encryptionConfig resources do not include secrets.\n- This rule is also NON_COMPLIANT if the key used to encrypt EKS secrets does not match with the parameter.',
        'trigger_type': 'Periodic',
    },
    'ELASTICACHE_REDIS_CLUSTER_AUTOMATIC_BACKUP_CHECK': {
        'description': 'Check if the Amazon ElastiCache Redis clusters have automatic backup turned on. The rule is NON_COMPLIANT if the SnapshotRetentionLimit for Redis cluster is less than the SnapshotRetentionPeriod parameter. For example: If the parameter is 15 then the rule is non-compliant if the snapshotRetentionPeriod is between 0-15.',
        'trigger_type': 'Periodic',
    },
    'ELASTICSEARCH_ENCRYPTED_AT_REST': {
        'description': 'Checks if Elasticsearch domains have encryption at rest configuration enabled. The rule is NON_COMPLIANT if the EncryptionAtRestOptions field is not enabled.',
        'trigger_type': 'Periodic',
    },
    'ELASTICSEARCH_IN_VPC_ONLY': {
        'description': 'Checks if Elasticsearch domains are in Amazon Virtual Private Cloud (Amazon VPC). The rule is NON_COMPLIANT if an Elasticsearch domain endpoint is public.',
        'trigger_type': 'Periodic',
    },
    'ELASTICSEARCH_LOGS_TO_CLOUDWATCH': {
        'description': 'Checks if Elasticsearch domains are configured to send logs to Amazon CloudWatch Logs. The rule is COMPLIANT if a log is enabled for an Elasticsearch domain. This rule is NON_COMPLIANT if logging is not configured.',
        'trigger_type': 'Configuration changes',
    },
    'ELASTICSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK': {
        'description': 'Check if Elasticsearch nodes are encrypted end to end. The rule is NON_COMPLIANT if the node-to-node encryption is not enabled on the domain.',
        'trigger_type': 'Configuration changes',
    },
    'ELASTIC_BEANSTALK_MANAGED_UPDATES_ENABLED': {
        'description': 'Checks if managed platform updates in an AWS Elastic Beanstalk environment is enabled. The rule is COMPLIANT if the value for ManagedActionsEnabled is set to true. The rule is NON_COMPLIANT if the value for ManagedActionsEnabled is set to false, or if a parameter is provided and its value does not match the existing configurations.',
        'trigger_type': 'Configuration changes',
    },
    'ELBV2_ACM_CERTIFICATE_REQUIRED': {
        'description': 'Checks if Application Load Balancers and Network Load Balancers have listeners that are configured to use certificates from AWS Certificate Manager (ACM). This rule is NON_COMPLIANT if at least 1 load balancer has at least 1 listener that is configured without a certificate from ACM or is configured with a certificate different from an ACM certificate.',
        'trigger_type': 'Periodic',
    },
    'ELBV2_MULTIPLE_AZ': {
        'description': "Checks if an Elastic Load Balancer V2 (Application, Network, or Gateway Load Balancer) has registered instances from multiple Availability Zones (AZ's). The rule is NON_COMPLIANT if an Elastic Load Balancer V2 has instances registered in less than 2 AZ's.",
        'trigger_type': 'Configuration changes',
    },
    'ELB_ACM_CERTIFICATE_REQUIRED': {
        'description': 'Checks if the Classic Load Balancers use SSL certificates provided by AWS Certificate Manager. To use this rule, use an SSL or HTTPS listener with your Classic Load Balancer. This rule is only applicable to Classic Load Balancers. This rule does not check Application Load Balancers and Network Load Balancers.',
        'trigger_type': 'Configuration changes',
    },
    'ELB_CROSS_ZONE_LOAD_BALANCING_ENABLED': {
        'description': 'Checks if cross-zone load balancing is enabled for the Classic Load Balancers (CLBs). This rule is NON_COMPLIANT if cross-zone load balancing is not enabled for a CLB.',
        'trigger_type': 'Configuration changes',
    },
    'ELB_CUSTOM_SECURITY_POLICY_SSL_CHECK': {
        'description': 'Checks whether your Classic Load Balancer SSL listeners are using a custom policy. The rule is only applicable if there are SSL listeners for the Classic Load Balancer.',
        'trigger_type': 'Configuration changes',
    },
    'ELB_DELETION_PROTECTION_ENABLED': {
        'description': 'Checks whether an Elastic Load Balancer has deletion protection enabled. The rule is NON_COMPLIANT if deletion_protection.enabled is false.',
        'trigger_type': 'Configuration changes',
    },
    'ELB_LOGGING_ENABLED': {
        'description': 'Checks if the Application Load Balancer and the Classic Load Balancer have logging enabled. The rule is NON_COMPLIANT if the access_logs.s3.enabled is false or access_logs.S3.bucket is not equal to the s3BucketName that you provided.',
        'trigger_type': 'Configuration changes',
    },
    'ELB_PREDEFINED_SECURITY_POLICY_SSL_CHECK': {
        'description': 'Checks whether your Classic Load Balancer SSL listeners are using a predefined policy. The rule is only applicable if there are SSL listeners for the Classic Load Balancer.',
        'trigger_type': 'Configuration changes',
    },
    'ELB_TLS_HTTPS_LISTENERS_ONLY': {
        'description': 'Checks if your Classic Load Balancer is configured with SSL or HTTPS listeners.',
        'trigger_type': 'Configuration changes',
    },
    'EMR_KERBEROS_ENABLED': {
        'description': 'Checks if Amazon EMR clusters have Kerberos enabled. The rule is NON_COMPLIANT if a security configuration is not attached to the cluster or the security configuration does not satisfy the specified rule parameters.',
        'trigger_type': 'Periodic',
    },
    'EMR_MASTER_NO_PUBLIC_IP': {
        'description': "Checks if Amazon Elastic MapReduce (EMR) clusters' master nodes have public IPs. The rule is NON_COMPLIANT if the master node has a public IP.",
        'trigger_type': 'Periodic',
    },
    'ENCRYPTED_VOLUMES': {
        'description': 'Checks if the EBS volumes that are in an attached state are encrypted. If you specify the ID of a KMS key for encryption using the kmsId parameter, the rule checks if the EBS volumes in an attached state are encrypted with that KMS key.',
        'trigger_type': 'Configuration changes',
    },
    'FMS_SHIELD_RESOURCE_POLICY_CHECK': {
        'description': 'Checks whether an Application Load Balancer, Amazon CloudFront distributions, Elastic Load Balancer or Elastic IP has AWS Shield protection. It also checks if they have web ACL associated for Application Load Balancer and Amazon CloudFront distributions.',
        'trigger_type': 'Configuration changes',
    },
    'FMS_WEBACL_RESOURCE_POLICY_CHECK': {
        'description': 'Checks if the web ACL is associated with an Application Load Balancer, API Gateway stage, or Amazon CloudFront distributions. When AWS Firewall Manager creates this rule, the FMS policy owner specifies the WebACLId in the FMS policy and can optionally enable remediation.',
        'trigger_type': 'Configuration changes',
    },
    'FMS_WEBACL_RULEGROUP_ASSOCIATION_CHECK': {
        'description': 'Checks if the rule groups associate with the web ACL at the correct priority. The correct priority is decided by the rank of the rule groups in the ruleGroups parameter. When AWS Firewall Manager creates this rule, it assigns the highest priority 0 followed by 1, 2, and so on. The FMS policy owner specifies the ruleGroups rank in the FMS policy and can optionally enable remediation.',
        'trigger_type': 'Configuration changes',
    },
    'FSX_LAST_BACKUP_RECOVERY_POINT_CREATED': {
        'description': 'Checks if a recovery point was created for Amazon FSx File Systems. The rule is NON_COMPLIANT if the Amazon FSx File System does not have a corresponding recovery point created within the specified time period.',
        'trigger_type': 'Periodic',
    },
    'FSX_RESOURCES_PROTECTED_BY_BACKUP_PLAN': {
        'description': 'Checks if Amazon FSx File Systems are protected by a backup plan. The rule is NON_COMPLIANT if the Amazon FSx File System is not covered by a backup plan.',
        'trigger_type': 'Periodic',
    },
    'GUARDDUTY_ENABLED_CENTRALIZED': {
        'description': 'Checks if Amazon GuardDuty is enabled in your AWS account and region. If you provide an AWS account for centralization, the rule evaluates the Amazon GuardDuty results in the centralized account. The rule is COMPLIANT when Amazon GuardDuty is enabled.',
        'trigger_type': 'Periodic',
    },
    'GUARDDUTY_NON_ARCHIVED_FINDINGS': {
        'description': 'Checks whether Amazon GuardDuty has findings that are non archived. The rule is NON_COMPLIANT if Amazon GuardDuty has non archived low/medium/high severity findings older than the specified number in the daysLowSev/daysMediumSev/daysHighSev parameter.',
        'trigger_type': 'Periodic',
    },
    'IAM_CUSTOMER_POLICY_BLOCKED_KMS_ACTIONS': {
        'description': 'Checks if the managed AWS Identity and Access Management (IAM) policies that you create do not allow blocked actions on AWS KMS keys. The rule is NON_COMPLIANT if any blocked action is allowed on AWS KMS keys by the managed IAM policy.',
        'trigger_type': 'Configuration changes',
    },
    'IAM_GROUP_HAS_USERS_CHECK': {
        'description': 'Checks whether IAM groups have at least one IAM user.',
        'trigger_type': 'Configuration changes',
    },
    'IAM_INLINE_POLICY_BLOCKED_KMS_ACTIONS': {
        'description': 'Checks that the inline policies attached to your IAM users, roles, and groups do not allow blocked actions on all AWS Key Management Service (KMS) keys. The rule is NON_COMPLIANT if any blocked action is allowed on all KMS keys in an inline policy.',
        'trigger_type': 'Configuration changes',
    },
    'IAM_NO_INLINE_POLICY_CHECK': {
        'description': 'Checks that inline policy feature is not in use. The rule is NON_COMPLIANT if an AWS Identity and Access Management (IAM) user, IAM role or IAM group has any inline policy.',
        'trigger_type': 'Configuration changes',
    },
    'IAM_PASSWORD_POLICY': {
        'description': 'Checks if the account password policy for IAM users meets the specified requirements indicated in the parameters. This rule is NON_COMPLIANT if the account password policy does not meet the specified requirements.',
        'trigger_type': 'Periodic',
    },
    'IAM_POLICY_BLACKLISTED_CHECK': {
        'description': 'Checks if for each IAM resource, a policy ARN in the input parameter is attached to the IAM resource. The rule is NON_COMPLIANT if the policy ARN is attached to the IAM resource. AWS Config marks the resource as COMPLIANT if the IAM resource is part of the exceptionList parameter irrespective of the presence of the policy ARN.',
        'trigger_type': 'Configuration changes',
    },
    'IAM_POLICY_IN_USE': {
        'description': 'Checks whether the IAM policy ARN is attached to an IAM user, or a group with one or more IAM users, or an IAM role with one or more trusted entity.',
        'trigger_type': 'Periodic',
    },
    'IAM_POLICY_NO_STATEMENTS_WITH_ADMIN_ACCESS': {
        'description': 'Checks if AWS Identity and Access Management (IAM) policies that you create have Allow statements that grant permissions to all actions on all resources. The rule is NON_COMPLIANT if any customer managed IAM policy statement includes "Effect": "Allow" with "Action": "*" over "Resource": "*".',
        'trigger_type': 'Configuration changes',
    },
    'IAM_POLICY_NO_STATEMENTS_WITH_FULL_ACCESS': {
        'description': 'Checks if AWS Identity and Access Management (IAM) policies that you create grant permissions to all actions on individual AWS resources. The rule is NON_COMPLIANT if any customer managed IAM policy allows full access to at least 1 AWS service.',
        'trigger_type': 'Configuration changes',
    },
    'IAM_ROLE_MANAGED_POLICY_CHECK': {
        'description': 'Checks if all AWS managed policies specified in the list of managed policies are attached to the AWS Identity and Access Management (IAM) role. The rule is NON_COMPLIANT if an AWS managed policy is not attached to the IAM role.',
        'trigger_type': 'Configuration changes',
    },
    'IAM_ROOT_ACCESS_KEY_CHECK': {
        'description': 'Checks if the root user access key is available. The rule is COMPLIANT if the user access key does not exist. Otherwise, NON_COMPLIANT.',
        'trigger_type': 'Periodic',
    },
    'IAM_USER_GROUP_MEMBERSHIP_CHECK': {
        'description': 'Checks whether IAM users are members of at least one IAM group.',
        'trigger_type': 'Configuration changes',
    },
    'IAM_USER_MFA_ENABLED': {
        'description': 'Checks whether the AWS Identity and Access Management users have multi-factor authentication (MFA) enabled.',
        'trigger_type': 'Periodic',
    },
    'IAM_USER_NO_POLICIES_CHECK': {
        'description': 'Checks that none of your IAM users have policies attached. IAM users must inherit permissions from IAM groups or roles. The rule is NONCOMPLIANT if there is at least one IAM user with policies attached.',
        'trigger_type': 'Configuration changes',
    },
    'IAM_USER_UNUSED_CREDENTIALS_CHECK': {
        'description': 'Checks if your AWS Identity and Access Management (IAM) users have passwords or active access keys that have not been used within the specified number of days you provided. The rule is NON_COMPLIANT if there are inactive accounts not recently used.',
        'trigger_type': 'Periodic',
    },
    'INCOMING_SSH_DISABLED': {
        'description': 'Checks if the incoming SSH traffic for the security groups is accessible. The rule is COMPLIANT when IP addresses of the incoming SSH traffic in the security groups are restricted (CIDR other than 0.0.0.0/0). This rule applies only to IPv4.',
        'trigger_type': 'Configuration changes',
    },
    'INSTANCES_IN_VPC': {
        'description': 'Checks if your EC2 instances belong to a virtual private cloud (VPC). Optionally, you can specify the VPC ID to associate with your instances',
        'trigger_type': 'Configuration changes',
    },
    'INTERNET_GATEWAY_AUTHORIZED_VPC_ONLY': {
        'description': 'Checks that Internet gateways (IGWs) are only attached to an authorized Amazon Virtual Private Cloud (VPCs). The rule is NON_COMPLIANT if IGWs are not attached to an authorized VPC.',
        'trigger_type': 'Configuration changes',
    },
    'KINESIS_STREAM_ENCRYPTED': {
        'description': "Checks if Amazon Kinesis streams are encrypted at rest with server-side encryption. The rule is NON_COMPLIANT for a Kinesis stream if 'StreamEncryption' is not present.",
        'trigger_type': 'Configuration changes',
    },
    'KMS_CMK_NOT_SCHEDULED_FOR_DELETION': {
        'description': 'Checks if AWS KMS keys are not scheduled for deletion in AWS Key Management Service (AWS KMS). The rule is NON_COMPLAINT if KMS keys are scheduled for deletion.',
        'trigger_type': 'Periodic',
    },
    'LAMBDA_CONCURRENCY_CHECK': {
        'description': 'Checks whether the AWS Lambda function is configured with function-level concurrent execution limit. The rule is NON_COMPLIANT if the Lambda function is not configured with function-level concurrent execution limit.',
        'trigger_type': 'Configuration changes',
    },
    'LAMBDA_DLQ_CHECK': {
        'description': 'Checks whether an AWS Lambda function is configured with a dead-letter queue. The rule is NON_COMPLIANT if the Lambda function is not configured with a dead-letter queue.',
        'trigger_type': 'Configuration changes',
    },
    'LAMBDA_FUNCTION_PUBLIC_ACCESS_PROHIBITED': {
        'description': 'Checks if the AWS Lambda function policy attached to the Lambda resource prohibits public access. If the Lambda function policy allows public access it is NON_COMPLIANT.',
        'trigger_type': 'Configuration changes',
    },
    'LAMBDA_FUNCTION_SETTINGS_CHECK': {
        'description': "Checks if the AWS Lambda function settings for runtime, role, timeout, and memory size match the expected values. The rule ignores functions with the 'Image' package type. The rule is NON_COMPLIANT if the Lambda function settings do not match the expected values.",
        'trigger_type': 'Configuration changes',
    },
    'LAMBDA_INSIDE_VPC': {
        'description': 'Checks whether an AWS Lambda function is allowed access to an Amazon Virtual Private Cloud. The rule is NON_COMPLIANT if the Lambda function is not VPC enabled.',
        'trigger_type': 'Configuration changes',
    },
    'LAMBDA_VPC_MULTI_AZ_CHECK': {
        'description': 'Checks if Lambda has more than 1 availability zone associated. The rule is NON_COMPLIANT if only 1 availability zone is associated with the Lambda or the number of availability zones associated is less than number specified in the optional parameter.',
        'trigger_type': 'Configuration changes',
    },
    'MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS': {
        'description': 'Checks whether AWS Multi-Factor Authentication (MFA) is enabled for all AWS Identity and Access Management (IAM) users that use a console password. The rule is compliant if MFA is enabled.',
        'trigger_type': 'Periodic',
    },
    'MULTI_REGION_CLOUD_TRAIL_ENABLED': {
        'description': 'Checks if there is at least one multi-region AWS CloudTrail. The rule is NON_COMPLIANT if the trails do not match input parameters. The rule is NON_COMPLIANT if the ExcludeManagementEventSources field is not empty or if AWS CloudTrail is configured to exclude management events such as AWS KMS events or Amazon RDS Data API events.',
        'trigger_type': 'Periodic',
    },
    'NACL_NO_UNRESTRICTED_SSH_RDP': {
        'description': 'Checks if default ports for SSH/RDP ingress traffic for network access control lists (NACLs) is unrestricted. The rule is NON_COMPLIANT if a NACL inbound entry allows a source TCP or UDP CIDR block for ports 22 or 3389.',
        'trigger_type': 'Configuration changes',
    },
    'NETFW_POLICY_DEFAULT_ACTION_FRAGMENT_PACKETS': {
        'description': 'Checks if an AWS Network Firewall policy is configured with a user defined stateless default action for fragmented packets. The rule is NON_COMPLIANT if stateless default action for fragmented packets does not match with user defined default action.',
        'trigger_type': 'Configuration changes',
    },
    'NETFW_POLICY_DEFAULT_ACTION_FULL_PACKETS': {
        'description': 'Checks if an AWS Network Firewall policy is configured with a user defined default stateless action for full packets. This rule is NON_COMPLIANT if default stateless action for full packets does not match with user defined default stateless action.',
        'trigger_type': 'Configuration changes',
    },
    'NETFW_POLICY_RULE_GROUP_ASSOCIATED': {
        'description': 'Check AWS Network Firewall policy is associated with stateful OR stateless rule groups. This rule is NON_COMPLIANT if no stateful or stateless rule groups are associated with the Network Firewall policy else COMPLIANT if any one of the rule group exists.',
        'trigger_type': 'Configuration changes',
    },
    'NETFW_STATELESS_RULE_GROUP_NOT_EMPTY': {
        'description': 'Checks if a Stateless Network Firewall Rule Group contains rules. The rule is NON_COMPLIANT if there are no rules in a Stateless Network Firewall Rule Group.',
        'trigger_type': 'Configuration changes',
    },
    'NLB_CROSS_ZONE_LOAD_BALANCING_ENABLED': {
        'description': 'Checks if cross-zone load balancing is enabled on Network Load Balancers (NLBs). The rule is NON_COMPLIANT if cross-zone load balancing is not enabled for an NLB.',
        'trigger_type': 'Configuration changes',
    },
    'NO_UNRESTRICTED_ROUTE_TO_IGW': {
        'description': "Checks if there are public routes in the route table to an Internet Gateway (IGW). The rule is NON_COMPLIANT if a route to an IGW has a destination CIDR block of '0.0.0.0/0' or '::/0' or if a destination CIDR block does not match the rule parameter.",
        'trigger_type': 'Configuration changes',
    },
    'OPENSEARCH_ACCESS_CONTROL_ENABLED': {
        'description': 'Checks if Amazon OpenSearch Service domains have fine-grained access control enabled. The rule is NON_COMPLIANT if AdvancedSecurityOptions is not enabled for the OpenSearch Service domain.',
        'trigger_type': 'Configuration changes',
    },
    'OPENSEARCH_AUDIT_LOGGING_ENABLED': {
        'description': 'Checks if Amazon OpenSearch Service domains have audit logging enabled. The rule is NON_COMPLIANT if an OpenSearch Service domain does not have audit logging enabled.',
        'trigger_type': 'Configuration changes',
    },
    'OPENSEARCH_DATA_NODE_FAULT_TOLERANCE': {
        'description': "Checks if Amazon OpenSearch Service domains are configured with at least three data nodes and zoneAwarenessEnabled is true. The rule is NON_COMPLIANT for an OpenSearch domain if 'instanceCount' is less than 3 or 'zoneAwarenessEnabled' is set to 'false'.",
        'trigger_type': 'Configuration changes',
    },
    'OPENSEARCH_ENCRYPTED_AT_REST': {
        'description': 'Checks if Amazon OpenSearch Service domains have encryption at rest configuration enabled. The rule is NON_COMPLIANT if the EncryptionAtRestOptions field is not enabled.',
        'trigger_type': 'Configuration changes',
    },
    'OPENSEARCH_HTTPS_REQUIRED': {
        'description': "Checks whether connections to OpenSearch domains are using HTTPS. The rule is NON_COMPLIANT if the Amazon OpenSearch domain 'EnforceHTTPS' is not 'true' or is 'true' and 'TLSSecurityPolicy' is not in 'tlsPolicies'.",
        'trigger_type': 'Configuration changes',
    },
    'OPENSEARCH_IN_VPC_ONLY': {
        'description': 'Checks if Amazon OpenSearch Service domains are in an Amazon Virtual Private Cloud (VPC). The rule is NON_COMPLIANT if an OpenSearch Service domain endpoint is public.',
        'trigger_type': 'Configuration changes',
    },
    'OPENSEARCH_LOGS_TO_CLOUDWATCH': {
        'description': 'Checks if Amazon OpenSearch Service domains are configured to send logs to Amazon CloudWatch Logs. The rule is NON_COMPLIANT if logging is not configured.',
        'trigger_type': 'Configuration changes',
    },
    'OPENSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK': {
        'description': 'Check if Amazon OpenSearch Service nodes are encrypted end to end. The rule is NON_COMPLIANT if the node-to-node encryption is not enabled on the domain',
        'trigger_type': 'Configuration changes',
    },
    'RDS_AUTOMATIC_MINOR_VERSION_UPGRADE_ENABLED': {
        'description': "Checks if Amazon Relational Database Service (RDS) database instances are configured for automatic minor version upgrades. The rule is NON_COMPLIANT if the value of 'autoMinorVersionUpgrade' is false.",
        'trigger_type': 'Configuration changes',
    },
    'RDS_CLUSTER_DEFAULT_ADMIN_CHECK': {
        'description': 'Checks if an Amazon Relational Database Service (Amazon RDS) database cluster has changed the admin username from its default value. The rule is NON_COMPLIANT if the admin username is set to the default value.',
        'trigger_type': 'Configuration changes',
    },
    'RDS_CLUSTER_DELETION_PROTECTION_ENABLED': {
        'description': 'Checks if an Amazon Relational Database Service (Amazon RDS) cluster has deletion protection enabled. This rule is NON_COMPLIANT if an RDS cluster does not have deletion protection enabled.',
        'trigger_type': 'Configuration changes',
    },
    'RDS_CLUSTER_IAM_AUTHENTICATION_ENABLED': {
        'description': 'Checks if an Amazon RDS Cluster has AWS Identity and Access Management (IAM) authentication enabled. The rule is NON_COMPLIANT if an RDS Cluster does not have IAM authentication enabled.',
        'trigger_type': 'Configuration changes',
    },
    'RDS_CLUSTER_MULTI_AZ_ENABLED': {
        'description': 'Checks if Multi-AZ replication is enabled on Amazon Aurora and Hermes clusters managed by Amazon Relational Database Service (Amazon RDS). This rule is NON_COMPLIANT if an Amazon RDS instance is not configured with Multi-AZ.',
        'trigger_type': 'Configuration changes',
    },
    'RDS_DB_SECURITY_GROUP_NOT_ALLOWED': {
        'description': 'Checks if there are any Amazon Relational Database Service (RDS) DB security groups that are not the default DB security group. The rule is NON_COMPLIANT is there are any DB security groups that are not the default DB security group.',
        'trigger_type': 'Configuration changes',
    },
    'RDS_ENHANCED_MONITORING_ENABLED': {
        'description': 'Checks whether enhanced monitoring is enabled for Amazon Relational Database Service (Amazon RDS) instances.',
        'trigger_type': 'Configuration changes',
    },
    'RDS_INSTANCE_DEFAULT_ADMIN_CHECK': {
        'description': 'Checks if an Amazon Relational Database Service (Amazon RDS) database has changed the admin username from its default value. This rule will only run on RDS database instances. The rule is NON_COMPLIANT if the admin username is set to the default value.',
        'trigger_type': 'Configuration changes',
    },
    'RDS_INSTANCE_DELETION_PROTECTION_ENABLED': {
        'description': 'Checks if an Amazon Relational Database Service (Amazon RDS) instance has deletion protection enabled. This rule is NON_COMPLIANT if an Amazon RDS instance does not have deletion protection enabled i.e deletionProtection is set to fals',
        'trigger_type': 'Configuration changes',
    },
    'RDS_INSTANCE_IAM_AUTHENTICATION_ENABLED': {
        'description': 'Checks if an Amazon Relational Database Service (Amazon RDS) instance has AWS Identity and Access Management (IAM) authentication enabled. This rule is NON_COMPLIANT if an Amazon RDS instance does not have AWS IAM authentication enabled.',
        'trigger_type': 'Configuration changes'
    },
    'RDS_INSTANCE_PUBLIC_ACCESS_CHECK': {
      'description': 'Checks whether the Amazon Relational Database Service (RDS) instances are not publicly accessible. The rule is non-compliant if the publiclyAccessible field is true in the instance configuration item.',
      'trigger_type': 'Configuration changes'
    },
    'RDS_IN_BACKUP_PLAN': {
        'description': 'Checks whether Amazon RDS database is present in back plans of AWS Backup. The rule is NON_COMPLIANT if Amazon RDS databases are not included in any AWS Backup plan.',
        'trigger_type': 'Periodic',
    },
    'RDS_LAST_BACKUP_RECOVERY_POINT_CREATED': {
        'description': 'Checks if a recovery point was created for Amazon Relational Database Service (Amazon RDS). The rule is NON_COMPLIANT if the Amazon RDS instance does not have a corresponding recovery point created within the specified time period.',
        'trigger_type': 'Periodic',
    },
    'RDS_LOGGING_ENABLED': {
        'description': 'Checks that respective logs of Amazon Relational Database Service (Amazon RDS) are enabled. The rule is NON_COMPLIANT if any log types are not enabled.',
        'trigger_type': 'Configuration changes',
    },
    'RDS_MULTI_AZ_SUPPORT': {
        'description': 'Checks whether high availability is enabled for your RDS DB instances.\nIn a Multi-AZ deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone. For more information, see High Availability (Multi-AZ) in the Amazon RDS User Guide.',
        'trigger_type': 'Configuration changes',
    },
    'RDS_RESOURCES_PROTECTED_BY_BACKUP_PLAN': {
        'description': 'Checks if Amazon Relational Database Service (Amazon RDS) instances are protected by a backup plan. The rule is NON_COMPLIANT if the Amazon RDS Database instance is not covered by a backup plan.',
        'trigger_type': 'Periodic',
    },
    'RDS_SNAPSHOTS_PUBLIC_PROHIBITED': {
        'description': 'Checks if Amazon Relational Database Service (Amazon RDS) snapshots are public. The rule is NON_COMPLIANT if any existing and new Amazon RDS snapshots are public.',
        'trigger_type': 'Configuration changes',
    },
    'RDS_SNAPSHOT_ENCRYPTED': {
        'description': 'Checks whether Amazon Relational Database Service (Amazon RDS) DB snapshots are encrypted. The rule is NON_COMPLIANT, if the Amazon RDS DB snapshots are not encrypted.',
        'trigger_type': 'Configuration changes',
    },
    'RDS_STORAGE_ENCRYPTED': {
        'description': 'Checks whether storage encryption is enabled for your RDS DB instances.',
        'trigger_type': 'Configuration changes',
    },
    'REDSHIFT_AUDIT_LOGGING_ENABLED': {
        'description': "Checks if Amazon Redshift clusters are logging audits to a specific bucket. The rule is NON_COMPLIANT if audit logging is not enabled for a Redshift cluster or if the 'bucketNames' parameter is provided but the audit logging destination does not match.",
        'trigger_type': 'Configuration changes',
    },
    'REDSHIFT_BACKUP_ENABLED': {
        'description': 'Checks that Amazon Redshift automated snapshots are enabled for clusters. The rule is NON_COMPLIANT if the value for automatedSnapshotRetentionPeriod is greater than MaxRetentionPeriod or less than MinRetentionPeriod or the value is 0.',
        'trigger_type': 'Configuration changes',
    },
    'REDSHIFT_CLUSTER_CONFIGURATION_CHECK': {
        'description': 'Checks whether Amazon Redshift clusters have the specified settings.',
        'trigger_type': 'Configuration changes',
    },
    'REDSHIFT_CLUSTER_KMS_ENABLED': {
        'description': 'Checks if Amazon Redshift clusters are using a specified AWS Key Management Service (AWS KMS) key for encryption. The rule is COMPLIANT if encryption is enabled and the cluster is encrypted with the key provided in the kmsKeyArn parameter. The rule is NON_COMPLIANT if the cluster is not encrypted or encrypted with another key.',
        'trigger_type': 'Configuration changes',
    },
    'REDSHIFT_CLUSTER_MAINTENANCESETTINGS_CHECK': {
        'description': 'Checks whether Amazon Redshift clusters have the specified maintenance settings.',
        'trigger_type': 'Configuration changes',
    },
    'REDSHIFT_CLUSTER_PUBLIC_ACCESS_CHECK': {
        'description': 'Checks whether Amazon Redshift clusters are not publicly accessible. The rule is NON_COMPLIANT if the publiclyAccessible field is true in the cluster configuration item.',
        'trigger_type': 'Configuration changes',
    },
    'REDSHIFT_DEFAULT_ADMIN_CHECK': {
        'description': 'Checks if an Amazon Redshift cluster has changed the admin username from its default value. The rule is NON_COMPLIANT if the admin username for a Redshift cluster is set to “awsuser” or if the username does not match what is listed in parameter.',
        'trigger_type': 'Configuration changes',
    },
    'REDSHIFT_DEFAULT_DB_NAME_CHECK': {
        'description': "Checks if a Redshift cluster has changed its database name from the default value. The rule is NON_COMPLIANT if the database name for a Redshift cluster is set to “dev”, or if the optional parameter is provided and the database name does not match.",
        'trigger_type': 'Configuration changes',
    },
    'REDSHIFT_ENHANCED_VPC_ROUTING_ENABLED': {
        'description': "Checks if Amazon Redshift cluster has 'enhancedVpcRouting' enabled. The rule is NON_COMPLIANT if 'enhancedVpcRouting' is not enabled or if the configuration.enhancedVpcRouting field is 'false'.",
        'trigger_type': 'Configuration changes',
    },
    'REDSHIFT_REQUIRE_TLS_SSL': {
        'description': 'Checks whether Amazon Redshift clusters require TLS/SSL encryption to connect to SQL clients. The rule is NON_COMPLIANT if any Amazon Redshift cluster has parameter require_SSL not set to true.',
        'trigger_type': 'Configuration changes',
    },
    'REQUIRED_TAGS': {
        'description': 'Checks if your resources have the tags that you specify. For example, you can check whether your Amazon EC2 instances have the CostCenter tag. Separate multiple values with commas. You can check up to 6 tags at a time.\nThe AWS-managed AWS Systems Manager automation document AWS-SetRequiredTags does not work as a remediation with this rule. You will need to create your own custom Systems Manager automation documentation for remediation',
        'trigger_type': 'Configuration changes',
    },
    'RESTRICTED_INCOMING_TRAFFIC': {
        'description': 'Checks if the security groups in use do not allow unrestricted incoming TCP traffic to the specified ports. The rule is COMPLIANT when the IP addresses for inbound TCP connections are restricted to the specified ports. This rule applies only to IPv4.',
        'trigger_type': 'Configuration changes',
    },
    'ROOT_ACCOUNT_HARDWARE_MFA_ENABLED': {
        'description': 'Checks if your AWS account is enabled to use multi-factor authentication (MFA) hardware device to sign in with root credentials. The rule is NON_COMPLIANT if any virtual MFA devices are permitted for signing in with root credentials.',
        'trigger_type': 'Periodic',
    },
    'ROOT_ACCOUNT_MFA_ENABLED': {
        'description': 'Checks whether the root user of your AWS account requires multi-factor authentication for console sign-in.',
        'trigger_type': 'Periodic',
    },
    'S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS': {
        'description': 'Checks if the required public access block settings are configured from account level. The rule is only NON_COMPLIANT when the fields set below do not match the corresponding fields in the configuration item.',
        'trigger_type': 'Configuration changes',
    },
    'S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS_PERIODIC': {
        'description': 'Checks if the required public access block settings are configured from account level.',
        'trigger_type': 'Periodic',
    },
    'S3_BUCKET_ACL_PROHIBITED': {
        'description': 'Checks if Amazon Simple Storage Service (Amazon S3) Buckets allow user permissions through access control lists (ACLs). The rule is NON_COMPLIANT if ACLs are configured for user access in Amazon S3 Buckets.',
        'trigger_type': 'Configuration changes',
    },
    'S3_BUCKET_BLACKLISTED_ACTIONS_PROHIBITED': {
        'description': 'Checks if an Amazon Simple Storage Service (Amazon S3) bucket policy does not allow blocklisted bucket-level and object-level actions on resources in the bucket for principals from other AWS accounts. For example, the rule checks that the Amazon S3 bucket policy does not allow another AWS account to perform any s3:GetBucket* actions and s3:DeleteObject on any object in the bucket. The rule is NON_COMPLIANT if any blocklisted actions are allowed by the Amazon S3 bucket policy.',
        'trigger_type': 'Configuration changes',
    },
    'S3_BUCKET_DEFAULT_LOCK_ENABLED': {
        'description': 'Checks whether Amazon S3 bucket has lock enabled, by default. The rule is NON_COMPLIANT if the lock is not enabled.',
        'trigger_type': 'Configuration changes',
    },
    'S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED': {
        'description': 'Checks if Amazon Simple Storage Service (Amazon S3) buckets are publicly accessible. This rule is NON_COMPLIANT if an Amazon S3 bucket is not listed in the excludedPublicBuckets parameter and bucket level settings are public.',
        'trigger_type': 'Configuration changes',
    },
    'S3_BUCKET_LOGGING_ENABLED': {
        'description': 'Checks whether logging is enabled for your S3 buckets.',
        'trigger_type': 'Configuration changes',
    },
    'S3_BUCKET_POLICY_GRANTEE_CHECK': {
        'description': 'Checks that the access granted by the Amazon S3 bucket is restricted by any of the AWS principals, federated users, service principals, IP addresses, or VPCs that you provide. The rule is COMPLIANT if a bucket policy is not present.\nFor example, if the input parameter to the rule is the list of two principals: 111122223333 and 444455556666 and the bucket policy specifies that only 111122223333 can access the bucket, then the rule is COMPLIANT. With the same input parameters: If the bucket policy specifies that 111122223333 and 444455556666 can access the bucket, it is also compliant. However, if the bucket policy specifies that 999900009999 can access the bucket, the rule is NON-COMPLIANT.',
        'trigger_type': 'Configuration changes',
    },
    'S3_BUCKET_POLICY_NOT_MORE_PERMISSIVE': {
        'description': 'Checks if your Amazon Simple Storage Service bucket policies do not allow other inter-account permissions than the control Amazon S3 bucket policy that you provide.',
        'trigger_type': 'Configuration changes',
    },
    'S3_BUCKET_PUBLIC_READ_PROHIBITED': {
        'description': 'Checks if your Amazon S3 buckets do not allow public read access. The rule checks the Block Public Access settings, the bucket policy, and the bucket access control list (ACL).\nThe rule is compliant when both of the following are true:\n- The Block Public Access setting restricts public policies or the bucket policy does not allow public read access.\n- The Block Public Access setting restricts public ACLs or the bucket ACL does not allow public read access.\nThe rule is noncompliant when:\n- If the Block Public Access setting does not restrict public policies, AWS Config evaluates whether the policy allows public read access. If the policy allows public read access, the rule is noncompliant.\n- If the Block Public Access setting does not restrict public bucket ACLs, AWS Config evaluates whether the bucket ACL allows public read access. If the bucket ACL allows public read access, the rule is noncompliant.',
        'trigger_type': 'Configuration changes and Periodic',
    },
    'S3_BUCKET_PUBLIC_WRITE_PROHIBITED': {
        'description': 'Checks if your Amazon S3 buckets do not allow public write access. The rule checks the Block Public Access settings, the bucket policy, and the bucket access control list (ACL).\nThe rule is compliant when both of the following are true:\n- The Block Public Access setting restricts public policies or the bucket policy does not allow public write access.\n- The Block Public Access setting restricts public ACLs or the bucket ACL does not allow public write access.\nThe rule is noncompliant when:\n- If the Block Public Access setting does not restrict public policies, AWS Config evaluates whether the policy allows public write access. If the policy allows public write access, the rule is noncompliant.\n- If the Block Public Access setting does not restrict public bucket ACLs, AWS Config evaluates whether the bucket ACL allows public write access. If the bucket ACL allows public write access, the rule is noncompliant.',
        'trigger_type': 'Configuration changes and Periodic',
    },
    'S3_BUCKET_REPLICATION_ENABLED': {
        'description': 'Checks if your Amazon S3 buckets have replication rules enabled. The rule is NON_COMPLIANT if an S3 bucket does not have a replication rule or has a replication rule that is not enabled.',
        'trigger_type': 'Configuration changes',
    },
    'S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED': {
        'description': 'Checks if your Amazon S3 bucket either has the Amazon S3 default encryption enabled or that the Amazon S3 bucket policy explicitly denies put-object requests without server side encryption that uses AES-256 or AWS Key Management Service. The rule is NON_COMPLIANT if your Amazon S3 bucket is not encrypted by default.',
        'trigger_type': 'Configuration changes',
    },
    'S3_BUCKET_SSL_REQUESTS_ONLY': {
        'description': 'Checks if Amazon S3 buckets have policies that require requests to use Secure Socket Layer (SSL). The rule is COMPLIANT if buckets explicitly deny access to HTTP requests. The rule is NON_COMPLIANT if bucket policies allow HTTP requests.',
        'trigger_type': 'Configuration changes',
    },
    'S3_BUCKET_VERSIONING_ENABLED': {
        'description': 'Checks if versioning is enabled for your S3 buckets. Optionally, the rule checks if MFA delete is enabled for your S3 buckets.',
        'trigger_type': 'Configuration changes',
    },
    'S3_DEFAULT_ENCRYPTION_KMS': {
        'description': 'Checks whether the Amazon S3 buckets are encrypted with AWS Key Management Service(AWS KMS). The rule is NON_COMPLIANT if the Amazon S3 bucket is not encrypted with AWS KMS key.',
        'trigger_type': 'Configuration changes',
    },
    'S3_EVENT_NOTIFICATIONS_ENABLED': {
        'description': 'Checks if Amazon S3 Events Notifications are enabled on an S3 bucket. The rule is NON_COMPLIANT if S3 Events Notifications are not set on a bucket, or if the event type or destination do not match the eventTypes and destinationArn parameters.',
        'trigger_type': 'Configuration changes',
    },
    'S3_LAST_BACKUP_RECOVERY_POINT_CREATED': {
        'description': 'Checks if a recovery point was created for Amazon Simple Storage Service (Amazon S3). The rule is NON_COMPLIANT if the Amazon S3 bucket does not have a corresponding recovery point created within the specified time period.',
        'trigger_type': 'Periodic',
    },
    'S3_LIFECYCLE_POLICY_CHECK': {
        'description': 'Checks if a lifecycle rule is configured for an Amazon Simple Storage Service (Amazon S3) bucket. The rule is NON_COMPLIANT if there is no active lifecycle configuration rules or the configuration does not match with the parameter values.',
        'trigger_type': 'Configuration changes',
    },
    'S3_RESOURCES_PROTECTED_BY_BACKUP_PLAN': {
        'description': 'Checks if Amazon Simple Storage Service (Amazon S3) buckets are protected by a backup plan. The rule is NON_COMPLIANT if the Amazon S3 bucket is not covered by a backup plan.',
        'trigger_type': 'Periodic',
    },
    'S3_VERSION_LIFECYCLE_POLICY_CHECK': {
        'description': 'Checks if Amazon Simple Storage Service (Amazon S3) version enabled buckets have lifecycle policy configured. The rule is NON_COMPLIANT if Amazon S3 lifecycle policy is not enabled.',
        'trigger_type': 'Configuration changes',
    },
    'SAGEMAKER_ENDPOINT_CONFIGURATION_KMS_KEY_CONFIGURED': {
        'description': "Checks whether AWS Key Management Service (KMS) key is configured for an Amazon SageMaker endpoint configuration. The rule is NON_COMPLIANT if 'KmsKeyId' is not specified for the Amazon SageMaker endpoint configuration.",
        'trigger_type': 'Periodic',
    },
    'SAGEMAKER_NOTEBOOK_INSTANCE_KMS_KEY_CONFIGURED': {
        'description': "Check whether an AWS Key Management Service (KMS) key is configured for an Amazon SageMaker notebook instance. The rule is NON_COMPLIANT if 'KmsKeyId' is not specified for the Amazon SageMaker notebook instance.",
        'trigger_type': 'Periodic',
    },
    'SAGEMAKER_NOTEBOOK_NO_DIRECT_INTERNET_ACCESS': {
        'description': 'Checks whether direct internet access is disabled for an Amazon SageMaker notebook instance. The rule is NON_COMPLIANT if Amazon SageMaker notebook instances are internet-enabled.',
        'trigger_type': 'Periodic',
    },
    'SECRETSMANAGER_ROTATION_ENABLED_CHECK': {
        'description': 'Checks if AWS Secrets Manager secret has rotation enabled. The rule also checks an optional maximumAllowedRotationFrequency parameter. If the parameter is specified, the rotation frequency of the secret is compared with the maximum allowed frequency. The rule is NON_COMPLIANT if the secret is not scheduled for rotation. The rule is also NON_COMPLIANT if the rotation frequency is higher than the number specified in the maximumAllowedRotationFrequency parameter.',
        'trigger_type': 'Configuration changes',
    },
    'SECRETSMANAGER_SCHEDULED_ROTATION_SUCCESS_CHECK': {
        'description': "Checks if AWS Secrets Manager secrets rotated successfully according to the rotation schedule. Secrets Manager calculates the date the rotation should happen. The rule is NON_COMPLIANT if the date passes and the secret isn't rotated.",
        'trigger_type': 'Configuration changes',
    },
    'SECRETSMANAGER_SECRET_PERIODIC_ROTATION': {
        'description': 'Checks if AWS Secrets Manager secrets have been rotated in the past specified number of days. The rule is NON_COMPLIANT if a secret has not been rotated for more than maxDaysSinceRotation number of days. The default value is 90 days.',
        'trigger_type': 'Periodic',
    },
    'SECRETSMANAGER_SECRET_UNUSED': {
        'description': 'Checks if AWS Secrets Manager secrets have been accessed within a specified number of days. The rule is NON_COMPLIANT if a secret has not been accessed in â€˜unusedForDaysâ€™ number of days. The default value is 90 days.',
        'trigger_type': 'Periodic',
    },
    'SECRETSMANAGER_USING_CMK': {
        'description': 'Checks if all secrets in AWS Secrets Manager are encrypted using the AWS managed key (aws/secretsmanager) or a customer managed key that was created in AWS Key Management Service (AWS KMS). The rule is COMPLIANT if a secret is encrypted using a customer managed key. This rule is NON_COMPLIANT if a secret is encrypted using aws/secretsmanager.',
        'trigger_type': 'Configuration changes',
    },
    'SECURITYHUB_ENABLED': {
        'description': 'Checks that AWS Security Hub is enabled for an AWS Account. The rule is NON_COMPLIANT if AWS Security Hub is not enabled.',
        'trigger_type': 'Periodic',
    },
    'SERVICE_VPC_ENDPOINT_ENABLED': {
        'description': "Checks whether Service Endpoint for the service provided in rule parameter is created for each Amazon VPC. The rule returns NON_COMPLIANT if an Amazon VPC doesn't have a VPC endpoint created for the service.",
        'trigger_type': 'Periodic',
    },
    'SHIELD_ADVANCED_ENABLED_AUTORENEW': {
        'description': 'Checks if AWS Shield Advanced is enabled in your AWS account and this subscription is set to automatically renew.',
        'trigger_type': 'Periodic',
    },
    'SHIELD_DRT_ACCESS': {
        'description': 'Checks if the Shield Response Team (SRT) can access your AWS account. The rule is NON_COMPLIANT if AWS Shield Advanced is enabled but the role for SRT access is not configured.',
        'trigger_type': 'Periodic',
    },
    'SNS_ENCRYPTED_KMS': {
        'description': 'Checks if Amazon SNS topic is encrypted with AWS Key Management Service (AWS KMS). The rule is NON_COMPLIANT if the Amazon SNS topic is not encrypted with AWS KMS. The rule is also NON_COMPLIANT when encrypted KMS key is not present in kmsKeyIds input parameter.',
        'trigger_type': 'Configuration changes',
    },
    'SNS_TOPIC_MESSAGE_DELIVERY_NOTIFICATION_ENABLED': {
        'description': 'Checks if Amazon Simple Notification Service (SNS) logging is enabled for the delivery status of notification messages sent to a topic for the endpoints. The rule is NON_COMPLIANT if the delivery status notification for messages is not enabled.',
        'trigger_type': 'Configuration changes',
    },
    'SSM_DOCUMENT_NOT_PUBLIC': {
        'description': "Checks if AWS Systems Manager documents owned by the account are public. This rule is NON_COMPLIANT if SSM documents with owner 'Self' are public.",
        'trigger_type': 'Periodic',
    },
    'STORAGEGATEWAY_LAST_BACKUP_RECOVERY_POINT_CREATED': {
        'description': 'Checks if a recovery point was created for AWS Storage Gateway volumes. The rule is NON_COMPLIANT if the Storage Gateway volume does not have a corresponding recovery point created within the specified time period.',
        'trigger_type': 'Periodic',
    },
    'SUBNET_AUTO_ASSIGN_PUBLIC_IP_DISABLED': {
        'description': 'Checks if Amazon Virtual Private Cloud (Amazon VPC) subnets are assigned a public IP address. The rule is COMPLIANT if Amazon VPC does not have subnets that are assigned a public IP address. The rule is NON_COMPLIANT if Amazon VPC has subnets that are assigned a public IP address.',
        'trigger_type': 'Configuration changes',
    },
    'VIRTUALMACHINE_LAST_BACKUP_RECOVERY_POINT_CREATED': {
        'description': 'Checks if a recovery point was created for AWS Backup-Gateway VirtualMachines. The rule is NON_COMPLIANT if an AWS Backup-Gateway VirtualMachines does not have a corresponding recovery point created within the specified time period.',
        'trigger_type': 'Periodic',
    },
    'VIRTUALMACHINE_RESOURCES_PROTECTED_BY_BACKUP_PLAN': {
        'description': 'Checks if AWS Backup-Gateway VirtualMachines are protected by a backup plan. The rule is NON_COMPLIANT if the Backup-Gateway VirtualMachine is not covered by a backup plan.',
        'trigger_type': 'Periodic',
    },
    'VPC_DEFAULT_SECURITY_GROUP_CLOSED': {
        'description': 'Checks if the default security group of any Amazon Virtual Private Cloud (VPC) does not allow inbound or outbound traffic. The rule returns NOT_APPLICABLE if the security group is not default. The rule is NON_COMPLIANT if the default security group has one or more inbound or outbound traffic rules.',
        'trigger_type': 'Configuration changes',
    },
    'VPC_FLOW_LOGS_ENABLED': {
        'description': 'Checks whether Amazon Virtual Private Cloud flow logs are found and enabled for Amazon VPC.',
        'trigger_type': 'Periodic',
    },
    'VPC_NETWORK_ACL_UNUSED_CHECK': {
        'description': 'Checks if there are unused network access control lists (network ACLs). The rule is COMPLIANT if each network ACL is associated with a subnet. The rule is NON_COMPLIANT if a network ACL is not associated with a subnet.',
        'trigger_type': 'Configuration changes',
    },
    'VPC_PEERING_DNS_RESOLUTION_CHECK': {
        'description': 'Checks if DNS resolution from accepter/requester VPC to private IP is enabled. The rule is NON_COMPLIANT if DNS resolution from accepter/requester VPC to private IP is not enabled.',
        'trigger_type': 'Configuration changes',
    },
    'VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS': {
        'description': 'Checks whether any security groups with inbound 0.0.0.0/0 have TCP or UDP ports accessible. The rule is NON_COMPLIANT when a security group with inbound 0.0.0.0/0 has a port accessible which is not specified in the rule parameters.',
        'trigger_type': 'Configuration changes',
    },
    'VPC_VPN_2_TUNNELS_UP': {
        'description': 'Checks that both VPN tunnels provided by AWS Site-to-Site VPN are in UP status. The rule returns NON_COMPLIANT if one or both tunnels are in DOWN status.',
        'trigger_type': 'Configuration changes',
    },
    'WAFV2_LOGGING_ENABLED': {
        'description': 'Checks whether logging is enabled on AWS Web Application Firewall (WAFV2) regional and global web access control list (ACLs). The rule is NON_COMPLIANT if the logging is enabled but the logging destination does not match the value of the parameter.',
        'trigger_type': 'Periodic',
    },
    'WAF_CLASSIC_LOGGING_ENABLED': {
        'description': 'Checks if logging is enabled on AWS Web Application Firewall (WAF) classic global web ACLs. This rule is NON_COMPLIANT for a global web ACL, if it does not have logging enabled.',
        'trigger_type': 'Periodic',
    },
    'WAF_GLOBAL_RULEGROUP_NOT_EMPTY': {
        'description': 'Checks if an AWS WAF Classic rule group contains any rules. The rule is NON_COMPLIANT if there are no rules present within a rule group.',
        'trigger_type': 'Configuration changes',
    },
    'WAF_GLOBAL_RULE_NOT_EMPTY': {
        'description': 'Checks if an AWS WAF global rule contains any conditions. The rule is NON_COMPLIANT if no conditions are present within the WAF global rule.',
        'trigger_type': 'Configuration changes',
    },
    'WAF_GLOBAL_WEBACL_NOT_EMPTY': {
        'description': 'Checks whether a WAF Global Web ACL contains any WAF rules or rule groups. This rule is NON_COMPLIANT if a Web ACL does not contain any WAF rule or rule group.',
        'trigger_type': 'Configuration changes',
    },
    'WAF_REGIONAL_RULEGROUP_NOT_EMPTY': {
        'description': 'Checks if WAF Regional rule groups contain any rules. The rule is NON_COMPLIANT if there are no rules present within a WAF Regional rule group.',
        'trigger_type': 'Configuration changes',
    },
    'WAF_REGIONAL_RULE_NOT_EMPTY': {
        'description': 'Checks whether WAF regional rule contains conditions. This rule is COMPLIANT if the regional rule contains at least one condition and NON_COMPLIANT otherwise.',
        'trigger_type': 'Configuration changes',
    },
    'WAF_REGIONAL_WEBACL_NOT_EMPTY': {
        'description': 'Checks if a WAF regional Web ACL contains any WAF rules or rule groups. The rule is NON_COMPLIANT if there are no WAF rules or rule groups present within a Web ACL.',
        'trigger_type': 'Configuration changes',
    }
}
