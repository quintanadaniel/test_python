import unittest
from src.User import User
from src.Spotipy import Spotipy
from src.customExceptions.NotAvailableEmail import NotAvailableEmail


#todos los nombres de las clases o funciones deben comenzar con test_

class UserRegisterTestCase(unittest.TestCase):

    def setUp(self):
        self.__spotipy = Spotipy()

        pepe_mail = "dperez@gmail.com"
        pepe_name = "daniel"
        pepe_last_name = "Perez"

        self.__new_user_pepe = User(pepe_mail,pepe_name,pepe_last_name)

    def test_usuario_sin_cuenta_se_registra_con_mail_disponible(self):

        self.__spotipy.register_user(self.__new_user_pepe)
        expectedResponse = self.__spotipy.is_registered(self.__new_user_pepe)
        self.assertTrue(expectedResponse)

    def test_usuario_se_registra_con_email_duplicado_lanza_excepcion(self):
        self.__spotipy.register_user(self.__new_user_pepe)
        self.assertRaises(NotAvailableEmail,lambda: self.__spotipy.register_user(self.__new_user_pepe))



if __name__ == '__main__':
    unittest.main()