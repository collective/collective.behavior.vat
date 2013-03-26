from collective.behavior.vat.behavior import VAT
from collective.behavior.vat.interfaces import IVAT

import mock
import unittest


class VATTestCase(unittest.TestCase):
    """TestCase for VAT"""

    def test_subclass(self):
        self.assertTrue(issubclass(VAT, object))

    def test_instance(self):
        context = mock.Mock()
        self.assertIsInstance(VAT(context), VAT)

    def test_provides(self):
        context = mock.Mock()
        self.assertTrue(IVAT.providedBy(VAT(context)))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        context = mock.Mock()
        self.assertTrue(verifyObject(IVAT, VAT(context)))

    def test_vat(self):
        context = object()
        instance = VAT(context)
        self.assertIsNone(instance.rate)
        with self.assertRaises(AttributeError):
            context.vat_rate

        with self.assertRaises(ValueError):
            instance.rate = 'AAA'
        with self.assertRaises(AttributeError):
            context.vat_rate

        context = mock.Mock()
        instance = VAT(context)
        instance.rate = 5.0
        self.assertEqual(context.vat_rate, 5.0)
        self.assertEqual(instance.rate, 5.0)

        instance.rate = 6
        self.assertEqual(context.vat_rate, 6.0)
        self.assertEqual(instance.rate, 6.0)
