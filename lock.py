#!/usr/bin/env python3
# coding=utf-8 -*- python -*-

# erzeugt Mittwoch, 10. April 2019 23:09 (C) 2019 von Leander Jedamus
# modifiziert Mittwoch, 10. April 2019 23:14 von Leander Jedamus

import threading
import time

value=1

def work(l):
  global value
  for i in range(5):
    l.acquire() # schaltet den Lock ein
    value += 1
    print(threading.currentThread().getName(), value)
    l.release() # schaltet den Lock frei
    time.sleep(3)

l = threading.Lock() # erzeugen
t1 = threading.Thread(target=work, args=(l,))
t1.start()
t2 = threading.Thread(target=work, args=(l,))
t2.start()

t1.join()
t2.join()

# vim:ai sw=2 sts=4 expandtab

