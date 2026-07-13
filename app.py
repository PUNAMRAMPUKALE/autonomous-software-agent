from agents.github_agent import GitHubAgent
from agents.planner import PlannerAgent
from agents.repository_analyzer import RepositoryAnalyzer


def main():

    print("=" * 60)
    print("AUTONOMOUS SOFTWARE ENGINEERING AGENT")
    print("=" * 60)

    planner = PlannerAgent()

    state = planner.choose_next_story()

    if state is None:
        return

    github = GitHubAgent()

    state = github.prepare_repository(state)

    analyzer = RepositoryAnalyzer()

    state = analyzer.analyze(state)

    print()

    planner.print_selected_story(state)

    print()

    print("=" * 60)

    print("Repository :", state.repository)

    print("Language   :", state.language)

    print("Framework  :", state.framework)

    print("Tests      :", state.test_framework)

    print("Entry      :", state.entry_point)

    print("README     :", state.readme)

    print()

    print("Project Structure")

    for folder in state.project_structure:

        print("-", folder)

    print()

    print("Implementation Plan")

    for step in state.implementation_plan:

        print("-", step)

    print("=" * 60)


if __name__ == "__main__":
    main()