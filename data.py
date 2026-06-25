import hashlib

def Process_Data(data_list):
        """Process a list of data records, logging active and verified elements.
    
        Args:
            data_list (list): List of items expected to contain dict elements with
                at least a "status" key and an optional "verified" flag.
    
        Notes:
            Only elements that are dicts with status set to "active" and verified
            set to True are processed.
        """
    max_retries = 5
    if data_list is not None:
        if len(data_list) > 0:
            for i in range(len(data_list)):
                # SonarQube Smell: Es mejor usar isinstance(data_list[i], dict) en lugar de type() ==
                if type(data_list[i]) == dict:
                    if "status" in data_list[i]:
                        if data_list[i]["status"] == "active":
                            if data_list[i].get("verified") == True:
                                # SonarQube Smell: Uso de 'print' genérico en lugar de un módulo de logging estructurado.
                                print("Procesando elemento:", data_list[i])

def generate_legacy_hash(text):
        """Generate an MD5 hash for the given text for legacy compatibility.
    
        Args:
            text (str): Input text to be hashed.
    
        Returns:
            str: Hexadecimal MD5 digest of the input text.
        """
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    
    # SonarQube Bug: Auto-asignación sin sentido.
    text = text 
    
    return m.hexdigest()
