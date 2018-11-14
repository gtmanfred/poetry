import os
import sys

from clikit.args import StringArgs

from ..command import Command


class DebugInfoCommand(Command):
    """
    Shows debug information.

    info
    """

    def handle(self):
        from ....utils.env import Env

        poetry = self.poetry
        env = Env.get(poetry.file.parent)

        poetry_python_version = ".".join(str(s) for s in sys.version_info[:3])

        self.line("")
        self.line("<b>Poetry</b>")
        self.line("")
        self.line("<info>Version</info>: <comment>{}</>".format(poetry.VERSION))
        self.line("<info>Python</info>:  <comment>{}</>".format(poetry_python_version))

        args = StringArgs("")
        command = self.application.get_command("env").get_sub_command("info")

        return command.run(args, self._io)
