import random
import string

def generar_contraseña():
    """Genera una contraseña de 20 caracteres: 5 números, 5 caracteres especiales y 10 letras mayúsculas."""
    numeros = ''.join(random.choices(string.digits, k=5))  # 5 números
    especiales = ''.join(random.choices(string.punctuation, k=5))  # 5 caracteres especiales
    mayusculas = ''.join(random.choices(string.ascii_uppercase, k=10))  # 10 letras mayúsculas

    # Combina y mezcla los caracteres
    contraseña = list(numeros + especiales + mayusculas)
    random.shuffle(contraseña)  # Mezcla los caracteres
    return ''.join(contraseña)

if __name__ == "__main__":
    print("Generador de Contraseñas")
    try:
        contraseña = generar_contraseña()
        print(f"Tu contraseña generada es: {contraseña}")
    except ValueError as e:
        print(f"Error: {e}")