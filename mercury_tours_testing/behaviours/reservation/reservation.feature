Feature: Buscar vuelos en Mercury Tours

  Scenario Outline: Consulta vuelos
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "osolisd" y un password "Moscar13*"
    And Busco vuelos de "<origen>" hacia "<destino>" para "<numpasajero>" pasajeros en la aerolinea "<aerolinea>"
    Then El sistema muestra los vuelos disponibles
    Examples:
      | origen | destino   | numpasajero | aerolinea           |
      | Paris  | Seattle   | 2           | Blue Skies Airlines |
      | London | Frankfurt | 3           | Unified Airlines    |

  Scenario Outline: Confirmación de reserva
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "osolisd" y un password "Moscar13*"
    And Busco vuelos de "<origen>" hacia "<destino>" para "<numpasajero>" pasajeros en la aerolinea "<aerolinea>"
    And Selecciono el vuelo de ida y de regreso
    And Ingreso los datos de los pasajeros <nombre> <apellido> "<tipoTarjeta>" <numeroTarjeta> <mesExp> <anioExp> <direccion> <ciudad> <estado> <codPostal>
    Then El sistema confirma la reserva
    Examples:
      | origen | destino   | numpasajero | aerolinea           | nombre | apellido  | tipoTarjeta | numeroTarjeta | mesExp | anioExp | direccion   | ciudad   | estado    | codPostal |
      | London | Frankfurt | 1           | Blue Skies Airlines | Carlos | Jaramillo | Visa        | 123456789     | 02     | 2010    | cll10#40-20 | Medellin | Antioquia | 057       |
      | Paris  | London    | 1           | Pangea Airlines     | Ana    | Torres    | MasterCard  | 987456987     | 05     | 2009    | cll50#10-32 | Sabaneta | Antioquia | 057       |

  Scenario Outline: Selecion de vuelo
    Given Estoy en la pagina de Mercury Tours
    When Ingreso un usuario "osolisd" y un password "Moscar13*"
    And Busco vuelos de "<origen>" hacia "<destino>" para "<numpasajero>" pasajeros en la aerolinea "<aerolinea>"
    And Selecciono el vuelo de ida y de regreso
    Then Se despliega la pagina de reserva del vuelo

    Examples:
      | origen | destino   | numpasajero | aerolinea           |
      | London | Frankfurt | 1           | Blue Skies Airlines |
      | Paris  | London    | 1           | Pangea Airlines     |
