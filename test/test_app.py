import pytest
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Create an instance of the App class
    app_instance = App()
    
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    with pytest.raises(SystemExit) as e:  # Expect a SystemExit exception
        app_instance.start()
    assert e.type == SystemExit
    assert e.value.code == "Exiting..."
    out, err = capfd.readouterr()
    # Check that the initial greeting is printed and the REPL exits gracefully
    assert "Hello World. Type 'exit' to exit." in out

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Create an instance of the App class
    app_instance = App()
    
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit) as e:  # Expect a SystemExit exception
        app_instance.start()
    assert e.type == SystemExit
    assert e.value.code == "Exiting..."
    out, err = capfd.readouterr()
    # Check that the REPL responds to an unknown command and then exits after 'exit' command
    assert "Hello World. Type 'exit' to exit." in out
