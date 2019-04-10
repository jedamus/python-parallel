#!/usr/bin/env python3
# coding=utf-8 -*- python -*-

# erzeugt Mittwoch, 10. April 2019 23:16 (C) 2019 von Leander Jedamus
# modifiziert Mittwoch, 10. April 2019 23:20 von Leander Jedamus

from multiprocessing import Process
import time
import os

def test_it():
  print("test_it", os.getpid())
  time.sleep(3)

if __name__ == '__main__':
  print("main", os.getpid())
  p = Process(target=test_it)
  p.start()
  time.sleep(1)
  p.terminate()
  print("test_it is alive", p.is_alive())
  p.join()
  print(p.exitcode)

# vim:ai sw=2 sts=4 expandtab

