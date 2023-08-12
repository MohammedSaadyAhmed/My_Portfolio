# prometheus1


1. What is different HTTP status code and explain meaning of each of them ?

    • 2xx Success:
          200 OK: The request was successful, and the response contains the requested data.
          201 Created: A new resource has been successfully created on the server.
          204 No Content: The server processed the request but does not return any content in response.
    • 3xx Redirection:
          301 Moved Permanently: The requested resource has moved permanently to a new location specified in the Location header.
          302 Found / 303 See Other / 307 Temporary Redirect: Similar to 301, but indicates temporary redirection instead of permanent.
    • 4xx Client Errors:
          400 Bad Request: The server cannot process due to malformed syntax or invalid parameters in client's request.
          401 Unauthorized: Authentication is required for accessing this resource. Typically used when authentication credentials are missing or invalid.
          404 Not Found: Indicates that no matching resource could be found at this URL.
    • 5xx Server Errors:
          500 Internal Server Error: A generic error message indicating that an unexpected condition occurred on the server while processing the request, causing it unable to fulfill it properly.

2. What database is used by Prometheus?
Prometheus uses its own custom-built database called "TSDB" (Time Series Database). TSDB is specifically designed for storing time-series data efficiently and supports fast retrieval of metrics data over time.

3. What is the difference between different metrics types ( counter , gauge ,
histogram)?
    • Counter: A counter represents a cumulative value that only increases over time without decreasing or resetting unless manually modified. It is often used to measure things like total requests received or total events occurred since starting monitoring.
    • Gauge: A gauge represents a single numeric value that can arbitrarily increase or decrease over time based on current observations. It can go up and down depending on changes in observed values like CPU usage, memory consumption, etc.
    • Histogram: A histogram measures distributions of observed values across predefined buckets (e.g., response times). It provides statistical summaries such as counts per bucket and cumulative counts at each boundary value.
