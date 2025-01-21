# TERRAFORM ===============================================
provider "azurerm" {
  features {}
}

variable restore_point_in_time {
  type        = string
  default     = null
  description = "If Specified, perform a database restore point in time"
}

variable restore_point_in_time_source_id {
  type        = string
  default     = null
  description = "If Specified, perform a database restore point in time with this id"
}

variable restore_dropped_database_id {
  type        = string
  default     = null
  description = "If Specified, perform a database restore from a deleted database id"
}

locals{
    # TODO 4: if  restore_point_in_time is specified (not null), set create_mode to PointInTimeRestore, 
    #       else if restore_dropped_database_id is specified, set create_mode to Restore
    # else leave create_mode at Default

    create_mode = "Default" # Change this to meet above specification

    primary_server = "server-westus" 
}

resource "azurerm_resource_group" "this" {
  name     = "my_resource_group"
  location = "EastUS"
}


resource "azurerm_mssql_server" "primary" {
  name                         = #TODO 1 - set this value to come from the local variable primary_server
  resource_group_name          = azurerm_resource_group.this.name
  location                     = "eastus"
  version                      = "12.0"
  administrator_login          = "4dm1n157r470r"
  administrator_login_password = "4-v3ry-53cr37-p455w0rd"
}

# TODO 2 - Modify this resource to deploy only after the primary server has completed deployment
resource "azurerm_mssql_server" "secondary" {
  name                         = "server-pair"
  resource_group_name          = azurerm_resource_group.this.name
  location                     = "centralus"
  version                      = "12.0"
  administrator_login          = "4dm1n157r470r"
  administrator_login_password = "4-v3ry-53cr37-p455w0rd"
}

resource "azurerm_mssql_database" "example" {
  name         = "example-db"
  create_mode  = local.create_mode # TODO 4 - see locals
  server_id    = # TODO 3 - set this to the secondary server's id.
  collation    = "SQL_Latin1_General_CP1_CI_AS"
  max_size_gb  = 2
  sku_name     = "S0"

  restore_point_in_time = var.restore_point_in_time
  restore_dropped_database_id = var.restore_dropped_database_id
  creation_source_database_id = var.restore_point_in_time_source_id
}