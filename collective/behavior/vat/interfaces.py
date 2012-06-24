from collective.behavior.vat import _
from zope.interface import Interface
from zope.schema import Choice


class IVAT(Interface):
    """Interface for VAT behavior."""

    vat = Choice(
        title=_(u'VAT'),
        vocabulary=u'collective.behavior.vat.vats')
