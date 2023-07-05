
#create vpc

resource "aws_vpc" "vpc1" {
  cidr_block = "10.0.0.0/16"
  tags = {
    "Name" = "terraform1-vpc"
    project = "sprints"
  }
}

# use data source to get all avalablility zones in region

data "aws_availability_zones" "available_zones" {}


# create subnet

resource "aws_subnet" "subnet-1" {
    vpc_id     = aws_vpc.vpc1.id
    availability_zone = data.aws_availability_zones.available_zones.names[0]
    cidr_block= "10.0.0.0/24"
    tags = {
        Name = "terraform1-subnet"
  }
} 


# create security group for the ec2 instance

resource "aws_security_group" "terraform1_security_group" {
  name        = "ec2 terraform security group"
  description = "allow access on ports 80 and 22"
  vpc_id      = aws_vpc.vpc1.id

  ingress {
    description      = "http access"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
    description      = "ssh access"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags   = {
    Name = "terraform1-security group"
  }
}

# launch the ec2 instance and install apache

resource "aws_instance" "terraform1_instance" {
  ami = "ami-053b0d53c279acc90"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.subnet-1.id
  vpc_security_group_ids = [aws_security_group.terraform1_security_group.id]
  key_name = "sprints-key"
  user_data = file("install-apache.sh")

  tags = {
    "Name" = "ec2-terraform1"
  }
}


# print the ec2's public ipv4 address
output "public_ipv4_address" {
  value = aws_instance.terraform1_instance.id
}