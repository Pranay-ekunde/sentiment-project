import unittest
from app.app import app

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # 🔹 Test homepage loads
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # 🔹 Test positive sentiment
    def test_positive(self):
        response = self.app.post('/', data=dict(review="This is amazing"))
        self.assertEqual(response.status_code, 302)  # redirect

    # 🔹 Test negative sentiment
    def test_negative(self):
        response = self.app.post('/', data=dict(review="Worst experience"))
        self.assertEqual(response.status_code, 302)

    # 🔹 Test empty input
    def test_empty_input(self):
        response = self.app.post('/', data=dict(review=""))
        self.assertEqual(response.status_code, 302)

    def test_positive_output(self):
        response = self.app.post('/', data=dict(review="This is amazing"), follow_redirects=True)
        self.assertIn(b"Positive", response.data)

if __name__ == "__main__":
    unittest.main()