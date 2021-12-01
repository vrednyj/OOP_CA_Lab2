variable "region_west" {
  default     = "eu-west-1"
  description = "AWS West Region(Ireland)"
}

variable "region_east" {
  default     = "us-east-1"
  description = "AWS East Region"
}

variable "ami_linux" {
  default     = "ami-09ce2fc392a4c0fbc"
  description = " amzn2-ami-kernel-5.10-hvm-2.0.20211103.1-x86_64-gp2"

}

variable "ami_windows" {
  default     = "ami-08da401b2768d4754"
  description = "Windows_Server-2012-R2_RTM-English-64Bit-Base-2021.11.10"
}



