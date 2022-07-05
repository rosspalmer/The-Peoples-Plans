
resource "aws_s3_bucket" "json_s3_bucket" {
  bucket = var.json_bucket["prod"]
  tags = {
    Environment = "Prod"
  }
}
