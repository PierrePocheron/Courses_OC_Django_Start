from os import lseek
from django.test import TestCase

class URLTests(TestCase):
  def test_testhomePage(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)

  def test_testhello(self):
    response = self.client.get('/hello/')
    self.assertEquals(response.status_code, 200)

  def test_testrandom(self):
    response = self.client.get('/jnkfsdfnkjdsnkfj/')
    self.assertEquals(response.status_code, 404)