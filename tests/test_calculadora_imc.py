import unittest
from src.calculadora_imc import calculadora_imc

class TestCalculadoraIMC(unittest.TestCase):
    def testCriancaIMC(self):
        resultado, imc = calculadora_imc(40, 1.6, 17)
        self.assertEqual(resultado, 'IMC inválido para crianças e adolescentes')
        self.assertEqual(imc, 0)        

    def testIdosoIMC(self):
        resultado, imc = calculadora_imc(40, 1.6, 61)
        self.assertEqual(resultado, 'IMC inválido para idosos')
        self.assertEqual(imc, 0)


    def testMuitoAbaixoIMC(self):
        resultado, imc = calculadora_imc(50, 1.75, 20)
        self.assertEqual(resultado, 'Muito abaixo do peso')
        self.assertAlmostEqual(imc, 16.33, delta=0.01)

    def testAbaixoIMC(self):
        resultado, imc = calculadora_imc(50, 1.65, 20)
        self.assertEqual(resultado, 'Abaixo do peso')
        self.assertAlmostEqual(imc, 18.37, delta=0.01)  

    def testNormalIMC(self):
        resultado, imc = calculadora_imc(60, 1.6, 20)
        self.assertEqual(resultado, 'Peso normal')
        self.assertAlmostEqual(imc, 23.44, delta=0.01)

    def testAcimaIMC(self):
        resultado, imc = calculadora_imc(85, 1.75, 20)
        self.assertEqual(resultado, 'Acima do peso')
        self.assertAlmostEqual(imc, 27.76, delta=0.01)         

    def testObesaIMC(self):
        resultado, imc = calculadora_imc(100, 1.7, 20)
        self.assertEqual(resultado, 'Obesidade')
        self.assertAlmostEqual(imc, 34.60, delta=0.01)

    def testSeveraIMC(self):
        resultado, imc = calculadora_imc(105, 1.65, 20)
        self.assertEqual(resultado, 'Obesidade severa')
        self.assertAlmostEqual(imc, 38.57, delta=0.01)

    def testMorbidaIMC(self):
        resultado, imc = calculadora_imc(120, 1.7, 20)
        self.assertEqual(resultado, 'Obesidade mórbida')
        self.assertAlmostEqual(imc, 41.52, delta=0.01)


    def testPrecisoIMC(self):
        resultado, imc = calculadora_imc(120, 1.7, 20, True)
        self.assertEqual(resultado, 'Obesidade mórbida')
        self.assertAlmostEqual(imc, 41.40, delta=0.01)
