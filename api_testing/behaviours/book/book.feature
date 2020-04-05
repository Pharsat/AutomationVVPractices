Feature: Administracion de libros

  Scenario: consultar todos los libros
    Given usuario consulta el endpoint
    When  realiza la peticion
    Then  ve el codigo de respuesta 200
    And   el ve 200 libros listados

  Scenario Outline: Agregar nuevo libro
    Given usuario consulta el endpoint
    When  envia la información del libro nuevo: "<id>","<titulo>","<descripcion>","<num_pag>","<extracto>","<fecha_publicacion>"
    Then  Ve el codigo de respuesta 200
    And   el ve la informacion del libro creado en la respuesta
    Examples:
      | id  | titulo             | descripcion                                         | num_pag | extracto           | fecha_publicacion   |
      | 202 | Catalino Bocachica | Suenos hechos realidad gracias al empeno y el valor | 100     | Lorem lorem lorem. | 1998-03-05T00:00:00 |

  Scenario: Elimina libro por id
    Given usuario consulta el endpoint
    When  elimina el libro con id 1
    Then  ve el codigo de respuesta 200

  Scenario Outline: Consulta libro por id
    Given usuario consulta el endpoint
    When  consulta el libro con id 10
    Then  ve el codigo de respuesta 200
    And   el ve la informacion del libro: "<id>","<titulo>","<descripcion>","<num_pag>","<extracto>","<fecha_publicacion>"
    Examples:
      | id | titulo  | descripcion                                                  | num_pag | extracto                                                                                                                                                                                                                                                                                                     | fecha_publicacion                 |
      | 10 | Book 10 | Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\r\n | 1000    | Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\r\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\r\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\r\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\r\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\r\n | 2020-03-20T11:02:53.1151091+00:00 |

  Scenario Outline: Actualizar libro
    Given usuario consulta el endpoint
    When  ingresa el id del libro 10
    And   envia la informacion del libro para actualizar: "<id>","<titulo>","<descripcion>","<num_pag>","<extracto>","<fecha_publicacion>"
    Then  ve el codigo de respuesta 200
    And   el ve la informacion del libro actualizado
    Examples:
      | id | titulo             | descripcion                                         | num_pag | extracto           | fecha_publicacion   |
      | 10 | Catalino Bocachica | Suenos hechos realidad gracias al empeno y el valor | 100     | Lorem lorem lorem. | 0001-01-01T00:00:00 |
