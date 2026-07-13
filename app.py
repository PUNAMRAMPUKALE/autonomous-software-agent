from agents.planner import PlannerAgent
from agents.github_agent import GitHubAgent
from agents.repository_analyzer import RepositoryAnalyzer
from agents.developer_agent import DeveloperAgent
from agents.indexing_agent import IndexingAgent


def main():

    print("=" * 70)
    print("AUTONOMOUS SOFTWARE ENGINEERING AGENT")
    print("=" * 70)

    planner = PlannerAgent()

    state = planner.choose_next_story()

    if state is None:
        return

    github = GitHubAgent()

    state = github.prepare_repository(state)

    analyzer = RepositoryAnalyzer()

    state = analyzer.analyze(state)

    developer = DeveloperAgent()

    state = developer.prepare_task(state)

    indexer = IndexingAgent()

    state = indexer.build_index(state)

    planner.print_selected_story(state)

    developer.preview_prompt(state)

    print()

    print("=" * 70)

    print("REPOSITORY SUMMARY")

    print("=" * 70)

    print(f"Issue              : {state.issue_key}")
    print(f"Language           : {state.language}")
    print(f"Framework          : {state.framework}")
    print(f"Entry Point        : {state.entry_point}")
    print(f"Source Files       : {len(state.source_files)}")
    print(f"Indexed Symbols    : {len(state.symbols)}")

    print("=" * 70)


if __name__ == "__main__":
    main()