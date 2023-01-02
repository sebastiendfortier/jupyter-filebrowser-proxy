"""
Return config on servers to start for filebrowser

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil

def setup_filebrowser():
    # Make sure filebrowser is in $PATH
    def _filebrowser_command(port):
        full_path = shutil.which('filebrowser')
        if not full_path:
            raise FileNotFoundError('Can not find filebrowser in $PATH')
        working_dir = os.getenv("WORKINGDIR", None)
        if working_dir is None:
            working_dir = os.getenv("JUPYTER_SERVER_ROOT", ".")

        return [full_path, f'--port={port}', "--noauth", "-r", working_dir ]

    return {
        'command': _filebrowser_command,
        'timeout': 20,
        'launcher_entry': {
            'title': 'Filebrowser',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'icons', 'filebrowser-logo.svg')
        }
    }