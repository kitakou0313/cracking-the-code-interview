import unittest
import copy


class XMLObject():
    def __init__(self, tag, attribute, children=[]):
        self.tag, self.attribute = tag, attribute
        self.children = copy.deepcopy(children)


def encodingXML(xml, mapping):

    attrString = ""

    for attribute in xml.attribute:
        attrString += " " + str(mapping[attribute]) + \
            " "+xml.attribute[attribute]

    childrenStrings = ""

    for child in xml.children:
        childrenStrings += " " + encodingXML(child, mapping)

    return str(mapping[xml.tag]) + attrString + " 0" + childrenStrings + " 0"


class Test(unittest.TestCase):
    def test_xml_encoding(self):
        mapping = {"name": 1, "instrument": 2,
                   "person": 3, "monkey": 4, "color": 5}
        xml = XMLObject("person",
                        {"name": "The Man with the Yellow Hat", "instrument": "tuba"},
                        [XMLObject("monkey", {"name": "George", "color": "brown"})])

        self.assertEqual(encodingXML(xml, mapping),
                         "3 1 The Man with the Yellow Hat 2 tuba 0 4 1 George 5 brown 0 0 0")


if __name__ == "__main__":
    unittest.main()
