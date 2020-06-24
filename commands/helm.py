from systems.commands.index import Command
from utility.filesystem import filesystem_dir

import os


class Helm(Command('helm')):

    def exec(self):
        config_path = os.path.join(self.manager.data_dir, '.kube')
        helm_path = os.path.join(self.manager.data_dir, '.helm')

        with filesystem_dir(helm_path) as home_dir:
            home_dir.mkdir('cache')
            home_dir.mkdir('config')
            home_dir.mkdir('data')

            command = ['helm'] + self.options.get('args', [])
            success = self.sh(
                command,
                env = {
                    "KUBECONFIG": os.path.join(config_path, 'config'),
                    "HELM_HOME": home_dir.base_path,
                    "XDG_CACHE_HOME": home_dir.path('cache'),
                    "XDG_CONFIG_HOME": home_dir.path('config'),
                    "XDG_DATA_HOME": home_dir.path('data')
                },
                cwd = self.manager.module_dir,
                display = True
            )
            if not success:
                self.error("Helm command failed: {}".format(" ".join(command)))
