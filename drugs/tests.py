from django.test import TestCase
from drugs.models import Drug

class DrugTests(TestCase):
    def test_str(self):
        my_title = Drug(name='This is a basic title for a basic test case')
        self.assertEquals(
            str(my_title), 'This is a basic title for a basic test case',
        )
