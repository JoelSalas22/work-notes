# Basic Resource Types for AWS


## S3 Buckets

```terraform
resource "aws_s3_bucket" "example" {
    bucket = "learning-terraform.example.com"
    acl = "public-read"
    policy =file("policy.json")
}
```

```terraform
resource "aws_s3_bucket_website_configuration" "example" 
{
    bucket = aws_s3_bucket.example.bucket
    index_document {
        suffix = "index.html"
    } 
}
```