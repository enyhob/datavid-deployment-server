import logging
import os
import subprocess
import sys
import threading
import time

from flask import Flask, request, Response

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(levelname)s - %(module)s: %(message)s',
                    stream=sys.stdout)
logger = logging.getLogger(__name__)


def deploy():
    logger.info('Waiting on docker hub.')
    # wait on docker hub
    time.sleep(60)
    logger.info('Running make')
    # execute redeploy
    subprocess.run(f'make -C {os.environ["PROJECT"]} redeploy'.split())
    logger.info('Finished')


@app.route('/status')
def status():
    logger.info('Status ok')
    return 'ok'


@app.route('/redeploy')
def deploy_service():
    logger.info('Checking token')
    header = request.headers.get('auth')
    logger.info('Header found.')
    if header == os.environ.get('TOKEN'):
        logger.info('Header matched.')
        threading.Thread(target=deploy).start()
        logger.info('Thread started.')
        return 'OK'
    else:
        logger.warning(f'Auth failed for {header}')

    return Response('Access denied, wrong or missing token.', 401)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9091)
