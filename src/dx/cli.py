import typer

app = typer.Typer(invoke_without_command=True)


@app.callback()
def main():
    """dx CLI"""
    print("dx is working ✅")
