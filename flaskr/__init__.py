from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def create_app(test_config=None):

    app = Flask(__name__)
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["300 per minute", "15000 per hour"]
    )

    # jumble input string
    @app.route("/api/jumble/<int:n>", methods=["POST"])
    def jumble(n=0):
        scrambled_string = ""
        if request.is_json:
            try:
                # Parse JSON data from the request body
                data = request.get_json()
                # Assuming JSON data contains a 'message' field
                name = data.get("message")
                if name:
                    scrambled_string = ""
                    for ch in name:
                        if ch.isdigit() or ch == " ":
                            # don't scramble if digit or space
                            scrambled_string += ch
                        elif "a" <= ch <= "z":
                            # jumble - shift right by n
                            c = ord(ch) - ord("a")
                            scrambled_string += chr(((c + n) % 26) + ord("a"))
                        elif "A" <= ch <= "Z":
                            # jumble - shift right by n
                            c = ord(ch) - ord("A")
                            scrambled_string += chr(((c + n) % 26) + ord("A"))

                    return jsonify({"jumbled": scrambled_string}), 200
                else:
                    return jsonify({"error": "message not found in JSON data"}), 400
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": "Request does not contain valid JSON"}), 400

    # healthcheck for app
    @app.route('/api/health')
    def hello():
        return 'Healthy'
    
    return app
