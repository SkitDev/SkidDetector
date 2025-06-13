[New_Projectisaidoooooooooohimblindedbythelights-removebg-preview](https://github.com/user-attachments/assets/80f022f3-ee82-4a36-b27c-666ecde0ab82)
# SkitDetector 🕵️‍♂️
An advanced AI-powered tool to detect potentially skidded code using Google's Gemini AI.

## Features

- 🔍 AI-powered code analysis
- 🎨 Beautiful CLI interface with rich formatting
- 📊 Detailed analysis reports
- 🔐 Secure API key management
- 🚀 Fast and efficient scanning

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your Google Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

3. Run the tool:
```bash
python skitdetector.py scan <file_or_directory>
```

## Usage

```bash
# Scan a single file
python skitdetector.py scan path/to/file.py

# Scan a directory
python skitdetector.py scan path/to/directory

# Get help
python skitdetector.py --help
```

## Requirements

- Python 3.8+
- Google Gemini API key
- Internet connection for AI analysis

## License

MIT License 
