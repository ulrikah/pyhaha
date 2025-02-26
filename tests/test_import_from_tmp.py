from pathlib import Path
import sys
import pytest
import tempfile

def test_import_from_temp():
    with tempfile.TemporaryDirectory() as dir:
        dir_path = Path(dir)
        module_path = dir_path / "tmpmodule.py"
        module_path.touch()

        with open(module_path, "wt+") as fp:
            fp.writelines([
                'def foo():',
                '   return "bar"'
            ])
        
        sys.path.append(str(dir_path))

        from tmpmodule import foo
        assert foo() == "bar"
    
    assert not dir_path.is_dir()
    assert foo() == "bar"