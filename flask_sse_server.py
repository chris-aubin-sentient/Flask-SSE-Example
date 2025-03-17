import time
from flask import Flask, Response


app = Flask(__name__)


def generate_data():
    for i in range(10):
        # The "data:" prefix and the "\n\n" suffix are required
        yield f"data: Data chunk {i}\n\n"
        time.sleep(1)


@app.route('/stream')
def stream():
    return Response(generate_data(), content_type='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)