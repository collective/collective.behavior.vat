import unittest


class TestIVAT(unittest.TestCase):

    def test_subclass(self):
        from collective.behavior.vat.interfaces import IVAT
        from zope.interface import Interface
        self.assertTrue(issubclass(IVAT, Interface))

    def get_schema(self, name):
        """Get schema by name.

        :param name: Name of schema.
        :type name: str
        """
        from collective.behavior.vat.interfaces import IVAT
        return IVAT.get(name)

    def test_vat__instance(self):
        schema = self.get_schema('vat')
        from zope.schema import Choice
        self.assertIsInstance(schema, Choice)

    def test_vat__title(self):
        schema = self.get_schema('vat')
        self.assertEqual(schema.title, u'VAT')

    def test_vat__vocabylary(self):
        schema = self.get_schema('vat')
        self.assertEqual(
            schema.vocabularyName, u'collective.behavior.vat.vats')
