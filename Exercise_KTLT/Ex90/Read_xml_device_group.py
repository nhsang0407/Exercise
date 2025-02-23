from xml.dom.minidom import parse

DOMTree = parse("groupdevices.xml")
elements = DOMTree.documentElement

groups = elements.getElementsByTagName("group")
for g in groups:
    pro_id = (g.getElementsByTagName("id")[0]).childNodes[0].data
    pro_name = (g.getElementsByTagName("name")[0]).childNodes[0].data
    print(pro_id + " -> " + pro_name)