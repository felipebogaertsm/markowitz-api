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

# How to use it

Once the set up has been completed, the application should be running in localhost port 8000. In order to test it,
make a GET request to the main endpoint by entering the following string in your browser's URL bar:

`http://localhost:8000/api/optimizer?tickers=AAPL,MSFT&target_return=10`

Your response should be something like that:

```
{
    "optimized_weights": [
        1.0,
        0.0
    ],
    "expected_return": 0.31560102462129547,
    "volatility": 0.19967570436575924,
    "sharpe_ratio": 1.3301619516752847
}
```

# References

The official documentation for Polygon was used.

https://github.com/polygon-io/client-python

https://polygon.io/docs/stocks/getting-started

```

```
