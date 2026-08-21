from cat import Cat
from mouse import Mouse
from duck import Duck

cat = Cat("Katy", 2, 22)

mouse = Mouse("Mickey")

duck = Duck("Donald")

print("----- CAT -----")
cat.showInfo()
cat.move()

print("----- MOUSE -----")
mouse.showInfo()
mouse.move()

print("----- DUCK -----")
duck.showInfo()
duck.move()