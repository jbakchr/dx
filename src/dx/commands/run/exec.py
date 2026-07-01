import subprocess

from dx.ui.output import execution_header, execution_done


def execute(cmd: str) -> None:
    """
    Execute a Docker command.

    Displays execution status messages before and after
    running the command.

    Args:
        cmd: The Docker command to execute.

    Returns:
        None.
    """
    execution_header()
    subprocess.run(cmd, shell=True)
    execution_done()