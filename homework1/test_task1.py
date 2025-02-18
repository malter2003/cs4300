import subprocess

def test_task1_output():
    # this will capture the standard output when the task is ran
    result = subprocess.run(["python3", "task1.py"], capture_output=True, text=True)
    assert result.stdout.strip() == 'Hello, world!'