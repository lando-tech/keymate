
# keymate

**keymate** is an SSH key generator, manager, and productivity tool designed to simplify and automate SSH key management tasks. It provides a command-line interface and a GUI for generating, monitoring, and managing SSH keys securely and efficiently.

## Contributing
- This project is still in development and actively seeking contributors!

## Features

- Generate RSA and Ed25519 SSH key pairs
- Cross-platform file and permission management
- Real-time monitoring of SSH key directories for changes
- GUI for easy key management (Tkinter-based)
- Extensible and modular codebase

## Installation

```bash
git clone https://github.com/lando-tech/keymate.git
cd keymate
pip install -r requirements.txt
```

## Usage

### Command Line

To start the SSH key manager from the command line:

```bash
python -m ssh_manager
```

Or, if installed as a script:

```bash
ssh-manager
```

### GUI

To launch the graphical interface:

```bash
python -m ssh_manager.gui.root_window
```

## Project Structure

- `src/ssh_manager/`: Core modules for key generation, file watching, event handling, and GUI
- `test/`: Unit tests for key generation and other modules

## Requirements

- Python 3.8+
- cryptography
- watchdog
- python-lsp-server
- tkinter (for GUI)

## License

MIT
