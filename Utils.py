# Copyright (C) 2004 by Dr. Dieter Maurer, Eichendorffstr. 23, D-66386 St. Ingbert, Germany
# see "LICENSE.txt" for details
#       $Id: Utils.py,v 1.1 2004/09/06 17:00:46 faassen Exp $
'''Utilities'''

from ExtensionClass import Base

class _UnCustomizable(Base):
  '''mixin class to prevent customization.'''
  def manage_doCustomize(self):
    "do not allow customization"
    raise TypeError('This object does not support customization')
