"""Repo-level entry point.
Runs the Dash app defined in data/app.py so `python app.py` works.
"""
import runpy

if __name__ == "__main__":
    # Execute the app script as if run directly
    runpy.run_path("data/app.py", run_name="__main__")
