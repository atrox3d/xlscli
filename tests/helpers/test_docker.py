from time import sleep

import pytest
from helpers import docker


def test_check_yml():
    assert docker.check_yml() == None


# @pytest.mark.slow
def test_docker_compose_ps_two_containers():
    docker.db_up()
    sleep(1)
    containers = docker.docker_compose_ps()
    assert len(containers) == 2
    docker.db_down()
    containers = docker.docker_compose_ps()
    assert containers is None


def test_docker_compose_ps_no_containers():
    docker.db_down()
    assert docker.docker_compose_ps() is None