from multiprocessing import cpu_count

# The socket for Gunicorn to bind to
bind = "0.0.0.0:8000"

# Workers silent for more than this many seconds are killed and restarted
timeout = 300

# Each worker can handle one request at a time
worker_class = "sync"

# The number of worker processes. This should generally be set to 2 * CPU cores + 1
workers = (cpu_count() * 2) + 1

# The maximum number of pending connections. Excess connections will be dropped
backlog = 1024

# The maximum number of requests a worker will process before restarting
max_requests = 10000

# The maximum jitter added to the max-requests setting. It causes workers to restart at a random point in time
max_requests_jitter = 1000

# After receiving a restart signal, workers have this much time to finish serving requests
graceful_timeout = 30

# Send to stdout
accesslog = "-"
access_log_format = '%(t)s %(p)s %(h)s %(l)s %(u)s"%(r)s" %(s)s %(b)s %(T)ss "%(f)s" "%(a)s"'

# Commenting out sends to stdout
# errorlog = 'logs/error.log'