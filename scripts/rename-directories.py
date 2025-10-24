import argparse
import os

def set_arg_parser():
    """
    Creates an argument parser to take the submitted issue body as an argument.

        :returns: Argument parser
    """
    parser = argparse.ArgumentParser(description="Target and replacement characters")
    parser.add_argument("target_dir", help="The target directory to act as the root")
    parser.add_argument("target_character", help="The character that will be replaced")
    parser.add_argument("new_character", help="The character that the target will be replaced with")
    args = parser.parse_args()
  
    return args


def get_number_of_matches(args):
    total_count = 0
    for dirpath, dirnames, _ in os.walk(args.target_dir):
        for dirname in dirnames:
            if args.target_character in dirname:
                total_count += 1

    return total_count


def get_new_paths(dirpath, dirname, target, new):
    old_path = os.path.join(dirpath, dirname)
    new_name = dirname.replace(target, new)
    new_path = os.path.join(dirpath, new_name)
    
    return old_path, new_path


def main():
    args = set_arg_parser()
    total_count = get_number_of_matches(args)
    renamed_count = 0

    for dirpath, dirnames, _ in os.walk(args.target_dir):
        for dirname in dirnames:
            if args.target_character in dirname:
                old_path, new_path = get_new_paths(dirpath, dirname, args.target_character, args.new_character)

                if os.path.exists(new_path):
                    print(f"Skipping: {new_path} already exists.")
                    continue
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} to {new_path}")
                    renamed_count += 1
                except Exception as e:
                    print(f"WARNING: Error renaming {old_path}: {e}")
                    quit()
    print(f"{renamed_count}/{total_count} directoires successflly renamed")
    
if __name__ == "__main__":
    main()
