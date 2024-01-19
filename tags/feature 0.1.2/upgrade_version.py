import sys

def increment_version(version, component):
    """
    Increments the specified component of the given semantic version.

    Args:
    - version (str): The semantic version (e.g., "1.2.3").
    - component (str): The component to increment ("major", "minor", or "patch").

    Returns:
    - str: The updated semantic version.
    """
    major, minor, patch = map(int, version.split('.'))
    
    if component == 'major':
        major += 1
        minor = 0
        patch = 0
    elif component == 'minor':
        minor += 1
        patch = 0
    elif component == 'patch':
        patch += 1
    else:
        raise ValueError("Invalid component. Use 'major', 'minor', or 'patch'.")

    return f"{major}.{minor}.{patch}"

def main():
    if len(sys.argv) != 3:
        print("Usage: python upgrade_version.py <current_version> <component>")
        sys.exit(1)

    current_version = sys.argv[1]
    component = sys.argv[2]

    try:
        new_version = increment_version(current_version, component)
        print(f"Upgraded {component} version. New version: {new_version}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
