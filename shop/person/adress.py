

class Adress:
    def __init__(self, strasse: str, postleitzahl: int, ort: str) -> None:
        self._strasse = strasse
        self._postleitzahl = postleitzahl
        self._ort = ort

    def anschrift(self) -> str:
        return f'{self._strasse}\n{self._postleitzahl} {self._ort}'

    def __str__(self) -> str:
        return f'{self._strasse} {self._ort}'