from agents.planner import PlannerAgent


def main():

    planner = PlannerAgent()

    story = planner.choose_next_story()

    if story:

        print()

        print("Planner finished.")

        planner.print_selected_story(
            story
        )


if __name__ == "__main__":
    main()