from systems.commands.index import CommandMixin
from utility.data import ensure_list
from utility.filesystem import load_yaml, save_file, save_yaml

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
        self.edit_config(config_path)

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


    def edit_config(self, config_path):
        edit_file = os.path.join(self.manager.data_dir, '.kube', '.edit')
        if not os.path.exists(edit_file):
            config = load_yaml(config_path)
            for cluster_info in config['clusters']:
                cluster_info['cluster']['insecure-skip-tls-verify'] = True

            save_yaml(config_path, config)
            save_file(edit_file, '')
