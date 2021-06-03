import xml.etree.ElementTree as ET

def parse_xml():
    tree = ET.parse('smil.xml')
    root = tree.getroot()

    

    x = root.iter('img')
    for img in root.findall('./body/par/img'):
        print(img)
    print(x)

def find_rec(node, element, result):
    root = node.getroot()
   
    for item in root.findall(element):
        
        result.append(item)
        find_rec(item, element, result)
        return result
           

if __name__ == '__main__':
    find_rec(ET.parse("smil.xml"), 'img', [])
    