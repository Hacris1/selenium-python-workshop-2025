Feature: MercadoLibre Search
  Scenario: Search for "iPhone 13" and verify results contain "iPhone"
    Given the user is on the MercadoLibre homepage
    When the user searches for "iPhone 13"
    Then the search results should contain the text "iPhone"