
# Language API Demo Repo Structure

This repo aims to act as a template for starting API First projects, with the aim of ensuring we are building our tools with deployment and usability in mind at the first steps.

Ideally all new modules should have:

1. A docker images for easy building and deploying with 2 commands
2. Testing Suite (TODO)
3. API Interface
4. An importable Query Schema if using GraphQL
4. Example UI Interface 
5. Security (TODO)
6. Easy local install through requirements
7. QA suite 
8. A way to scale with many calls in a queue (TODO)

# Installation

This can be installed in its own conda, or used as an API through docker.

Along with the requirements, this repo requires
1. Sorcero-nl
2. http-requests from nl-lab/toos

# Local API
uvicorn server:app --reload --port <PORT>

# Docker Deployment

We use docker for deployment

```
docker build -t language_api ./
sudo docker run -d --name language_api -p 8123:80 language_api
```