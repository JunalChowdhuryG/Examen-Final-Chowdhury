
#patron composite
# conjunto de recursos agrupados en modulos reutilizables como network, subnet, iam
module "network" {
  source = "./modules/network"
}
module "" {
  source = "./modules/subnet"
}
module "iam" {
  source = "./modules/iam"
}

#patron factory
# crea instancias de recursos de computo 
module "compute" {
  source = "./modules/compute"
  instance_count = var.instance_count
  instance_type = var.instance_type
  image_id = var.image_id
  subnet_id = module.subnet.subnet_id
  security_group_ids = module.network.security_group_ids
}


