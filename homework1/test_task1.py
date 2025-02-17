import subprocess

def test_task1_output():
    result = subprocess.run(["python3", "task1.py"], capture_output=True, text=True)
    assert result.stdout.strip() == 'Hello, world!'