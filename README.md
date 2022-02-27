# The-Peoples-Plans

Prod Site: https://master.d2vt7v2anveb09.amplifyapp.com/

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
