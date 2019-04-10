#!/usr/bin/env python3
# coding=utf-8 -*- python -*-

# erzeugt Mittwoch, 10. April 2019 22:52 (C) 2019 von Leander Jedamus
# modifiziert Mittwoch, 10. April 2019 22:57 von Leander Jedamus

#from __future__ import print_function
from threading import Thread
import time

def gui():
  for i in range(10):
    print("#",end="")
    time.sleep(1)

def work(how_long):
  time.sleep(how_long)

t1 = Thread(target=gui, name="Oberfläche", args=())
t2 = Thread(target=work, name="Verarbeitung", args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()

# vim:ai sw=2 sts=4 expandtab

