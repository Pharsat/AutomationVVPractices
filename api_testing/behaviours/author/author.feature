Feature: Administracion de autores

  Scenario: consultar los autores del libro 1
    Given usuario consulta el enpoint de autores por libro para el libro numero 1
    When  realiza la peticion get al endpoint /authors/books/"1"
    Then  ve el codigo de respuesta "200"

  Scenario: consultar los autores del libro 100
    Given usuario consulta el enpoint de autores por libro para el libro 100
    When  realiza la peticion get al endpoint /authors/books/"100" del libro 100
    Then  ve el codigo de respuesta "200"

  Scenario: consultar todos los autores
    Given usuario consulta el enpoint de todos los autores
    When  realiza la peticion get al endpoint /api/Authors
    Then  ve el codigo de respuesta "200"
    And   el ve "400" cuatroscientos autores listados

  Scenario: crear un autor
    Given usuario consulta el enpoing de crear un autor
    When  realiza la peticion post al endpoint /api/Authors mandando un autor de nombre "Cristian", apellido "Gallego" autor del libro "4"
    Then  ve el codigo de respuesta "200"
    And   el usuario ve que el autor que acaba de crear tiene nombre "Cristian", apellido "Gallego" autor del libro "4"

  Scenario: eliminar el autor numero 10
    Given usuario consulta el endpoint de eliminar un autor
    When  realiza la peticion delete al endpoint /api/Authors/"10"
    Then  ve el codigo de respuesta "200"
    And   el usuario obtiene una respuesta vacia.

  Scenario: consulta el autor numero 15
    Given usuario consulta el enpoint de un unico autor por id, el id es el 15
    When  realiza la peticion get a la url /api/Authors/"15"
    Then  ve el codigo de respuesta "200"
    And   el ve un objeto de autor devuelto con id "15", IDBook "8", FirstName "First Name 15" y LastName "Last Name 15"

  Scenario: actualizar el autor numero 20
    Given usuario consulta el enpoint de actualizar un autor
    When  realiza la peticion put a la /api/Authors/"20" mandando a actualizar el autor 20 con nombre "Cristian 2", apellido "Gallego 2" autor del libro "6"
    Then  ve el codigo de respuesta "200"
    And   el usuario ve que el autor que acaba de crear tiene nombre "Cristian 2", apellido "Gallego 2" autor del libro "6"