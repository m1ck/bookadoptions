import unittest
from aos.models import Person, Greeting
from google.appengine.ext import testbed

class Test(unittest.TestCase):


    def test_trivial(self):
        self.assertEqual(0, 0)

class TestPerson(unittest.TestCase):
    
    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
    
    def test_is_old(self):  
        person = Person(name='JJ', age=22)
        self.assertFalse(person.is_old())
        
    def test_is_empty(self):
        self.assertEqual(Person.all().count(), 0)

        person = Person(name='JJ', age=22)
        person.put()

        self.assertEqual(Person.all().count(), 1)

    def test_assert_empty_again(self):
        self.assertEqual(Person.all().count(), 0)
    
        person = Person(name='JJ', age=22)
        person.put()
    
        self.assertEqual(Person.all().count(), 1)

    def test_Greetings(self):
        Greeting(content='This is a test greeting').save()
        self.assertEqual(1, len(Greeting.objects.all()))
        self.assertEqual('This is a test greeting', Greeting.objects.all()[0].content)
