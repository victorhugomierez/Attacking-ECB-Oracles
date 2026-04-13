from bs4 import BeautifulSoup
import requests

# =========================
# CONFIG
# =========================
URL = "http://Machine_ip:5000/oracle"   # Ajusta la IP de tu servidor Flask
# =========================
# ORACLE INTERFACE
# =========================
def chat_to_oracle(username):
    r = requests.post(URL, data={'username': username})
    soup = BeautifulSoup(r.text, 'html.parser')
    value = soup.find(id='encrypted-result').find('strong').text
    return value
# =========================
# BLOCK SIZE DETECTION
# =========================
def calculate_block_size():
    base_len = len(chat_to_oracle("A"))
    i = 1
    while True:
        new_len = len(chat_to_oracle("A" * i))
        if new_len > base_len:
            block_size = new_len - base_len
            print("[+] Block size detected:", block_size)
            return block_size
        i += 1
# =========================
# SPLIT CIPHERTEXT
# =========================
def split_ciphertext(ciphertext, block_size):
    block_size *= 2  # hex encoding
    return [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
# =========================
# OFFSET DETECTION
# =========================
def calculate_offset(block_size):
    payload = "A" * (block_size * 2)
    ct = chat_to_oracle(payload)
    chunks = split_ciphertext(ct, block_size)
    if len(chunks) != len(set(chunks)):
        print("[+] No offset detected")
        return 0
    offset = 0
    while True:
        offset += 1
        payload = "B" + payload
        ct = chat_to_oracle(payload)
        chunks = split_ciphertext(ct, block_size)
        if len(chunks) != len(set(chunks)):
            print("[+] Offset detected:", offset)
            return offset
# =========================
# FULL SECRET EXTRACTION
# =========================
def extract_secret(block_size, offset):
    known = ""
    print("\n[+] Starting full secret extraction...\n")
    while True:
        # Calcular padding dinámico
        pad_len = block_size - 1 - (len(known) % block_size)
        reference_input = "B" * offset + "A" * pad_len
        ct = chat_to_oracle(reference_input)
        chunks = split_ciphertext(ct, block_size)
        block_index = 1 + (len(known) // block_size)
        reference_chunk = chunks[block_index]

        found = False
        # Probar todo el rango ASCII imprimible
        for c in range(32, 127):
            guess = chr(c)
            test_input = reference_input + known + guess
            test_ct = chat_to_oracle(test_input)
            test_chunks = split_ciphertext(test_ct, block_size)
            if test_chunks[block_index] == reference_chunk:
                known += guess
                print(f"[✓] Found byte: {guess}")
                print(f"[✓] Secret so far: {known}\n")
                found = True
                break
        if not found:
            print("[!] No matching byte found — end of secret.")
            break
    return known
# =========================
# MAIN
# =========================
if __name__ == "__main__":
    print("[*] Testing oracle...")
    print(chat_to_oracle("test"))

    print("\n[*] Detecting block size...")
    block_size = calculate_block_size()

    print("\n[*] Detecting offset...")
    offset = calculate_offset(block_size)

    secret = extract_secret(block_size, offset)
    print("\n==============================")
    print("[FINAL SECRET]")
    print(secret)
    print("==============================")
