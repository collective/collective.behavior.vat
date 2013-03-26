from collective.behavior.vat.interfaces import IVAT

import unittest


class TestIVAT(unittest.TestCase):
    """TestCase for IVAT"""

    def test_subclass(self):
        from plone.directives import form
        self.assertTrue(issubclass(IVAT, form.Schema))

    def get_schema(self, name):
        """Get schema by name.

        :param name: Name of schema.
        :type name: str
        """
        return IVAT.get(name)

    def test_rate__instance(self):
        schema = self.get_schema('rate')
        from zope.schema import Choice
        self.assertIsInstance(schema, Choice)

    def test_rate__title(self):
        schema = self.get_schema('rate')
        self.assertEqual(schema.title, u'VAT rate')

    def test_rate__vocabylary(self):
        schema = self.get_schema('rate')
        self.assertEqual(schema.vocabularyName, u'collective.behavior.vat.rates')
