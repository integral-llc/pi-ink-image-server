"""Entry point for running the server."""

import uvicorn

from .app import create_app

app = create_app()

if __name__ == "__main__":
    print("Starting Pi2W Content Server on http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
