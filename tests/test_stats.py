import pytest
from redactor import writeStats


def test_writeStats(tmp_path):
    # Create a temporary stats file
    stats_file = tmp_path / "stats.txt"
    # Call the function with the temporary stats file
    writeStats([str(stats_file)])

    # Read the content of the stats file
    with open(stats_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "Number of phone numbers that are redacted:"
