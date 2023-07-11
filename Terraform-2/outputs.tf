output "public_ip" {
  value = aws_instance.terraform1_public_instance.public_ip
}

output "private_ip" {
  value = aws_instance.terraform1_public_instance.private_ip
}
