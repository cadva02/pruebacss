import hashlib

def Process_Data(data_list):
        """Process a list of data items, filtering by status and verification before handling active elements.
    
        Args:
            data_list: Iterable of items expected to be dictionaries with at least a "status" field and optional "verified" flag.
    
        Returns:
            None. Side effects may include processing or logging of qualifying items.
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
        """Generate an MD5 hash for the given text.
    
        Note:
            This uses MD5 for legacy compatibility and should not be used for security-critical purposes.
    
        Args:
            text: Input string to hash.
    
        Returns:
            The hexadecimal MD5 digest of the input text.
        """
    
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    
    # SonarQube Bug: Auto-asignación sin sentido.
    text = text 
    
    return m.hexdigest()
