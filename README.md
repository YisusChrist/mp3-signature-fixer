This Python script is a utility for working with MP3 files. It allows you to visualize the hexdump of an MP3 file, check if it contains the MP3 file signature, add the signature if missing, and save the modified file. The script uses the Tkinter library for a simple GUI file selection interface.

Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contributions](#contributions)

# Features

- Visualize the hexdump of an MP3 file.
- Check if an MP3 file contains the ID3 signature.
- Add the ID3 signature to an MP3 file if missing.
- Save the modified MP3 file.

# Requirements

Python 3.x
Required Python packages: `hexdump`, `rich`

# Usage

1. **Run the Script**:

```sh
python mp3-test.py
```

2. **Select an MP3 File**:

   A file dialog will prompt you to select an MP3 file.

3. **View Hexdump**:

   The script will display the hexdump of the selected MP3 file.

4. **Check for MP3 Signature**:

   The script will determine if the selected file already contains the MP3 signature.

5. **Add MP3 Signature (Optional)**:

   If the file lacks the MP3 signature, the script will add it.

6. **Save Modified MP3 File (Optional)**:

   You can choose to save the modified file with the added MP3 signature.

# Example

```sh
poetry run python mp3-signature-fixer.py
```

# License

This script is licensed under the [GNU General Public License v3.0](https://opensource.org/licenses/GPL-3.0).

# Acknowledgments

The script utilizes the [hexdump](https://pypi.org/project/hexdump) and [rich](https://github.com/Textualize/rich) Python libraries.
Inspired by the ID3v2 container specification: https://en.wikipedia.org/wiki/MP3#File_structure.

# Contributions

Contributions are welcome! Feel free to open issues or pull requests.
