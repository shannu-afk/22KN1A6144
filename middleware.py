from datetime import datetime


class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        method = environ.get("REQUEST_METHOD")
        path = environ.get("PATH_INFO")
        timestamp = datetime.utcnow().isoformat()

        with open("logs.txt", "a") as log_file:
            log_file.write(f"[{timestamp}] {method} {path}\n")

        return self.app(environ, start_response)
