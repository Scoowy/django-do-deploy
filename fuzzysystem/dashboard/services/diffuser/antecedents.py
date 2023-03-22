import numpy as __np
import skfuzzy as __fuzz
from skfuzzy import control as __ctrl


#########################################################################
#                       Rasgos de Personalidad                          #
#########################################################################

# racional
racional = __ctrl.Antecedent(__np.arange(0, 100, 0.1), 'racional')
racional['bajo'] = __fuzz.gaussmf(racional.universe, 30, 20)
racional['medio'] = __fuzz.gaussmf(racional.universe, 70, 20)
racional['alto'] = __fuzz.gaussmf(racional.universe, 100, 20)

# emocional
emocional = __ctrl.Antecedent(__np.arange(0, 101, 0.1), 'emocional')
emocional['bajo'] = __fuzz.gaussmf(emocional.universe, 30, 20)
emocional['medio'] = __fuzz.gaussmf(emocional.universe, 70, 20)
emocional['alto'] = __fuzz.gaussmf(emocional.universe, 100, 20)

#########################################################################
#                              Emociones                                #
#########################################################################

# tristeza
tristeza = __ctrl.Antecedent(__np.arange(0, 101, 0.1), 'tristeza')
tristeza['bajo'] = __fuzz.gaussmf(tristeza.universe, 30, 20)
tristeza['medio'] = __fuzz.gaussmf(tristeza.universe, 70, 30)
tristeza['alto'] = __fuzz.gaussmf(tristeza.universe, 100, 20)

# sorpresa
sorpresa = __ctrl.Antecedent(__np.arange(0, 101, 0.1), 'sorpresa')
sorpresa['bajo'] = __fuzz.gaussmf(sorpresa.universe, 30, 20)
sorpresa['medio'] = __fuzz.gaussmf(sorpresa.universe, 70, 15)
sorpresa['alto'] = __fuzz.gaussmf(sorpresa.universe, 100, 20)

# disfrute
disfrute = __ctrl.Antecedent(__np.arange(0, 101, 0.1), 'disfrute')
disfrute['bajo'] = __fuzz.gaussmf(disfrute.universe, 30, 20)
disfrute['medio'] = __fuzz.gaussmf(disfrute.universe, 70, 15)
disfrute['alto'] = __fuzz.gaussmf(disfrute.universe, 100, 20)

# enfado
enfado = __ctrl.Antecedent(__np.arange(0, 101, 0.1), 'enfado')
enfado['bajo'] = __fuzz.gaussmf(enfado.universe, 30, 20)
enfado['medio'] = __fuzz.gaussmf(enfado.universe, 70, 15)
enfado['alto'] = __fuzz.gaussmf(enfado.universe, 90, 20)

# asco
asco = __ctrl.Antecedent(__np.arange(0, 101, 0.1), 'asco')
asco['bajo'] = __fuzz.gaussmf(asco.universe, 30, 20)
asco['medio'] = __fuzz.gaussmf(asco.universe, 75, 20)
asco['alto'] = __fuzz.gaussmf(asco.universe, 100, 20)

# temor
temor = __ctrl.Antecedent(__np.arange(0, 101, 0.1), 'temor')
temor['bajo'] = __fuzz.gaussmf(temor.universe, 30, 20)
temor['medio'] = __fuzz.gaussmf(temor.universe, 70, 15)
temor['alto'] = __fuzz.gaussmf(temor.universe, 90, 20)

# sin emoción
noEmocion = __ctrl.Antecedent(__np.arange(0, 101, 0.1), 'noEmocion')
noEmocion['bajo'] = __fuzz.gaussmf(noEmocion.universe, 30, 20)
noEmocion['medio'] = __fuzz.gaussmf(noEmocion.universe, 70, 10)
noEmocion['alto'] = __fuzz.gaussmf(noEmocion.universe, 90, 20)
