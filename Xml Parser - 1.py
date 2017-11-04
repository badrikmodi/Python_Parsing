#Refer xml1.xml
import os
os.chdir("C:\\Users\\Badrik Modi\\Desktop\\Python")
import xml.etree.cElementTree as ET
#This is used to parse the xml file
#Tree is an object created from ET 
tree = ET.parse('xml1.xml')
#Once we created tree as an object, we could use that object to create another object
#Root will give the first branch of tree. Over here it is <data>
root = tree.getroot()
print(root)
#The first loop will help you to find the first children of the tree which is <country>
#Each element can have tag, attribute and text.
#To parse tag, use child.tag and for attribute use child.attrib, same for child.text
for child in root:
    print(child.tag,'tag',child.attrib)
    for child1 in child:
        print(child1.text,'text',child1.tag,'tag',child1.attrib,'attrib')
    print('over')
#To grab each element, we can do using root.getchildren
##y=root.getchildren()[0]
##print(y,'y')

#child.attrib will give dictionary as output
