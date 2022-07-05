provider "aws" {
  region = var.region
}

module lambda_module {
  source = "./lambda-module"
  json_bucket = local.json_bucket
}

module s3_module {
  source = "./s3-module"
  json_bucket = local.json_bucket
}

module web_module {
  source = "./web-module"
  repository = var.repository
}