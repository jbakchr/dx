import subprocess

from dx.ui.output import execution_header, execution_done

def execute(cmd: str):
    execution_header()
    subprocess.run(cmd, shell=True)
    execution_done()