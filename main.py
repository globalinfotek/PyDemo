import os
import tempfile

from source.update_service import UpdateService

"""
    This is the entrypoint for the application. This function will create the thread timer that is
    responsible for posting updates to the update API. The function also starts a simple web server
    that exposes a health check endpoint.
"""
if __name__ == '__main__':
    UpdateService().post_update()
    # Once the app is running, write to the tmp directory.
    tempDir = tempfile.gettempdir()
    with open(os.path.join(tempDir, 'health'), 'w') as temp_file:
        temp_file.writelines('PYTHON - OK')
