from behave import *
from numpy.ma.testutils import assert_equal
from selenium import webdriver
from configuration.config import BaseConfig
import logging


@given("Visito la web de Altea")
def visit_main_page(context):
    try:
        context.logger.info("Accedemos a la página principal")
        context.driver.get(BaseConfig.URL)
        assert_equal(context.driver.current_url,"https://www.alten.es/")
    except:
        assert False, "Test failed trying to access to the main page"

@when("Buscamos ofertas de empleo de {nombre}")
def search_job_by_name(context,nombre):
    try:
        context.mainPage.search_job_by_name(nombre)
        context.jobName=nombre
    except:
        assert False, "Test failed trying to search a job by a name"

@then("Aparecen ofertas que contengan ese nombre")
def check_job_result_by_name(context):
    offers=context.mainPage.get_list_offers_names()
    for offer in offers:
        assert context.jobName in offer.text, "The position "+offer.text+" does not match with "+context.jobName

@then("No aparece ningun resultado")
def check_empty_list_offers(context):
    n=context.mainPage.get_offers_number()
    assert n == 0, "The number of offers should be 0"
