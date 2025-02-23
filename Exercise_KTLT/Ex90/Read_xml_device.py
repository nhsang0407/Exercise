from xml.dom.minidom import parse

DOMTree = parse("Device.xml")
elements = DOMTree.documentElement

devices = elements.getElementsByTagName("device")
for d in devices:
    pro_id = (d.getElementsByTagName("id")[0]).childNodes[0].data
    pro_name = (d.getElementsByTagName("name")[0]).childNodes[0].data
    print(pro_id + " -> " + pro_name)