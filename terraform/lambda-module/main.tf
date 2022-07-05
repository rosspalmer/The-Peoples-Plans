
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
  filename      = "./lambda-module/lambda-zips/python-lambdas.zip"
  function_name = "insert-data"
  role          = aws_iam_role.iam_demo_lambda.arn
  source_code_hash = filebase64sha256("./lambda-module/lambda-zips/python-lambdas.zip")
  handler          = "lambdas.insert_data.handler"
  runtime = "python3.8"

  environment {
    variables = {
      JSON_BUCKET = var.json_bucket["prod"]
    }
  }

}

resource "aws_lambda_function" "other_file" {
  filename      = "./lambda-module/lambda-zips/python-lambdas.zip"
  function_name = "other-file"
  role          = aws_iam_role.iam_demo_lambda.arn
  source_code_hash = filebase64sha256("./lambda-module/lambda-zips/python-lambdas.zip")
  handler          = "lambdas.other_file.handler"
  runtime = "python3.8"

}
