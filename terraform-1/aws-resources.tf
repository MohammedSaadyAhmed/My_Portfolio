
#create vpc

resource "aws_vpc" "vpc1" {
  cidr_block = "10.0.0.0/16"
  tags = {
    "Name" = "terraform1-vpc"
    project = "sprints"
  }
}



# create subnet

resource "aws_subnet" "subnet-1" {
    vpc_id     = aws_vpc.vpc1.id
    cidr_block= "10.0.0.0/24"
    tags = {
        Name = "terraform1-subnet"
  }
} 

resource "aws_internet_gateway" "igw" {
    vpc_id = aws_vpc.vpc1.id
  
}

resource "aws_route_table" "terraform-rt" {
  vpc_id = aws_vpc.vpc1.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
}

resource "aws_route_table_association" "PublicRtassociation" {
    subnet_id = aws_subnet.subnet-1.id
    route_table_id = aws_route_table.terraform-rt.id
}


# create security group for the ec2 instance

resource "aws_security_group" "terraform1_security_group" {
  name        = "ec2 terraform security group"
  description = "allow access on ports 80 and 22"
  vpc_id      = aws_vpc.vpc1.id

  ingress {
    description = "HTTPS"
    from_port = 443
    to_port = 443
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "http access"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "ssh access"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags   = {
    Name = "terraform1-security group"
  }
}

data "aws_ami" "ubuntu" {

  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"]
}



# launch the ec2 instance and install apache

resource "aws_instance" "terraform1_instance" {
  ami = "ami-053b0d53c279acc90"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.subnet-1.id
  security_groups = [aws_security_group.terraform1_security_group.id]
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