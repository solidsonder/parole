a = {
  "md5": {
    "Properties": "Generates a 128-bit hash value. Designed to ensure data integrity over the Internet. However, not considered secure due to fast and efficient collision attacks.",
    "Initialization Vector": "No initialization vector."
  },
  "md4": {
    "Properties": "Generates a 128-bit hash value. Predecessor of MD5 and is faster than MD5, but weaker in terms of security; contains serious cryptographic weaknesses.",
    "Initialization Vector": "No initialization vector."
  },
  "md2": {
    "Properties": "Generates a 128-bit hash value and designed for 8-bit microprocessors. Slower than MD4 and MD5, and not compliant with current security standards.",
    "Initialization Vector": "No initialization vector."
  },
  "sha1": {
    "Properties": "Generates a 160-bit hash value. Widely used for digital signatures and file integrity verification. However, vulnerable to collision attacks.",
    "Initialization Vector": "No initialization vector."
  },
  "sha224": {
    "Properties": "Part of the SHA-2 family and produces a 224-bit hash value. Based on SHA-256, but generates a shorter hash using different initial values.",
    "Initialization Vector": "No initialization vector."
  },
  "sha3224": {
    "Properties": "Part of the SHA-3 family and produces a 224-bit hash value. Although it produces hashes of the same length as SHA-2, it is based on a completely different design using the Keccak algorithm.",
    "Initialization Vector": "No initialization vector."
  },
  "sha256": {
    "Properties": "Part of the SHA-2 family and generates a 256-bit hash value. A strong general-purpose hash function widely used.",
    "Initialization Vector": "No initialization vector."
  },
  "sha3256": {
    "Properties": "Part of the SHA-3 family and generates a 256-bit hash value. Despite having the same length as SHA-256, its structure is completely different and provides different security guarantees.",
    "Initialization Vector": "No initialization vector."
  },
  "blake2s": {
    "Properties": "Part of the BLAKE2 family and can produce 256-bit or shorter hash values. One of the finalists of the SHA-3 competition and is faster than SHA-3.",
    "Initialization Vector": "No initialization vector."
  },
  "sha384": {
    "Properties": "Part of the SHA-2 family and produces a 384-bit hash value. Based on SHA-512, but with different initial values and a shorter output.",
    "Initialization Vector": "No initialization vector."
  },
  "sha3384": {
    "Properties": "Part of the SHA-3 family and produces a 384-bit hash value. Based on the Keccak algorithm, it has a structurally different design compared to SHA-2.",
    "Initialization Vector": "No initialization vector."
  },
  "sha512": {
    "Properties": "Part of the SHA-2 family and generates a 512-bit hash value. Used to verify the integrity of large files and data.",
    "Initialization Vector": "No initialization vector."
  },
  "sha3512": {
    "Properties": "Part of the SHA-3 family and generates a 512-bit hash value. Despite having the same length as SHA-512, it relies on a different security model based on the Keccak algorithm.",
    "Initialization Vector": "No initialization vector."
  },
  "blake2b": {
    "Properties": "Part of the BLAKE2 family and can produce hash values of configurable length, often used as 512-bit hashes. Faster than SHA-3 and offers various security features.",
    "Initialization Vector": "No initialization vector."
  },
  "whirlpool": {
    "Properties": "Produces a 512-bit hash.",
    "Initialization Vector": "No initialization vector."
  },
  "sha1(sha1_bin)": {
    "Properties": "Applies nested SHA1 hash operations to generate a hash value. First, the original SHA1 hash of the data is obtained. Then, this SHA1 hash value is subjected to SHA1_BIN operation to create a nested hash. This operation can be used to hash data more securely. However, it can be costly in terms of performance and is typically preferred for scenarios requiring extra security.",
    "Initialization Vector": "No initialization vector."
  }
}

def guidie():
  return a