import numpy as __np
import skfuzzy as __fuzz
from skfuzzy import control as __ctrl


#########################################################################
#                             Concecuentes                              #
#               Basado en los 5 grandes de la Psicología                #
#########################################################################

# Estabilidad Emocional
estEmocional = __ctrl.Consequent(__np.arange(0, 101, 0.1), 'estEmocional')
estEmocional['bajo'] = __fuzz.gaussmf(estEmocional.universe, 30, 30)
estEmocional['medio'] = __fuzz.gaussmf(estEmocional.universe, 70, 20)
estEmocional['alto'] = __fuzz.gaussmf(estEmocional.universe, 100, 20)

# Extrovertido
extrovertido = __ctrl.Consequent(__np.arange(0, 101, 0.1), 'extrovertido')
extrovertido['bajo'] = __fuzz.gaussmf(extrovertido.universe, 30, 30)
extrovertido['medio'] = __fuzz.gaussmf(extrovertido.universe, 70, 20)
extrovertido['alto'] = __fuzz.gaussmf(extrovertido.universe, 100, 20)

# Apertura Experiencias
apExperiencias = __ctrl.Consequent(__np.arange(0, 101, 0.1), 'apExperiencias')
apExperiencias['bajo'] = __fuzz.gaussmf(apExperiencias.universe, 0, 30)
apExperiencias['medio'] = __fuzz.gaussmf(apExperiencias.universe, 75, 10)
apExperiencias['alto'] = __fuzz.gaussmf(apExperiencias.universe, 100, 10)

# Amabilidad
amabilidad = __ctrl.Consequent(__np.arange(0, 101, 0.1), 'amabilidad')
amabilidad['bajo'] = __fuzz.gaussmf(amabilidad.universe, 40, 30)
amabilidad['medio'] = __fuzz.gaussmf(amabilidad.universe, 70, 10)
amabilidad['alto'] = __fuzz.gaussmf(amabilidad.universe, 90, 10)

# responsabilidad
responsabilidad = __ctrl.Consequent(
    __np.arange(0, 101, 0.1), 'responsabilidad')
responsabilidad['bajo'] = __fuzz.gaussmf(responsabilidad.universe, 0, 30)
responsabilidad['medio'] = __fuzz.gaussmf(responsabilidad.universe, 50, 10)
responsabilidad['alto'] = __fuzz.gaussmf(responsabilidad.universe, 100, 10)
