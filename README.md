# Markowitz Optimizer REST API

# Introduction

This project is a Django implementation of a Markowitz optimizer. This algorithm is used in finance to optimize the
distribution of a given portfolio, according to the risk appetite of the client/user.

Django is a fast, widely used and mature web framework for the Python programming language. The combination of
performance write-time speed and many years of constant improvement makes it an ideal tool for building this project.

However, Django does provide a lot of boilerplate code, which may be unnecessary. In projects where the logic is mostly
dissociated from the Django models, templates or the database, this is especially true. FastAPI could achieve the same
results with less files and a simpler architecture.

# Set up on your machine

1. Clone the repository

2. Add "dev.env" file to the ".envs" folder. Follow the preset in the "example.env" file.

3. Run the `docker compose up` command. Make sure Docker is pre-installed and running.
