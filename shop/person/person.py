from __future__ import annotations

from shop.person.adress import Adress


class Person:
    def __init__(self, vorname: str, nachname: str, gebname : str = '', adresse: Adress = None) -> None:
        self._vorname = vorname
        self._nachname = nachname
        self._gebname = gebname
        self._adresse = adresse

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

    def postanschrift(self) -> str:
        if (self._adresse is None ):
            return self.shortRepresentation()
        return f'{self.shortRepresentation()}\n{self._adresse.anschrift()}'

    def __str__(self):
        return self.shortRepresentation()