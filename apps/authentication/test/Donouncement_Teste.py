from django.test import TestCase
from ..models import User,Denouncement
from django.core.files.uploadedfile import SimpleUploadedFile

class DenouncementTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')

    def test_create_denouncement(self):
        denouncement = Denouncement.objects.create(
            title='test',
            description='Just teste',
            image=SimpleUploadedFile('test_image.jpg', b'cont', content_type='image/jpeg'),#act like a real image
            author=self.user,
        )
        self.assertEqual(denouncement.title, 'The Title')
        self.assertEqual(denouncement.description, 'The Description')
        self.assertEqual(denouncement.image.read(), b'cont')
        self.assertEqual(denouncement.author, self.user)