import unittest
from unittest.mock import patch, mock_open  # Import mock_open

# Function to count lines in a file
def count_lines(file_path):
    with open(file_path, 'r') as _file:
        file_content_list = _file.readlines()
        return len(file_content_list)

# Test Case
class TestReadFiles(unittest.TestCase):
    def test_count_lines(self):
        # Mock file content
        file_content_mock = """Hello World!!
Hello World is in a file.
A mocked file.
He is not real.
But he thinks he is.
He doesn't know he is mocked."""

        fake_file_path = 'file/path/mock'

        # Correct patching of built-in open()
        with patch('builtins.open', new=mock_open(read_data=file_content_mock)) as _file:
            actual = count_lines(fake_file_path)  # Direct function call
            _file.assert_called_once_with(fake_file_path, 'r')

        # Expected number of lines
        expected = len(file_content_mock.split('\n'))
        self.assertEqual(expected, actual)

# Run the tests
if __name__ == '__main__':
    unittest.main()
