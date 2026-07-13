from tools.git_operations import GitOperations

REPOSITORY = r"C:\Users\punam\autonomous-software-agent"

git = GitOperations(REPOSITORY)

print("=" * 70)
print("STATUS")
print("=" * 70)

git.status()