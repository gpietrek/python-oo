from shape.circle import Circle
from shape.rectangle import Rectangle
from shape.shape import Shape
from shop.person.PersonMitTitel import PersonMitTitel
from shop.person.person import Person

if __name__ == '__main__':

    # person1 = Person('Georg', 'Pietrek')
    # person1_string = person1.shortRepresentation()
    # print(f"person1: {person1_string}")
    #
    # person2 = Person('Otto', 'Meier')
    # print(f"person2: {person2}")
    # print(f"person2: {person2.longRepresentation()}")
    #
    # person3 = PersonMitTitel("Dr.", "Werner", "Müller", "Schmidt")
    # print(f"person3: {person3}")
    # print(f"person3: {person3.longRepresentation()}")
    # print(f"person3: {person3.shortRepresentation()}")
    #
    #
    # person2.heiratet(person3)
    # print(f"person2: {person2.longRepresentation()}")

    circle = Circle(2.0, 3.0, 4.0)
    print(f"circle: {circle}")
    print(f"area: {circle.calculate_area()}")

    rectangle = Rectangle(2.0, 3.0, 4.0, 5.0)
    print(f"rectangle: {rectangle}")
    print(f"area: {rectangle.calculate_area()}")

    shape = Shape(1.0, 2.0)
    print(f"shape: {shape}")
    print(f"area: {shape.calculate_area()}")
