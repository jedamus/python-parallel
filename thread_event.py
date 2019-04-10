#!/usr/bin/env python3
# coding=utf-8 -*- python -*-

# erzeugt Mittwoch, 10. April 2019 22:58 (C) 2019 von Leander Jedamus
# modifiziert Mittwoch, 10. April 2019 23:15 von Leander Jedamus

from threading import Thread, Event
import time

def gui(e):
  while not e.is_set():
    e.wait(1)
    print("#",end="")

def work(how_long,e):
  time.sleep(how_long)
  e.set()

e = Event()
t1 = Thread(target=gui, name="Oberfläche", args=(e,))
t1.start()
t2 = Thread(target=work, name="Verarbeitung", args=(2, e))
t2.start()

t1.join()
t2.join()

# vim:ai sw=2 sts=4 expandtab

