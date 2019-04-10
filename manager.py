#!/usr/bin/env python3
# coding=utf-8 -*- python -*-

# erzeugt Mittwoch, 10. April 2019 23:26 (C) 2019 von Leander Jedamus
# modifiziert Mittwoch, 10. April 2019 23:28 von Leander Jedamus

from multiprocessing import Process, Manager

def fun(d,l):
  d[1] = "eins"
  d[2] = "zwei"
  l.reverse()

if __name__ == '__main__':
  mgr = Manager()
  d = mgr.dict()
  l = mgr.list(["a","b","c","d"])

  p = Process(target=fun, args=(d,l))
  p.start()
  p.join()

  print(d)
  print(l)

# vim:ai sw=2 sts=4 expandtab

# vim:ai sw=2 sts=4 expandtab

