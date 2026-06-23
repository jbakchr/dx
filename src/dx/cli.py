import typer

from dx.commands.run import run as run_command
from dx.commands.supported import supported as supported_command

app = typer.Typer()


@app.callback(invoke_without_command=True)
def default(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print(
            """
dx — Docker learning CLI

Usage:
  dx [COMMAND]

Commands:
  run     Run a container (interactive learning)

Tip:
  Use "dx --help" for more details
"""
        )


@app.command()
def run(image: str):
    """Run a container (interactive learning)"""
    run_command(image=image)


@app.command()
def supported():
    """Show images supported by dx"""
    supported_command()


