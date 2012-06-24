from collective.behavior.vat.interfaces import IVAT
from decimal import Decimal
from plone.directives import form
from rwproperty import getproperty
from rwproperty import setproperty
from zope.interface import alsoProvides
from zope.interface import implements

import logging

logger = logging.getLogger(__name__)


alsoProvides(IVAT, form.IFormFieldProvider)


class VAT(object):
    """
    """
    implements(IVAT)

    def __init__(self, context):
        self.context = context

    @getproperty
    def vat(self):
        return getattr(self.context, 'vat', None)

    @setproperty
    def vat(self, value):
        """Setting vat as Decimal.

        :param value: VAT value such as 5.00.
        :type value: decimal.Decimal
        """
        if isinstance(value, Decimal):
            # Set vat
            setattr(self.context, 'vat', value)
        else:
            raise ValueError('Not Decimal.')
