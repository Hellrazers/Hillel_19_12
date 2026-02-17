from pprint import pprint

from constant import DATA_FOR_TEST_DIR
import xmltodict


with open(DATA_FOR_TEST_DIR/'xml_test.xml') as file:
    data_xml = file.read()
    data_xml_parse = xmltodict.parse(data_xml)

print(data_xml)

# data_xml_parse = xmltodict.parse(data_xml)
pprint(data_xml_parse)
name = data_xml_parse.get('groups').get('group').get('name')
print()

with open(DATA_FOR_TEST_DIR/'xml_test2.xml', mode='w') as file:
    # file.w
    xmltodict.unparse(data_xml_parse, output=file, pretty=True)