
def empaquetar(Q,gripper,motor):
    paquete = "<" + str(Q[0]) + ":" + str(Q[1]) + ":" + str(Q[2]) + ":" + str(Q[3]) + ":" + str(gripper) + ":" + str(motor) + ">"
    return paquete