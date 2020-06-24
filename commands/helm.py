from systems.commands.index import Command
from utility.filesystem import filesystem_dir

import os


class Helm(Command('helm')):

    def exec(self):
        with filesystem_dir(os.path.join(self.manager.data_dir, '.helm')) as home_dir:
            home_dir.mkdir('cache')
            home_dir.mkdir('config')
            home_dir.mkdir('data')

            self.kube_exec(home_dir, 'helm',
                env = {
                    "HELM_HOME": home_dir.base_path,
                    "XDG_CACHE_HOME": home_dir.path('cache'),
                    "XDG_CONFIG_HOME": home_dir.path('config'),
                    "XDG_DATA_HOME": home_dir.path('data')
                }
            )
