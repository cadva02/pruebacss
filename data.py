import hashlib

def Process_Data(data_list):
        """Process a list of data items, printing information for active and verified entries.
    
        Args:
            data_list: Iterable of items expected to be dictionaries containing at least a "status" field
                and optionally a "verified" flag.
    
        Notes:
            Only items with status equal to "active" and a truthy "verified" field are processed.
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
        """Generate an MD5 hexadecimal hash string from the given text.
    
        Args:
            text: Input string to be hashed.
    
        Returns:
            The MD5 hash of the input text as a hexadecimal string.
    
        Warning:
            MD5 is considered cryptographically broken and should only be used for legacy or
            non-security-critical purposes.
        """
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    
    # SonarQube Bug: Auto-asignación sin sentido.
    text = text 
    
    return m.hexdigest()
