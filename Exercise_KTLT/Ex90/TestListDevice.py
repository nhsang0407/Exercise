from Exercise_KTLT.Ex90.ListDevice import ListDevice

list_device=ListDevice()
filename1="groupdevices.xml"
filename2="Device.xml"
print("Display the list of Device Groups: ")
list_device.import_device_group_from_xml(filename1)
list_device.print_all_device()
print("Display all Devices: ")
list_device.import_device_from_xml(filename2)
list_device.print_all_device()
print("Filter the Device List by Device Group: ")
list_device.filter_device_by_group(filename2,"g1")
list_device.print_all_device()
print("Print the Device Group with the largest number of devices:")
list_device.read_largest(filename2)
list_device.print_all_device()
