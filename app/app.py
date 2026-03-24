from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest

# 🔥 Crear app PRIMERO
app = Flask(__name__)

# 🔥 Métricas
REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total requests',
    ['endpoint']
)

REQUEST_LATENCY = Histogram(
    'request_duration_seconds',
    'Request latency',
    ['endpoint']
)

# 🔥 Endpoint principal
@app.route("/")
def home():
    with REQUEST_LATENCY.labels(endpoint="/").time():
        REQUEST_COUNT.labels(endpoint="/").inc()
        return {"message": "Observability 🚀"}

# 🔥 Endpoint metrics
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")