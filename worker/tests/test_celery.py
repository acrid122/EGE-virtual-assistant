from tasks import add
import pytest

def test_celery_task():
    result = add.delay(2, 3).get(timeout=10)
    assert result == 5