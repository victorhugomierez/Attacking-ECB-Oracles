from Crypto.Cipher import AES
import binascii

# Configuración
BLOCK_SIZE = 16
key = b'superpassword123'  # clave de ejemplo, debe ser de 16 bytes

# Leer la imagen
with open("test.bmp", "rb") as f:
    data = f.read()

# Padding para que sea múltiplo de 16
pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
data += bytes([pad_len]) * pad_len

# Cifrado ECB
cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(data)

# Guardar resultado
with open("test_ecb.bmp", "wb") as f:
    f.write(encrypted)

print("Imagen cifrada guardada como test_ecb.bmp")
