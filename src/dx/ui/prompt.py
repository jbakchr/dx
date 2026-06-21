# src/dx/ui/prompt.py

def ask_port(default: str):
    port = input(f"? Expose port? (default {default}) → ").strip()
    return port if port else default


def ask_detached():
    val = input("? Run in background? (Y/n) → ").strip().lower()
    return val != "n"


def ask_name():
    return input("? Name container? → ").strip()


def confirm_run():
    val = input("Run? (Y/n) ").strip().lower()
    return val != "n"
