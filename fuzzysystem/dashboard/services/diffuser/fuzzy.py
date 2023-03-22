import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np


class fuzzySystem:
    def __init__(self, diccionario):
        self.rasgo = diccionario[0]['rasgo'][0]['predictions'][0]
        self.emocion = diccionario[1]['emocion'][0]['predictions'][0]
        self.indentify()
        self.res

    def indentify(self):
        opciones = {
            ('rational', 'sadness'): self.racionalTristeza,
            ('rational', 'surprise'): self.racionalSorpresa,
            ('rational', 'anger'): self.racionalEnfado,
            ('rational', 'fear'): self.racionalTemor,
            ('rational', 'disgust'): self.racionalAsco,
            ('rational', 'joy'): self.racionalDisfrute,
            ('rational', 'no-emotion'): self.racionalNoEmocion,
            ('emotional', 'sadness'): self.emocionalTristeza,
            ('emotional', 'surprise'): self.emocionalSorpresa,
            ('emotional', 'anger'): self.emocionalEnfado,
            ('emotional', 'fear'): self.emocionalTemor,
            ('emotional', 'disgust'): self.emocionalAsco,
            ('emotional', 'joy'): self.emocionalDisfrute,
            ('emotional', 'no-emotion'): self.emocionalNoEmocion,
        }
        key = (self.rasgo['prediction'], self.emocion['prediction'])
        if key in opciones:
            metodo = opciones[key]
            print(f'entró en {key[0]} - {key[1]}')
            self.res = metodo(
                self.rasgo['probability']*100, self.emocion['probability']*100)

        else:
            print(f'No hay un método asociado para la opción {key}')
        return self.res

    # Metodos para separar los diferentes Antecedentes
    def racionalTristeza(self, rasgo, emocion):
        activador1 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
        activador2 = (rasgo in range(0, 51)) and (emocion in range(50, 81))
        activador3 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

        if (activador1 or activador2 or activador3):
            sys_ctrl = ctrl.ControlSystem([self.rule4, self.rule8, self.rule9])
            racTrisSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            racTrisSimulation.input['racional'] = rasgo
            racTrisSimulation.input['tristeza'] = emocion
            print(racTrisSimulation.input)
            racTrisSimulation.compute()
            print(racTrisSimulation.output)
            return racTrisSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule1, self.rule2, self.rule3, self.rule5, self.rule6, self.rule7])
            racTrisSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            racTrisSimulation.input['racional'] = rasgo
            racTrisSimulation.input['tristeza'] = emocion
            print(racTrisSimulation.input)
            racTrisSimulation.compute()
            print(racTrisSimulation.output)
            return racTrisSimulation.output

    def racionalSorpresa(self, rasgo, emocion):
        activador1 = (rasgo in range(80, 101)) and (emocion in range(0, 51))
        activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
        activador3 = (rasgo in range(0, 51)) and (emocion in range(80, 101))
        activador4 = (rasgo in range(0, 51)) and (emocion in range(50, 81))

        if (activador1 or activador2 or activador3 or activador4):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule12, self.rule13, self.rule16, self.rule17])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['sorpresa'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule10, self.rule11, self.rule14, self.rule15, self.rule18])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['sorpresa'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def racionalEnfado(self, rasgo, emocion):
        activador1 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
        activador2 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
        activador3 = (rasgo in range(0, 51)) and (emocion in range(80, 101))
        activador4 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

        if (activador1 or activador2 or activador3 or activador4):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule22, self.rule24, self.rule25, self.rule27])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['enfado'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule19, self.rule20, self.rule21, self.rule23, self.rule26])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['enfado'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def racionalTemor(self, rasgo, emocion):
        activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
        activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
        activador3 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
        activador4 = (rasgo in range(0, 51)) and (emocion in range(80, 101))

        if (activador1 or activador2 or activador3 or activador4):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule28, self.rule31, self.rule33, self.rule34])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['temor'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule29, self.rule30, self.rule32, self.rule35, self.rule36])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['temor'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def racionalAsco(self, rasgo, emocion):
        activador1 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
        activador2 = (rasgo in range(0, 51)) and (emocion in range(50, 81))
        activador3 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

        if (activador1 or activador2 or activador3):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule42, self.rule44, self.rule45])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['asco'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule37, self.rule38, self.rule39, self.rule40, self.rule41, self.rule43])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['asco'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def racionalDisfrute(self, rasgo, emocion):
        activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
        activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
        activador3 = (rasgo in range(50, 81)) and (emocion in range(50, 81))
        activador4 = (rasgo in range(0, 51)) and (emocion in range(80, 101))

        if (activador1 or activador2 or activador3 or activador4):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule46, self.rule49, self.rule50, self.rule52])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['disfrute'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule47, self.rule48, self.rule51, self.rule53, self.rule54])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['disfrute'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def racionalNoEmocion(self, rasgo, emocion):
        activador1 = (rasgo in range(80, 101)) and (emocion in range(0, 51))
        activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
        activador3 = (rasgo in range(0, 51)) and (emocion in range(80, 101))
        activador4 = (rasgo in range(0, 51)) and (emocion in range(50, 81))

        if (activador1 or activador2 or activador3 or activador4):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule57, self.rule58, self.rule61, self.rule62])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['sorpresa'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule55, self.rule56, self.rule59, self.rule60, self.rule63])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['racional'] = rasgo
            sysSimulation.input['noEmocion'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def emocionalNoEmocion(self, rasgo, emocion):
        activador1 = (rasgo in range(80, 101)) and (emocion in range(0, 51))
        activador2 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
        activador3 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

        if (activador1 or activador2 or activador3):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule66, self.rule69, self.rule72])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['sorpresa'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule64, self.rule65, self.rule67, self.rule68, self.rule70, self.rule71])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['sorpresa'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def emocionalDisfrute(self, rasgo, emocion):
        activador1 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
        activador2 = (rasgo in range(0, 51)) and (emocion in range(80, 101))
        activador3 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

        if (activador1 or activador2 or activador3):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule76, self.rule79, self.rule81])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['disfrute'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule73, self.rule74, self.rule75, self.rule77, self.rule78, self.rule80])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['disfrute'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def emocionalAsco(self, rasgo, emocion):
        activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
        activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
        activador3 = (rasgo in range(50, 81)) and (emocion in range(50, 81))
        activador4 = (rasgo in range(0, 51)) and (emocion in range(80, 101))

        if (activador1 or activador2 or activador3 or activador4):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule82, self.rule85, self.rule86, self.rule88])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['asco'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule83, self.rule84, self.rule87, self.rule89, self.rule90])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['asco'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def emocionalTemor(self, rasgo, emocion):
        activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
        activador2 = (rasgo in range(80, 101)) and (emocion in range(0, 51))
        activador3 = (rasgo in range(50, 81)) and (emocion in range(50, 81))
        activador4 = (rasgo in range(0, 51)) and (emocion in range(50, 81))

        if (activador1 or activador2 or activador3 or activador4):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule91, self.rule93, self.rule95, self.rule98])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['temor'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output.items()
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule92, self.rule94, self.rule96, self.rule97, self.rule99])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['temor'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def emocionalEnfado(self, rasgo, emocion):
        activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
        activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
        activador3 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
        activador4 = (rasgo in range(0, 51)) and (emocion in range(80, 101))

        if (activador1 or activador2 or activador3 or activador4):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule100, self.rule103, self.rule105, self.rule106])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['enfado'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule101, self.rule102, self.rule104, self.rule107, self.rule108])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['enfado'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def emocionalSorpresa(self, rasgo, emocion):
        activador1 = (rasgo in range(80, 101)) and (emocion in range(0, 51))
        activador2 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
        activador3 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

        if (activador1 or activador2 or activador3):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule111, self.rule114, self.rule117])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['sorpresa'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule109, self.rule110, self.rule112, self.rule113, self.rule115, self.rule116])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['sorpresa'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    def emocionalTristeza(self, rasgo, emocion):
        activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
        activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
        activador3 = (rasgo in range(0, 51)) and (emocion in range(80, 101))
        activador4 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

        if (activador1 or activador2 or activador3 or activador4):
            sys_ctrl = ctrl.ControlSystem(
                [self.rule118, self.rule121, self.rule124, self.rule126])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['tristeza'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output
        else:
            sys_ctrl = ctrl.ControlSystem(
                [self.rule119, self.rule120, self.rule122, self.rule123, self.rule125])
            sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
            sysSimulation.input['emocional'] = rasgo
            sysSimulation.input['tristeza'] = emocion
            print(sysSimulation.input)
            sysSimulation.compute()
            print(sysSimulation.output)
            return sysSimulation.output

    #########################################################################
    #                       Rasgos de Personalidad                          #
    #########################################################################

    # racional
    racional = ctrl.Antecedent(np.arange(0, 100, 0.1), 'racional')
    racional['bajo'] = fuzz.gaussmf(racional.universe, 30, 20)
    racional['medio'] = fuzz.gaussmf(racional.universe, 70, 20)
    racional['alto'] = fuzz.gaussmf(racional.universe, 100, 20)

    # emocional
    emocional = ctrl.Antecedent(np.arange(0, 101, 0.1), 'emocional')
    emocional['bajo'] = fuzz.gaussmf(emocional.universe, 30, 20)
    emocional['medio'] = fuzz.gaussmf(emocional.universe, 70, 20)
    emocional['alto'] = fuzz.gaussmf(emocional.universe, 100, 20)

    #########################################################################
    #                              Emociones                                #
    #########################################################################

    # tristeza
    tristeza = ctrl.Antecedent(np.arange(0, 101, 0.1), 'tristeza')
    tristeza['bajo'] = fuzz.gaussmf(tristeza.universe, 30, 20)
    tristeza['medio'] = fuzz.gaussmf(tristeza.universe, 70, 30)
    tristeza['alto'] = fuzz.gaussmf(tristeza.universe, 100, 20)

    # sorpresa
    sorpresa = ctrl.Antecedent(np.arange(0, 101, 0.1), 'sorpresa')
    sorpresa['bajo'] = fuzz.gaussmf(sorpresa.universe, 30, 20)
    sorpresa['medio'] = fuzz.gaussmf(sorpresa.universe, 70, 15)
    sorpresa['alto'] = fuzz.gaussmf(sorpresa.universe, 100, 20)

    # disfrute
    disfrute = ctrl.Antecedent(np.arange(0, 101, 0.1), 'disfrute')
    disfrute['bajo'] = fuzz.gaussmf(disfrute.universe, 30, 20)
    disfrute['medio'] = fuzz.gaussmf(disfrute.universe, 70, 15)
    disfrute['alto'] = fuzz.gaussmf(disfrute.universe, 100, 20)

    # enfado
    enfado = ctrl.Antecedent(np.arange(0, 101, 0.1), 'enfado')
    enfado['bajo'] = fuzz.gaussmf(enfado.universe, 30, 20)
    enfado['medio'] = fuzz.gaussmf(enfado.universe, 70, 15)
    enfado['alto'] = fuzz.gaussmf(enfado.universe, 90, 20)

    # asco
    asco = ctrl.Antecedent(np.arange(0, 101, 0.1), 'asco')
    asco['bajo'] = fuzz.gaussmf(asco.universe, 30, 20)
    asco['medio'] = fuzz.gaussmf(asco.universe, 75, 20)
    asco['alto'] = fuzz.gaussmf(asco.universe, 100, 20)

    # temor
    temor = ctrl.Antecedent(np.arange(0, 101, 0.1), 'temor')
    temor['bajo'] = fuzz.gaussmf(temor.universe, 30, 20)
    temor['medio'] = fuzz.gaussmf(temor.universe, 70, 15)
    temor['alto'] = fuzz.gaussmf(temor.universe, 90, 20)

    # sin emoción
    noEmocion = ctrl.Antecedent(np.arange(0, 101, 0.1), 'noEmocion')
    noEmocion['bajo'] = fuzz.gaussmf(noEmocion.universe, 30, 20)
    noEmocion['medio'] = fuzz.gaussmf(noEmocion.universe, 70, 10)
    noEmocion['alto'] = fuzz.gaussmf(noEmocion.universe, 90, 20)

    #########################################################################
    #                             Concecuentes                              #
    #               Basado en los 5 grandes de la Psicología                #
    #########################################################################

    # Estabilidad Emocional
    estEmocional = ctrl.Consequent(np.arange(0, 101, 0.1), 'estEmocional')
    estEmocional['bajo'] = fuzz.gaussmf(estEmocional.universe, 30, 30)
    estEmocional['medio'] = fuzz.gaussmf(estEmocional.universe, 70, 20)
    estEmocional['alto'] = fuzz.gaussmf(estEmocional.universe, 100, 20)

    # Extrovertido
    extrovertido = ctrl.Consequent(np.arange(0, 101, 0.1), 'extrovertido')
    extrovertido['bajo'] = fuzz.gaussmf(extrovertido.universe, 30, 30)
    extrovertido['medio'] = fuzz.gaussmf(extrovertido.universe, 70, 20)
    extrovertido['alto'] = fuzz.gaussmf(extrovertido.universe, 100, 20)

    # Apertura Experiencias
    apExperiencias = ctrl.Consequent(np.arange(0, 101, 0.1), 'apExperiencias')
    apExperiencias['bajo'] = fuzz.gaussmf(apExperiencias.universe, 0, 30)
    apExperiencias['medio'] = fuzz.gaussmf(apExperiencias.universe, 75, 10)
    apExperiencias['alto'] = fuzz.gaussmf(apExperiencias.universe, 100, 10)

    # Amabilidad
    amabilidad = ctrl.Consequent(np.arange(0, 101, 0.1), 'amabilidad')
    amabilidad['bajo'] = fuzz.gaussmf(amabilidad.universe, 40, 30)
    amabilidad['medio'] = fuzz.gaussmf(amabilidad.universe, 70, 10)
    amabilidad['alto'] = fuzz.gaussmf(amabilidad.universe, 90, 10)

    # responsabilidad
    responsabilidad = ctrl.Consequent(
        np.arange(0, 101, 0.1), 'responsabilidad')
    responsabilidad['bajo'] = fuzz.gaussmf(responsabilidad.universe, 0, 30)
    responsabilidad['medio'] = fuzz.gaussmf(responsabilidad.universe, 50, 10)
    responsabilidad['alto'] = fuzz.gaussmf(responsabilidad.universe, 100, 10)

    #################################################################################
    #                                 REGLAS DIFUSAS                                #
    #                                  PARA RACIONAL                                #
    #################################################################################

    # Reglas para Racional - Tristeza
    rule1 = ctrl.Rule(racional['alto'] &
                      tristeza['alto'], extrovertido['bajo'])
    rule2 = ctrl.Rule(racional['alto'] &
                      tristeza['medio'], extrovertido['medio'])
    rule3 = ctrl.Rule(racional['alto'] &
                      tristeza['bajo'], extrovertido['alto'])
    rule4 = ctrl.Rule(racional['medio'] &
                      tristeza['alto'], estEmocional['bajo'])
    rule5 = ctrl.Rule(racional['medio'] &
                      tristeza['medio'], extrovertido['medio'])
    rule6 = ctrl.Rule(racional['medio'] &
                      tristeza['bajo'], extrovertido['alto'])
    rule7 = ctrl.Rule(racional['bajo'] &
                      tristeza['alto'], extrovertido['bajo'])
    rule8 = ctrl.Rule(racional['bajo'] &
                      tristeza['medio'], estEmocional['medio'])
    rule9 = ctrl.Rule(racional['bajo'] &
                      tristeza['bajo'], estEmocional['alto'])

    # Reglas para Racional - Sorpresa
    rule10 = ctrl.Rule(racional['alto'] &
                       sorpresa['alto'], responsabilidad['alto'])
    rule11 = ctrl.Rule(racional['alto'] &
                       sorpresa['medio'], responsabilidad['medio'])
    rule12 = ctrl.Rule(racional['alto'] &
                       sorpresa['bajo'], apExperiencias['medio'])
    rule13 = ctrl.Rule(racional['medio'] &
                       sorpresa['alto'], apExperiencias['medio'])
    rule14 = ctrl.Rule(racional['medio'] &
                       sorpresa['medio'], responsabilidad['medio'])
    rule15 = ctrl.Rule(racional['medio'] &
                       sorpresa['bajo'], responsabilidad['alto'])
    rule16 = ctrl.Rule(racional['bajo'] &
                       sorpresa['alto'], apExperiencias['alto'])
    rule17 = ctrl.Rule(racional['bajo'] &
                       sorpresa['medio'], apExperiencias['medio'])
    rule18 = ctrl.Rule(racional['bajo'] &
                       sorpresa['bajo'], responsabilidad['medio'])

    # Reglas para Racional - Enfado
    rule19 = ctrl.Rule(racional['alto'] & enfado['alto'], estEmocional['bajo'])
    rule20 = ctrl.Rule(racional['alto'] &
                       enfado['medio'], estEmocional['medio'])
    rule21 = ctrl.Rule(racional['alto'] & enfado['bajo'], estEmocional['alto'])
    rule22 = ctrl.Rule(racional['medio'] &
                       enfado['alto'], apExperiencias['bajo'])
    rule23 = ctrl.Rule(racional['medio'] &
                       enfado['medio'], estEmocional['medio'])
    rule24 = ctrl.Rule(racional['medio'] &
                       enfado['bajo'], apExperiencias['medio'])
    rule25 = ctrl.Rule(racional['bajo'] &
                       enfado['alto'], apExperiencias['medio'])
    rule26 = ctrl.Rule(racional['bajo'] &
                       enfado['medio'], estEmocional['medio'])
    rule27 = ctrl.Rule(racional['bajo'] &
                       enfado['bajo'], apExperiencias['alto'])

    # Reglas para Racional - Temor
    rule28 = ctrl.Rule(racional['alto'] & temor['alto'], estEmocional['bajo'])
    rule29 = ctrl.Rule(racional['alto'] &
                       temor['medio'], responsabilidad['medio'])
    rule30 = ctrl.Rule(racional['alto'] &
                       temor['bajo'], responsabilidad['alto'])
    rule31 = ctrl.Rule(racional['medio'] &
                       temor['alto'], estEmocional['medio'])
    rule32 = ctrl.Rule(racional['medio'] &
                       temor['medio'], responsabilidad['medio'])
    rule33 = ctrl.Rule(racional['medio'] &
                       temor['bajo'], estEmocional['medio'])
    rule34 = ctrl.Rule(racional['bajo'] & temor['alto'], estEmocional['medio'])
    rule35 = ctrl.Rule(racional['bajo'] &
                       temor['medio'], responsabilidad['medio'])
    rule36 = ctrl.Rule(racional['bajo'] &
                       temor['bajo'], responsabilidad['alto'])

    # Reglas para Racional - Asco
    rule37 = ctrl.Rule(racional['alto'] & asco['alto'], apExperiencias['bajo'])
    rule38 = ctrl.Rule(racional['alto'] &
                       asco['medio'], apExperiencias['medio'])
    rule39 = ctrl.Rule(racional['alto'] & asco['bajo'], apExperiencias['alto'])
    rule40 = ctrl.Rule(racional['medio'] &
                       asco['alto'], apExperiencias['medio'])
    rule41 = ctrl.Rule(racional['medio'] &
                       asco['medio'], apExperiencias['bajo'])
    rule42 = ctrl.Rule(racional['medio'] & asco['bajo'], extrovertido['medio'])
    rule43 = ctrl.Rule(racional['bajo'] & asco['alto'], apExperiencias['bajo'])
    rule44 = ctrl.Rule(racional['bajo'] & asco['medio'], extrovertido['medio'])
    rule45 = ctrl.Rule(racional['bajo'] & asco['bajo'], extrovertido['bajo'])

    # Reglas para Racional - Disfrute
    rule46 = ctrl.Rule(racional['alto'] & disfrute['alto'], amabilidad['alto'])
    rule47 = ctrl.Rule(racional['alto'] &
                       disfrute['medio'], extrovertido['medio'])
    rule48 = ctrl.Rule(racional['alto'] &
                       disfrute['bajo'], extrovertido['bajo'])
    rule49 = ctrl.Rule(racional['medio'] &
                       disfrute['alto'], amabilidad['alto'])
    rule50 = ctrl.Rule(racional['medio'] &
                       disfrute['medio'], amabilidad['medio'])
    rule51 = ctrl.Rule(racional['medio'] &
                       disfrute['bajo'], extrovertido['bajo'])
    rule52 = ctrl.Rule(racional['bajo'] & disfrute['alto'], amabilidad['alto'])
    rule53 = ctrl.Rule(racional['bajo'] &
                       disfrute['medio'], extrovertido['medio'])
    rule54 = ctrl.Rule(racional['bajo'] &
                       disfrute['bajo'], extrovertido['bajo'])

    # Reglas para Racional - Sin Emoción
    rule55 = ctrl.Rule(racional['alto'] &
                       noEmocion['alto'], responsabilidad['alto'])
    rule56 = ctrl.Rule(racional['alto'] &
                       noEmocion['medio'], responsabilidad['medio'])
    rule57 = ctrl.Rule(racional['alto'] &
                       noEmocion['bajo'], estEmocional['medio'])
    rule58 = ctrl.Rule(racional['medio'] &
                       noEmocion['alto'], estEmocional['medio'])
    rule59 = ctrl.Rule(racional['medio'] &
                       noEmocion['medio'], responsabilidad['medio'])
    rule60 = ctrl.Rule(racional['medio'] &
                       noEmocion['bajo'], responsabilidad['alto'])
    rule61 = ctrl.Rule(racional['bajo'] &
                       noEmocion['alto'], estEmocional['alto'])
    rule62 = ctrl.Rule(racional['bajo'] &
                       noEmocion['medio'], estEmocional['medio'])
    rule63 = ctrl.Rule(racional['bajo'] &
                       noEmocion['bajo'], responsabilidad['bajo'])

    #################################################################################
    #                                 REGLAS DIFUSAS                                #
    #                                 PARA EMOCIONAL                                #
    #################################################################################

    # Reglas para Emocional - Sin Emoción
    rule64 = ctrl.Rule(emocional['alto'] &
                       noEmocion['alto'], apExperiencias['alto'])
    rule65 = ctrl.Rule(emocional['alto'] &
                       noEmocion['medio'], apExperiencias['medio'])
    rule66 = ctrl.Rule(emocional['alto'] &
                       noEmocion['bajo'], estEmocional['alto'])
    rule67 = ctrl.Rule(emocional['medio'] &
                       noEmocion['alto'], apExperiencias['alto'])
    rule68 = ctrl.Rule(emocional['medio'] &
                       noEmocion['medio'], apExperiencias['medio'])
    rule69 = ctrl.Rule(emocional['medio'] &
                       noEmocion['bajo'], estEmocional['alto'])
    rule70 = ctrl.Rule(emocional['bajo'] &
                       noEmocion['alto'], apExperiencias['alto'])
    rule71 = ctrl.Rule(emocional['bajo'] &
                       noEmocion['medio'], apExperiencias['medio'])
    rule72 = ctrl.Rule(emocional['bajo'] &
                       noEmocion['bajo'], estEmocional['alto'])

    # Reglas para Emocional - Disfrute
    rule73 = ctrl.Rule(emocional['alto'] &
                       disfrute['alto'], apExperiencias['alto'])
    rule74 = ctrl.Rule(emocional['alto'] &
                       disfrute['medio'], apExperiencias['medio'])
    rule75 = ctrl.Rule(emocional['alto'] &
                       disfrute['bajo'], apExperiencias['bajo'])
    rule76 = ctrl.Rule(emocional['medio'] &
                       disfrute['alto'], extrovertido['bajo'])
    rule77 = ctrl.Rule(emocional['medio'] &
                       disfrute['medio'], apExperiencias['medio'])
    rule78 = ctrl.Rule(emocional['medio'] &
                       disfrute['bajo'], apExperiencias['bajo'])
    rule79 = ctrl.Rule(emocional['bajo'] &
                       disfrute['alto'], extrovertido['medio'])
    rule80 = ctrl.Rule(emocional['bajo'] &
                       disfrute['medio'], apExperiencias['medio'])
    rule81 = ctrl.Rule(emocional['bajo'] &
                       disfrute['bajo'], extrovertido['alto'])

    # Reglas para Emocional - Asco
    rule82 = ctrl.Rule(emocional['alto'] &
                       asco['alto'], apExperiencias['medio'])
    rule83 = ctrl.Rule(emocional['alto'] & asco['medio'], amabilidad['medio'])
    rule84 = ctrl.Rule(emocional['alto'] & asco['bajo'], amabilidad['alto'])
    rule85 = ctrl.Rule(emocional['medio'] &
                       asco['alto'], apExperiencias['alto'])
    rule86 = ctrl.Rule(emocional['medio'] &
                       asco['medio'], apExperiencias['medio'])
    rule87 = ctrl.Rule(emocional['medio'] & asco['bajo'], amabilidad['medio'])
    rule88 = ctrl.Rule(emocional['bajo'] &
                       asco['alto'], apExperiencias['medio'])
    rule89 = ctrl.Rule(emocional['bajo'] & asco['medio'], amabilidad['medio'])
    rule90 = ctrl.Rule(emocional['bajo'] & asco['bajo'], amabilidad['alto'])

    # Reglas para Emocional - Temor
    rule91 = ctrl.Rule(emocional['alto'] &
                       temor['alto'], estEmocional['medio'])
    rule92 = ctrl.Rule(emocional['alto'] & temor['medio'], amabilidad['bajo'])
    rule93 = ctrl.Rule(emocional['alto'] & temor['bajo'], estEmocional['alto'])
    rule94 = ctrl.Rule(emocional['medio'] & temor['alto'], amabilidad['medio'])
    rule95 = ctrl.Rule(emocional['medio'] &
                       temor['medio'], estEmocional['medio'])
    rule96 = ctrl.Rule(emocional['medio'] & temor['bajo'], amabilidad['alto'])
    rule97 = ctrl.Rule(emocional['bajo'] & temor['alto'], amabilidad['bajo'])
    rule98 = ctrl.Rule(emocional['bajo'] &
                       temor['medio'], estEmocional['medio'])
    rule99 = ctrl.Rule(emocional['bajo'] & temor['bajo'], amabilidad['medio'])

    # Reglas para Emocional - Enfado
    rule100 = ctrl.Rule(emocional['alto'] &
                        enfado['alto'], responsabilidad['medio'])
    rule101 = ctrl.Rule(emocional['alto'] &
                        enfado['medio'], amabilidad['bajo'])
    rule102 = ctrl.Rule(emocional['alto'] & enfado['bajo'], amabilidad['alto'])
    rule103 = ctrl.Rule(emocional['medio'] &
                        enfado['alto'], responsabilidad['medio'])
    rule104 = ctrl.Rule(emocional['medio'] &
                        enfado['medio'], amabilidad['medio'])
    rule105 = ctrl.Rule(emocional['medio'] &
                        enfado['bajo'], responsabilidad['alto'])
    rule106 = ctrl.Rule(emocional['bajo'] &
                        enfado['alto'], responsabilidad['medio'])
    rule107 = ctrl.Rule(emocional['bajo'] &
                        enfado['medio'], amabilidad['alto'])
    rule108 = ctrl.Rule(emocional['bajo'] &
                        enfado['bajo'], amabilidad['medio'])

    # Reglas para emocional - Sorpresa
    rule109 = ctrl.Rule(emocional['alto'] &
                        sorpresa['alto'], apExperiencias['alto'])
    rule110 = ctrl.Rule(emocional['alto'] &
                        sorpresa['medio'], apExperiencias['medio'])
    rule111 = ctrl.Rule(emocional['alto'] &
                        sorpresa['bajo'], responsabilidad['alto'])
    rule112 = ctrl.Rule(emocional['medio'] &
                        sorpresa['alto'], apExperiencias['alto'])
    rule113 = ctrl.Rule(emocional['medio'] &
                        sorpresa['medio'], apExperiencias['medio'])
    rule114 = ctrl.Rule(emocional['medio'] &
                        sorpresa['bajo'], responsabilidad['alto'])
    rule115 = ctrl.Rule(emocional['bajo'] &
                        sorpresa['alto'], apExperiencias['alto'])
    rule116 = ctrl.Rule(emocional['bajo'] &
                        sorpresa['medio'], apExperiencias['medio'])
    rule117 = ctrl.Rule(emocional['bajo'] &
                        sorpresa['bajo'], responsabilidad['alto'])

    # Reglas para emocional - Tristeza
    rule118 = ctrl.Rule(emocional['alto'] &
                        tristeza['alto'], extrovertido['bajo'])
    rule119 = ctrl.Rule(emocional['alto'] &
                        tristeza['medio'], amabilidad['medio'])
    rule120 = ctrl.Rule(emocional['alto'] &
                        tristeza['bajo'], amabilidad['bajo'])
    rule121 = ctrl.Rule(emocional['medio'] &
                        tristeza['alto'], extrovertido['bajo'])
    rule122 = ctrl.Rule(emocional['medio'] &
                        tristeza['medio'], amabilidad['medio'])
    rule123 = ctrl.Rule(emocional['medio'] &
                        tristeza['bajo'], amabilidad['bajo'])
    rule124 = ctrl.Rule(emocional['bajo'] &
                        tristeza['alto'], extrovertido['bajo'])
    rule125 = ctrl.Rule(emocional['bajo'] &
                        tristeza['medio'], amabilidad['medio'])
    rule126 = ctrl.Rule(emocional['bajo'] &
                        tristeza['bajo'], extrovertido['alto'])

    # Extrovertido, estEmocional, responsabilidad, apExperiencias, amabilidad
    # Bajo: 0 - 50
    # Medio: 51 - 80
    # Alto: 81 - 100


if __name__ == "__main__":
    # para probar
    mi_diccionario = [
        {
            'rasgo': [
                {
                    'id': '2',
                    'predictions': [
                        {
                            'prediction': 'emotional',
                            'probability': 0.9992
                        }
                    ]
                }
            ]
        },
        {
            'emocion': [
                {
                    'id': '2',
                    'predictions': [
                        {
                            'prediction': 'fear',
                            'probability': 0.34702
                        }
                    ]
                }
            ]
        }
    ]
    ex = fuzzySystem(mi_diccionario)
    print(list(ex.indentify().items()))
