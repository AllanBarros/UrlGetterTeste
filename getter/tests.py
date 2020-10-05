from django.test import TestCase, Client
from .views import dbSave


# Create your tests here.

class TestUrlGetter(TestCase):

    def setUp(self):
        self.c = Client()

    def test_url_getter_pass(self):
        response = self.c.post('/crawler/', data="https://www.google.com", content_type="JSON")
        self.assertEqual(response.status_code, 200)

    def test_url_getter_not_pass(self):
        response = self.c.post('/crawler/', data="", content_type="JSON")
        self.assertContains(response, "Url não informada", status_code=200)

class TestDbSave(TestCase):

        def setUp(self):
            self.urls_internas = ["https://www.google.com/a", "https://www.google.com/b", "https://www.google.com/c"]
            self.urls_internas_vazias = []
            self.link_inicial = "https://www.google.com"
            self.link_inicial_vazio = ""

        def test_db_save_pass(self):
            response = dbSave(self.link_inicial, self.urls_internas)
            self.assertFalse(len(response) == 0)
            
        def test_db_save_not_pass_link_inicial(self):
            response = dbSave(self.link_inicial_vazio, self.urls_internas)
            self.assertContains(response, "Url inicial não informada", status_code=200)

        def test_db_save_not_pass_link_inicial(self):
            response = dbSave(self.link_inicial, self.urls_internas_vazias)
            self.assertContains(response, "Não existem urls relacionadas", status_code=200)