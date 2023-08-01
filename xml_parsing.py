import xml.etree.ElementTree as ET

tree = ET.parse("same_data.xml")
root = tree.getroot()
print(root)
for i in root:
    print(i.tag, i.attrib)
    for j in i:
        print(j.tag,j.text)