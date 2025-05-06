import os
import sys
import subprocess
from config.env_config import setup_env

# Define test directories and corresponding coverage targets
TEST_CONFIG = {
    "unit": {"dir": "tests/unit_tests", "cov": ["config", "utils", "etl"]},
    "integration": {"dir": "tests/integration_tests", "cov": ["etl"]},
    "component": {"dir": "tests/component_tests", "cov": ["etl"]},
    "all": {"dir": "tests", "cov": ["config", "etl", "utils"]},
}


def run_linting(command):
    py_result = subprocess.CompletedProcess(
        args=[], returncode=0, stdout="Python linting not run", stderr=""
    )
    sql_result = subprocess.CompletedProcess(
        args=[], returncode=0, stdout="SQL linting not run", stderr=""
    )
    if command == "lint:python" or command == "lint:all":
        print("Running python linting checks")
        py_result = run_python_linting()
    if command == "lint:sql" or command == "lint:all":
        print("Running SQL linting checks")
        sql_result = run_sql_linting()
    if py_result is None and sql_result is None:
        raise ValueError("Unknown linting command: {command}")
    report_results(py_result, sql_result)


def report_results(py_result, sql_result):
    if py_result.returncode == 0:
        if py_result.stdout.find("not run") == -1:
            print(f"Python linting checks passed! {py_result.stdout}")
        else:
            print(py_result.stdout)
    else:
        print(f"Python linting failed with return code: " f"{py_result.returncode}")
        print(py_result.stdout)
        print(py_result.stderr)

    if sql_result.returncode == 0:
        if sql_result.stdout.find("not run") == -1:
            print(f"SQL linting checks passed! {sql_result.stdout}")
        else:
            print(sql_result.stdout)
    else:
        print(f"SQL linting failed with return code {sql_result.returncode}")
        print(sql_result.stdout)
        print(sql_result.stderr)


def run_python_linting():
    return subprocess.run(["flake8", "."], capture_output=True, text=True)


def run_sql_linting():
    # Specify the folder to lint
    folder_to_lint = "etl/sql"

    # Check if there are any SQL files in the folder
    sql_files = [f for f in os.listdir(folder_to_lint) if f.endswith(".sql")]
    if not sql_files:
        raise FileNotFoundError(f"No SQL files found in {folder_to_lint}")

    return subprocess.run(
        ["sqlfluff", "lint", folder_to_lint], capture_output=True, text=True
    )


def get_cov_command(command):
    # Access the TEST_CONFIG dictionary to get the test directory
    # and coverage targets
    test_dir = TEST_CONFIG[command]["dir"]
    cov_sources = ",".join(TEST_CONFIG[command]["cov"])

    # Build the test command for tests with coverage
    try:
        return create_cov_command_str(test_dir, cov_sources)
    except ValueError:
        raise ValueError(f"Test failure with: {command}")


def create_cov_command_str(test_dir, cov_sources):
    return (
        # f'ENV=test coverage run --source={cov_sources} '
        # f'--omit=*/__init__.py -m pytest --verbose {test_dir} '
        # '&& coverage report -m && coverage html '
        # '&& coverage report --fail-under=90'
        # Moved options to .coveragerc file
        f"coverage run -m pytest --verbose {test_dir} "
        "&& coverage report -m"
    )


def main():
    setup_env(["None", "test"])
    # Get the argument passed to run_tests
    command = sys.argv[1]

    # Lint then stop executing test run if command is 'lint'
    if command.find("lint") != -1:
        run_linting(command)
        return

    # Check to see if a command was supplied for the test run
    if command in TEST_CONFIG:
        # Run the test command
        subprocess.run(get_cov_command(command), shell=True)
        # Run the linting checks
        run_linting("lint:all")
    else:
        raise ValueError(f"Unknown command: {command}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Usage: run_tests.py <unit|integration|component|all|lint>")
    else:
        main()
