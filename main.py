def validar (numero):
    if len(numero) != nDigitos:
        print("El número debe tener %s dígitos" % nDigitos)


def divide_I(numero):
    return numero


def divide_D(numero):
    return numero


def DyV(A, B, n):
    return 2


def productoDyV(A, B, n):
    if n == 1:
        print(A * B)
    else:
        iA = divide_I(A)
        dA = divide_D(A)
        iB = divide_I(B)
        dB = divide_D(B)

        p1 = DyV(iA, iB, n/2)
        p2 = DyV(iA, dB, n/2)
        p3 = DyV(dA, iB, n/2)
        p4 = DyV(dA, dB, n/2)

        r = pow(10, n)*p1 + pow(10,  n/2)*p2 + pow(10, n/2)*p3 + p4
        return r



# Main
print("\nMultiplicación de dos números con dígitos de 2^n usando el método de divide y vencerás")

print("\nIntroduzca el valor de n:")
n = input()
n = int(n)
nDigitos = pow(2, n)

numeroA = ""
numeroB = ""

while(len(numeroA) != nDigitos):
    print("\nIngresa el primer número de %s dígitos:" % nDigitos)
    numeroA = input()
    validar(numeroA)

while(len(numeroB) != nDigitos):
    print("\nIngresa el segundo número de %s dígitos:" % nDigitos)
    numeroB = input()
    validar(numeroB)

# Dividir y vencer
resultado = productoDyV(numeroA, numeroB, nDigitos)
print(resultado)
