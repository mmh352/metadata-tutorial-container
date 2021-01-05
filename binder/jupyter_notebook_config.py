import os

## The default URL to redirect to from `/`
#c.NotebookApp.default_url = '/tree'
c.NotebookApp.default_url = '/lab'

## (bytes/sec) Maximum rate at which stream output can be sent on iopub before
#  they are limited.
c.NotebookApp.iopub_data_rate_limit = 10000000

## (msgs/sec) Maximum rate at which messages can be sent on iopub before they are
#  limited.
#c.NotebookApp.iopub_msg_rate_limit = 1000

## The IP address the notebook server will listen on.
#c.NotebookApp.ip = 'localhost'
c.NotebookApp.ip = '0.0.0.0'

## The directory to use for notebooks and kernels.
#c.NotebookApp.notebook_dir = ''
c.NotebookApp.notebook_dir = 'workspace'
if not os.path.exists(c.NotebookApp.notebook_dir):
    os.makedirs(c.NotebookApp.notebook_dir, exist_ok=True)

## Whether to open in a browser after starting. The specific browser used is
#  platform dependent and determined by the python standard library `webbrowser`
#  module, unless it is overridden using the --browser (NotebookApp.browser)
#  configuration option.
#c.NotebookApp.open_browser = True
c.NotebookApp.open_browser = False

## If True, display a button in the dashboard to quit (shutdown the notebook
#  server).
c.NotebookApp.quit_button = False

## Timeout (in seconds) after which a kernel is considered idle and ready to be
#  culled. Values of 0 or lower disable culling. Very short timeouts may result
#  in kernels being culled for users with poor network connections.
c.MappingKernelManager.cull_idle_timeout = 1200

## The interval (in seconds) on which to check for idle kernels exceeding the
#  cull timeout value.
c.MappingKernelManager.cull_interval = 10

## Shut down the kernel when the user logs out
c.JupyterHub.shutdown_on_logout

#-------------
# Server Proxy
#-------------

c.ServerProxy.servers = {
  'tutorial': {
    #'command': ['python', '-m', 'tutorial_server', '--config=/etc/tutorial-server/production.ini', '--port={port}', 'basepath={base_url}'],
    'command': ['touch', '/home/jovyan/workspace/testing.txt']
    'absolute_url': True,
    'timeout': 30
  }
}
