# NetAtlas Network Scanner

A lightweight, cross-platform Python script to quickly scan a local network for active hosts using parallel pinging.

## Features
- **Blazing Fast:** Uses multi-threading to scan a /24 network in seconds instead of minutes.
- **Zero Dependencies:** Uses only Python standard libraries (`subprocess`, `concurrent.futures`, `ipaddress`).
- **Cross-Platform:** Works on Windows, macOS, and Linux automatically.

## Requirements
- Python 3.6+
- `ping` command available in your system PATH (standard on all OSs)

## Usage

1. Clone or download the script.
2. Navigate to the `app` folder:
```bash
cd app
```
3. Run it via terminal:
```bash
python network_scanner.py
```

> **Note:** By default, it scans `192.168.1.0/24`. To change the range, edit the `if __name__ == "__main__":` block.

## How It Works

The script generates a list of IPs from the provided CIDR range and submits them to a thread pool of 50 workers. Each worker runs a system ping command with a 1-second timeout. If a host responds, it is added to the results list.

## License

[MIT License](LICENSE)
