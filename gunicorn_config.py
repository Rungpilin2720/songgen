# Gunicorn configuration file
# Note: bind will be set via command line to use $PORT env var
workers = 1  # Use 1 worker for this AI model
worker_class = "sync"
worker_connections = 1000
timeout = 300  # 5 minutes timeout for song generation
keepalive = 2
max_requests = 1000
max_requests_jitter = 50
preload_app = True 