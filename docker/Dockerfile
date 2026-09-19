# Minimal image for running the prime_checker CLI.
#
# Build:
#   docker build -f docker/Dockerfile -t prime-checker .
# Run:
#   docker run --rm prime-checker 97 --method known-primes

FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src/ src/

RUN pip install --no-cache-dir .

ENTRYPOINT ["prime-check"]
CMD ["97"]
