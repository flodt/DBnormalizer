# DBnormalizer by David Becher (self-hostable)

This is a self-hostable version of the DBnormalizer created by David Becher.
Install [Docker](https://docs.docker.com/get-docker/) and run the commands listed below in the repository's directory to setup the server.

## Setup
1. `docker build -t dbserve .`
2. `docker run -d -i -t -p 8080:80 dbserve`
3. open `localhost:8080`

## Sources
Adapted from [hypoport/httpd-cgi](https://github.com/hypoport/httpd-cgi) and [becherd/DBnormalizer](https://github.com/becherd/DBnormalizer).
