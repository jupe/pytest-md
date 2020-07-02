# pytest-md

Plugin for generating Markdown reports for [pytest] results 📝

[pytest]: https://github.com/pytest-dev/pytest

## Installation

**pytest-md** is available on [PyPI][PyPI] for Python versions 3.6 and newer
and can be installed into your enviroment from your terminal via [pip][pip]:

```text
$ pip install pytest-md
```

[PyPI]: https://pypi.org/
[pip]: https://pypi.org/project/pip/

## Usage

The following example code produces all of the different pytest test outcomes.

```python
import random
import pytest


def test_failed():
    assert "emoji" == "hello world"


@pytest.mark.xfail
def test_xfailed():
    assert random.random() == 1.0


@pytest.mark.xfail
def test_xpassed():
    assert 0.0 < random.random() < 1.0


@pytest.mark.skip(reason="don't run this test")
def test_skipped():
    assert "pytest-emoji" != ""


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Sara", "Hello Sara!"),
        ("Mat", "Hello Mat!"),
        ("Annie", "Hello Annie!"),
    ],
)
def test_passed(name, expected):
    assert f"Hello {name}!" == expected


@pytest.fixture
def number():
    return 1234 / 0


def test_error(number):
    assert number == number
```

With **pytest-md** installed, you can now generate a Markdown test report as
follows:

```text
$ pytest --md report.md
```

```Markdown
# Test Report

*Report generated on 25-Feb-2019 at 17:18:29 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

8 tests ran in 0.05 seconds

- 1 failed
- 3 passed
- 1 skipped
- 1 xfailed
- 1 xpassed
- 1 error
```

## pytest-emoji

**pytest-md** also integrates with [pytest-emoji], which allows us to include
emojis in the generated Markdown test report:

```text
$ pytest --emoji --md-verbose --md report.md
```

```Markdown
# Test Report

*Report generated on 25-Feb-2019 at 17:18:29 by [pytest-md]* 📝

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

8 tests ran in 0.06 seconds ⏱

- 1 failed 😰
- 3 passed 😃
- 1 skipped 🙄
- 1 xfailed 😞
- 1 xpassed 😲
- 1 error 😡
```

## pytest-metadata

**pytest-md** also integrates with [pytest-metadata], which allows us to include
metadata in the generated Markdown test report:

```text
$ pytest --md-metadata --metadata key=value
```

````markdown
# Test Report

*Report generated on 02-Jul-2020 at 14:11:48 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

8 tests ran in 0.08 seconds

- 1 error
- 1 failed
- 3 passed
- 1 skipped
- 1 xfailed
- 1 xpassed

## Metadata

Python: 3.7.7
Platform: Darwin-19.5.0-x86_64-i386-64bit
Packages
  pytest: 5.4.3
  py: 1.9.0
  pluggy: 0.13.1
key: value
Plugins
  metadata: 1.10.0

````

[pytest-emoji]: https://github.com/hackebrot/pytest-emoji
[pytest-metadata]: https://github.com/pytest-dev/pytest-metadata

## Credits

This project is inspired by the fantastic [pytest-html] plugin! 💻

[pytest-html]: https://github.com/pytest-dev/pytest-html

## Community

Would you like to contribute to **pytest-md**? You're awesome! 😃

Please check out the [good first issue][good first issue] label for tasks,
that are good candidates for your first contribution to **pytest-md**. Your
contributions are greatly appreciated! Every little bit helps, and credit
will always be given.

Please note that **pytest-md** is released with a [Contributor Code of
Conduct][code of conduct]. By participating in this project you agree to
abide by its terms.

Join the pytest-md [community][community]! 🌍🌏🌎

[good first issue]: https://github.com/hackebrot/pytest-md/labels/good%20first%20issue
[code of conduct]: https://github.com/hackebrot/pytest-md/blob/master/CODE_OF_CONDUCT.md
[community]: https://github.com/hackebrot/pytest-md/blob/master/COMMUNITY.md

## License

Distributed under the terms of the MIT license, **pytest-md** is free and open
source software.
