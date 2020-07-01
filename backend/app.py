from flask import Flask, jsonify, make_response, render_template
import uuid

DEBUG = True

app = Flask(__name__, template_folder='templates', static_folder="static")

@app.route('/api/ping', methods=['GET', 'POST'])
def ping_pong():
    return jsonify('pong!')


@app.route('/')
def index():
    return make_response(render_template('index.html', name="test_user", token=uuid.uuid1()))
    # return app.send_static_file('index.html')

# @app.errorhandler(404)
# def page_not_found(e):
#     return make_response(render_template('/index.html'))
#     # return app.send_static_file('index.html')

@app.route("/<path:fallback>")
def fallback(fallback):
    print('fallback = ' + fallback)
    if fallback.startswith('css/') or fallback.startswith('js/') or fallback.startswith('img/') or fallback == 'favicon.ico':
        # return make_response(render_template('/' + fallback))
        return app.send_static_file(fallback)
    else:
        # return make_response(render_template('/index.html'))
        return app.send_static_file('index.html')
    # resp = make_response(render_template("/index.html"))
    # return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
