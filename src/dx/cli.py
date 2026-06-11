import typer

from dx.commands.run import run as run_command

app = typer.Typer()


@app.command()
def run(image: str):
    """Run a container (interactive learning)"""
    run_command(image=image)


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
