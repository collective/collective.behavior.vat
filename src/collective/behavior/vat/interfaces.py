from collective.behavior.vat import _
from plone.directives import form
from zope.interface import Interface
from zope.schema import Choice


class IVAT(form.Schema):
    """Interface for VAT behavior."""

    rate = Choice(
        title=_(u'VAT rate'),
        vocabulary=u'collective.behavior.vat.rates')


class IAdapter(Interface):
    """Adapter interface for handling vat rate"""

    def percent(rate):  # pragma: no cover
        """Returns localized vat rate with percent

        :param rate: VAT rate
        :type rate: float

        :rtype: unicode
        """
