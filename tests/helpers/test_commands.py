from pathlib import Path
import os
import subprocess
from typing import Generator
import pytest
from unittest.mock import patch

from helpers import commands


def test_run_ls(temp_dir, fake_files, fake_xls_files_ls_output):
    cwd = os.getcwd()   # avoid vscode pytest internal error
    
    result = commands.run(
                'ls', 
                path=temp_dir
            )
    assert result.args == ['ls']
    assert result.returncode == 0
    assert result.stderr == ''
    assert result.stdout == fake_xls_files_ls_output
    
    os.chdir(cwd)       # avoid vscode pytest internal error


def test_pushd_decorator(temp_dir, fake_files, fake_xls_files_ls_output):
    cwd = os.getcwd()
    run = commands.pushd(commands.run)
    result = run(
                'ls', 
                path=temp_dir
            )
    assert result.args == ['ls']
    assert result.returncode == 0
    assert result.stderr == ''
    assert result.stdout == fake_xls_files_ls_output
    assert cwd == os.getcwd()


def test_pushd_param(temp_dir, fake_files, fake_xls_files_ls_output):
    cwd = os.getcwd()
    result = commands.run(
                'ls', 
                path=temp_dir,
                pushd=True
            )
    assert result.args == ['ls']
    assert result.returncode == 0
    assert result.stderr == ''
    assert result.stdout == fake_xls_files_ls_output
    assert cwd == os.getcwd()


def test_run_shell_wildcards(temp_dir, fake_files):
    result = commands.run(
                'rm *', 
                path=temp_dir,
                pushd=True,
                shell=True  # needed for wildcard
            )
    assert result.args == 'rm *'
    assert result.returncode == 0
    assert result.stdout == ''
    assert result.stderr == ''
    
    result = commands.run(
                'ls', 
                path=temp_dir,
                pushd=True,
            )
    assert result.args == ['ls']
    assert result.returncode == 0
    assert result.stdout == ''
    assert result.stderr == ''


def test_dry_run(temp_dir, fake_files, fake_xls_files_ls_output):
    result = commands.run(
                'rm *', 
                path=temp_dir,
                pushd=True,
                dry_run=True,
                shell=True  # needed for wildcard
            )
    assert result is None
    
    result = commands.run(
                'ls', 
                path=temp_dir,
                pushd=True,
            )
    assert result.args == ['ls']
    assert result.returncode == 0
    assert result.stdout == fake_xls_files_ls_output
    assert result.stderr == ''


def test_run_without_raise(temp_dir):
    result = commands.run(
                'ls dontexist', 
                path=temp_dir,
                pushd=True,
    )
    assert result.args == ['ls', 'dontexist']
    assert result.returncode == 1
    assert result.stdout == ''
    assert result.stderr == 'ls: dontexist: No such file or directory\n'


def test_run_with_raise(temp_dir):
    with pytest.raises(subprocess.CalledProcessError):
        result = commands.run(
                    'ls dontexist', 
                    path=temp_dir,
                    pushd=True,
                    raise_for_errors=True
        )


def test_confirmy():
    with patch( 'helpers.commands.input', side_effect=['y']):
        assert commands.confirm(make_sure=False) == True


def test_confirmn():
    with patch( 'helpers.commands.input', side_effect=['n']):
        assert commands.confirm(make_sure=False) == False


def test_confirmy_makesurey():
    with patch( 'helpers.commands.input', side_effect=['y', 'y']):
        assert commands.confirm(make_sure=True) == True


def test_confirmy_makesuren():
    with patch( 'helpers.commands.input', side_effect=['y', 'n']):
        assert commands.confirm(make_sure=True) == False
