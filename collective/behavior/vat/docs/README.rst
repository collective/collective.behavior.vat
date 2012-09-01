=======================
collective.behavior.vat
=======================

collective.behavior.vat provides VAT related behavior to dexterity content types.

Currently Tested with
---------------------

* Plone-4.2.1 [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.behavior.vat.interfaces.IVAT" />
    ...
  </property>

* VAT value can be preset through registry.

Farther Documentation URL
-------------------------

`http://packages.python.org/collective.behavior.vat/
<http://packages.python.org/collective.behavior.vat/>`_

Repository URL
--------------

`https://github.com/collective/collective.behavior.vat/
<https://github.com/collective/collective.behavior.vat/>`_
