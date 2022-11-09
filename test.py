import unittest
import io
import sys
from unittest.mock import patch
from inventory import *
import json
import os

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)

class Test01_CreatObjectNoFile(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') *** EXPECT: i.data = {} ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        self.assertEqual(i.data, {})
        remove_file('t99.dat')
        print()

class Test02_CreatObjectWithFile(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** GIVEN: filename t99.dat contains {"BC9001": ["Paper", 0]} *** IMPLEMENT: i = Inventory(filename='t99.dat') *** EXPECT: i.data = {"BC9001": ["Paper", 0]} ***
        """
        remove_file('t99.dat')
        with open('t99.dat', 'w') as f:
            json.dump({"BC9001": ["Paper", 0]}, f)
        i = Inventory(filename='t99.dat')
        self.assertEqual(i.data, {"BC9001": ["Paper", 0]})
        remove_file('t99.dat')
        print()

class Test03_AddItemBarcodeNotString(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.add_item(barcode=9001, description="Paper") *** EXPECT: r = 109 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        r = i.add_item(barcode=9001, description="Paper")
        self.assertEqual(r, 109)
        remove_file('t99.dat')
        print()

class Test04_AddItemBarcodeTooLong(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.add_item(barcode="BC9001555", description="Paper") *** EXPECT: r = 109 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        r = i.add_item(barcode="BC9001555", description="Paper")
        self.assertEqual(r, 109)
        remove_file('t99.dat')
        print()

class Test05_AddItemBarcodeDoesNotContainBC(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.add_item(barcode="XX9001", description="Paper") *** EXPECT: r = 109 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        r = i.add_item(barcode="XX9001", description="Paper")
        self.assertEqual(r, 109)
        remove_file('t99.dat')
        print()

class Test06_AddItemBarcodeEndsWithChar(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.add_item(barcode="BC900X", description="Paper") *** EXPECT: r = 109 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        r = i.add_item(barcode="BC900X", description="Paper")
        self.assertEqual(r, 109)
        remove_file('t99.dat')
        print()

class Test07_AddItemBarcodeValid(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test07 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.add_item(barcode="BC9001", description="Paper") *** EXPECT: r = 100 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        r = i.add_item(barcode="BC9001", description="Paper")
        self.assertEqual(r, 100)
        remove_file('t99.dat')
        print()

class Test08_AddItemBarcodeDuplicate(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test08 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND x = i.add_item(barcode="BC9001", description="Paper") AND r = i.add_item(barcode="BC9001", description="Paper") *** EXPECT: r = 101 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        x = i.add_item(barcode="BC9001", description="Paper")
        r = i.add_item(barcode="BC9001", description="Paper")
        self.assertEqual(r, 101)
        remove_file('t99.dat')
        print()

class Test09_AddItemBarcodeValidDataWrite(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test09 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.add_item(barcode="BC9001", description="Paper") AND i = Inventory(filename='t99.dat') *** EXPECT: i.data = {"BC9001": ["Paper", 0]} ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        r = i.add_item(barcode="BC9001", description="Paper")
        i = Inventory(filename='t99.dat')
        self.assertEqual(i.data, {"BC9001": ["Paper", 0]})
        remove_file('t99.dat')
        print()

class Test10_ModifyDescriptionBarcodeNotFound(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test10 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND x = i.add_item(barcode="BC9001", description="Paper") AND r = i.modify_description(barcode="BC9003", description="Book") *** EXPECT: r = 101 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        x = i.add_item(barcode="BC9001", description="Paper")
        r = i.modify_description(barcode="BC9003", description="Book")
        self.assertEqual(r, 102)
        remove_file('t99.dat')
        print()

class Test11_ModifyDescriptionBarcodeValid(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test11 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND x = i.add_item(barcode="BC9001", description="Paper") AND r = i.modify_description(barcode="BC9001", description="Book") *** EXPECT: r = 100 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        x = i.add_item(barcode="BC9001", description="Paper")
        r = i.modify_description(barcode="BC9001", description="Book")
        self.assertEqual(r, 100)
        remove_file('t99.dat')
        print()

class Test12_ModifyDescriptionBarcodeValidDataWrite(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test12 *** GIVEN: filename t99.dat contains {"BC9001": ["Paper", 7]} *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.modify_description(barcode="BC9001", description="Book") AND i = Inventory(filename='t99.dat')*** EXPECT: i.data = {"BC9001": ["Book", 7]} ***
        """
        remove_file('t99.dat')
        with open('t99.dat', 'w') as f:
            json.dump({"BC9001": ["Paper", 7]}, f)
        i = Inventory(filename='t99.dat')
        r = i.modify_description(barcode="BC9001", description="Book")
        i = Inventory(filename='t99.dat')
        self.assertEqual(i.data, {"BC9001": ["Book", 7]})
        remove_file('t99.dat')
        print()

class Test13_AddQtyBarcodeNotFound(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test13 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.add_qty(barcode="BC9001", qty=5) *** EXPECT: r = 102 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        r = i.add_qty(barcode="BC9001", qty=5)
        self.assertEqual(r, 102)
        remove_file('t99.dat')
        print()

class Test14_AddQtyNotInt(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test14 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND x = i.add_item(barcode="BC9001", description="Paper") AND r = i.add_qty(barcode="BC9001", qty="5") *** EXPECT: r = 108 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        x = i.add_item(barcode="BC9001", description="Paper")
        r = i.add_qty(barcode="BC9001", qty="5")
        self.assertEqual(r, 108)
        remove_file('t99.dat')
        print()

class Test15_AddQtyValid(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test15 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND x = i.add_item(barcode="BC9001", description="Paper") AND r = i.add_qty(barcode="BC9001", qty=5) *** EXPECT: r = 100 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        x = i.add_item(barcode="BC9001", description="Paper")
        r = i.add_qty(barcode="BC9001", qty=5)
        self.assertEqual(r, 100)
        remove_file('t99.dat')
        print()

class Test16_AddQtyValidDataWrite(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test16 *** GIVEN: filename t99.dat contains {"BC9001": ["Paper", 7]} *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.add_qty(barcode="BC9001", qty=5) AND i = Inventory(filename='t99.dat')*** EXPECT: i.data = {"BC9001": ["Paper", 12]} ***
        """
        remove_file('t99.dat')
        with open('t99.dat', 'w') as f:
            json.dump({"BC9001": ["Paper", 7]}, f)
        i = Inventory(filename='t99.dat')
        r = i.add_qty(barcode="BC9001", qty=5)
        i = Inventory(filename='t99.dat')
        self.assertEqual(i.data, {"BC9001": ["Paper", 12]})
        remove_file('t99.dat')
        print()

class Test17_RemoveQtyBarcodeNotFound(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test17 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.remove_qty(barcode="BC9001", qty=5) *** EXPECT: r = 102 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        r = i.remove_qty(barcode="BC9001", qty=5)
        self.assertEqual(r, 102)
        remove_file('t99.dat')
        print()


class Test18_RemoveQtyNotInt(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test18 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND x = i.add_item(barcode="BC9001", description="Paper") AND r = i.remove_qty(barcode="BC9001", qty="5") *** EXPECT: r = 108 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        x = i.add_item(barcode="BC9001", description="Paper")
        r = i.remove_qty(barcode="BC9001", qty="5")
        self.assertEqual(r, 108)
        remove_file('t99.dat')
        print()

class Test19_RemoveQtyNotEnoughSupply(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test19 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND x = i.add_item(barcode="BC9001", description="Paper") AND r = i.remove_qty(barcode="BC9001", qty=5) *** EXPECT: r = 103 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        x = i.add_item(barcode="BC9001", description="Paper")
        r = i.remove_qty(barcode="BC9001", qty=5)
        self.assertEqual(r, 103)
        remove_file('t99.dat')
        print()

class Test20_RemoveQtyValid(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test20 *** GIVEN: filename t99.dat does not exist *** IMPLEMENT: i = Inventory(filename='t99.dat') AND x = i.add_item(barcode="BC9001", description="Paper") AND x = i.add_qty(barcode="BC9001", qty=7) AND r = i.remove_qty(barcode="BC9001", qty=5) *** EXPECT: r = 100 ***
        """
        remove_file('t99.dat')
        i = Inventory(filename='t99.dat')
        x = i.add_item(barcode="BC9001", description="Paper")
        x = i.add_qty(barcode="BC9001", qty=7)
        r = i.remove_qty(barcode="BC9001", qty=5)
        self.assertEqual(r, 100)
        remove_file('t99.dat')
        print()

class Test21_RemoveQtyValidDataWrite(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test21 *** GIVEN: filename t99.dat contains {"BC9001": ["Paper", 7]} *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.remove_qty(barcode="BC9001", qty=5) AND i = Inventory(filename='t99.dat')*** EXPECT: i.data = {"BC9001": ["Paper", 2]} ***
        """
        remove_file('t99.dat')
        with open('t99.dat', 'w') as f:
            json.dump({"BC9001": ["Paper", 7]}, f)
        i = Inventory(filename='t99.dat')
        r = i.remove_qty(barcode="BC9001", qty=5)
        i = Inventory(filename='t99.dat')
        self.assertEqual(i.data, {"BC9001": ["Paper", 2]})
        remove_file('t99.dat')
        print()

class Test22_GetInventory(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test22 *** GIVEN: filename t99.dat contains {"BC9001": ["Paper", 1211], "BC9034": ["Notebook", 588], "BC9026": ["Computer", 49], "BC9072": ["Pencil", 147]} *** IMPLEMENT: i = Inventory(filename='t99.dat') AND r = i.get_inventory() *** EXPECT: r = "BC9001  Paper                1211\nBC9034  Notebook              588\nBC9026  Computer               49\nBC9072  Pencil                147\n" ***
        """
        remove_file('t99.dat')
        with open('t99.dat', 'w') as f:
            json.dump({"BC9001": ["Paper", 1211], "BC9034": ["Notebook", 588], "BC9026": ["Computer", 49], "BC9072": ["Pencil", 147]}, f)
        i = Inventory(filename='t99.dat')
        r = i.get_inventory()
        self.assertEqual(r, "BC9001  Paper                1211\nBC9034  Notebook              588\nBC9026  Computer               49\nBC9072  Pencil                147\n")
        remove_file('t99.dat')
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
