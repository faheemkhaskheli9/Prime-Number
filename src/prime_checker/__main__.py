"""Allows ``python -m prime_checker ...`` to work."""

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())
