Feature: steps

Scenario: Testing routes
    Given Get to avtodispetcher "https://www.avtodispetcher.ru"
    When We are on avtodispetcher
    Then Enter initial route (г. Тула - г. Санкт-Петербург)
    Then Add a new city to the route (г. Тула - г. Великий Новгород - г. Санкт-Петербург)
