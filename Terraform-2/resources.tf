resource "aws_vpc" "vpc1" {
  cidr_block = var.CIDRS["vpc-cidr"]  #(10.0.0.0/16)
  tags = {
    "Name" = "terraform1-vpc"
    project = "sprints"
  }
}
resource "aws_subnet" "Public_Subnet" {
    vpc_id     = aws_vpc.vpc1.id
    cidr_block= var.CIDRS["public-subnet-cidr"]
    tags = {
        Name = "terraform1-public-subnet"
  }
} 
resource "aws_subnet" "Private_Subnet" {
    vpc_id     = aws_vpc.vpc1.id
    cidr_block= var.CIDRS["private-subnet-cidr"]
    tags = {
        Name = "terraform1-private-subnet"
  }
} 
resource "aws_internet_gateway" "igw" {
    vpc_id = aws_vpc.vpc1.id
  
}
resource "aws_route_table" "terraform-public-rt" {
  vpc_id = aws_vpc.vpc1.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
}
