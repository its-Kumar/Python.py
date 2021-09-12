from xml.dom.minidom import Document

mainNode = Document()

cars = mainNode.createElement("cars")
mainNode.appendChild(cars)

car = mainNode.createElement("car")
cars.appendChild(car)

ID = mainNode.createElement("id")
car.appendChild(ID)
info = mainNode.createTextNode("C1")
ID.appendChild(info)

make = mainNode.createElement("make")
car.appendChild(make)
info = mainNode.createTextNode("A")
make.appendChild(info)

model = mainNode.createElement("id")
car.appendChild(model)
info = mainNode.createTextNode("B")
model.appendChild(info)

year = mainNode.createElement("year")
car.appendChild(year)
info = mainNode.createTextNode("2000")
year.appendChild(info)

xmlFile = open("car.xml", "w")
xmlFile.write(mainNode.toprettyxml())
xmlFile.close()
