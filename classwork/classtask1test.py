from unittest import TestCase
import classtask1

class TestforPrimeNumber(TestCase):

    def test_that_function_exists(self):
        classtask1.prime_number_checker
        
    def test_that_function_checks_for_prime_numbers(self):    
        actual = classtask1.prime_number_checker
        expected = True
        self.assertTrue(actual,expected)
    
