import os.path
import subprocess
import sys
from pathlib import Path

COOKIECUTTER_BASEDIR = "{{ cookiecutter.project_name }}"


def python_files() -> list[str]:
    git_output: str = subprocess.getoutput("git ls-files")
    filenames = [line for line in git_output.split("\n") if line]
    return [
        filename[len(COOKIECUTTER_BASEDIR) + 1 :]
        for filename in filenames
        if filename.startswith(COOKIECUTTER_BASEDIR)
    ]


def create_symlinks(filenames: list[str]) -> bool:
    django_template_dir = Path("django")
    original_dir = Path(COOKIECUTTER_BASEDIR)
    changed_something = False
    for filename in filenames:
        django_file = django_template_dir / COOKIECUTTER_BASEDIR / filename
        if django_file.is_symlink():
            print(f"Symlink: {django_file}")
            continue
        if django_file.is_file():
            print(f"Custom:  {django_file}")
            print(f"    diff -u '{original_dir / filename}' '{django_file}'")
            continue
        # Create symlink (and possibly directory)
        django_file.parent.mkdir(parents=True, exist_ok=True)
        target = original_dir / filename
        our_relative_dir = [".."] * len(django_file.parent.parents)
        relative_target = os.path.join(*our_relative_dir, target)
        django_file.symlink_to(relative_target)
        print(f"CREATED: {django_file}")
        changed_something = True
    return changed_something


def check_for_dead_symlinks():
    for root, dirs, files in Path("django").walk():
        d = Path(root)  # d = directory
        for f in files:  # f = file
            if not (d / f).exists():
                print(f"BROKEN symlink '{d / f}'")


if __name__ == "__main__":
    changed_something = create_symlinks(python_files())
    if changed_something:
        # Exit with error code: that way we can be run as check in a github action.
        sys.exit("Some symlinks were created")
    check_for_dead_symlinks()
