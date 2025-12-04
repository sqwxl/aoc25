import importlib.util
import sys
import time
from pathlib import Path

input_path = Path("inputs")
solution_path = Path("solutions")


def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    assert spec
    assert spec.loader

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def run_solver(solver, text: str, ab: str | None = None):
    for part in ["a", "b"]:
        if ab is None or ab == part:
            t0 = time.perf_counter()
            result = getattr(solver, part)(text)
            t1 = time.perf_counter()
            print(f"{part}: {result} ({(t1 - t0) * 1000:.2f}ms)")


def solve(data: Path, ab: str | None = None):
    solver = import_from_path(data.name, solution_path / f"s{data.name}.py")
    text = data.read_text().strip()
    run_solver(solver, text, ab)


def main():
    if len(sys.argv) > 1:
        day = sys.argv[1]
        ab = sys.argv[2] if len(sys.argv) > 2 else None

        if not sys.stdin.isatty():
            text = sys.stdin.read().strip()
            solver = import_from_path(day, solution_path / f"s{day}.py")
            run_solver(solver, text, ab)
        else:
            solve(input_path / day, ab)
        return

    for i in input_path.iterdir():
        solve(i)


if __name__ == "__main__":
    main()
