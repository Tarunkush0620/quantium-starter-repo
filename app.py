"""Repo-level app module.
Exposes `app` for tests and runs the server when executed directly.
"""
from data.app import app  # Dash instance

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8050, use_reloader=False)
