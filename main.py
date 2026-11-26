"""Worst Superpower — make.fun entry.

Writes one line (128 characters, limit 140) inventing the most useless
superpower, to entry.txt in the output directory. Pure Python stdlib,
fully deterministic: the text is a fixed constant, no randomness, no
clock, no network, no input.
"""

import os

TEXT = (
    "I can teleport anything I touch to the exact spot it is already in, "
    "complete with a blinding flash, a thunderclap, and confetti."
)


def candidate_dirs():
    """Output directories to try, in order: MAKEFUN_OUTPUT_DIR first."""
    dirs = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        dirs.append(env_dir)
    dirs.append("/output")
    dirs.append(os.path.join(os.getcwd(), "output"))
    dirs.append(os.getcwd())
    return dirs


def main():
    payload = TEXT.encode("utf-8")
    last_error = None
    for directory in candidate_dirs():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "wb") as handle:
                handle.write(payload)
            return path
        except OSError as error:  # try the next candidate path
            last_error = error
    if last_error is not None:
        raise last_error


if __name__ == "__main__":
    main()
