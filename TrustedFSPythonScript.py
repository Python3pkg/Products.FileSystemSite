# Copyright (C) 2004 by Dr. Dieter Maurer, Eichendorffstr. 23, D-66386 St. Ingbert, Germany
# see "doc/TRUSTED_LICENSE.txt" for details
#       $Id: TrustedFSPythonScript.py,v 1.1 2004/09/06 17:00:46 faassen Exp $
'''FSPythonScript unrestricted by Zopes security.'''

from FSPythonScript import FSPythonScript, registerFileExtension, Cacheable

from ReuseUtils import rebindFunction
from Utils import _UnCustomizable
from TrustedPythonScriptMixin import TrustedPythonScriptMixin
from TrustedPythonScript import TrustedPythonScript


class TrustedFSPythonScript(_UnCustomizable, TrustedPythonScriptMixin,
                            FSPythonScript):
  meta_type = 'Trusted Filesystem Python Script'

  _write = rebindFunction(FSPythonScript._write.im_func,
                          PythonScript=TrustedPythonScript,
                          )

registerFileExtension('xpy', TrustedFSPythonScript)
