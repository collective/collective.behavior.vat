from collective.behavior.vat.adapter.interface import Adapter
from collective.behavior.vat.interfaces import IAdapter
from collective.behavior.vat.tests.base import IntegrationTestCase


class AdapterTestCase(IntegrationTestCase):
    """TestCase for Adapter"""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_subclass(self):
        self.assertTrue(issubclass(Adapter, object))

    def test_percent(self):
        adapter = IAdapter(self.portal)
        self.assertEqual(adapter.percent(5.0), u'5%')
        self.assertEqual(adapter.percent(5.1), u'5.1%')
        self.assertEqual(adapter.percent(5.12), u'5.12%')
        self.assertEqual(adapter.percent(5.123), u'5.123%')
