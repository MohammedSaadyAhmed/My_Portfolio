variable "CIDRS" {
  description = " CIDR blocks "
  type        = map 
  default     = {
    "vpc-cidr"            = "10.0.0.0/16"
    "public-subnet-cidr"  = "10.0.0.0/24"
    "private-subnet-cidr" = "10.0.1.0/24"
    "all traffic"         = "0.0.0.0/0"
  }
}


variable "Names" {
  description = "Tag Names "
  type        = map 
  default     = {
    "vpc"            = "terraform1-vpc"
    "public-subnet"  = "terraform1-public-subnet"
    "private-subnet" = "terraform1-private-subnet"
    "igw"            = "IGW" 
    "ngw"            = "NGW" 
    "public-instance"  = "ec2-public-terraform1"
    "private-instance"  = "ec2-private-terraform1"
  }
}
