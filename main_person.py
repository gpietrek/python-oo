from shop.person.person import Person
from shop.person.person_mit_titel import PersonMitTitel

if __name__ == '__main__':

    person1 = Person('Georg', 'Pietrek')
    person1_string = person1.shortRepresentation()
    print(f"person1: {person1_string}")

    person2 = Person('Otto', 'Meier')
    print(f"person2: {person2}")
    print(f"person2: {person2.longRepresentation()}")

    person3 = PersonMitTitel("Dr.", "Werner", "Müller", "Schmidt")
    print(f"person3: {person3}")
    print(f"person3: {person3.longRepresentation()}")
    print(f"person3: {person3.shortRepresentation()}")

    person2.heiratet(person3)
    print(f"person2: {person2.longRepresentation()}")
