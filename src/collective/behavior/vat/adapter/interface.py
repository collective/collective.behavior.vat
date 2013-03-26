from collective.behavior.vat.interfaces import IAdapter
from decimal import Decimal
from five import grok
from zope.interface import Interface


class Adapter(grok.Adapter):
    """Adapter for handling VAT rate"""
    grok.context(Interface)
    grok.provides(IAdapter)

    def percent(self, rate):
        """Returns localized vat rate with percent

        :param rate: VAT rate
        :type rate: float

        :rtype: unicode
        """
        if str(rate)[-1] == '0':
            decimal_place = 0
        else:
            decimal_place = abs(Decimal(str(rate)).as_tuple().exponent)

        pattern = u'#,###.{}%'.format(u'' + u'#' * decimal_place)
        return self.context.REQUEST.locale.numbers.getFormatter(u'percent').format(rate, pattern=pattern)
