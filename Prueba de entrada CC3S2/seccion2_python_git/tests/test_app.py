import pytest
import subprocess
import sys
from app.app import summarize


@pytest.fixture
def sample():
    return ["1", "2", "3"]


def test_ok(sample):
    # Caso normal
    result = summarize(sample)
    assert result["sum"] == 6.0
    assert result["avg"] == 2.0
    assert result["count"] == 3


def test_empty():
    # Caso borde: lista vacía
    with pytest.raises(Exception):
        summarize([])


def test_non_numeric():
    # Caso error: valor no numérico
    with pytest.raises(Exception):
        summarize(["a", "2"])


def test_cli_runs():
    # Ejecuta el CLI como si fuera "python -m app 1,2,3"
    result = subprocess.run(
        [sys.executable, "-m", "app", "1,2,3"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "sum=6.0" in result.stdout
    assert "avg=2.0" in result.stdout
    assert "count=3" in result.stdout
