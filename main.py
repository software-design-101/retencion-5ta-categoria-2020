import datetime

# TODO: No se retiene ningun monto si es que el ingreso bruto anual no supera las 7 UIT
# Un trabajdor al año recibe 12 sueldos mas dos gratificaciones es decir 14 sueldos.
# El monto de la UIT para 2020 es 4300 soles

def tasa(rneto, uit):
    if rneto <= 5 * uit:
        return (0.08)

    if (rneto > 5 * uit and rneto <= 20 * uit):
        return (0.14)

    if (rneto > 20 * uit and rneto <= 35 * uit):
        return (0.17)

    if (rneto > 35 * uit and rneto <= 45 * uit):
        return (0.2)

    if (rneto > 45 * uit):
        return (0.3)


def ret_mes(m, anual):
    if (m >= 1 and m <= 3):
        return (anual / 12)

    if (m == 3):
        ret = int(input("Ingrese retención de los meses enero, febrero y marzo: "))
        return ((anual - ret) / 9)

    if (m >= 4 and m <= 7):
        ret = int(input("Ingrese retención de los meses entre enero y abril: "))
        return ((anual - ret / 8))

    if (m == 8):
        ret = int(input("Ingrese retención de enero a julio: "))
        return ((anual - ret) / 5)

    if (m >= 9 and m <= 11):
        ret = int(input("Ingrese retención de enero a agosto: "))
        return ((anual - ret) / 4)

    if (m == 12):
        ret = int(input("Ingrese retención de enero a noviembre: "))
        return ((anual - ret))


x = datetime.datetime.now()
mes = int(x.strftime("%m"))

username = input("Ingrese su nombre de usuario: ")

rem_mes = int(input("Ingrese su remuneración mensual: "))
n_mes = 12 - mes + 1
print(n_mes)
grati = int(input("Ingrese el monto de remuneración ordinaria: "))
UIT = int(input("Ingrese el valor de la UIT: "))

rem_brut = ((rem_mes * n_mes) + grati)
rem_neto = (rem_brut - (7 * UIT))
print("Su remuneración bruta asciende a :", rem_brut)
print("Su remuneración neta asciende a :", rem_neto)

t = tasa(rem_neto, UIT)
print("La tasa impositiva es de: ", t)

impuesto_anual = rem_neto * t
print("El impuesto anual calculado tiene un valor de: ", impuesto_anual)

retencion = ret_mes(mes, impuesto_anual)
print("La retención para este mes es de : ", retencion)