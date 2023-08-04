from django.test import TestCase
from ..models import User,Voluntary


class VoluntaryTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.voluntary = Voluntary.objects.create(
            hours_worked=10.5,
            user=self.user
        )

    def test_hours_work(self):
        self.assertEqual(self.voluntary.hours_worked, 10.5)

    def test_foreign_key(self):
        self.assertEqual(self.voluntary.user, self.user)