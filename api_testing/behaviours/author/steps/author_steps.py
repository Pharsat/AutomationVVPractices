import json
from behave import *
from api_testing.request_test.author.definition_step import ApiRequestAuthors

test = ApiRequestAuthors()


@given(u'usuario consulta el enpoint de autores por libro para el libro numero 1')
def step_impl(context):
    context.endpoint = "/authors/books/{}"


@when(u'realiza la peticion get al endpoint /authors/books/"{book_id}"')
def step_impl(context, book_id):
    test.test_get_all_authors_by_book(context.endpoint, book_id)


@then(u've el codigo de respuesta "{response_code}"')
def step_impl(context, response_code):
    test.test_validate_response_code(int(response_code))


@given(u'usuario consulta el enpoint de autores por libro para el libro 100')
def step_impl(context):
    context.endpoint = "/authors/books/{}"


@when(u'realiza la peticion get al endpoint /authors/books/"{book_id}" del libro 100')
def step_impl(context, book_id):
    test.test_get_all_authors_by_book(context.endpoint, book_id)


@given(u'usuario consulta el enpoint de todos los autores')
def step_impl(context):
    context.endpoint = "/api/Authors"


@when(u'realiza la peticion get al endpoint /api/Authors')
def step_impl(context):
    test.test_get_all_authors(context.endpoint)


@then(u'el ve "{required_item_count}" cuatroscientos autores listados')
def step_impl(context, required_item_count):
    test.test_items_count(int(required_item_count))


@given(u'usuario consulta el enpoing de crear un autor')
def step_impl(context):
    context.endpoint = "/api/Authors"


@when(
    u'realiza la peticion post al endpoint /api/Authors mandando un autor de nombre "{author_name}", apellido "{author_lastname}" autor del libro "{book_id}"')
def step_impl(context, author_name, author_lastname, book_id):
    payload = json.dumps({
        "IDBook": int(book_id),
        "FirstName": "{}".format(author_name),
        "LastName": "{}".format(author_lastname)
    })
    test.test_create_author(context.endpoint, payload)


@then(
    u'el usuario ve que el autor que acaba de crear tiene nombre "{author_name}", apellido "{author_lastname}" autor del libro "{book_id}"')
def step_impl(context, author_name, author_lastname, book_id):
    payload = json.dumps({
        "ID": 0,
        "IDBook": int(book_id),
        "FirstName": "{}".format(author_name),
        "LastName": "{}".format(author_lastname)
    })
    test.text_validate_two_json_objects_are_equal(payload)


@given(u'usuario consulta el endpoint de eliminar un autor')
def step_impl(context):
    context.endpoint = "/api/Authors/{}"


@when(u'realiza la peticion delete al endpoint /api/Authors/"{authod_id}"')
def step_impl(context, authod_id):
    test.test_delete_author(context.endpoint, int(authod_id))


@then(u'el usuario obtiene una respuesta vacia.')
def step_impl(context):
    test.test_validate_empty_response()


@given(u'usuario consulta el enpoint de un unico autor por id, el id es el 15')
def step_impl(context):
    context.endpoint = "/api/Authors/{}"


@when(u'realiza la peticion get a la url /api/Authors/"{author_id}"')
def step_impl(context, author_id):
    test.test_get_author(context.endpoint, int(author_id))


@then(
    u'el ve un objeto de autor devuelto con id "{author_id}", IDBook "{id_book}", FirstName "{first_name}" y LastName "{last_name}"')
def step_impl(context, author_id, id_book, first_name, last_name):
    payload = json.dumps({
        "ID": int(author_id),
        "IDBook": int(id_book),
        "FirstName": "{}".format(first_name),
        "LastName": "{}".format(last_name)
    })
    test.text_validate_two_json_objects_are_equal(payload)

@given(u'usuario consulta el enpoint de actualizar un autor')
def step_impl(context):
    context.endpoint = "/api/Authors/{}"

@when(
    u'realiza la peticion put a la /api/Authors/"{author_id}" mandando a actualizar el autor 20 con nombre "{first_name}", apellido "{last_name}" autor del libro "{id_book}"')
def step_impl(context, author_id, id_book, first_name, last_name):
    payload = json.dumps({
        "ID": 0,
        "IDBook": int(id_book),
        "FirstName": "{}".format(first_name),
        "LastName": "{}".format(last_name)
    })
    test.test_update_author(context.endpoint, int(author_id), payload)
    test.text_validate_two_json_objects_are_equal(payload)
