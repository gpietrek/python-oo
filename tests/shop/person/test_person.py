from unittest import TestCase
from unittest.mock import Mock

from shop.person.person import Person


class TestPerson(TestCase):

    def setUp(self):
        self.cut = Person('Georg', 'Pietrek')

    def test_get_nachname_returns_correct_value(self):
        # act
        result = self.cut.get_nachname()

        # assert
        self.assertEqual('Pietrek', result)

    def test_str_returns_correct_value(self):
        # act
        result = self.cut.__str__()

        # assert
        self.assertEqual(result, 'Georg Pietrek')

    def test_longRepresentation_without_gebname_returns_correct_value(self):
        # act
        result = self.cut.longRepresentation()

        # assert
        self.assertEqual(result, 'Georg Pietrek')

    def test_longRepresentation_without_gebname_returns_correct_value(self):
        # arrange
        self.cut.changeNachnameDurchHeirat('Meier')

        # act
        result = self.cut.longRepresentation()

        # assert
        self.assertEqual(result, 'Georg Meier, geb. Pietrek')

    def test_postanschrift_returns_correct_value(self):
        # arrange
        adresseMock = Mock()
        adresseMock.anschrift.return_value = 'someAnschrift'
        cut = Person('Georg', 'Pietrek', adresse = adresseMock)

        # act
        postanschrift = cut.postanschrift()

        # assert
        self.assertEqual(postanschrift, 'Georg Pietrek\nsomeAnschrift')
        adresseMock.anschrift.assert_called_once()


