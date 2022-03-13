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

resource "aws_lambda_function" "insert_data" {
  filename      = "./lambda-zips/insert_data.zip"
  function_name = "insert_data"
  role          = aws_iam_role.iam_demo_lambda.arn
  source_code_hash = filebase64sha256("./lambda-zips/insert_data.zip")
  handler          = "insert_data.handler"
  runtime = "python3.8"

  environment {
    variables = {
      foo = "bar"
    }
  }
}

resource "aws_lambda_function" "other_file" {
  filename      = "./lambda-zips/insert_data.zip"
  function_name = "other_file"
  role          = aws_iam_role.iam_demo_lambda.arn
  source_code_hash = filebase64sha256("./lambda-zips/insert_data.zip")
  handler          = "other_file.handler"
  runtime = "python3.8"

  environment {
    variables = {
      foo = "bar"
    }
  }
}
