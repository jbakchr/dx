import typer

app = typer.Typer()


@app.command()
def hello():
    """Simple test command"""
    print("dx is working ✅")