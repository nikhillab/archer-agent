# src/main.py

from crew import CloudArchitectureReviewCrew

import json

def main():

    with open("input/service_extraction.json", "r") as file:
        extracted_json = json.load(file)
        with open("input/ascii.txt", "r") as ascii:

            input_context = {
                "extracted_input_context": extracted_json,
                "ascii_input_context": ascii.read()
            }
        ascii.close()
    file.close()
    # print(input_context)

    print("🚀 Starting Cloud Architecture Review Crew...")

    # Initialize the Crew from your class
    crew_instance = CloudArchitectureReviewCrew()

    # Kick off the review process
    result = crew_instance.crew().kickoff(inputs=input_context)

    print("✅ Review completed.")
    print("\n--- Final Token Output ---\n")
    print(result.token_usage)
    


if __name__ == "__main__":
    main()
    
