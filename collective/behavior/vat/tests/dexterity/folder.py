from five import grok
from plone.directives import form


class ITestFolder(form.Schema):
    """Schema interface for TestFolder"""


# class View(grok.View):
#     """Default view for page."""

#     grok.context(ITestFolder)
#     grok.require('zope2.View')
#     grok.name('view')
