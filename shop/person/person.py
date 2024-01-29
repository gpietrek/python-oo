from __future__ import annotations

class Person:
    def __init__(self, vorname: str, nachname: str, gebname : str = '') -> None:
        self._vorname = vorname
        self._nachname = nachname
        self._gebname = gebname

    def get_nachname(self) -> str:
        return self._nachname

    def heiratet(self, ehepartner: Person) -> None:
        if not isinstance(ehepartner, Person):
            raise TypeError("ehepartner can only be a Person")
        self._gebname = self._nachname
        self._nachname = ehepartner.get_nachname()

    def changeNachnameDurchHeirat(self, neuerNachname: str) -> None:
        self._gebname = self._nachname
        self._nachname = neuerNachname

    def shortRepresentation(self):
        return f"{self._vorname} {self._nachname}"

    def longRepresentation(self):
        if (len(self._gebname) == 0):
            return self.shortRepresentation()
        return f"{self._vorname} {self._nachname}, geb. {self._gebname}"

    def __str__(self):
        return self.shortRepresentation()