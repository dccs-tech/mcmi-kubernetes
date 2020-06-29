from systems.commands.index import CommandMixin
from utility.data import ensure_list

import os


class KubeExecMixin(CommandMixin('kube_exec')):

    def kube_exec(self, filesystem, executable, options = None, env = None):
        args = self.options.get('args', [])
        if options is None:
            options = []

        if options:
            command = [ executable ] + ensure_list(options) + args
        else:
            command = [ executable ] + args

        config_path = os.path.join(self.manager.data_dir, '.kube', 'config')
        command_env = {
            "KUBECONFIG": filesystem.link(config_path, '.kube')
        }
        if env and isinstance(env, dict):
            command_env = { **command_env, **env }

        success = self.sh(
            command,
            env = command_env,
            cwd = self.manager.module_dir,
            display = True
        )
        if not success:
            self.error("Command {} failed: {}".format(executable, " ".join(command)))
