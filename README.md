# keylogger
Sure, here's a sample `README.md` file for your keylogger project on GitHub:

```markdown
# Secure Keylogger

This project implements a keylogger application capable of recording keystrokes and mouse events generated by user interactions anywhere on the screen. The recorded data is securely stored in an encrypted log file.

## Features

- **Mouse Event Logging**: Records mouse movements, clicks, and scrolls.
- **Keyboard Event Logging**: Records key presses and releases.
- **Secure Logging**: Encrypts the log data using Fernet symmetric encryption.
- **Multiprocessing**: Efficiently manages the logging process using Python's multiprocessing module.

## Architecture

The project is structured into three main modules:

1. **main.py**: Initializes and starts the mouse and keyboard listeners and manages the multiprocessing.
2. **events_tracker.py**: Contains the event handling functions for mouse and keyboard events, and manages the logging of these events.
3. **fernet_cipher.py**: Handles the encryption and decryption of the logs using the `cryptography.fernet` module.

### Diagram

```plaintext
+-----------------+      +-----------------+      +-----------------+
|    main.py      |      |  events_tracker |      | fernet_cipher   |
|                 |      |                 |      |                 |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | Mouse       | |      | | on_move     | |      | | encrypt     | |
| | Listener    | |      | | on_click    | |      | | decrypt     | |
| | on_move     |<-------| | on_scroll   |<-------| +-------------+ |
| | on_click    | |      | | on_press    | |      +-----------------+
| | on_scroll   | |      | | on_release  | |
| +-------------+ |      | +-------------+ |
| +-------------+ |      | +-------------+ |
| | Keyboard    | |      | | stopper     | |
| | Listener    | |      | +-------------+ |
| | on_press    | |      | | Logs        | |
| | on_release  | |      | +-------------+ |
| +-------------+ |      +-----------------+
| +-------------+ |
| | Process     | |
| | stopper     | |
| +-------------+ |
+-----------------+
```

## Installation

### Prerequisites

- Python 3.x
- Virtual Environment
- `pynput` library
- `cryptography` library

### Setup

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/secure-keylogger.git
    cd secure-keylogger
    ```

2. **Create Virtual Environment**:

    ```bash
    python3 -m venv keylogger_env
    source keylogger_env/bin/activate  # On Windows use `keylogger_env\Scripts\activate`
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Ensure you have saved the provided code in respective Python files (`main.py`, `events_tracker.py`, `fernet_cipher.py`).
2. Run `main.py`:

    ```bash
    python main.py
    ```

## File Descriptions

- **main.py**: Initializes and starts the mouse and keyboard listeners, and manages the logging process.
- **events_tracker.py**: Contains event handlers for capturing mouse and keyboard events and logs them in an encrypted format.
- **fernet_cipher.py**: Handles encryption and decryption of log data using Fernet symmetric encryption.
- **requirements.txt**: Lists the dependencies required to run the project.

## Security Considerations

- Ensure the encryption key is securely stored and managed.
- Use appropriate permissions to restrict access to the log files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Pynput](https://pynput.readthedocs.io/en/latest/) for providing the mouse and keyboard event capturing functionality.
- [Cryptography](https://cryptography.io/en/latest/) for providing the encryption functionality.

## Disclaimer

This project is for educational purposes only. Unauthorized use of keyloggers to capture data without consent is illegal and unethical. Always use this software responsibly and in compliance with local laws and regulations.
```
