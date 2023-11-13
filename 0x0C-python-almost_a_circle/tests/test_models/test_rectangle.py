import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    def test_id(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r2.id, 6)

    def test_width(self):
        r1 = Rectangle(1, 2, 0, 0, 2)
        r2 = Rectangle(3, 4, 0, 0, 3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r2.width, 3)
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle('a', 2, 9, 9, 9)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(True, 2, 9, 9, 9)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(4.5, 2, 9, 9, 9)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle((1, 2), 2, 9, 9, 9)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle([1, 2], 2, 9, 9, 9)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle({'a' : 1}, 2, 9, 9, 9)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(ValueError) as context_2:
            r4 = Rectangle(0, 1, 2, 3, 4)
        self.assertEqual(str(context_2.exception), "width must be > 0")
        with self.assertRaises(ValueError) as context_2:
            r4 = Rectangle(-54, 1, 2, 3, 4)
        self.assertEqual(str(context_2.exception), "width must be > 0")

    def test_height(self):
        r1 = Rectangle(1, 2, 0, 0, 3)
        r2 = Rectangle(3, 4, 0, 0, 5)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 4)
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 'a', 0, 0, 3)
        self.assertEqual(str(context.exception), "height must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, True, 0, 0, 3)
        self.assertEqual(str(context.exception), "height must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 4.5, 0, 0, 3)
        self.assertEqual(str(context.exception), "height must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, (1, 2), 0, 0, 3)
        self.assertEqual(str(context.exception), "height must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, [1, 2], 0, 0, 3)
        self.assertEqual(str(context.exception), "height must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, {'a' : 2}, 0, 0, 3)
        self.assertEqual(str(context.exception), "height must be an integer")
        with self.assertRaises(ValueError) as context:
            r3 = Rectangle(1, 0, 2, 3, 4)
        self.assertEqual(str(context.exception), "height must be > 0")
        with self.assertRaises(ValueError) as context:
            r3 = Rectangle(1, -69, 2, 3, 4)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_x(self):
        r1 = Rectangle(1, 2, 10, 0, 3)
        r2 = Rectangle(3, 4, 20, 0, 5)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r2.x, 20)
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, 'a', 0, 3)
        self.assertEqual(str(context.exception), "x must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, True, 0, 3)
        self.assertEqual(str(context.exception), "x must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, 5.5, 0, 3)
        self.assertEqual(str(context.exception), "x must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, (1, 2), 0, 3)
        self.assertEqual(str(context.exception), "x must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, [1, 2], 0, 3)
        self.assertEqual(str(context.exception), "x must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, {'a' : 69}, 0, 3)
        self.assertEqual(str(context.exception), "x must be an integer")
        with self.assertRaises(ValueError) as context:
            r3 = Rectangle(1, 1, -1, 9, 10)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y(self):
        r1 = Rectangle(1, 2, 10, 33, 3)
        r2 = Rectangle(3, 4, 20, 45, 5)
        self.assertEqual(r1.y, 33)
        self.assertEqual(r2.y, 45)
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, 0, 'a', 3)
        self.assertEqual(str(context.exception), "y must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, 0, True, 3)
        self.assertEqual(str(context.exception), "y must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, 0, 5.5, 3)
        self.assertEqual(str(context.exception), "y must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, 0, (1, 2), 3)
        self.assertEqual(str(context.exception), "y must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, 0, [1, 2], 3)
        self.assertEqual(str(context.exception), "y must be an integer")
        with self.assertRaises(TypeError) as context:
            r3 = Rectangle(1, 1, 0, {'a' : 69}, 3)
        self.assertEqual(str(context.exception), "y must be an integer")
        with self.assertRaises(ValueError) as context:
            r3 = Rectangle(1, 1, 9, -1, 10)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_area(self):
        r1 = Rectangle(2, 4, 0, 0, 5)
        self.assertEqual(r1.area(), 2 * 4)
        r2 = Rectangle(2, 4, 0, 0, 0)
        self.assertEqual(r1.area(), r2.area())

    @patch('builtins.print')
    def test_display(self, mock_print):
        r1 = Rectangle(2, 3, 0, 0, 5)
        r1.display()

        mock_print.assert_called_with("##\n##\n##\n")
