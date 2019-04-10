#!/usr/bin/env python3
# coding=utf-8 -*- python -*-

# erzeugt Mittwoch, 10. April 2019 23:22 (C) 2019 von Leander Jedamus
# modifiziert Mittwoch, 10. April 2019 23:25 von Leander Jedamus

from multiprocessing import Process, Pipe

def fun(conn):
  conn.send([42, None, "hello"])
  conn.close()

if __name__ == '__main__':
  connection_1, connection_2 = Pipe()
  p = Process(target=fun, args=(connection_2,))
  p.start()
  print(connection_1.recv())
  p.join()

# vim:ai sw=2 sts=4 expandtab

