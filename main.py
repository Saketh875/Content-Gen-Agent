import argparse
from orchestrator import Orchestrator
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="GenEZ CLI")
    parser.add_argument("--topic", type=str, help="Topic for the campaign", required=False)
    args = parser.parse_args()

    print("Welcome to GenEZ!")
    
    orchestrator = Orchestrator()
    
    if args.topic:
        orchestrator.run_campaign(args.topic)
    else:
        print("No topic provided. Use --topic to start a campaign.")

if __name__ == "__main__":
    main()
