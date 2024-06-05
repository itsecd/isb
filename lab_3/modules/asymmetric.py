from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class Asymmetric:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generating_key_pair(self)->tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """
        Генерация пары ключей для алгоритма асимметричного шифрования.    
        """
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.private_key = keys
        self.public_key = keys.public_key()
        return (self.private_key, self.public_key)

    def serialization_public_key(self, path: str)->None:
        """
        Преобразование открытого ключа в файл в формате PEM.

        Params:
        path (str): Путь к файлу, в который будет записан открытый ключ.
        """
        with open(path, 'wb') as public_out:
            public_out.write(self.public_key.public_bytes(encoding=serialization.Encoding.PEM,
             format=serialization.PublicFormat.SubjectPublicKeyInfo))
            
    def serialization_private_key(self, path: str)->None:
        """
        Преобразуйте закрытый ключ в файл в формате PEM без шифрования.

        Params:
        path (str): Путь к файлу, в который будет записан закрытый ключ.
        """
        with open(path, 'wb') as private_out:
            private_out.write(self.private_key.private_bytes(encoding=serialization.Encoding.PEM,
              format=serialization.PrivateFormat.TraditionalOpenSSL,
              encryption_algorithm=serialization.NoEncryption()))
            
    def deserialization_public_key(self, path: str):
        """
        Десериализация открытого ключа из файла в формате PEM.

        Params:
        path (str): Путь к файлу, содержащему открытый ключ.
        """
        with open(path, 'rb') as pem_in:
            public_bytes = pem_in.read()
            self.public_key = load_pem_public_key(public_bytes)
        return self.public_key        
        
    def deserialization_private_key(self, path: str):
        """
        Десериализация закрытого ключа из файла в формате PEM без шифрования.

        Params:
        path (str): Путь к файлу, содержащему закрытый ключ.
        """
        with open(path, 'rb') as pem_in:
            private_bytes = pem_in.read()
            self.private_key = load_pem_private_key(private_bytes,password=None,)
        return self.private_key

    def encrypt_symmetric_key(self, key: bytes, path_to_public_key: str)->bytes:
        """
        Зашифруйте данный текст с помощью открытого ключа.

        Params:
        key (bytes): Ключ, который должен быть зашифрован.
        path_to_public_key (str): Путь к файлу открытого ключа.

        Returns:
        bytes: Зашифрованный ключ шифра.
        """
        public_key = self.deserialization_public_key(path_to_public_key)
        return public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), 
                                                    algorithm=hashes.SHA256(), label=None))       
    
    def decryption_symmetric_key(self, esymmetric_key: bytes, path_to_private_key: str)->str:
        """
        Расшифровка данного зашифрованного текста, с использованием закрытого ключа.

        Params:
        key (bytes): Зашифрованный ключ шифра.
        path_to_private_key (str): Путь к файлу закрытого ключа.

        Returns:
        str: Расшифрованный открытый текст.
        """
        private_key = self.deserialization_private_key(path_to_private_key)
        return private_key.decrypt(esymmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), 
                                                     algorithm=hashes.SHA256(), label=None))