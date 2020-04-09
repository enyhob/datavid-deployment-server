import os
import subprocess
import threading
import time

from flask import Flask, request, Response

app = Flask(__name__)

def deploy():
    # wait on docker hub
    time.sleep(60)
    # execute redeploy
    subprocess.run("make -C /app/datavid redeploy".split())


@app.route('/redeploy')
def deploy_service():
    header = request.headers['auth']
    if header == os.environ.get('TOKEN'):
        threading.Thread(target=deploy)
        return "OK"

    return Response('Access denied, wrong or missing token.', 401)


if __name__ == '__main__':
    app.run()
