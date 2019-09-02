import unittest

class ClassifyTriangle:
    """ Python Program on classify triangle
        Purpose: Home work Assignment for Software Testing
        Level:  Graduate Home work

    """

    def __init__(self, t1, t2, t3):
                
        
        if t1 <= 0 or t2 <= 0 or t3 <= 0:
            raise ValueError(" Triangle sides < 0")
        else:
            self.t1 = t1
            self.t2 = t2
            self.t3 = t3
            
            
    def right_triangle(self):
        return round(((self.t1 ** 2) + (self.t2 ** 2)), 2) == round((self.t3 ** 2), 2)



    def equilateral(self):
        """ To check if the sides are equilater triangle """
        if self.t1 == self.t2 and self.t2 == self.t3:
            return True
        else:
            return False

    def isosceles(self):
        """ To check if sides are isosceles triangle """
        if self.t1 == self.t2 or self.t2 == self.t3 or self.t3 == self.t1:
            return True
        else:
            return False

    def scalene(self):
        if (self.t1 != self.t2) and (self.t2 != self.t3) and (self.t3 != self.t1):
            return True
        else:
            return False

        




class TestClassifyTriangle(unittest.TestCase):
    def test_init(self):
        ct = ClassifyTriangle(3,4,5)
        self.assertEqual(ct.t1, 3)
        self.assertEqual(ct.t2, 4)
        self.assertEqual(ct.t3, 5)

    def test_right_triangle(self):
        ct = ClassifyTriangle(3,4,5)
        self.assertTrue(ct.right_triangle())
        self.assertFalse(ClassifyTriangle(5,4,3).right_triangle())

        
    def test_equilateral(self):
        ct = ClassifyTriangle(5,5,5)
        self.assertTrue(ct.equilateral())
        self.assertFalse(ClassifyTriangle(5,9,7).equilateral())



    def test_isosceles(self):
        ct =  ClassifyTriangle(3,5,5)
        self.assertTrue(ct.isosceles())
        self.assertFalse(ClassifyTriangle(3,6,7).isosceles())

    def test_scalene(self):
        ct =  ClassifyTriangle(7,8,9)
        self.assertTrue(ct.scalene())
        self.assertTrue(ClassifyTriangle(7,8,9).scalene())
    



if __name__=='__main__':
    unittest.main(exit = False, verbosity=2)
