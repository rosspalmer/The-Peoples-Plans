provider "aws" {
  region = var.region
}

# == S3 ==

resource "aws_s3_bucket" "json_s3_bucket" {
  bucket = local.json_bucket["prod"]
  tags = {
    Environment = "Prod"
  }
}

# == LAMBDAS ==

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

resource "aws_lambda_function" "insert_data" {
  filename      = "./lambda-zips/python-lambdas.zip"
  function_name = "insert-data"
  role          = aws_iam_role.iam_demo_lambda.arn
  source_code_hash = filebase64sha256("./lambda-zips/python-lambdas.zip")
  handler          = "insert_data.handler"
  runtime = "python3.8"

  environment {
    variables = {
      JSON_BUCKET = local.json_bucket['prod']
    }
  }

}

resource "aws_lambda_function" "other_file" {
  filename      = "./lambda-zips/python-lambdas.zip"
  function_name = "other-file"
  role          = aws_iam_role.iam_demo_lambda.arn
  source_code_hash = filebase64sha256("./lambda-zips/python-lambdas.zip")
  handler          = "other_file.handler"
  runtime = "python3.8"

}
