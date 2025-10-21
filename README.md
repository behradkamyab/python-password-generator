# 🔐 Python Password Generator

A flexible command-line and Streamlit web-based tool that generates secure passwords in three different styles: numeric PINs, cryptographically strong random passwords, and human-memorable word-based passwords.

## 🌟 Features

- **PIN Generator**: Creates numeric-only passwords (e.g., `739284`)
- **Random Password Generator**: Mixes uppercase, lowercase, digits, and symbols (e.g., `K9#mQ!vL2@`)
- **Memorable Password Generator**: Combines real dictionary words with separators (e.g., `apple-tree-moon-rocket`)
- **Web Interface**: Interactive UI built with Streamlit for easy password generation in the browser
- **CLI Support**: Also works as a command-line tool for terminal users
- All generators include input validation and customizable parameters

## 📦 Requirements

- **Python 3.6+**
- **Dependencies** (listed in `requirements.txt`):
  - `nltk` — for the memorable password word list
  - `streamlit` — for the web-based user interface

### 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/behradkamyab/python-password-generator.git
   cd python-password-generator
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Download the NLTK words corpus (one-time setup)**
   ```bash
   python -c "import nltk; nltk.download('words')"
   ```

▶️ Usage
Option 1: Web Interface (Recommended)
Run the Streamlit app to use the graphical interface:

```Bash
streamlit run main.py
```

This will open a browser window where you can select password types and customize options interactively.

Option 2: Command-Line Interface
Run the script in terminal mode:

```Bash
python main.py
```

The program will guide you through selecting a password type and customizing its properties (length, inclusion of numbers/symbols, capitalization, etc.).
