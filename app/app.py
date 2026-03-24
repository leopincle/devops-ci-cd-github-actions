from prometheus_client import Counter, Histogram, generate_latest
from flask import Response

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

@app.route("/")
def home():
    with REQUEST_LATENCY.labels(endpoint="/").time():
        REQUEST_COUNT.labels(endpoint="/").inc()
        return {"message": "Observability 🚀"}

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")