# encoding: utf-8

import os

url_b = "https://zidian.911cha.com/bihua_"

for i in range(64, 100, 1):
    while True:
		ret = os.system("wget " + url_b + str(i) + ".html")
		if (ret == 0) : break