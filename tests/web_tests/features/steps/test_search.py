from behave import given, when, then
from selenium import webdriver
from tests.web_tests.page_objects import HomePage, SearchResultsPage

@given('el usuario está en la página de inicio de Wikipedia')
def step_open_wikipedia(context):
    print("Abriendo Wikipedia...")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.home_page = HomePage(context.driver)
    context.results_page = SearchResultsPage(context.driver)
    print("Wikipedia cargada correctamente!")

@when('busca "{keyword}"')
def step_search_keyword(context, keyword):
    print(f"Buscando: {keyword}")
    context.home_page.search(keyword)

@then('el primer resultado debe contener "{expected_text}"')
def step_verify_search_result(context, expected_text):
    heading = context.results_page.get_first_heading()
    assert expected_text in heading, f"El resultado esperado no coincide: {heading}"
    print(f"Prueba exitosa, encontrado: {heading}")
    context.driver.quit()