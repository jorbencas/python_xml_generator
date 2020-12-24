import xml.etree.cElementTree as ET
import os

def get_all_data_modules_to_xml(proot = None, ref = None):
    if not proot:
        root = ET.Element('odoo') 
        attrs = dict({'noupdate':"0"})
        xml_elemente = generate_xml('data', root, attrs)  
        array = ["padre1","padre2"]
        subarray = [{"hijo":"2"},{"hijo":"1"}]
    else:
        array = ["madre1","madre2"]
        subarray = [{"hijo":"3"}]
    
    for res in array:
        attrs = dict({"id": '', 'model': res})
        xml_element = generate_xml("record", xml_elemente, attrs)
        for f in subarray:
            for (key, value) in f.items():
                if not proot and res == 'padre1' and value == "2":
                    if get_all_data_modules_to_xml(xml_element, res) == True:
                        attrs = dict({'name': key})
                        generate_xml("field", xml_element, attrs, value)     
                    else:
                        return True
    write_xml_file(root,'base')

def generate_xml(element = None, parent_element = None, attrs=None, text = None):
    xml_element = ET.SubElement(parent_element, element) 
    if attrs:
        for key, value in attrs.items():
            xml_element.set(str(key),str(value))
    
    if text:
        xml_element.text = str(text)

    return xml_element
    
def write_xml_file( root, data):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = base_path + "/" + data+"_test.xml"
    tree = ET.ElementTree(root)
    tree.write(file_path, 'utf-8',True)

get_all_data_modules_to_xml()
