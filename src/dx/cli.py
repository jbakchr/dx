import typer

from dx.commands.run import run as run_command

app = typer.Typer()


@app.command()
def run():
    """Run a container (placeholder)"""
    run_command()


@app.callback(invoke_without_command=True)
def default(ctx: typer.Context):
    """Default dx behavior"""
    if ctx.invoked_subcommand is None:
        print("dx is working ✅")