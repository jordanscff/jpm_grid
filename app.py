from flask import Flask, jsonify, render_template, request
from datetime import datetime, timezone, timedelta
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


def config_data(example=1):
    if example == 2:
        return {
            "highlight_recent": False,
            "heatmap_column": None
        }
    return {
        "highlight_recent": True,
        "heatmap_column": "score"
    }


def record_data():
    now = datetime.now(timezone.utc)
    return [
        {"name": "Alice", "score": 95, "timestamp": (now - timedelta(hours=1)).isoformat()},
        {"name": "Bob", "score": 60, "timestamp": (now - timedelta(days=2)).isoformat()},
        {"name": "Charlie", "score": 80, "timestamp": (now - timedelta(minutes=10)).isoformat()},
    ]

@app.route("/config")
def config():
    """Get grid config
    ---
    responses:
      200:
        description: Configuration for grid display
        examples:
          application/json: { "highlight_recent": true, "heatmap_column": "score" }
    """
    return jsonify(config_data())

@app.route("/data")
def data():
    """Get grid data
    ---
    responses:
      200:
        description: List of records to display in the grid
        examples:
          application/json: [
            { "name": "Alice", "score": 95, "timestamp": "2025-05-12T10:00:00+00:00" },
            { "name": "Bob", "score": 60, "timestamp": "2025-05-10T12:00:00+00:00" },
            { "name": "Charlie", "score": 80, "timestamp": "2025-05-12T11:50:00+00:00" }
          ]
    """
    return jsonify(record_data())

@app.route("/grid")
def grid():
    example = int(request.args.get("example", 1))
    config = config_data(example)
    data = record_data()

    for row in data:
        row["timestamp"] = datetime.fromisoformat(row["timestamp"])

    return render_template(
        "grid.html",
        data=data,
        config=config,
        now=datetime.now(timezone.utc),
        request=request
    )
