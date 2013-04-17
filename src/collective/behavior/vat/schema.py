from collective.behavior.vat import _
from plone.supermodel.model import Schema
from zope import schema


class VATSchema(Schema):
    """Schema for behavior: VAT"""

    rate = schema.Choice(
        title=_(u'VAT rate'),
        vocabulary=u'collective.behavior.vat.rates')
