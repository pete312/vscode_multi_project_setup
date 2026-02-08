from click.testing import CliRunner

def test_foo():
    assert True,  "this cant fail"


def test_clone_standalone():
    """Test the clone command directly"""
    from foo.app import clone
    runner = CliRunner()
    result = runner.invoke(clone)
    
    assert result.exit_code == 0
    assert 'clone command' in result.output