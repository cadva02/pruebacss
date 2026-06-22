import hashlib

# SonarQube Smell: El nombre de la función debería ser snake_case (process_data), no PascalCase.
def Process_Data(data_list):
    # SonarQube Smell: Variable declarada pero nunca utilizada.
    max_retries = 5
    
    # SonarQube Smell: Complejidad Cognitiva muy alta ("Pyramid of Doom").
    # Demasiados if anidados dificultan la lectura.
    if data_list is not None:
        if len(data_list) > 0:
            for i in range(len(data_list)):
                # SonarQube Smell: Es mejor usar isinstance(data_list[i], dict) en lugar de type() ==
                if type(data_list[i]) == dict:
                    if "status" in data_list[i]:
                        if data_list[i]["status"] == "active":
                            
                            # SonarQube Smell: Comprobación booleana redundante. 
                            # Debería ser simplemente 'if data_list[i].get("verified"):'.
                            if data_list[i].get("verified") == True:
                                # SonarQube Smell: Uso de 'print' genérico en lugar de un módulo de logging estructurado.
                                print("Procesando elemento:", data_list[i])

def generate_legacy_hash(text):
    # SonarQube Vulnerability / Security Hotspot: Uso de MD5. 
    # Es un algoritmo criptográfico débil y obsoleto, vulnerable a colisiones.
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    
    # SonarQube Bug: Auto-asignación sin sentido.
    text = text 
    
    return m.hexdigest()
