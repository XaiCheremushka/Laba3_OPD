import unittest
from flask import Flask
from flask.testing import FlaskClient
from website import app


class AppTestCase(unittest.TestCase):


    def setUp(self):
        app.config['TESTING'] = True # устанавливает флаг TESTING в значение True, чтобы приложение работало в режиме тестирования.
        self.app = app.test_client() # чтобы отправлять запросы к приложению.

    # проверка страницы verification
    def test_verification_route(self):
        response = self.app.get('/verification')
        self.assertEqual(response.status_code, 200)  # проверяет, что код состояния равен 200 (успешный запрос).
        self.assertIn(b'<!DOCTYPE html>', response.data)  # проверяет, что в содержимом ответа присутствует строка
                                                          # <!DOCTYPE html>

    # проверка главной страницы
    def test_log_in_route_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Авторизация".encode(), response.data)

    # проверка введения верных данных и перенаправления на другую страницу
    def test_log_in_route_post_correct_credentials(self):
        response = self.app.post('/', data={
            'username': 'Cheremushka',
            'password': '1234'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], '/verification')

    # проверка введения не верных данных и вывод сообщения на страницу
    def test_log_in_route_post_incorrect_credentials(self):
        response = self.app.post('/', data={
            'username': 'shfdhfg',
            'password': 'sghdggf'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Неправильный логин или пароль. Попробуйте снова.'.encode(), response.data)


if __name__ == '__main__':
    unittest.main()
