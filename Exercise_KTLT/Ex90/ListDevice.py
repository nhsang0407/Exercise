from xml.dom.minidom import parse

from Exercise_KTLT.Ex90.Device import Device
from Exercise_KTLT.Ex90.Group_Device import Group_Device


class ListDevice:
    def __init__(self):
        self.list=[]
    def print_all_device(self):
        for p in self.list:
            print(p)
    def import_device_group_from_xml(self,filename):
        self.list.clear()
        DOMTree = parse(filename)
        elements = DOMTree.documentElement

        groups = elements.getElementsByTagName("group")
        for g in groups:
            pro_id = (g.getElementsByTagName("id")[0]).childNodes[0].data
            pro_name = (g.getElementsByTagName("name")[0]).childNodes[0].data
            self.list.append(Group_Device(pro_id, pro_name))

    def import_device_from_xml(self,filename):
        self.list.clear()
        DOMTree = parse(filename)
        elements = DOMTree.documentElement

        devices = elements.getElementsByTagName("device")
        for d in devices:
            pro_id = (d.getElementsByTagName("id")[0]).childNodes[0].data
            pro_name = (d.getElementsByTagName("name")[0]).childNodes[0].data
            self.list.append(Device(pro_id,pro_name))

    def filter_device_by_group(self, filename, g):
        self.list.clear()
        DOMTree = parse(filename)
        elements = DOMTree.documentElement

        devices = elements.getElementsByTagName("device")
        group_to_filter = g

        print(f"Devices in group {group_to_filter}:")
        for d in devices:
            groupid = d.getAttribute("groupid")
            if groupid == group_to_filter:
                pro_id = (d.getElementsByTagName("id")[0]).childNodes[0].data
                pro_name = (d.getElementsByTagName("name")[0]).childNodes[0].data
                self.list.append(Device(pro_id, pro_name))

    def read_largest(self,filename):
        DOMTree = parse(filename)
        elements = DOMTree.documentElement

        devices = elements.getElementsByTagName("device")
        group_count = {}

        for d in devices:
            groupid = d.getAttribute("groupid")
            if groupid in group_count:
                group_count[groupid] += 1  # Nếu groupid đã có trong dictionary, tăng số lượng lên 1
            else:
                group_count[groupid] = 1  # Khởi tạo cặp key-value mới nếu chưa có
        max_group = None
        max_count = 0

        for groupid, count in group_count.items():
            if count > max_count:
                max_group = groupid
                max_count = count
        return f"Group with the largest number of devices: {max_group} ({max_count} devices)"