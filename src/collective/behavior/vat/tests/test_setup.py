from Products.CMFCore.utils import getToolByName
from collective.behavior.vat.tests.base import IntegrationTestCase


class TestSetup(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(
            installer.isProductInstalled('collective.behavior.vat'))

    def test_catalog__column__vat_rate(self):
        catalog = getToolByName(self.portal, 'portal_catalog')
        self.assertIn('vat_rate', catalog.schema())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile(
                'profile-collective.behavior.vat:default'), u'0')

    def get_record_rates(self):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        registry = getUtility(IRegistry)
        return registry.records.get('collective.behavior.vat.rates')

    def test_registry_record__rates__field__instance(self):
        record = self.get_record_rates()
        from plone.registry.field import List
        self.assertIsInstance(record.field, List)

    def test_registry_record__rates__field__title(self):
        record = self.get_record_rates()
        self.assertEqual(record.field.title, u'VAT')

    def test_registry_record__rates__field__description(self):
        record = self.get_record_rates()
        self.assertEqual(record.field.description, u'A list of VAT in %.')

    def test_registry_record__rates__field__value_type(self):
        record = self.get_record_rates()
        from plone.registry.field import Float
        self.assertIsInstance(record.field.value_type, Float)

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.behavior.vat'])
        self.failIf(installer.isProductInstalled('collective.behavior.vat'))

    def test_uninstall__registry_rates(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.behavior.vat'])
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        registry = getUtility(IRegistry)
        with self.assertRaises(KeyError):
            registry['collective.behavior.vat.rates']
