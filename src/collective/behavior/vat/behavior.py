from collective.behavior.vat.interfaces import IVAT
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.interface import implements


alsoProvides(IVAT, IFormFieldProvider)


class VAT(object):
    """Behavior to add vat field to content types"""

    implements(IVAT)

    def __init__(self, context):
        self.context = context

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
