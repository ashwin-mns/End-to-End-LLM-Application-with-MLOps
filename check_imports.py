print("Importing numpy...")
try:
    import numpy
    print("numpy ok")
except Exception as e:
    print(f"numpy failed: {e}")

print("Importing torch...")
try:
    import torch
    print("torch ok")
except Exception as e:
    print(f"torch failed: {e}")

print("Importing transformers...")
try:
    import transformers
    print("transformers ok")
except Exception as e:
    print(f"transformers failed: {e}")
