#!/usr/bin/env python
# coding=utf-8 -*- python -*-

# erzeugt Mittwoch, 10. April 2019 22:44 (C) 2019 von Leander Jedamus
# modifiziert Mittwoch, 10. April 2019 22:49 von Leander Jedamus

from threading import Thread

def m_fun(i):
  pass

t = Thread(target=m_fun, name="M-Fun Thread", args=(2,))
t.start()

# vim:ai sw=2 sts=4 expandtab

