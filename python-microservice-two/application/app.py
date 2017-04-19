from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/two')
def hello():
    count = redis.incr('hits')
    return 'Hello! I am microservice TWO on BLUE Deployment and you have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
