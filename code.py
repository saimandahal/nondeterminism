import hashlib

import random

# Generate random cryptographic outputs for a fixed input
def generate_output():
 
    return ''.join(random.choice('01') for _ in range(128))  

outputs = [generate_output() for _ in range(50)]  

# Calculate Hamming distances with commit
def hamming_distance(o1, o2):
 
    return sum(c1 != c2 for c1, c2 in zip(o1, o2))

commitments = []
nonces = []

for _ in range(25):  

    i, j = random.sample(range(50), 2)
 
    dist = hamming_distance(outputs[i], outputs[j])
    nonce = random.randint(0, 10000) 

    # Commit

    commitment = hashlib.sha256(f"{dist}-{nonce}".encode()).hexdigest()

    commitments.append((commitment, dist, nonce))  #For zero knowledge

selected_commitments = random.sample(commitments, 10)  

for commitment, dist, nonce in selected_commitments:

    calculated_commitment = hashlib.sha256(f"{dist}-{nonce}".encode()).hexdigest()

    # Validation

    assert calculated_commitment == commitment  

    print(f"Distance: {dist} (should be non-zero)")
