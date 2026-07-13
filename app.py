from agents.github_agent import GitHubAgent
from agents.planner import PlannerAgent


def main():

    print("=" * 60)
    print("AUTONOMOUS SOFTWARE ENGINEERING AGENT")
    print("=" * 60)

    planner = PlannerAgent()

    state = planner.choose_next_story()

    if state is None:
        return

    github = GitHubAgent()

    state = github.prepare_repository(
        state,
    )

    print()

    planner.print_selected_story(
        state,
    )

    print()

    print("=" * 60)

    print("PROJECT")

    print(state.project_key)

    print()

    print("REPOSITORY")

    print(state.repository)

    print()

    print("DEFAULT BRANCH")

    print(state.branch)

    print()

    print("FEATURE BRANCH")

    print(state.feature_branch)

    print()

    print("LOCAL PATH")

    print(state.local_path)

    print("=" * 60)


if __name__ == "__main__":
    main()