import unittest
from datetime import datetime
from models.plate_predictor import PlatePredictor


class TestPlatePredictor(unittest.TestCase):


    def test_get_provincial(self):
        p1 = PlatePredictor('abc-123', '2019/05/30 21:10:10')
        self.assertEqual(
            p1.get_provincial(),
            'Unknown'
        )
        p2 = PlatePredictor('BBc-123', '2019/05/30 21:10:10')
        self.assertEqual(
            p2.get_provincial(),
            'Bolívar'
        )

    def test_get_type(self):
        p0 = PlatePredictor('abc-123', '2019/05/30 21:10:10')
        p1 = PlatePredictor('aAc-123', '2019/05/30 21:10:10')
        p2 = PlatePredictor('aZc-123', '2019/05/30 21:10:10')
        p3 = PlatePredictor('aEc-123', '2019/05/30 21:10:10')
        p4 = PlatePredictor('aXc-123', '2019/05/30 21:10:10')
        p5 = PlatePredictor('aSc-123', '2019/05/30 21:10:10')
        p6 = PlatePredictor('aMc-123', '2019/05/30 21:10:10')
        self.assertEqual(
            p0.get_type(),
            'private vehicle'
        )
        self.assertEqual(
            p1.get_type(),
            'Commercial Vehicle'
        )
        self.assertEqual(
            p2.get_type(),
            'Commercial Vehicle'
        )
        self.assertEqual(
            p3.get_type(),
            'Government Vehicle'
        )
        self.assertEqual(
            p4.get_type(),
            'Official Use Vehicle'
        )
        self.assertEqual(
            p5.get_type(),
            'Provincial Government Vehicle'
        )
        self.assertEqual(
            p6.get_type(),
            'Municipal Vehicles'
        )


    def test_get_info(self):
        p0 = PlatePredictor('abc-123', '2019/05/24 21:10:10')
        p1 = PlatePredictor('aAc-123', '2019/05/25 21:10:10')
        p2 = PlatePredictor('aZc-123', '2019/05/26 21:10:10')
        p3 = PlatePredictor('aEc-123', '2019/05/27 21:10:10')
        p4 = PlatePredictor('aXc-123', '2019/05/28 21:10:10')
        p5 = PlatePredictor('aSc-123', '2019/05/29 21:10:10')
        p6 = PlatePredictor('aMc-123', '2019/05/30 21:10:10')
        self.assertEqual(
            p0.get_info(),
            """Plate :abc-123 </br> Provincial: Unknown </br> Type: private vehicle </br> Can road: Yes </br>"""
        )
        self.assertEqual(
            p1.get_info(),
            """Plate :aAc-123 </br> Provincial: Unknown </br> Type: Commercial Vehicle </br> Can road: Dont </br>"""
        )
        self.assertEqual(
            p2.get_info(),
            """Plate :aZc-123 </br> Provincial: Unknown </br> Type: Commercial Vehicle </br> Can road: Dont </br>"""
        )
        self.assertEqual(
            p3.get_info(),
            """Plate :aEc-123 </br> Provincial: Unknown </br> Type: Government Vehicle </br> Can road: Yes </br>"""
        )
        self.assertEqual(
            p4.get_info(),
            """Plate :aXc-123 </br> Provincial: Unknown </br> Type: Official Use Vehicle </br> Can road: Yes </br>"""
        )
        self.assertEqual(
            p5.get_info(),
            """Plate :aSc-123 </br> Provincial: Unknown </br> Type: Provincial Government Vehicle </br> Can road: Yes </br>"""
        )
        self.assertEqual(
            p6.get_info(),
            """Plate :aMc-123 </br> Provincial: Unknown </br> Type: Municipal Vehicles </br> Can road: Yes </br>"""
        )


if __name__ == '__main__':
    unittest.main()