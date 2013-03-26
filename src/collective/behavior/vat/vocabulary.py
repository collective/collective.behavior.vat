from collective.behavior.vat.interfaces import IAdapter
from five import grok
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


class VATRatesVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        registry = getUtility(IRegistry)
        vats = registry['collective.behavior.vat.rates']
        terms = []

        if vats:
            for vat in vats:
                locale_vat = IAdapter(context).percent(vat)
                terms.append(
                    SimpleVocabulary.createTerm(
                        vat, str(vat), locale_vat))

        return SimpleVocabulary(terms)


grok.global_utility(VATRatesVocabulary, name=u"collective.behavior.vat.rates")
