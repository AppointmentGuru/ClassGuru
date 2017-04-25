from django.test import TestCase, override_settings, Client
from django.core.urlresolvers import reverse
from classbooker.models import Class

class ClassListViewEndpointTestCase(TestCase):

    def setUp(self, *args, **kwargs):

        data = {
            "name": "Some class",
            "price": 123
        }
        Class.objects.create(**data)
        self.url = reverse('class-list')
        self.c = Client()
        self.result = self.c.get(self.url)

    def test_can_get_list_of_classes(self):
        assert self.result.status_code == 200, \
            'Expected 200 OK. got: {}' . format(self.result)

    def test_returns_exactly_one_result(self):
        assert len(self.result.json()) == 1



