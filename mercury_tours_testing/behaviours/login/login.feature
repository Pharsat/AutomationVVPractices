Feature: login en Mercury Tours

  Scenario:
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "osolisd" y un password "Moscar13*"
    Then El sistema me autentica como usuario legitimo

    Scenario:
      Given Estoy en la pagina de Mercury Tours
      When Ingreso un usuario "osolisd" y un password "Moscar13"
      Then El sistema me autentica como usuario Ilegitimo
