from skfuzzy import control as __ctrl

from . import antecedents as ant
from . import consequents as con

#################################################################################
#                                 REGLAS DIFUSAS                                #
#                                  PARA RACIONAL                                #
#################################################################################

# Reglas para Racional - Tristeza
rule1 = __ctrl.Rule(ant.racional['alto'] &
                    ant.tristeza['alto'], con.extrovertido['bajo'])
rule2 = __ctrl.Rule(ant.racional['alto'] &
                    ant.tristeza['medio'], con.extrovertido['medio'])
rule3 = __ctrl.Rule(ant.racional['alto'] &
                    ant.tristeza['bajo'], con.extrovertido['alto'])
rule4 = __ctrl.Rule(ant.racional['medio'] &
                    ant.tristeza['alto'], con.estEmocional['bajo'])
rule5 = __ctrl.Rule(ant.racional['medio'] &
                    ant.tristeza['medio'], con.extrovertido['medio'])
rule6 = __ctrl.Rule(ant.racional['medio'] &
                    ant.tristeza['bajo'], con.extrovertido['alto'])
rule7 = __ctrl.Rule(ant.racional['bajo'] &
                    ant.tristeza['alto'], con.extrovertido['bajo'])
rule8 = __ctrl.Rule(ant.racional['bajo'] &
                    ant.tristeza['medio'], con.estEmocional['medio'])
rule9 = __ctrl.Rule(ant.racional['bajo'] &
                    ant.tristeza['bajo'], con.estEmocional['alto'])

# Reglas para Racional - Sorpresa
rule10 = __ctrl.Rule(ant.racional['alto'] &
                     ant.sorpresa['alto'], con.responsabilidad['alto'])
rule11 = __ctrl.Rule(ant.racional['alto'] &
                     ant.sorpresa['medio'], con.responsabilidad['medio'])
rule12 = __ctrl.Rule(ant.racional['alto'] &
                     ant.sorpresa['bajo'], con.apExperiencias['medio'])
rule13 = __ctrl.Rule(ant.racional['medio'] &
                     ant.sorpresa['alto'], con.apExperiencias['medio'])
rule14 = __ctrl.Rule(ant.racional['medio'] &
                     ant.sorpresa['medio'], con.responsabilidad['medio'])
rule15 = __ctrl.Rule(ant.racional['medio'] &
                     ant.sorpresa['bajo'], con.responsabilidad['alto'])
rule16 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.sorpresa['alto'], con.apExperiencias['alto'])
rule17 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.sorpresa['medio'], con.apExperiencias['medio'])
rule18 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.sorpresa['bajo'], con.responsabilidad['medio'])

# Reglas para Racional - Enfado
rule19 = __ctrl.Rule(ant.racional['alto'] &
                     ant.enfado['alto'], con.estEmocional['bajo'])
rule20 = __ctrl.Rule(ant.racional['alto'] &
                     ant.enfado['medio'], con.estEmocional['medio'])
rule21 = __ctrl.Rule(ant.racional['alto'] &
                     ant.enfado['bajo'], con.estEmocional['alto'])
rule22 = __ctrl.Rule(ant.racional['medio'] &
                     ant.enfado['alto'], con.apExperiencias['bajo'])
rule23 = __ctrl.Rule(ant.racional['medio'] &
                     ant.enfado['medio'], con.estEmocional['medio'])
rule24 = __ctrl.Rule(ant.racional['medio'] &
                     ant.enfado['bajo'], con.apExperiencias['medio'])
rule25 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.enfado['alto'], con.apExperiencias['medio'])
rule26 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.enfado['medio'], con.estEmocional['medio'])
rule27 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.enfado['bajo'], con.apExperiencias['alto'])

# Reglas para Racional - Temor
rule28 = __ctrl.Rule(ant.racional['alto'] &
                     ant.temor['alto'], con.estEmocional['bajo'])
rule29 = __ctrl.Rule(ant.racional['alto'] &
                     ant.temor['medio'], con.responsabilidad['medio'])
rule30 = __ctrl.Rule(ant.racional['alto'] &
                     ant.temor['bajo'], con.responsabilidad['alto'])
rule31 = __ctrl.Rule(ant.racional['medio'] &
                     ant.temor['alto'], con.estEmocional['medio'])
rule32 = __ctrl.Rule(ant.racional['medio'] &
                     ant.temor['medio'], con.responsabilidad['medio'])
rule33 = __ctrl.Rule(ant.racional['medio'] &
                     ant.temor['bajo'], con.estEmocional['medio'])
rule34 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.temor['alto'], con.estEmocional['medio'])
rule35 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.temor['medio'], con.responsabilidad['medio'])
rule36 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.temor['bajo'], con.responsabilidad['alto'])

# Reglas para Racional - Asco
rule37 = __ctrl.Rule(ant.racional['alto'] &
                     ant.asco['alto'], con.apExperiencias['bajo'])
rule38 = __ctrl.Rule(ant.racional['alto'] &
                     ant.asco['medio'], con.apExperiencias['medio'])
rule39 = __ctrl.Rule(ant.racional['alto'] &
                     ant.asco['bajo'], con.apExperiencias['alto'])
rule40 = __ctrl.Rule(ant.racional['medio'] &
                     ant.asco['alto'], con.apExperiencias['medio'])
rule41 = __ctrl.Rule(ant.racional['medio'] &
                     ant.asco['medio'], con.apExperiencias['bajo'])
rule42 = __ctrl.Rule(ant.racional['medio'] &
                     ant.asco['bajo'], con.extrovertido['medio'])
rule43 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.asco['alto'], con.apExperiencias['bajo'])
rule44 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.asco['medio'], con.extrovertido['medio'])
rule45 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.asco['bajo'], con.extrovertido['bajo'])

# Reglas para Racional - Disfrute
rule46 = __ctrl.Rule(ant.racional['alto'] &
                     ant.disfrute['alto'], con.amabilidad['alto'])
rule47 = __ctrl.Rule(ant.racional['alto'] &
                     ant.disfrute['medio'], con.extrovertido['medio'])
rule48 = __ctrl.Rule(ant.racional['alto'] &
                     ant.disfrute['bajo'], con.extrovertido['bajo'])
rule49 = __ctrl.Rule(ant.racional['medio'] &
                     ant.disfrute['alto'], con.amabilidad['alto'])
rule50 = __ctrl.Rule(ant.racional['medio'] &
                     ant.disfrute['medio'], con.amabilidad['medio'])
rule51 = __ctrl.Rule(ant.racional['medio'] &
                     ant.disfrute['bajo'], con.extrovertido['bajo'])
rule52 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.disfrute['alto'], con.amabilidad['alto'])
rule53 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.disfrute['medio'], con.extrovertido['medio'])
rule54 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.disfrute['bajo'], con.extrovertido['bajo'])

# Reglas para Racional - Sin Emoción
rule55 = __ctrl.Rule(ant.racional['alto'] &
                     ant.noEmocion['alto'], con.responsabilidad['alto'])
rule56 = __ctrl.Rule(ant.racional['alto'] &
                     ant.noEmocion['medio'], con.responsabilidad['medio'])
rule57 = __ctrl.Rule(ant.racional['alto'] &
                     ant.noEmocion['bajo'], con.estEmocional['medio'])
rule58 = __ctrl.Rule(ant.racional['medio'] &
                     ant.noEmocion['alto'], con.estEmocional['medio'])
rule59 = __ctrl.Rule(ant.racional['medio'] &
                     ant.noEmocion['medio'], con.responsabilidad['medio'])
rule60 = __ctrl.Rule(ant.racional['medio'] &
                     ant.noEmocion['bajo'], con.responsabilidad['alto'])
rule61 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.noEmocion['alto'], con.estEmocional['alto'])
rule62 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.noEmocion['medio'], con.estEmocional['medio'])
rule63 = __ctrl.Rule(ant.racional['bajo'] &
                     ant.noEmocion['bajo'], con.responsabilidad['bajo'])

#################################################################################
#                                 REGLAS DIFUSAS                                #
#                                 PARA EMOCIONAL                                #
#################################################################################

# Reglas para Emocional - Sin Emoción
rule64 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.noEmocion['alto'], con.apExperiencias['alto'])
rule65 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.noEmocion['medio'], con.apExperiencias['medio'])
rule66 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.noEmocion['bajo'], con.estEmocional['alto'])
rule67 = __ctrl.Rule(ant.emocional['medio'] &
                     ant.noEmocion['alto'], con.apExperiencias['alto'])
rule68 = __ctrl.Rule(ant.emocional['medio'] &
                     ant.noEmocion['medio'], con.apExperiencias['medio'])
rule69 = __ctrl.Rule(ant.emocional['medio'] &
                     ant.noEmocion['bajo'], con.estEmocional['alto'])
rule70 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.noEmocion['alto'], con.apExperiencias['alto'])
rule71 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.noEmocion['medio'], con.apExperiencias['medio'])
rule72 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.noEmocion['bajo'], con.estEmocional['alto'])

# Reglas para Emocional - Disfrute
rule73 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.disfrute['alto'], con.apExperiencias['alto'])
rule74 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.disfrute['medio'], con.apExperiencias['medio'])
rule75 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.disfrute['bajo'], con.apExperiencias['bajo'])
rule76 = __ctrl.Rule(ant.emocional['medio'] &
                     ant.disfrute['alto'], con.extrovertido['bajo'])
rule77 = __ctrl.Rule(ant.emocional['medio'] &
                     ant.disfrute['medio'], con.apExperiencias['medio'])
rule78 = __ctrl.Rule(ant.emocional['medio'] &
                     ant.disfrute['bajo'], con.apExperiencias['bajo'])
rule79 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.disfrute['alto'], con.extrovertido['medio'])
rule80 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.disfrute['medio'], con.apExperiencias['medio'])
rule81 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.disfrute['bajo'], con.extrovertido['alto'])

# Reglas para Emocional - Asco
rule82 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.asco['alto'], con.apExperiencias['medio'])
rule83 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.asco['medio'], con.amabilidad['medio'])
rule84 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.asco['bajo'], con.amabilidad['alto'])
rule85 = __ctrl.Rule(ant.emocional['medio'] &
                     ant.asco['alto'], con.apExperiencias['alto'])
rule86 = __ctrl.Rule(ant.emocional['medio'] &
                     ant.asco['medio'], con.apExperiencias['medio'])
rule87 = __ctrl.Rule(ant.emocional['medio']
                     & ant.asco['bajo'], con.amabilidad['medio'])
rule88 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.asco['alto'], con.apExperiencias['medio'])
rule89 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.asco['medio'], con.amabilidad['medio'])
rule90 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.asco['bajo'], con.amabilidad['alto'])

# Reglas para Emocional - Temor
rule91 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.temor['alto'], con.estEmocional['medio'])
rule92 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.temor['medio'], con.amabilidad['bajo'])
rule93 = __ctrl.Rule(ant.emocional['alto'] &
                     ant.temor['bajo'], con.estEmocional['alto'])
rule94 = __ctrl.Rule(ant.emocional['medio']
                     & ant.temor['alto'], con.amabilidad['medio'])
rule95 = __ctrl.Rule(ant.emocional['medio'] &
                     ant.temor['medio'], con.estEmocional['medio'])
rule96 = __ctrl.Rule(ant.emocional['medio']
                     & ant.temor['bajo'], con.amabilidad['alto'])
rule97 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.temor['alto'], con.amabilidad['bajo'])
rule98 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.temor['medio'], con.estEmocional['medio'])
rule99 = __ctrl.Rule(ant.emocional['bajo'] &
                     ant.temor['bajo'], con.amabilidad['medio'])

# Reglas para Emocional - Enfado
rule100 = __ctrl.Rule(ant.emocional['alto'] &
                      ant.enfado['alto'], con.responsabilidad['medio'])
rule101 = __ctrl.Rule(ant.emocional['alto'] &
                      ant.enfado['medio'], con.amabilidad['bajo'])
rule102 = __ctrl.Rule(ant.emocional['alto']
                      & ant.enfado['bajo'], con.amabilidad['alto'])
rule103 = __ctrl.Rule(ant.emocional['medio'] &
                      ant.enfado['alto'], con.responsabilidad['medio'])
rule104 = __ctrl.Rule(ant.emocional['medio'] &
                      ant.enfado['medio'], con.amabilidad['medio'])
rule105 = __ctrl.Rule(ant.emocional['medio'] &
                      ant.enfado['bajo'], con.responsabilidad['alto'])
rule106 = __ctrl.Rule(ant.emocional['bajo'] &
                      ant.enfado['alto'], con.responsabilidad['medio'])
rule107 = __ctrl.Rule(ant.emocional['bajo'] &
                      ant.enfado['medio'], con.amabilidad['alto'])
rule108 = __ctrl.Rule(ant.emocional['bajo'] &
                      ant.enfado['bajo'], con.amabilidad['medio'])

# Reglas para ant.emocional - Sorpresa
rule109 = __ctrl.Rule(ant.emocional['alto'] &
                      ant.sorpresa['alto'], con.apExperiencias['alto'])
rule110 = __ctrl.Rule(ant.emocional['alto'] &
                      ant.sorpresa['medio'], con.apExperiencias['medio'])
rule111 = __ctrl.Rule(ant.emocional['alto'] &
                      ant.sorpresa['bajo'], con.responsabilidad['alto'])
rule112 = __ctrl.Rule(ant.emocional['medio'] &
                      ant.sorpresa['alto'], con.apExperiencias['alto'])
rule113 = __ctrl.Rule(ant.emocional['medio'] &
                      ant.sorpresa['medio'], con.apExperiencias['medio'])
rule114 = __ctrl.Rule(ant.emocional['medio'] &
                      ant.sorpresa['bajo'], con.responsabilidad['alto'])
rule115 = __ctrl.Rule(ant.emocional['bajo'] &
                      ant.sorpresa['alto'], con.apExperiencias['alto'])
rule116 = __ctrl.Rule(ant.emocional['bajo'] &
                      ant.sorpresa['medio'], con.apExperiencias['medio'])
rule117 = __ctrl.Rule(ant.emocional['bajo'] &
                      ant.sorpresa['bajo'], con.responsabilidad['alto'])

# Reglas para ant.emocional - Tristeza
rule118 = __ctrl.Rule(ant.emocional['alto'] &
                      ant.tristeza['alto'], con.extrovertido['bajo'])
rule119 = __ctrl.Rule(ant.emocional['alto'] &
                      ant.tristeza['medio'], con.amabilidad['medio'])
rule120 = __ctrl.Rule(ant.emocional['alto'] &
                      ant.tristeza['bajo'], con.amabilidad['bajo'])
rule121 = __ctrl.Rule(ant.emocional['medio'] &
                      ant.tristeza['alto'], con.extrovertido['bajo'])
rule122 = __ctrl.Rule(ant.emocional['medio'] &
                      ant.tristeza['medio'], con.amabilidad['medio'])
rule123 = __ctrl.Rule(ant.emocional['medio'] &
                      ant.tristeza['bajo'], con.amabilidad['bajo'])
rule124 = __ctrl.Rule(ant.emocional['bajo'] &
                      ant.tristeza['alto'], con.extrovertido['bajo'])
rule125 = __ctrl.Rule(ant.emocional['bajo'] &
                      ant.tristeza['medio'], con.amabilidad['medio'])
rule126 = __ctrl.Rule(ant.emocional['bajo'] &
                      ant.tristeza['bajo'], con.extrovertido['alto'])

# Extrovertido, con.estEmocional, con.responsabilidad, con.apExperiencias, con.amabilidad
# Bajo: 0 - 50
# Medio: 51 - 80
# Alto: 81 - 100
