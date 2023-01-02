import setuptools

setuptools.setup(
    name="jupyter-filebrowser-proxy",
    version='0.0.1',
    url="https://github.com/sebastiendfortier/jupyter-filebrowser-proxy",
    author="Sebastien Fortier",
    description="Jupyter extension to proxy filebrowser",
    packages=setuptools.find_packages(),
	keywords=['Jupyter', 'Filebrowser'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=3.2.2'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'filebrowser = jupyter_filebrowser_proxy:setup_filebrowser'
        ]
    },
    package_data={
        'jupyter_filebrowser_proxy': ['icons/filebrowser-logo.svg'],
    },
)
