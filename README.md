# Python mocking workshop

A workshop to introduce some concepts around mocking in python covering:

- Mocking functions (`mock.patch`)
- Mocking methods on classes (`mock.patch.object`)
- Mocking HTTP requests [responses](https://github.com/getsentry/responses)

## Getting started

```sh
cd $HOME/workspace
git clone ssh://git@bitbucket.bip.uk.fid-intl.com/acet/python-mocking-workshop.git
cd python-mocking-workshop
# Install deps
poetry install
# Open in vscode
code .
```

**Note**: Feel free to commit your solutions on a branch `git checkout -b <branch_name>` but we want to keep `main` nice and clean for everyone going through the exercise.


## The rules

1. You **MUST** make all the tests pass (approach them 1 at a time and remove `pytest.mark.skip()` to enable the next test).
2. You **MUST NOT** change anything in `code.py` or `module.py`
3. You **MUST NOT** change any `assert` statements

Basically, all you can do to make the tests pass is use some form of mocking.

To run the tests:

```sh
just test
```

If you want to double check linting errors etc:

```sh
just format lint
```

## Troubleshooting Note

If you have any issues with running `poetry install`, it may be that you are on an old version of Poetry, which does not fully understand the `pyproject.toml` in this project.

The error will look something like this:

```
RuntimeError

  The Poetry configuration is invalid:
    - Additional properties are not allowed ('group' was unexpected)
  

  at ~/.poetry/lib/poetry/_vendor/py3.10/poetry/core/factory.py:43 in create_poetry
       39│             message = ""
       40│             for error in check_result["errors"]:
       41│                 message += "  - {}\n".format(error)
       42│ 
    →  43│             raise RuntimeError("The Poetry configuration is invalid:\n" + message)
       44│ 
       45│         # Load package
       46│         name = local_config["name"]
       47│         version = local_config["version"]
```

You should be able to resolve this by removing the old version and then reinstalling it.


To remove/uninstall Poetry, run:

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - --uninstall`


Then, to reinstall Poetry, run these two commands:

`pip3 config set global.cert "${HOME}/certs/fil-combined.pem"`

`curl -sSL https://install.python-poetry.org | SSL_CERT_FILE="${HOME}/certs/fil-combined.pem" POETRY_HOME=$HOME/.poetry python3 -`


