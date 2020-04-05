import time
import unittest
from mercury_tours_testing.tests.login import LoginTest

login = LoginTest()


class FlightFinderTest(unittest.TestCase):

    # Este método realiza la búsqueda de los vuelos para la rutaespecificada
    def test_search_flight(self, desde, hacia, cantidadPasajeros, aerolinea):
        self.driver = login.driver
        self.driver.find_element_by_xpath(
            "//select[@name='passCount']/option[@value=" + cantidadPasajeros + "]").click()
        self.driver.find_element_by_xpath("//select[@name='fromPort']/option[@value=" + desde + "]").click()
        self.driver.find_element_by_xpath("//select[@name='fromMonth']/option[@value='12']").click()
        self.driver.find_element_by_xpath("//select[@name='fromDay']/option[@value='1']").click()
        self.driver.find_element_by_xpath("//select[@name='toPort']/option[@value=" + hacia + "]").click()
        self.driver.find_element_by_xpath("//select[@name='toMonth']/option[@value='12']").click()
        self.driver.find_element_by_xpath("//select[@name='toDay']/option[@value='23']").click()
        self.driver.find_element_by_xpath("//input[@name='servClass']").click()
        self.driver.find_element_by_xpath("//select[@name='airline']/option[text()=" + aerolinea + "]").click()
        self.driver.find_element_by_xpath("//input[@name='findFlights']").click()
        time.sleep(3)

    def test_flight_found(self):
        reserveFlights = self.driver.find_element_by_xpath("//input[@name='reserveFlights']").is_displayed()
        self.assertTrue(reserveFlights)

    def test_select_flight(self):
        self.driver.find_element_by_css_selector(
            "input[type='radio'][value='Blue Skies Airlines$360$270$5:03']").click()
        self.driver.find_element_by_css_selector(
            "input[type='radio'][value='Blue Skies Airlines$630$270$12:23']").click()
        self.driver.find_element_by_xpath("//input[@name='reserveFlights']").click()
        # time.sleep(5)

    def test_book_flight(self, nombre, apellido, tipoTarjeta, numeroTarjeta, mesExp, anioExp, direccion, ciudad, estado,
                         codPostal):
        self.driver.find_element_by_name("passFirst0").send_keys(nombre)
        self.driver.find_element_by_name("passLast0").send_keys(apellido)
        self.driver.find_element_by_xpath("//select[@name='creditCard']/option[text()=" + tipoTarjeta + "]").click()
        self.driver.find_element_by_name("creditnumber").send_keys(numeroTarjeta)
        self.driver.find_element_by_xpath("//select[@name='cc_exp_dt_mn']/option[text()=" + mesExp + "]").click()
        self.driver.find_element_by_xpath("//select[@name='cc_exp_dt_yr']/option[text()=" + anioExp + "]").click()
        self.driver.find_element_by_name("billAddress1").clear()
        self.driver.find_element_by_name("billAddress1").send_keys(direccion)
        self.driver.find_element_by_name("billCity").clear()
        self.driver.find_element_by_name("billCity").send_keys(ciudad)
        self.driver.find_element_by_name("billState").clear()
        self.driver.find_element_by_name("billState").send_keys(estado)
        self.driver.find_element_by_name("billZip").clear()
        self.driver.find_element_by_name("billZip").send_keys(codPostal)
        self.driver.find_element_by_name("buyFlights").click()
        # time.sleep(5)

    def test1_confirmation(self):
      image =self.driver.find_elements_by_xpath("//img[contains(@src,'/mast_confirmation.gif')]")
      self.assertTrue(image)
        # time.sleep(5)
    def test1_summary_flight(self):
        image = self.driver.find_elements_by_xpath("//img[contains(@src,'/masts/mast_book.gif')]")
        self.assertTrue(image)

    # Este método se ejecuta al final y cierra el navegador
    @classmethod
    def tearDownClass(self):
        login.tearDownClass()


if __name__ == '__main__':
    unittest.main()
