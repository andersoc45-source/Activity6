"""Module 6: Individual Git and GitHub Practice.

Run this starter program, complete the TODO tasks, and commit your changes.
No outside packages are required.
"""


def show_project_info():
    """Display basic information about this version-control exercise."""
    project_name = "Caleb Anderson's GitHub Practice Project"
    version = "1.1"
    print(f"Project: {project_name}")
    print(f"Version: {version}")
    print("Git helps track changes in a software project.")


def show_git_workflow():
    """Print the basic sequence used in this exercise."""
    steps = [
        "1. Edit and save your Python file.",
        "2. Stage your changes with git add.",
        "3. Record a local commit with git commit.",
        "4. Upload your commit to GitHub with git push.",
    ]
    for step in steps:
        print(step)


def main():
    show_project_info()
    print()
    show_git_workflow()
    print()


if __name__ == "__main__":
    main()
    print("Saving your code to Git gives you a detailed history on how your code has changed over time.")
    print("It gives you the ability to roll back your code if you need a more stable build.")
    print()
    print("By committing your code, changes are seved to the local repository.")
    print("Changes are seved to an external repository when you push code.")
