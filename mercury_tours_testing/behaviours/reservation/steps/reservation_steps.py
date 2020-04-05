from behave import *
from mercury_tours_testing.tests.reservation_tests import FlightFinderTest

flightFinderTest = FlightFinderTest()


@given(u'Estoy en la pagina de Mercury Tours')
def step_impl(context):
    flightFinderTest.setUpClass()
    flightFinderTest.test_go_url('http://newtours.demoaut.com/')


@when(u'Ingreso un usuario "{user}" y un password "{password}"')
def step_impl(context, user, password):
    context.user = user
    context.password = password
    flightFinderTest.test_login(context.user, context.password)


@when(u'Busco vuelos de {desde} hacia {hacia} para {cantidadPasajeros} pasajeros en la aerolinea {aerolinea}')
def step_impl(context, desde, hacia, cantidadPasajeros, aerolinea):
    context.desde = desde
    context.hacia = hacia
    context.cantidadPasajeros = cantidadPasajeros
    context.aerolinea = aerolinea
    flightFinderTest.test_search_flight(context.desde, context.hacia, context.cantidadPasajeros, context.aerolinea)


@when(u'Selecciono el vuelo de ida y de regreso')
def step_impl(context):
    flightFinderTest.test_select_flight()


@when(
    u'Ingreso los datos de los pasajeros {nombre} {apellido} {tipoTarjeta} {numeroTarjeta} {mesExp} {anioExp} {direccion} {ciudad} {estado} {codPostal}')
def step_impl(context, nombre, apellido, tipoTarjeta, numeroTarjeta, mesExp, anioExp, direccion, ciudad, estado,
              codPostal):
    context.nombre = nombre
    context.apellido = apellido
    context.tipoTarjeta = tipoTarjeta
    context.numeroTarjeta = numeroTarjeta
    context.mesExp = mesExp
    context.anioExp = anioExp
    context.direccion = direccion
    context.ciudad = ciudad
    context.estado = estado
    context.codPostal = codPostal
    flightFinderTest.test_book_flight(context.nombre, context.apellido, context.tipoTarjeta,
                                      context.numeroTarjeta, context.mesExp, context.anioExp, context.direccion,
                                      context.ciudad, context.estado, context.codPostal)


@then(u'El sistema muestra los vuelos disponibles')
def step_impl(context):
    flightFinderTest.test_flight_found()
    flightFinderTest.tearDownClass()


@then(u'El sistema confirma la reserva')
def step_impl(context):
    flightFinderTest.test1_confirmation()
    flightFinderTest.tearDownClass()

@then(u'Se despliega la pagina de reserva del vuelo')
def step_impl(context):
    flightFinderTest.test1_summary_flight()
    flightFinderTest.tearDownClass()
