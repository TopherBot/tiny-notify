#!/usr/bin/env python3
"""
 tiny-notify – send a desktop notification from the command line.

 Supported platforms:
 * macOS – uses AppleScript via `osascript`.
 * Linux – uses `notify-send` (must be installed).
 * Windows – uses `win10toast` if available, otherwise falls back to a simple printed message.
"""

import sys
import subprocess
import platform


def _mac_notify(message: str) -> None:
    """Show a notification on macOS using AppleScript."""
    script = f'display notification "{message}" with title "tiny-notify"'
    subprocess.run(["osascript", "-e", script], check=False)


def _linux_notify(message: str) -> None:
    """Show a notification on Linux using `notify-send`."""
    subprocess.run(["notify-send", "tiny-notify", message], check=False)


def _windows_notify(message: str) -> None:
    """Show a toast on Windows using `win10toast` if installed."""
    try:
        from win10toast import ToastNotifier
        ToastNotifier().show_toast("tiny-notify", message, duration=5)
    except Exception:
        # Fallback – just print to console
        print(f"[tiny-notify] {message}")


def notify(message: str) -> None:
    """Dispatch the notification to the appropriate platform implementation."""
    system = platform.system()
    if system == "Darwin":
        _mac_notify(message)
    elif system == "Linux":
        _linux_notify(message)
    elif system == "Windows":
        _windows_notify(message)
    else:
        print(f"[tiny-notify] Unsupported platform {system}. Message: {message}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: notify.py <message>")
        sys.exit(1)
    message = " ".join(sys.argv[1:])
    notify(message)


if __name__ == "__main__":
    main()
