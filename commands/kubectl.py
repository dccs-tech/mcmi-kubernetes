from systems.commands.index import Command
from utility.temp import temp_dir


class Kubectl(Command('kubectl')):

    def exec(self):
        with temp_dir() as temp:
            self.kube_exec(temp, 'kubectl',
                options = ['--insecure-skip-tls-verify=true']
            )
