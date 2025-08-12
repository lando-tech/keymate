"""
Generate private/public key pairs
"""

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


KEY_SIZES = [2048, 3072, 4096]


class KeyGen:
    """
    A utility class for generating and managing SSH key pairs.

    This class provides methods to generate RSA and Ed25519 key pairs,
    serialize them in OpenSSH format, and save them to files.
    """

    #
    # def __init__(self):
    #     """
    #     Initialize a new KeyGen instance.
    #
    #     This constructor currently performs no initialization as the class
    #     uses static methods for key generation operations.
    #     """
    #     pass

    def generate_rsa_keypair(self, key_size: int = KEY_SIZES[2]) -> tuple[bytes, bytes]:
        """
        Generate an RSA key pair with the specified key size.

        Args:
            key_size (int): The size of the RSA key in bits. Common values are
                           2048, 3072, or 4096 bits.

        Returns:
            tuple[bytes, bytes]: A tuple containing (private_key_bytes, public_key_bytes)
                                in OpenSSH format.

        Raises:
            ValueError: If the key_size is invalid or not supported.
        """
        self.verify_key_size(key_size)
        private_key: RSAPrivateKey = rsa.generate_private_key(
            public_exponent=65537, key_size=key_size, backend=default_backend()
        )
        private_bytes, public_bytes = self.serialize_rsa(private_key)
        return private_bytes, public_bytes

    def generate_ed25519_keypair(self) -> tuple[bytes, bytes]:
        """
        Generate an Ed25519 key pair.

        Ed25519 is a modern elliptic curve signature scheme that provides
        better security and performance than RSA with a fixed key size of 256 bits.

        Returns:
            tuple[bytes, bytes]: A tuple containing (private_key_bytes, public_key_bytes)
                                in OpenSSH format.
        """
        private_key: Ed25519PrivateKey = ed25519.Ed25519PrivateKey.generate()
        private_bytes, public_bytes = self.serialize_ed25519(private_key)
        return private_bytes, public_bytes

    def generate_rsa_keypair_with_passphrase(
        self, key_size: int, passphrase: str
    ) -> tuple[bytes, bytes]:
        """
        Generate an RSA key pair with the specified key size and encrypt it with a passphrase.

        Args:
            key_size (int): The size of the RSA key in bits. Common values are
                           2048, 3072, or 4096 bits.
            passphrase (str): The passphrase to encrypt the private key with.

        Returns:
            tuple[bytes, bytes]: A tuple containing (private_key_bytes, public_key_bytes)
                                in OpenSSH format, with the private key encrypted.

        Raises:
            ValueError: If the key_size is invalid or not supported.
        """
        self.verify_key_size(key_size)
        private_key: RSAPrivateKey = rsa.generate_private_key(
            public_exponent=65537, key_size=key_size, backend=default_backend()
        )
        private_bytes, public_bytes = self.serialize_rsa_with_passphrase(
            private_key, passphrase
        )
        return private_bytes, public_bytes

    def generate_ed25519_keypair_with_passphrase(
        self, passphrase: str
    ) -> tuple[bytes, bytes]:
        """
        Generate an Ed25519 key pair and encrypt it with a passphrase.

        Ed25519 is a modern elliptic curve signature scheme that provides
        better security and performance than RSA with a fixed key size of 256 bits.

        Args:
            passphrase (str): The passphrase to encrypt the private key with.

        Returns:
            tuple[bytes, bytes]: A tuple containing (private_key_bytes, public_key_bytes)
                                in OpenSSH format, with the private key encrypted.
        """
        private_key: Ed25519PrivateKey = ed25519.Ed25519PrivateKey.generate()
        private_bytes, public_bytes = self.serialize_ed25519_with_passphrase(
            private_key, passphrase
        )
        return private_bytes, public_bytes

    @staticmethod
    def serialize_rsa(private_key: RSAPrivateKey):
        """
        Serialize an RSA private key and its corresponding public key to OpenSSH format.

        Args:
            private_key (RSAPrivateKey): The RSA private key object to serialize.

        Returns:
            tuple[bytes, bytes]: A tuple containing (private_key_bytes, public_key_bytes)
                                serialized in OpenSSH PEM and OpenSSH formats respectively.
        """
        private_bytes: bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption(),
        )
        public_bytes: bytes = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH,
        )
        return private_bytes, public_bytes

    @staticmethod
    def serialize_rsa_with_passphrase(
        private_key: RSAPrivateKey, passphrase: str
    ) -> tuple[bytes, bytes]:
        """
        Serialize an RSA private key with passphrase encryption and
        its corresponding public key to OpenSSH format.

        Args:
            private_key (RSAPrivateKey): The RSA private key object to serialize.
            passphrase (str): The passphrase to encrypt the private key with.

        Returns:
            tuple[bytes, bytes]: A tuple containing (private_key_bytes, public_key_bytes)
                                serialized in OpenSSH PEM and OpenSSH formats respectively,
                                with the private key encrypted using the passphrase.
        """
        private_bytes: bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.BestAvailableEncryption(
                passphrase.encode()
            ),
        )
        public_bytes: bytes = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH,
        )
        return private_bytes, public_bytes

    @staticmethod
    def serialize_ed25519(private_key: Ed25519PrivateKey) -> tuple[bytes, bytes]:
        """
        Serialize an Ed25519 private key and its corresponding public key to OpenSSH format.

        Args:
            private_key (Ed25519PrivateKey): The Ed25519 private key object to serialize.

        Returns:
            tuple[bytes, bytes]: A tuple containing (private_key_bytes, public_key_bytes)
                                serialized in OpenSSH PEM and OpenSSH formats respectively.
        """
        private_bytes: bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.NoEncryption(),
        )
        public_bytes: bytes = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH,
        )
        return private_bytes, public_bytes

    @staticmethod
    def serialize_ed25519_with_passphrase(
        private_key: Ed25519PrivateKey, passphrase: str
    ) -> tuple[bytes, bytes]:
        """
        Serialize an Ed25519 private key with passphrase encryption and
        its corresponding public key to OpenSSH format.

        Args:
            private_key (Ed25519PrivateKey): The Ed25519 private key object to serialize.
            passphrase (str): The passphrase to encrypt the private key with.

        Returns:
            tuple[bytes, bytes]: A tuple containing (private_key_bytes, public_key_bytes)
                                serialized in OpenSSH PEM and OpenSSH formats respectively,
                                with the private key encrypted using the passphrase.
        """
        private_bytes: bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.OpenSSH,
            encryption_algorithm=serialization.BestAvailableEncryption(
                passphrase.encode()
            ),
        )
        public_bytes: bytes = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH,
        )
        return private_bytes, public_bytes

    @staticmethod
    def verify_key_size(key_size: int) -> bool:
        """
        Verify the key size for RSA generated keys.
        Compares the provided key size with the constant 'KEY_SIZES'.

        Args:
            key_size (int): The key size to verify.

        Returns:
            bool: If the key size is allowed and supported

        Raises:
            ValueError: If the key size is not allowed or unsupported

        """
        err_msg = f"Key size not allowed: {key_size}. Please use one of the following: {KEY_SIZES}"
        for i in KEY_SIZES:
            if i == key_size:
                return True
        raise ValueError(err_msg)

    @staticmethod
    def save_keypair(file_path: str, private_bytes: bytes, public_bytes: bytes):
        """
        Save a key pair to files on disk.

        The private key is saved to the specified file path, and the public key
        is saved to the same path with a '.pub' extension.

        Args:
            file_path (str): The file path where the private key will be saved.
                           The public key will be saved as file_path + '.pub'.
            private_bytes (bytes): The serialized private key data.
            public_bytes (bytes): The serialized public key data.

        Raises:
            IOError: If there's an error writing the files to disk.

        Example:
            >>> key_gen = KeyGen()
            >>> priv_key, pub_key = key_gen.generate_rsa_keypair(2048)
            >>> key_gen.save_keypair("my_key", priv_key, pub_key)
            # Creates files: my_key (private) and my_key.pub (public)
        """
        try:
            with open(file_path, "wb") as private_file:
                private_file.write(private_bytes)
            with open(file_path + ".pub", "wb") as public_file:
                public_file.write(public_bytes)
        except IOError as io_err:
            print(f"Failed to save SSH key pair. Original error: {io_err}")

    @staticmethod
    def save_keypair_with_comment(
        file_path: str, private_bytes: bytes, public_bytes: bytes, comment: bytes
    ):
        """
        Save a key pair to files on disk with a comment added to the public key.

        The private key is saved to the specified file path, and the public key
        is saved to the same path with a '.pub' extension, including the comment.

        Args:
            file_path (str): The file path where the private key will be saved.
                           The public key will be saved as file_path + '.pub'.
            private_bytes (bytes): The serialized private key data.
            public_bytes (bytes): The serialized public key data.
            comment (bytes): The comment to append to the public key file.

        Raises:
            IOError: If there's an error writing the files to disk.

        Example:
            >>> key_gen = KeyGen()
            >>> priv_key, pub_key = key_gen.generate_rsa_keypair(2048)
            >>> comment = b"user@hostname"
            >>> key_gen.save_keypair_with_comment("my_key", priv_key, pub_key, comment)
            # Creates files: my_key (private) and my_key.pub (public with comment)
        """
        try:
            with open(file_path, "wb") as private_file:
                private_file.write(private_bytes)
            with open(file_path + ".pub", "wb") as public_file:
                public_file.write(public_bytes + b" " + comment)
        except IOError as io_err:
            print(f"Failed to save SSH key pair. Original error: {io_err}")
