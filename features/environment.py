from behave import *
import os
import logging

from behave.model_core import Status
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from configuration.config import BaseConfig
from pages.main_page import MainPage


def before_all(context):
    #Set up the loggin
    context.logger = logging.getLogger(__name__)
    context.logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    context.logger.addHandler(handler)
    if not os.path.exists(BaseConfig.SCREENSHOT_DIRECTORY):
        os.makedirs(BaseConfig.SCREENSHOT_DIRECTORY)
    f = open("Results.csv", "w")
    f.write("Name,Result,Error\n")
    f.close()

def before_scenario(context, scenario):
    service = Service(BaseConfig.CHROME_PATH)
    options = webdriver.ChromeOptions()
    context.driver  = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()
    context.logger.info('Abriendo el navegador')
    context.mainPage = MainPage(context.driver,context.logger)
    path=(BaseConfig.SCREENSHOT_DIRECTORY+"/"+scenario.name).replace(" ","_")
    if not os.path.exists(path):
        os.makedirs(path)

def after_step(context, step):
    path=(BaseConfig.SCREENSHOT_DIRECTORY+"/"+context.scenario.name).replace(" ","_")
    name=("Step_"+step.name+".png").replace(" ","_")
    context.driver.save_screenshot(path+"/"+name)
    context.logger.info('Captura guardada en '+path+"/"+name)
    if step.status == Status.failed:
        f = open("Results.csv", "a")
        f.write(context.scenario.name+",Failed,"+step.error_message+"\n")
        f.close()


def after_scenario(context, scenario):
    context.driver.close()
    context.logger.info('Cerrando el navegador')
    if scenario.status == Status.passed:
        f = open("Results.csv", "a")
        f.write(scenario.name+",Passed,None\n")
        f.close()