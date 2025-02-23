from xml.dom.minidom import parse

DOMTree = parse("Device.xml")
elements = DOMTree.documentElement

devices = elements.getElementsByTagName("device")
g=input("Enter group (g1, g2, g3): ")
group_to_filter = g

print(f"Devices in group {group_to_filter}:")
for d in devices:
    groupid = d.getAttribute("groupid")
    if groupid == group_to_filter:
        pro_id = (d.getElementsByTagName("id")[0]).childNodes[0].data
        pro_name = (d.getElementsByTagName("name")[0]).childNodes[0].data
        print(pro_id + " -> " + pro_name)