from collective.behavior.vat.adapter.interface import Adapter
from collective.behavior.vat.interfaces import IAdapter
from collective.behavior.vat.tests.base import IntegrationTestCase


class AdapterTestCase(IntegrationTestCase):
    """TestCase for Adapter"""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_subclass(self):
        from five.grok import Adapter as BaseAdapter
        self.assertTrue(issubclass(Adapter, BaseAdapter))

    def test_context(self):
        from zope.interface import Interface
        self.assertEqual(getattr(Adapter, 'grokcore.component.directive.context'), Interface)

    def test_provides(self):
        self.assertEqual(getattr(Adapter, 'grokcore.component.directive.provides'), IAdapter)

    def test_percent(self):
        adapter = IAdapter(self.portal)
        self.assertEqual(adapter.percent(5.0), u'5%')
        self.assertEqual(adapter.percent(5.1), u'5.1%')
        self.assertEqual(adapter.percent(5.12), u'5.12%')
        self.assertEqual(adapter.percent(5.123), u'5.123%')
