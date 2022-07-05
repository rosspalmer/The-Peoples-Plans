# The-Peoples-Plans

Prod Site: TODO

## Dev plan

- Terraform setup
  - Open library for functionality
    - Private library for deploying (contains keys)

- Data is stored in s3
  - Json events
  - Encrypted
    - Review base s3 encryption vs kms

- Data apps for processing ingest links / messages
  - Lambda based (python/scala)
  - EC2 + Docker based (python/scala/spark/whatever)

- Lambda to receive and store text/email
  - SES -> SNS -> Lambda -> S3
  - Access restriction by sender

- Amplify for web app
  - Public 
  - Static / SPA (Single page app)
  - HTML/CSS/JS

## Dev Process

1. Create a new **branch** off of current `master` branch
2. Develop and **commit** new changes to new branch
3. Create pull request (**PR**) in Github to **merge** into `master` branch
4. Code review of new PR by other developers for required **approvals**
5. Push a new **plan** in Terraform to deploy changes

## Process Maps

![Overall Map](./docs/overall.png)

![Component Map](./docs/component-map.png)


## Terraform Setup

NOTE: This setup gives your `terraform` AWS user a large amount of power
and potential to effect your entire AWS account. Not recommended for use
along other resources on a shared AWS account.

### Terraform AWS Account Permissions

- `IAMFullAccess`
- `AmazonS3FullAccess`
- `AWSLambda_FullAccess`
- `AdministratorAccess-Amplify`

### Required Input Variables


_Environmental Variables_

- **AWS_ACCESS_KEY_ID** - Terraform AWS account access key
- **AWS_SECRET_ACCESS_KEY** - Terraform AWS account secret access key

_Terraform Variables_

- **access_token** - GitHub access token
- **repository** - Link to repository root of project
