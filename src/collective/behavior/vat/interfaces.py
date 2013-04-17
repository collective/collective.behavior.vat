from collective.behavior.vat.schema import VATSchema
from zope.interface import Interface


class IVAT(VATSchema):
    """Interface for behavior: VAT"""


class IAdapter(Interface):
    """Adapter interface for handling vat rate"""

    def percent(rate):  # pragma: no cover
        """Returns localized vat rate with percent

        :param rate: VAT rate
        :type rate: float

        :rtype: unicode
        """
