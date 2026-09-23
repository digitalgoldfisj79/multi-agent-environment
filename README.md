# Multi Agent Environment

This project is a multi-agent environment designed to simulate and manage multiple agents. The purpose of this project is to provide a framework for creating and testing multi-agent systems, which can be used in various applications such as robotics, artificial intelligence, and distributed systems.

## Setup and Running the Project

1. Clone the repository:
   ```
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the project:
   ```
   python main.py
   ```

## Contributing

We welcome contributions to the project! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Create a pull request to the main repository.

Please ensure that your code follows the project's coding standards and includes appropriate tests.

## Test Harness

A zero-dependency (stdlib only) harness lives in `harness/`, with unit tests in `tests/`.

- `python -m unittest discover -s tests -t .` runs the unit tests
- `python -m harness` runs every scenario and prints each check (the exit code is non-zero on failure)
- `python -m harness run chase --steps 5 --seed 1` runs a single scenario
- `python -m harness serve --port 8000` starts the web UI at http://127.0.0.1:8000

In the UI you can pick a scenario, set the steps and seed, scrub or play the trajectory on the grid, inspect each agent's state at every step, see check results and tracebacks, and run the unit test suite.

To add a scenario, decorate a builder in `harness/scenarios.py` with `@scenario(...)`. The builder returns `(env, checks)`, and each check takes the recorded trace and returns `(passed, detail)`.
