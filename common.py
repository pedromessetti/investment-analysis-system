# common.py

import os
import openpyxl
import csv
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def setup_firefox_driver():
    try:
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
        wait = WebDriverWait(driver, 10)
        return driver, wait
    except:
        print('Erro ao iniciar o driver do Firefox')
        exit()
