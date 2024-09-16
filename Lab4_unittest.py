import unittest
from Lab3_2sem import *


class TestSumMethods(unittest.TestCase):

    def test_sort_by_weight(self):
        pump_objects = [
            Pump(110, 600, "Green Cycle", Countries.Ukraine.name, 100, "Type A"),
            Pump(185, 300, "Alan Bike", Countries.Italy.name, 90, "Type C"),
            Pump(114.9, 750, "American Bicycle Group", Countries.USA.name, 50, "Type B"),
        ]
        sort_by_weight(pump_objects, False)
        self.assertGreaterEqual(pump_objects[1]._Good__weight_in_grams, pump_objects[0]._Good__weight_in_grams)
        self.assertTrue(pump_objects[1]._Good__weight_in_grams <= pump_objects[2]._Good__weight_in_grams)

        sort_by_weight(pump_objects, True)
        self.assertLessEqual(pump_objects[1]._Good__weight_in_grams, pump_objects[0]._Good__weight_in_grams)
        self.assertFalse(pump_objects[1]._Good__weight_in_grams < pump_objects[2]._Good__weight_in_grams)


    def test_sort_by_producer(self):
        pump_objects = [
            Pump(110, 600, "Green Cycle", Countries.Ukraine.name, 100, "Type A"),
            Pump(185, 300, "Alan Bike", Countries.Italy.name, 90, "Type C"),
            Pump(114.9, 750, "American Bicycle Group", Countries.USA.name, 50, "Type B"),
        ]
        sort_by_producer(pump_objects, False)
        self.assertTrue(pump_objects[0].producer <= pump_objects[1].producer)
        self.assertTrue(pump_objects[1].producer <= pump_objects[2].producer)

        sort_by_producer(pump_objects, True)
        self.assertGreaterEqual(pump_objects[0].producer, pump_objects[1].producer)
        self.assertGreaterEqual(pump_objects[1].producer, pump_objects[2].producer)


    def test_search_by_producer(self):
        lamp_objects = [
            Lamp(60, 150, "Norco Performance Bikes", Countries.Canada.name, 4, 5000, 6),
            Lamp(80, 225, "DK", Countries.USA.name, 4, 6000, 7),
            Lamp(45, 80, "GAMMA", Countries.China.name, 2, 3000, 9),
            Lamp(75, 120, "Flybikes", Countries.Spain.name, 7, 4500, 5),
        ]
        producer_of_lamp = search_by_producer(lamp_objects, "Norco Performance Bikes").producer
        self.assertEqual(producer_of_lamp, "Norco Performance Bikes")
        self.assertEqual(search_by_producer(lamp_objects, "Norco"), None)

    
if __name__ == '__main__':
    unittest.main()