import typer

from dx.commands.run.command import run as run_command
from dx.commands.supported import supported as supported_command
from dx.commands.stop import stop as stop_command
from dx.commands.rm import rm as rm_command
from dx.commands.reset import reset as reset_command
from dx.commands.dockerfile.command import run as run_dockerfile_command

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
  run         Run a container (interactive learning)
  stop        Stop containers
  rm          Remove containers
  reset       Stop and remove all containers
  dockerfile  Run the Dockerfile command
  supported   Show supported images

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


@app.command()
def stop(all: bool = typer.Option(False, "--all", help="Stop all running containers")):
    """Stop containers"""
    stop_command(all=all)


@app.command()
def rm(all: bool = typer.Option(False, "--all", help="Remove all containers")):
    """Remove containers"""
    rm_command(all=all)


@app.command()
def reset():
    """Stop and remove all containers"""
    reset_command()

@app.command()
def dockerfile(
    image: str = typer.Argument(
        None,
        help="Base image profile (e.g. python, node, nginx)",
    )
):
    """Run the Dockerfile command"""
    run_dockerfile_command(image=image)