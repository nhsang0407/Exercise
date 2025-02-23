from xml.dom.minidom import parse

DOMTree = parse("Device.xml")
elements = DOMTree.documentElement

devices = elements.getElementsByTagName("device")
group_count={}

for d in devices:
    groupid = d.getAttribute("groupid")
    if groupid in group_count:
        group_count[groupid] += 1  # Nếu groupid đã có trong dictionary, tăng số lượng lên 1
    else:
        group_count[groupid] = 1 #Khởi tạo cặp key-value mới nếu chưa có
max_group = None
max_count = 0

for groupid, count in group_count.items():
    if count > max_count:
        max_group = groupid
        max_count = count
print(f"Group with the largest number of devices: {max_group} ({max_count} devices)")