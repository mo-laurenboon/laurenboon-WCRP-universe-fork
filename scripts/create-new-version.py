import argparse
import re
import sys
import os

def set_arg_parser():
    """
    Creates an argument parser to take the submitted issue body as an argument.

        :returns: Argument parser
    """
    parser = argparse.ArgumentParser(description="Version variable")
    parser.add_argument("number", help="The current release version")
    parser.add_argument("changes", help="Changes made on the previous commmit")
    args = parser.parse_args()
  
    return args

def split_version_components(number):
    """
    Splits the input version string into 3 integers

        :param number: The numerical part of the current version
        :returns: Each element of the current version as individual integers
    """
    version = number.split(".")
    major = int(version[0])
    minor = int(version[1])
    patch = int(version[2])

    return major, minor, patch


def determine_update_type(changes): 
    """
    Determines the type of release update that should be triggered based off of the previous commit

        :param changes: A list of changes made in the previous commit.
        :returns: The type of release update that should be triggered (patch, major, minor, undetermined)
    """
    changes = re.split(" |\n", changes)
    if not changes:
        update_type = "patch"
    if "R100" in changes:
        update_type = "major"
    if "X" in changes or "U" in changes:
        update_type = "undetermined"
    else:
        update_type = "minor"
    
    return update_type


def update_version(number, changes):
    """
    Updates each element of the current version based on the update type

        :param number: The numerical part of the current version
        :param update_type: major, minor or patch type release
        :returns: The new, complete numerical element of the version as a string
    """
    major, minor, patch = split_version_components(number)
    update_type = determine_update_type(changes)

    if update_type == "major":
        major += 1
        minor = patch = 0
    elif update_type == "minor":
        minor += 1
        patch = 0
    elif update_type == "patch":
        patch += 1
    elif update_type == "undetermined":
        print("WARNING: Merge conflict tor uncategorised change reported")
        sys.exit(1)
    else:
        print ("WARNING: update type not recognised")
        sys.exit(1)

    new_version = f"{major}.{minor}.{patch}"

    return new_version

def main():
    """
    Holds the main body of the script.

        :returns: None
    """
    args = set_arg_parser()
    number = args.number
    changes = args.changes
  
    new_version = update_version(number, changes)

    with open(os.environ["GITHUB_OUTPUT"], "a") as out:
        out.write(f"version={new_version}\n")

if __name__ == "__main__":
    main()
