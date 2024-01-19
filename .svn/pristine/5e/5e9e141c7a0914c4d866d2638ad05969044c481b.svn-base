provider "vsphere" {
  user                  = "root"
  password              = "root@123"
  vsphere_server        = "10.91.26.130"
  allow_unverified_ssl  = true
}


data "vsphere_datacenter" "dc" {
	name = "newdatacenter"
}

data "vsphere_datastore" "datastore" {
	name = "VFMS92"
	datacenter_id = "${data.vsphere_datacenter.dc.id}"
}
data "vsphere_resource_pool" "pool" {
	name = "DEV"
	datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_network" "network" {
  name          = "VM Network"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}




resource "vsphere_virtual_machine" "newTfVm" {
	name = "Terraform_Ubuntu22.04"
 
	resource_pool_id = "${data.vsphere_resource_pool.pool.id}"
	datastore_id = "${data.vsphere_datastore.datastore.id}"
	num_cpus = 5
	memory = 2048
	guest_id = "ubuntu64Guest"
	scsi_type = "pvscsi"
	wait_for_guest_net_timeout = 10
	
	 network_interface {
    network_id = "${data.vsphere_network.network.id}"
  }

	disk {
		label = "WIN2012R2_TF.vmdk"
		thin_provisioned = true
		size = 128
	}

	cdrom {
		datastore_id = "${data.vsphere_datastore.datastore.id}"
		path = "ubuntu-22.04.3-desktop-amd64 (1).iso"
	}

}