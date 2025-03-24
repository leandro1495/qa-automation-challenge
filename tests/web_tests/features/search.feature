Feature: Búsqueda en Wikipedia
  Como usuario quiero buscar información en Wikipedia 
  para obtener artículos relevantes

  Scenario: Búsqueda de un término válido
    Given el usuario está en la página de inicio de Wikipedia
    When busca "Selenium"
    Then el primer resultado debe contener "Selenium"
