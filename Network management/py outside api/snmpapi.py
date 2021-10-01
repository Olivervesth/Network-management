from flask import Flask
import os
from datetime import date
app = Flask(__name__)


def write_to_logfile(string, writemethod):
    path = './logfiles/'
    filename = f'weblog_{date.today().year}_{date.today().month}_{date.today().day}.txt'
    if not os.path.isfile(f'{path}{filename}'):
        print('New file created!')

    with open(f'{path}{filename}', writemethod) as f:
        f.write(f"{string}\n")


@app.route("/<string:message>")
def log_updater(message):
    write_to_logfile(message, 'a')
    return 'written to log file'

if __name__ == "__main__":
  app.run()