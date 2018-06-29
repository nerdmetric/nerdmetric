# nerdmetric
Temporary repository for nerdmetric development.
Prototype of a metric for contributions to scientific community resources.
A lot of the current code is taken from [here](https://github.com/nih-fmrif/mriqcwebapi).


## Things to look at

- Invenio ORCID OAuth: https://github.com/zenodo/invenio/blob/zenodo-master/invenio/modules/oauthclient/contrib/orcid.py



## Running nerdmetric with Docker

First, make sure that you have [Docker](https://docs.docker.com/engine/installation/) installed. Then:  
1) Navigate into the nerdmetric directory. (`cd nerdmetric/`)
2) Build the Docker image with `docker build -t nerdmetric .`
3) Create the Docker container and run with `docker run --name nerdmetric -ti -p 5000:5000 nerdmetric`

nerdmetric should be running at `http://localhost:5000/`. The next time that you want to run the Docker container, simply execute `docker start -a nerdmetric`, and stop the Docker container with `docker stop nerdmetric`.


## Badges

[![nerdmetric](https://img.shields.io/badge/nerdmetric-affiliate-brightgreen.svg)](https://nerdmetric.github.io)
