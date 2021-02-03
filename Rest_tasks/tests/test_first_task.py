import requests
import task1
import pytest

def test_create_folder():
    assert task1.create_folder().status_code == 201
    assert task1.check_folder().status_code == 200

def test_delete_folder():
    assert task1.delete_folder().status_code == 204

def test_check_folder():
    assert task1.check_folder().status_code == 404