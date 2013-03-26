from collective.behavior.vat.interfaces import IVAT
from plone.directives import form
from zope.interface import alsoProvides
from zope.interface import implements


alsoProvides(IVAT, form.IFormFieldProvider)


class VAT(object):
    """
    """
    implements(IVAT)

    def __init__(self, context):
        self.context = context

    # @property
    # def vat(self):
    #     return getattr(self.context, 'vat', None)

    # @vat.setter
    # def vat(self, value):
    #     """Setting vat as Decimal.

    #     :param value: VAT value such as 5.00.
    #     :type value: decimal.Decimal
    #     """
    #     if isinstance(value, Decimal):
    #         # Set vat
    #         setattr(self.context, 'vat', value)
    #     else:
    #         raise ValueError('Not Decimal.')

    @property
    def rate(self):
        return getattr(self.context, 'vat_rate', None)

    @rate.setter
    def rate(self, value):
        """Setting rate

        :param value: Rate of vat whicl could be converted into float
        :type value: basestring, decimal, int, float
        """
        if not isinstance(value, float):
            value = float(value)
        setattr(self.context, 'vat_rate', value)
