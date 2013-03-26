from collective.behavior.vat.tests.base import IntegrationTestCase
from collective.behavior.vat.vocabulary import VATRatesVocabulary


class VATRatesVocabularyTestCase(IntegrationTestCase):
    """TestCase for VATRatesVocabulary"""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_subclass(self):
        self.assertTrue(issubclass(VATRatesVocabulary, object))

    def test_instance(self):
        instance = VATRatesVocabulary()
        self.assertIsInstance(instance, VATRatesVocabulary)

    def test_implements(self):
        instance = VATRatesVocabulary()
        from zope.schema.interfaces import IVocabularyFactory
        self.assertTrue(IVocabularyFactory.providedBy(instance))

    def test___call__(self):
        instance = VATRatesVocabulary()
        self.assertEqual(len(instance(self.portal)), 4)

        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        getUtility(IRegistry)['collective.behavior.vat.rates'] = []
        self.assertEqual(len(instance(self.portal)), 0)
