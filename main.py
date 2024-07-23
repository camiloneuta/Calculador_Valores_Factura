print("====================")
print("")
print("CONSECUTIVO REMISION")
print("")
print("====================")

valor_base = input("Ingrese el valor base del servicio: ")
valor_iva = float(input("Ingrese el valor del IVA del servicio: "))

valor_base = int(valor_base)
valor_iva = int(valor_iva)

valor_aiu = valor_iva / 0.19
valor_aiu = int(valor_aiu)
valor_total = valor_base + valor_iva

print(f"El valor total de la factura es: {valor_total}")
print("")
print("====================")
print(f"Los valores a facturar son:\n"
      f"Servicio de carga: {valor_base - valor_aiu}\n"
      f"Valor AIU: {valor_aiu}\n "
      f"Valor IVA: {valor_iva}")
print("====================")
