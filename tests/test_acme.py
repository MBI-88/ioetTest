import unittest
from acme import acme
from acme import datastruct
from decorators import decorator
import os
from datetime import datetime


class TestACME(unittest.TestCase):

    def test_readData_right(self) -> None:
        with open("data_test.txt", 'w') as f:
            f.write(
                "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00")
        f.close()
        self.assertEqual(["RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"],
                         decorator.readData("data_test.txt"))
        os.remove("data_test.txt")

    def test_readData_fail(self) -> None:
        with open("data_test.csv", "w") as f:
            f.write(
                "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00")
        f.close()

        with self.assertRaises(SystemExit):
            decorator.readData("data_test.csv")

        os.remove("data_test.csv")

    def test_processData_right(self) -> None:
        sample = acme.ACME()
        test = {
            "RENE": 215,
            "ASTRID": 85,
        }
        data = ["RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00",
                "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"]
        sample.processData(data)
        self.assertEqual(test, sample.moneyToPay)

    def test_processData_fail(self) -> None:
        sample = acme.ACME()
        data = [
            "RENE=MO10:00/12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"]
        with self.assertRaises(SystemExit):
            sample.processData(data)

    def test_handlerData_right(self) -> None:
        name = "RENE"
        start = datetime.strptime("10:00", "%H:%M").time()
        end = datetime.strptime("12:00", "%H:%M").time()
        sample = acme.ACME()
        sample.moneyToPay[name] = 0
        ranges = datastruct.payKeys["Week"]
        sample.handlerData(ranges, name, start, end)
        test = {"RENE": 30}
        self.assertEqual(test, sample.moneyToPay)

    def test_handlerData_fail(self) -> None:
        name = "RENE"
        start = 90
        end = 100
        sample = acme.ACME()
        sample.moneyToPay[name] = 0
        ranges = datastruct.payKeys["Week"]
        with self.assertRaises(SystemExit):
            sample.handlerData(ranges, name, start, end)


if __name__ == "__main__":
    unittest.main()
