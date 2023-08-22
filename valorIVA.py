# Función para calcular el valor del IVA
def calcular_iva(subtotal, tasa_iva):
    iva = subtotal * (tasa_iva / 100)
    return iva

# Función principal del programa
def main():
    print("Valor de Compra con IVA")
    precio1 = float(input("Ingrese el precio de su primera compra: $ "))
    precio2 = float(input("Ingrese el precio de su segunda compra: $ "))
    
    subtotal = precio1 + precio2
    # Tasa de IVA fija al 12%
    tasa_iva = 12

    iva = calcular_iva(subtotal, tasa_iva)
    total = subtotal + iva

    print(f"Subtotal: ${subtotal}")
    print(f"IVA ({tasa_iva}%): ${iva}")
    print(f"Total a pagar: ${total}")

if __name__ == "__main__":
    main()