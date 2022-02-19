
## version 0.1

- Terraform setup
    - Open library for functionality
    - Private library for deploying (contains keys)
- Data is stored in s3
    - Json events
- Lambda to receive text/email
    - SES -> SNS -> Lambda -> S3
- Store event data from text/email
- Script to generate basic report

