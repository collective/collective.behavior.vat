=======================
collective.behavior.vat
=======================

collective.behavior.vat provides VAT related behavior to dexterity content types.

Currently tested with
---------------------

* Plone-4.2.5 and Python-2.7.x [taito]

Behavior
--------

The behavior can be added through the web or directly through the file system to the dexterity content type xml file like::

  <property name="behaviors">
    ...
    <element value="collective.behavior.vat.interfaces.IVAT" />
    ...
  </property>

* VAT value can be preset through registry.
