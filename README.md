# Setup
- `docker build -t dbserve .`
- `docker run -d -i -t -p 8080:80 dbserve`
- open `localhost:8080`

# Todos
- links to static files have to be updated
- navigating to the server yields "not found"

# Sources
Adapted from [hypoport/httpd-cgi](https://github.com/hypoport/httpd-cgi) and [becherd/DBnormalizer](https://github.com/becherd/DBnormalizer).
