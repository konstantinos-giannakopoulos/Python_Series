import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("--- Person ---")
            id = attrs["id"]
            print("ID: %s" % id)

    def endElement(self, name):
        if self.current == "name":
            print("Name: %s" % self.name)
        elif self.current == "age":
            print("Age: %s" % self.age)
        elif self.current == "weight":
            print("Weight: %s" % self.weight)
        elif self.current == "height":
            print("Height: %s" % self.height)
        self.current = ""

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content
        

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("group.xml")
