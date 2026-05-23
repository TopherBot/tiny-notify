# tiny-notify

A tiny Python command‑line tool that displays a desktop notification with a custom message. It works on macOS, Linux, and Windows without any external runtime dependencies.

---

## Features

- **Zero‑dependency** single‑file implementation.
- Platform‑aware: uses `osascript` on macOS, `notify-send` on Linux, and `win10toast` on Windows (falls back to console output).
- Includes a simple GitHub Actions CI workflow (see the repository’s **.github/workflows/** directory) that lints the script with **ruff** and performs a basic sanity test.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your‑user/tiny-notify.git
cd tiny-notify

# (Optional) Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

No extra packages are required for the core functionality. If you want Windows toast support, install `win10toast`:

```bash
pip install win10toast
```

---

## Usage

```bash
python notify.py "Time to stretch!"
```

If you run the script without arguments, it will display a short usage message.

---

## Development

### Linting

```bash
# Install the linter (ruff) – it is the only development dependency
pip install ruff
ruff check notify.py
```

### Running the CI locally

You can use the **act** tool to execute the GitHub Actions workflow locally:

```bash
act -j lint
act -j test
```

---

## License

MIT License – see the **LICENSE** file in the repository (the project is intended to be public‑domain friendly).
