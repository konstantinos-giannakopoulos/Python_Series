import xml.dom.minidom

domtree = xml.dom.minidom.parse("group.xml")
group = domtree.documentElement

persons = group.getElementsByTagName("person")

for person in persons:
    print("--- Person ---")
    if person.hasAttribute("id"):
        print("ID: %s" % person.getAttribute("id"))
    name = person.getElementsByTagName("name")[0]
    age = person.getElementsByTagName("age")[0]
    weight = person.getElementsByTagName("weight")[0]
    height = person.getElementsByTagName("height")[0]
    print("Name: %s" % name.childNodes[0].nodeValue)
    print("Age: %s" % age.childNodes[0].nodeValue)
    print("Weight: %s" % weight.childNodes[0].nodeValue)
    print("Height: %s" % height.childNodes[0].nodeValue)


# edit a record
persons[0].getElementsByTagName("name")[0].childNodes[0].nodeValue = "New Name"
domtree.writexml(open("group.xml","w"))

persons[0].setAttribute("id","10")
domtree.writexml(open("group.xml","w"))

# create a new person
newperson = domtree.createElement("person")
newperson.setAttribute("id","6")
name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Paul Smith"))
age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("45"))
weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("78"))
height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("178"))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)
group.appendChild(newperson)
domtree.writexml(open("group.xml","w"))
