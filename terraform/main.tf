provider "aws" {
  region = var.region
}

resource "aws_iam_role" "iam_demo_lambda" {
  name = "iam_demo_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "demo_lambda" {
  filename      = "./lambda-zips/demo-lambda.zip"
  function_name = "demo_lambda"
  role          = aws_iam_role.iam_demo_lambda.arn
  handler       = "index.test"
  source_code_hash = filebase64sha256("./lambda-zips/demo-lambda.zip")

  runtime = "python3.9"

  environment {
    variables = {
      foo = "bar"
    }
  }
}