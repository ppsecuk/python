#!flask/bin/python
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

baseUrl = "https://api.statuspage.io/v1/pages/"
headers = {'Authorization': 'OAuth xxxxx'}


def secured(f):
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key or api_key != 'xxxxx':
            return jsonify({'Error': 'x-api-key not provided or the value is wrong'}), 401

        return f(*args, **kwargs)

    return decorated_function


@app.route('/ready')
def readiness():
    return jsonify({'status': 'OK'})


@app.route('/live')
def liveness():
    return jsonify({'status': 'OK'})


@app.route("/api/v1/set-component-status/operational", methods=['POST'], endpoint='operational')
@secured
def operational():
    datadog_data = request.json
    status_page_url = baseUrl + datadog_data['page_id'] + "/components/" + datadog_data['component_id']
    payload = '{"component": {"status": "operational"}}'
    r = requests.patch(status_page_url, data=payload, headers=headers)
    return r.json()


@app.route("/api/v1/set-component-status/major-outage", methods=['POST'], endpoint='major_outage')
@secured
def major_outage():
    datadog_data = request.json
    status_page_url = baseUrl + datadog_data['page_id'] + "/components/" + datadog_data['component_id']
    payload = '{"component": {"status": "major_outage"}}'
    r = requests.patch(status_page_url, data=payload, headers=headers)
    return r.json()


@app.route("/api/v1/set-component-status/partial-outage", methods=['POST'], endpoint='partial_outage')
@secured
def partial_outage():
    datadog_data = request.json
    status_page_url = baseUrl + datadog_data['page_id'] + "/components/" + datadog_data['component_id']
    payload = '{"component": {"status": "partial_outage"}}'
    r = requests.patch(status_page_url, data=payload, headers=headers)
    return r.json()


@app.route("/api/v1/set-component-status/degraded-performance", methods=['POST'], endpoint='degraded_performance')
@secured
def degraded_performance():
    datadog_data = request.json
    status_page_url = baseUrl + datadog_data['page_id'] + "/components/" + datadog_data['component_id']
    payload = '{"component": {"status": "degraded_performance"}}'
    r = requests.patch(status_page_url, data=payload, headers=headers)
    return r.json()


@app.route("/api/v1/set-component-status/under-maintenance", methods=['POST'], endpoint='under_maintenance')
@secured
def under_maintenance():
    datadog_data = request.json
    status_page_url = baseUrl + datadog_data['page_id'] + "/components/" + datadog_data['component_id']
    payload = '{"component": {"status": "under_maintenance"}}'
    r = requests.patch(status_page_url, data=payload, headers=headers)
    return r.json()


if __name__ == '__main__':
    app.run("0.0.0.0", port=8000, debug=True)