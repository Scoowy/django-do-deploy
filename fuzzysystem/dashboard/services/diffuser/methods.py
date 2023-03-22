from skfuzzy import control as ctrl
from . import rules as rul


def racionalTristeza(rasgo: float, emocion: float):
    activador1 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
    activador2 = (rasgo in range(0, 51)) and (emocion in range(50, 81))
    activador3 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

    if (activador1 or activador2 or activador3):
        sys_ctrl = ctrl.ControlSystem([rul.rule4, rul.rule8, rul.rule9])
        racTrisSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        racTrisSimulation.input['racional'] = rasgo
        racTrisSimulation.input['tristeza'] = emocion
        print(racTrisSimulation.input)
        racTrisSimulation.compute()
        print(racTrisSimulation.output)
        return racTrisSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule1, rul.rule2, rul.rule3, rul.rule5, rul.rule6, rul.rule7])
        racTrisSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        racTrisSimulation.input['racional'] = rasgo
        racTrisSimulation.input['tristeza'] = emocion
        print(racTrisSimulation.input)
        racTrisSimulation.compute()
        print(racTrisSimulation.output)
        return racTrisSimulation.output


def racionalSorpresa(rasgo: float, emocion: float):
    activador1 = (rasgo in range(80, 101)) and (emocion in range(0, 51))
    activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
    activador3 = (rasgo in range(0, 51)) and (emocion in range(80, 101))
    activador4 = (rasgo in range(0, 51)) and (emocion in range(50, 81))

    if (activador1 or activador2 or activador3 or activador4):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule12, rul.rule13, rul.rule16, rul.rule17])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['sorpresa'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule10, rul.rule11, rul.rule14, rul.rule15, rul.rule18])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['sorpresa'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def racionalEnfado(rasgo: float, emocion: float):
    activador1 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
    activador2 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
    activador3 = (rasgo in range(0, 51)) and (emocion in range(80, 101))
    activador4 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

    if (activador1 or activador2 or activador3 or activador4):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule22, rul.rule24, rul.rule25, rul.rule27])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['enfado'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule19, rul.rule20, rul.rule21, rul.rule23, rul.rule26])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['enfado'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def racionalTemor(rasgo: float, emocion: float):
    activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
    activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
    activador3 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
    activador4 = (rasgo in range(0, 51)) and (emocion in range(80, 101))

    if (activador1 or activador2 or activador3 or activador4):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule28, rul.rule31, rul.rule33, rul.rule34])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['temor'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule29, rul.rule30, rul.rule32, rul.rule35, rul.rule36])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['temor'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def racionalAsco(rasgo: float, emocion: float):
    activador1 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
    activador2 = (rasgo in range(0, 51)) and (emocion in range(50, 81))
    activador3 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

    if (activador1 or activador2 or activador3):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule42, rul.rule44, rul.rule45])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['asco'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule37, rul.rule38, rul.rule39, rul.rule40, rul.rule41, rul.rule43])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['asco'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def racionalDisfrute(rasgo: float, emocion: float):
    activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
    activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
    activador3 = (rasgo in range(50, 81)) and (emocion in range(50, 81))
    activador4 = (rasgo in range(0, 51)) and (emocion in range(80, 101))

    if (activador1 or activador2 or activador3 or activador4):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule46, rul.rule49, rul.rule50, rul.rule52])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['disfrute'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule47, rul.rule48, rul.rule51, rul.rule53, rul.rule54])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['disfrute'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def racionalNoEmocion(rasgo: float, emocion: float):
    activador1 = (rasgo in range(80, 101)) and (emocion in range(0, 51))
    activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
    activador3 = (rasgo in range(0, 51)) and (emocion in range(80, 101))
    activador4 = (rasgo in range(0, 51)) and (emocion in range(50, 81))

    if (activador1 or activador2 or activador3 or activador4):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule57, rul.rule58, rul.rule61, rul.rule62])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['sorpresa'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule55, rul.rule56, rul.rule59, rul.rule60, rul.rule63])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['racional'] = rasgo
        sysSimulation.input['noEmocion'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def emocionalNoEmocion(rasgo: float, emocion: float):
    activador1 = (rasgo in range(80, 101)) and (emocion in range(0, 51))
    activador2 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
    activador3 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

    if (activador1 or activador2 or activador3):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule66, rul.rule69, rul.rule72])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['sorpresa'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule64, rul.rule65, rul.rule67, rul.rule68, rul.rule70, rul.rule71])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['noEmocion'] = emocion  # TODO : Review this
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def emocionalDisfrute(rasgo: float, emocion: float):
    activador1 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
    activador2 = (rasgo in range(0, 51)) and (emocion in range(80, 101))
    activador3 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

    if (activador1 or activador2 or activador3):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule76, rul.rule79, rul.rule81])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['disfrute'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule73, rul.rule74, rul.rule75, rul.rule77, rul.rule78, rul.rule80])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['disfrute'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def emocionalAsco(rasgo: float, emocion: float):
    activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
    activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
    activador3 = (rasgo in range(50, 81)) and (emocion in range(50, 81))
    activador4 = (rasgo in range(0, 51)) and (emocion in range(80, 101))

    if (activador1 or activador2 or activador3 or activador4):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule82, rul.rule85, rul.rule86, rul.rule88])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['asco'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule83, rul.rule84, rul.rule87, rul.rule89, rul.rule90])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['asco'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def emocionalTemor(rasgo: float, emocion: float):
    activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
    activador2 = (rasgo in range(80, 101)) and (emocion in range(0, 51))
    activador3 = (rasgo in range(50, 81)) and (emocion in range(50, 81))
    activador4 = (rasgo in range(0, 51)) and (emocion in range(50, 81))

    if (activador1 or activador2 or activador3 or activador4):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule91, rul.rule93, rul.rule95, rul.rule98])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['temor'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output.items()
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule92, rul.rule94, rul.rule96, rul.rule97, rul.rule99])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['temor'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def emocionalEnfado(rasgo: float, emocion: float):
    activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
    activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
    activador3 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
    activador4 = (rasgo in range(0, 51)) and (emocion in range(80, 101))

    if (activador1 or activador2 or activador3 or activador4):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule100, rul.rule103, rul.rule105, rul.rule106])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['enfado'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule101, rul.rule102, rul.rule104, rul.rule107, rul.rule108])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['enfado'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def emocionalSorpresa(rasgo: float, emocion: float):
    activador1 = (rasgo in range(80, 101)) and (emocion in range(0, 51))
    activador2 = (rasgo in range(50, 81)) and (emocion in range(0, 51))
    activador3 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

    if (activador1 or activador2 or activador3):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule111, rul.rule114, rul.rule117])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['sorpresa'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule109, rul.rule110, rul.rule112, rul.rule113, rul.rule115, rul.rule116])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['sorpresa'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output


def emocionalTristeza(rasgo: float, emocion: float):
    activador1 = (rasgo in range(80, 101)) and (emocion in range(80, 101))
    activador2 = (rasgo in range(50, 81)) and (emocion in range(80, 101))
    activador3 = (rasgo in range(0, 51)) and (emocion in range(80, 101))
    activador4 = (rasgo in range(0, 51)) and (emocion in range(0, 51))

    if (activador1 or activador2 or activador3 or activador4):
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule118, rul.rule121, rul.rule124, rul.rule126])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['tristeza'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
    else:
        sys_ctrl = ctrl.ControlSystem(
            [rul.rule119, rul.rule120, rul.rule122, rul.rule123, rul.rule125])
        sysSimulation = ctrl.ControlSystemSimulation(sys_ctrl)
        sysSimulation.input['emocional'] = rasgo
        sysSimulation.input['tristeza'] = emocion
        print(sysSimulation.input)
        sysSimulation.compute()
        print(sysSimulation.output)
        return sysSimulation.output
