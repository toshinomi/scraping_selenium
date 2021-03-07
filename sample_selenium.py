# -*- coding: utf-8 -*-
from selenium import webdriver
import sys

if __name__ == '__main__':
    driver_file = sys.argv[1]
    driver = webdriver.Firefox(executable_path=driver_file)
    driver.get("https://www.yahoo.co.jp/")
    driver.quit()