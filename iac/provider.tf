#patron singleton define los providers y el backend una vez, y no genera copiass
terraform {
  required_version = ">= 1.0"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }
  backend "local" {
    path = "terraform.tfstate"
  }
}