nombre = str(input("Ingrese su nombre: "))
print ("")
placa = str(input("Ingrese su placa del vehículo: "))
print ("")
valor_P = int(input("Ingrese el valor total por concepto de pasajes: "))
print ("")
valor_E = int(input("Ingrese el valor total por concepto de encomiendas: "))
print ("")
liquidacion_p = valor_P * 0.25
liquidacion_E = valor_E * 0.15
Valor_a_Pagar = liquidacion_E + liquidacion_p
print ("Su nombre es: ", (nombre))
print ("")
print ("Su placa es: ", (placa))
print ("")
print (f"El valor total de los pasajes es:  {valor_P:,.0f} ")
print ("")
print (f"El valor total a pagar por concepto de encomiendas es:  {liquidacion_E:,.0f}")
print ("")
print (f"El valor total a pagar por concepto de pasajes es:  {liquidacion_p:,.0f}")
print ("")
print (f"El valor total a pagar al conductor es:  {Valor_a_Pagar:,.0f}")