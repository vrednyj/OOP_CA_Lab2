terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.67"
    }
  }
  required_version = ">= 0.14.9"
}
provider "aws" {
  profile = "default"
  region  = var.region_west
}
resource "aws_instance" "app_server" {
  ami                  = var.ami_linux
  instance_type        = "t2.micro"
  iam_instance_profile = "EnablesEC2ToAccessSystemsManagerRole"
  key_name             = "Windows_instance"
  security_groups      = ["SSH_Connection"]
  tags = {
    Name = "L00169827_Linux "
    #Name = "L00169827_Windows "

  }
}
