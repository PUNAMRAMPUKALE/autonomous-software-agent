from agents.planner import PlannerAgent
from agents.github_agent import GitHubAgent
from agents.repository_analyzer import RepositoryAnalyzer
from agents.developer_agent import DeveloperAgent


def main():

    print("=" * 70)
    print("AUTONOMOUS SOFTWARE ENGINEERING AGENT")
    print("=" * 70)

    # --------------------------------------------------

    planner = PlannerAgent()

    state = planner.choose_next_story()

    if state is None:
        return

    # --------------------------------------------------

    github = GitHubAgent()

    state = github.prepare_repository(
        state
    )

    # --------------------------------------------------

    analyzer = RepositoryAnalyzer()

    state = analyzer.analyze(
        state
    )

    # --------------------------------------------------

    developer = DeveloperAgent()

    state = developer.prepare_task(
        state
    )

    # --------------------------------------------------

    planner.print_selected_story(
        state
    )

    developer.preview_prompt(
        state
    )

    # --------------------------------------------------

    print()

    print("=" * 70)

    print("PROJECT SUMMARY")

    print("=" * 70)

    print("Issue :", state.issue_key)

    print("Repository :", state.repository)

    print("Language :", state.language)

    print("Framework :", state.framework)

    print("Entry Point :", state.entry_point)

    print("Files :", len(state.source_files))

    print("=" * 70)


if __name__ == "__main__":
    main()