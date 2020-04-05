from behave import *
from mercury_tours_testing.tests.login_tests import LoginTest

test = LoginTest()


@given(u'Estoy en la pagina de Mercury Tours')
def step_impl(context):
    test.setUpClass()
    test.test_go_url('http://newtours.demoaut.com/')


@when(u'Ingreso un usuario "{user}" y un password "{password}"')
def step_impl(context, user, password):
    context.user = user
    context.password = password
    test.test_login(context.user, context.password)


@then(u'El sistema me autentica como usuario legitimo')
def step_impl(context):
    test.test_image()
    test.tearDownClass()


@then(u'El sistema me autentica como usuario Ilegitimo')
def step_impl(context):
    test.test_wrong_user_pwd()
    test.tearDownClass()
