output "Public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}

output "Public_dns" {
  description = "Public DNS address of the EC2 instance"
  value       = aws_instance.app_server.public_dns
}

output "Private_ip" {
  description = "Private IP address of the EC2 instance"
  value       = aws_instance.app_server.private_ip
}

output "Private_dns" {
  description = "Private DNS address of the EC2 instance"
  value       = aws_instance.app_server.private_dns
}