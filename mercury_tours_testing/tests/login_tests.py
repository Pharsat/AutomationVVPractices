import time
import unittest
from selenium import webdriver


class LoginTest(unittest.TestCase):
    # Este método se ejecuta la primera vez para instanciar el navegador
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:\Oscar\Cursos\U\Verificacion y validacion\ApiTesting\venv\ui_testing\drivers\chromedriver.exe")
        cls.driver.maximize_window()

    # Este método recibe como parámetro la URL del sitio
    def test_go_url(self, url):
        self.driver.get(url)

    # Este método recibe como parámetro el login y password y hace clic en el botin Sign - In
    def test_login(self, user, password):
        self.driver.find_element_by_name("userName").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("login").click()

    # Este método hace clic en el botón SIGN-OFF
    def test_logout(self):
        self.driver.find_element_by_link_text("SIGN-OFF")
        time.sleep(2)

    # Este método hace clic en el botón SIGN-OFF
    def test_wrong_user_pwd(self):
        self.assertTrue(self.driver.find_element_by_link_text("registration form").is_displayed())
        time.sleep(2)

    def test_image(self):
        image = self.driver.find_element_by_xpath("//img[contains(@src,'mast_flightfinder.gif')]").is_displayed()
        self.assertTrue(image)

    # Este método se ejecuta al final y cierra el navegador
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("prueba completada con éxito")


if __name__ == '__main__':
    unittest.main()
