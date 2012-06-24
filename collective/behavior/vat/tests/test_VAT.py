import mock
import unittest


class TestVAT(unittest.TestCase):

    def test_subclass(self):
        from collective.behavior.vat.behavior import VAT
        self.assertTrue(issubclass(VAT, object))

    def create_instance(self, context=mock.Mock()):
        from collective.behavior.vat.behavior import VAT
        return VAT(context)

    def test_instance(self):
        instance = self.create_instance()
        from collective.behavior.vat.behavior import VAT
        self.assertIsInstance(instance, VAT)

    def test_instance_provides_IVAT(self):
        instance = self.create_instance()
        from collective.behavior.vat.interfaces import IVAT
        self.assertTrue(IVAT.providedBy(instance))

    def test_instance__verifyObject(self):
        instance = self.create_instance()
        from collective.behavior.vat.interfaces import IVAT
        from zope.interface.verify import verifyObject
        self.assertTrue(verifyObject(IVAT, instance))

    def test_instance__vat_empty(self):
        """First time access to vat"""
        context = object()
        instance = self.create_instance(context=context)
        self.assertIsNone(instance.vat)

    def test_instance__vat_not_empty(self):
        """Price is not empty"""
        context = mock.Mock()
        from decimal import Decimal
        vat = Decimal('5.00')
        context.vat = vat
        instance = self.create_instance(context=context)
        self.assertEqual(instance.vat, vat)

    def set_vat(self, instance, vat):
        """Setting vat to instance."""
        instance.vat = vat

    def test_instance__vat__ValueError(self):
        """Raise ValueError when setting other than Decimal."""
        instance = self.create_instance()
        self.assertRaises(ValueError, lambda: self.set_vat(instance, 'AAA'))

    def test_instance__vat__(self):
        instance = self.create_instance()
        from decimal import Decimal
        vat = Decimal('5.00')
        instance.vat = vat
        self.assertEqual(instance.context.vat, vat)
