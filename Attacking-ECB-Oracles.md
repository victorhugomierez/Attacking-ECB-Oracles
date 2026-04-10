# Encryption and ECB Weakness
Encryption is designed to protect data both at rest (stored) and in transit (transmitted). However, if implemented incorrectly, it can introduce serious vulnerabilities. One common mistake is relying on legacy cipher modes such as Electronic Codebook (ECB).

- Why ECB is insecure
Pattern leakage: ECB encrypts identical plaintext blocks into identical ciphertext blocks. This means patterns in the data remain visible after encryption.

No randomness: Unlike modern modes (CBC, GCM), ECB does not use an initialization vector (IV), so it fails to provide semantic security.

### Example
Imagine encrypting an image with ECB:

- Original image: a bitmap of a penguin.

- Encrypted with ECB: the outline of the penguin is still visible in the ciphertext image because repeating blocks produce repeating ciphertext.

Encrypted with CBC or GCM: the image becomes completely scrambled, hiding all patterns.

 Practical exploitation
Detecting ECB: If ciphertext shows repeating blocks, it’s a sign ECB is in use.

- Attack scenario: An attacker could infer structure or sensitive information (like repeated headers, predictable fields in a database) even without decrypting.

Mitigation: Always use modern, authenticated modes such as AES‑GCM or ChaCha20‑Poly1305.

- Key takeaway: Encryption is only as strong as its implementation. Using insecure modes like ECB can expose patterns and allow attackers to exploit data, even if they don’t know the key.

## Cryptography Basics
Encryption relies on two main components:

Key → a secret value used to encrypt/decrypt data.

Cipher algorithm → the mathematical process that transforms plaintext into ciphertext.

A common confusion is between encoding and encryption:

Encoding: transforms data into another format (e.g., Base64) without a key.

Encryption: transforms data using both an algorithm and a key, ensuring confidentiality.

### Example: ROT13
ROT13 uses a rotation algorithm with a “key” of 13.

It technically qualifies as encryption, but it’s extremely weak since anyone can reverse it easily.

This highlights why relying on secret algorithms (instead of strong keys) is insecure.

- Historical Context
Before 1997, many systems relied on keeping algorithms secret.

NIST organized a competition to create a mathematically secure algorithm where only the key mattered.

Out of this, AES (Advanced Encryption Standard) was born, created by Vincent Rijmen and Joan Daemen.

AES is now the global standard, used in countless applications.

### Core Principles of Secure Encryption

Confusion → obscure the relationship between plaintext and ciphertext.
- Example: AES substitution-permutation networks make it hard to trace input-output relations.

Diffusion → spread out plaintext influence across ciphertext.
- Example: a single bit change in plaintext alters many bits in ciphertext.

Key-only reliance → security depends solely on the secrecy of the key, not the algorithm.
- Example: AES is public, but without the key, ciphertext cannot be decrypted.

### Symmetric vs Asymmetric

Symmetric encryption: same key for encryption and decryption.
- Example: AES — fast and efficient, but requires secure key sharing.

Asymmetric encryption: uses public/private key pairs.
- Example: RSA — slower, but solves the key distribution problem.

#### Key takeaway: Modern cryptography is secure only when it follows the principles of confusion, diffusion, and key-only reliance. AES embodies these principles, but insecure implementations (like ECB mode) can still break confidentiality.

![Cryptography Basics](assets/cryptography-basics.png)


- AES as a Building Block
AES is a secure encryption algorithm, but it should not be used “as is”. Instead, it serves as a building block inside larger symmetric encryption schemes. If those blocks are combined incorrectly, vulnerabilities can arise even though AES itself is mathematically sound.

- Example of insecure use
AES in ECB mode: encrypts identical plaintext blocks into identical ciphertext blocks, leaking patterns.

- AES without authentication: if used only for confidentiality, attackers can manipulate ciphertext (bit flipping) without detection.

- Example of secure use
AES‑GCM: combines AES with Galois/Counter Mode, providing both confidentiality and integrity.

AES‑CBC with HMAC: adds authentication to prevent tampering.

- Key takeaway: AES is strong, but its security depends on how it’s implemented. Using it in insecure modes or without proper authentication can expose systems to attacks.

