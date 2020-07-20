import os
import subprocess
from dotenv import load_dotenv
from mypacks.uploader_builder import UploaderBuilder

try:
    # Load environment variables
    load_dotenv()
    # Initialize uploader instance
    uploader = (UploaderBuilder()
                .set_path(os.getenv('PATHS').split('|'))
                .set_output(os.getenv('OUTPUT'))
                .set_zipping_mode(os.getenv('ZIPPING_MODE'))
                .set_parent_id(os.getenv('PARENT_ID'))
                .set_interval(int(os.getenv('INTERVAL')))
                .build())
    # Upload files
    uploader.upload()
except Exception as e:
    subprocess.Popen(['notify-send', str(e)])
    print(e)