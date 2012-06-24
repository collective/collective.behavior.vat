import mock
import unittest


class TestVATsVocabulary(unittest.TestCase):

    def test_subclass(self):
        from collective.behavior.vat.vocabulary import VATsVocabulary
        self.assertTrue(issubclass(VATsVocabulary, object))

    def create_instance(self):
        from collective.behavior.vat.vocabulary import VATsVocabulary
        return VATsVocabulary()

    def test_instance(self):
        instance = self.create_instance()
        from collective.behavior.vat.vocabulary import VATsVocabulary
        self.assertIsInstance(instance, VATsVocabulary)

    def test_instance__implements(self):
        instance = self.create_instance()
        from zope.schema.interfaces import IVocabularyFactory
        self.assertTrue(IVocabularyFactory.providedBy(instance))

    @mock.patch('collective.behavior.vat.vocabulary.SimpleVocabulary')
    @mock.patch('collective.behavior.vat.vocabulary.getUtility')
    def test_instance__call__(self, getUtility, SimpleVocabulary):
        instance = self.create_instance()
        context = mock.Mock()
        getUtility.return_value = {
            'collective.behavior.vat.VAT': [0.0, 9.0, 13.0, 23.0]
        }
        instance(context)
        self.assertEqual(SimpleVocabulary.createTerm.call_count, 4)
        from decimal import Decimal
        SimpleVocabulary.createTerm.assert_called_with(
            Decimal('23.00'), '23.00', '23.00 %')

    @mock.patch('collective.behavior.vat.vocabulary.SimpleVocabulary')
    @mock.patch('collective.behavior.vat.vocabulary.getUtility')
    def test_instance__call__no_vats(self, getUtility, SimpleVocabulary):
        instance = self.create_instance()
        context = mock.Mock()
        getUtility.return_value = {
            'collective.behavior.vat.VAT': []
        }
        instance(context)
        SimpleVocabulary.assert_called_with([])
