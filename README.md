# 📘 Attacking-ECB-Oracles

## Overview
This repository documents experiments and notes on **ECB oracle attacks**.  
It demonstrates how to:
- Identify the **block size** of the cipher.
- Calculate the **offset** when secrets are prepended/appended.
- Align chosen plaintext to fully control a block.
- Brute‑force unknown bytes of the secret using controlled input.

The project is designed as a **learning lab** for cryptanalysis and portfolio documentation.

---

## 📂 Repository Structure
| Path | Description |
|------|-------------|
| `script/` | Python scripts implementing ECB oracle attack logic (`ecb-script.py`, `ecb-script2.py`). |
| `assets/` | Supporting files including screenshots (`error.png`) and demo video (`test.mp4`). |
| `test/`   | Example tests showing ECB behaviour (each block encrypted independently). |
| `Attacking-ECB-Oracles.md` | Detailed notes explaining block size discovery, offset alignment, and attack methodology. |

---

## ▶️ Demo Video
[![Demo Screenshot](assets/error.png)](assets/test.mp4)

Click the image above to watch the short demo video (`assets/test.mp4`).  
The screenshot (`assets/error.png`) serves as a preview thumbnail.

---

## 🔑 Key Concepts Demonstrated
- **Block Size Discovery:** Measure ciphertext growth to identify AES block size (16 bytes).  
- **Offset Calculation:** Prepend characters until two identical ciphertext blocks appear, revealing the offset.  
- **Controlled Block Injection:** Align input so that chosen plaintext fills an entire block.  
- **Byte‑by‑Byte Recovery:** Brute‑force the final byte of a controlled block to leak secret data.  

---

## 🚀 Usage
Clone the repository and run the scripts:

```bash
git clone https://github.com/victorhugomierez/Attacking-ECB-Oracles.git
cd Attacking-ECB-Oracles

python script/ecb-script.py
python script/ecb-script2.py





## Demo Video - Victorhugo

[![Demo Screenshot](assets/error.png)](assets/test.mp4)

- `assets/error.png` → imagen previa que se mostrará en el README.  
- `assets/test.mp4` → el vídeo que se abrirá al hacer clic.

