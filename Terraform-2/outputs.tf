# print the ec2's public ipv4 address

output "public_ipv4_address" {
  value = aws_instance.terraform1_instance.id
}

output "public_ip" {
  value = aws_instance.terraform1_public_instance.public_ip
}

output "private_ip" {
  value = aws_instance.terraform1_public_instance.private_ip
}
