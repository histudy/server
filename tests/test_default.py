import pytest
# import re

def test_ufw_is_installed(host):
    pkg = host.package("ufw")
    assert pkg.is_installed


@pytest.mark.parametrize("name", [
    "mackerel-agent",
    "mackerel-agent-plugins",
    "mackerel-check-plugins",
    "mkr",
])
def test_mackerel_is_installed(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


def test_nginx_is_installed(host):
    pkg = host.package("nginx")
    assert pkg.is_installed


@pytest.mark.parametrize("name", [
    "dehydrated",
    "lexicon",
])
def test_dehydrated_is_installed(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


def test_nginx_is_installed(host):
    pkg = host.package("nginx")
    assert pkg.is_installed


def test_nginx_running_and_enabled(host):
    service = host.service("nginx")
    assert service.is_running
    assert service.is_enabled


def test_mackerel_running_and_enabled(host):
    service = host.service("mackerel-agent")
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("name", [
    "histudy",
    "kakogawa_infra",
    "webadmin"
])
def test_group_exists(host, name):
    group = host.group(name)
    assert group.exists


@pytest.mark.parametrize("name,shell", [
    ("wate", "/bin/bash"),
    ("sperkbird", "/bin/bash"),
    ("223n", "/bin/bash"),
    ("fu7mu4", "/bin/bash"),
    ("nogajun", "/bin/bash"),
])
def test_user_exists(host, name, shell):
    user = host.user(name)
    assert user
    assert user.shell == shell

@pytest.mark.parametrize("name", [
    "wate",
    "sperkbird",
])
def test_admin_user(host, name):
    user = host.user(name)
    assert 'adm' in user.groups
