import data
import hw1
import unittest

from data import Point
from hw1 import add_prices


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowels(self):
        x="how are you doing"
        result =  hw1.vowel_count(x)
        expected = 7
        self.assertEqual(result,expected)
    def test_vowels2(self):
        x="I am doing well"
        result =  hw1.vowel_count(x)
        expected = 5
        self.assertEqual(result,expected)

    # Part 2
    def test_short_lists(self):
        list1=[[2,3,4],[4],[8,7],[9],[5,3]]
        result=hw1.short_lists(list1)
        expected=[[8,7],[5,3]]
        self.assertEqual(result, expected)
    def test_short_lists2(self):
        list1=[[2,4],[4,5],[50,67,279],[9],[100,101]]
        result=hw1.short_lists(list1)
        expected=[[2,4],[4,5],[100,101]]
        self.assertEqual(result, expected)

    # Part 3
    def test_ascending_pairs(self):
        list1=[[6,3],[9,10,45],[4,1]]
        result=hw1.ascending_pairs(list1)
        expected=[[3,6],[9,10,45],[1,4]]
        self.assertEqual(result, expected)
    def test_ascending_pairs2(self):
        list1=[[3,1],[99,50,45,76],[100,105,96]]
        result=hw1.ascending_pairs(list1)
        expected=[[1,3],[99,50,45,76],[100,105,96]]
        self.assertEqual(result, expected)


    # Part 4
    def test_add_prices(self):
        price1=data.Price(2,75)
        price2=data.Price(4,35)
        result=hw1.add_prices(price1,price2)
        expected=data.Price(7,10)
        self.assertEqual(result, expected)

    def test_add_prices2(self):
        price1=data.Price(5,75)
        price2=data.Price(9,25)
        result=hw1.add_prices(price1,price2)
        expected=data.Price(15,0)
        self.assertEqual(result, expected)

    # Part 5
    def test_rectangle(self):
        rectangle= data.Rectangle(top_left=Point(0,0),bottom_right=Point(3, -4))
        result=hw1.rectangle_area(rectangle)
        expected = 12
        self.assertEqual(result,expected)
    def test_rectangle2(self):
        rectangle= data.Rectangle(top_left=Point(2, 2), bottom_right=Point(4, -6))
        result=hw1.rectangle_area(rectangle)
        expected = 16
        self.assertEqual(result,expected)


    # Part 6
    def test_books_by_author(self):
        books=[data.Book(["Mike"],"The End"), data.Book(["Robert"],"Beginning"),data.Book(["Dave"],"Middle")]
        result=hw1.books_by_author("Mike",books)
        expected=["The End"]
        self.assertEqual(result, expected)

    def test_books_by_author2(self):
        books=[data.Book(["Scott"],"Scott's World"), data.Book(["Scott"],"World's Beginning"),data.Book(["Bob"],"World's Middle")]
        result=hw1.books_by_author("Scott",books)
        expected=["Scott's World", "World's Beginning"]
        self.assertEqual(result, expected)


    # Part 7
    def test_circle_bound(self):
        rectangle=data.Rectangle(top_left=Point(0,0),bottom_right=Point(3,-4))
        result=hw1.circle_bound(rectangle)
        expected=data.Circle(data.Point(1.5,-2),2.5)
        self.assertEqual(result, expected)
    def test_circle_bound2(self):
        rectangle=data.Rectangle(top_left=Point(2,2),bottom_right=Point(4,-6))
        result=hw1.circle_bound(rectangle)
        expected=data.Circle(data.Point(3,-2),(17**0.5))
        self.assertEqual(result, expected)

    # Part 8
    def test_below_pay_average(self):
        employees=[data.Employee("Bob",36582),data.Employee("Cooper",94758),data.Employee("Alice",62783)]
        result=hw1.below_pay_average(employees)
        expected=["Bob","Alice"]
        self.assertEqual(result, expected)

    def test_below_pay_average2(self):
        employees = [data.Employee("Sophia", 284759), data.Employee("Heather", 379399), data.Employee("Doug", 273829)]
        result = hw1.below_pay_average(employees)
        expected = ["Sophia", "Doug"]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
