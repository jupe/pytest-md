from typing import Pattern


def test_generate_report(testdir, cli_options, report_path, report_content):
    """Check the contents of a generated Markdown report."""
    # run pytest with the following CLI options
    result = testdir.runpytest(*cli_options, "--md", f"{report_path}")

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1

    report = report_path.read_text()

    # Check the generated Markdown report
    if isinstance(report_content, Pattern):
        assert report_content.match(report)
    else:
        assert report == report_content
