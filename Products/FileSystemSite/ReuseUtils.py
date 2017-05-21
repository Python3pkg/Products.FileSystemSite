# Copyright (C) 2004 by Dr. Dieter Maurer, Eichendorffstr. 23, D-66386 St. Ingbert, Germany
# see "LICENSE.txt" for details
#       $Id: ReuseUtils.py,v 1.1 2004/09/06 17:00:46 faassen Exp $

from new import function

def rebindFunction(f,rebindDir=None,**rebinds):
  '''return *f* with some globals rebound.'''
  d= {}
  if rebindDir : d.update(rebindDir)
  if rebinds: d.update(rebinds)
  if not d: return f
  f= getattr(f,'im_func',f)
  fd= f.__globals__.copy()
  fd.update(d)
  nf= function(f.__code__,fd,f.__name__,f.__defaults__ or ())
  nf.__doc__= f.__doc__
  if f.__dict__ is not None: nf.__dict__= f.__dict__.copy()
  return nf
