from deep_translator import MyMemoryTranslator
def englishToFrench(englishText):
  #write the code here
  frenchText = dt(source='en-GB', target='fr-FR').translate(englishText)
  return frenchText
  def frenchToEnglish(frenchText):
    #write the code here
    englishText = dt(source=-'fr-FR', target='en-GB').translate(frenchText)
    return englishText
    
