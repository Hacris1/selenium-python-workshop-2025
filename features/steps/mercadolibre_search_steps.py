from behave import given, when, then
from pages.mercadolibre_search_page import MercadoLibreSearchPage

@given('the user is on the MercadoLibre homepage')
def step_user_on_homepage(context):
    context.page = MercadoLibreSearchPage(context.driver)
    context.page.open_homepage()

@when('the user searches for "{query}"')
def step_user_searches(context, query):
    context.page.search_product(query)

@then('the search results should contain the text "{expected_text}"')
def step_verify_results(context, expected_text):
    assert context.page.verify_results(expected_text), f"Results do not contain '{expected_text}'"