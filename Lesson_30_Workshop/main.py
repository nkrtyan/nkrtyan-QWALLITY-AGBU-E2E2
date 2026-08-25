from cat import Cat
from mouse import Mouse
from duck import Duck

cat = Cat("Katy", 2, 22)
mouse = Mouse("Mickey")
duck = Duck("Donald")

print("CAT")
cat.showINFO()
cat.move()

print("MOUSE")
mouse.showINFO()
mouse.move()

print("DUCK")
duck.showINFO()
duck.move()