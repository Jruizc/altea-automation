Feature: Funcionalidad Busqueda de ofertas

  Scenario: Busqueda de oferta por nombre
    Given Visito la web de Altea
    When Buscamos ofertas de empleo de Cloud Engineer AWS
    Then Aparecen ofertas que contengan ese nombre

  Scenario: Busqueda de oferta sin resultados por nombre
    Given Visito la web de Altea
    When Buscamos ofertas de empleo de Fontanero
    Then No aparece ningun resultado