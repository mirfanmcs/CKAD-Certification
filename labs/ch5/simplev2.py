#!/usr/bin/python

import time
import socket

while True :

  host = socket.gethostname()
  date = time.strftime("%d-%m-%Y %H: %M: %S")

  now = str(date)
  
  f = open("./tmp/datev2.out","a")
  f.write(now + "\n")
  f.write(host + "\n")
  f.close()

  time.sleep(5)

