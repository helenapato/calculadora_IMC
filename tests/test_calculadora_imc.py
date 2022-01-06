import unittest
from src.calculadora_imc import calculadora_imc

class TestCalculadoraIMC(unittest.TestCase):
    def testCriancaIMC(self):
        resultado, imc = calculadora_imc(40, 1.6, 12)
        self.assertEqual(resultado, 'IMC inválido para crianças e adolescentes')
        self.assertEqual(imc, 0)