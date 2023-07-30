import unittest
import translator

class TestTranslate(unittest.TestCase):
  
  def test_e2f(self):
    self.assertEqual(trasnslator.englishToFrench('Hello'),'Bonjour')
    self.assertEqual(translator.englishToFrench('welcome my love'),'mon amour')

def test_f2e(self):
  self.assertEqual(translator.frenchToEnglish('Bonjour'),'Hello')
  self.assertEqual(translator.frenchToEnglish('mon amour'),'welcome my love')

if __name__== '__main__':
  unittest.main()
