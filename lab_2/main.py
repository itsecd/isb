import file_handler
from NIST_TESTS import NistTests


if __name__ == "__main__":
    test_c = NistTests(file_handler.read_json("sequence.json")["cpp_sequence"])
    test_java = NistTests(file_handler.read_json("sequence.json")["java_sequence"])
    print(test_c)
    print(test_java)