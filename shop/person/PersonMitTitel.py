from shop.person.person import Person


class PersonMitTitel(Person):
    def __init__(self, titel: str, vorname: str, nachname: str, gebname:str = '') -> None:
        super().__init__(vorname, nachname, gebname)
        self._titel = titel

    def shortRepresentation(self):
        return f'{self._titel} {super().shortRepresentation()}'

    def longRepresentation(self):
        if (len(self._gebname) == 0):
            return self.shortRepresentation()
        return f'{self._titel} {super().longRepresentation()}'
