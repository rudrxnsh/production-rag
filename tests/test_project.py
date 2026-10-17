from importlib.metadata import version


def test_project_metadata_is_available():
    assert version("production-rag") == "0.1.0"
