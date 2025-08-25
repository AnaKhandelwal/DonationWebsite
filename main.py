from typing import Dict, List, Optional, Tuple
from models import ImpactReport
from charity_database import CharityDatabase
from agents import OnboardingAgent, CurationAgent, DonationPlanningAgent, ImpactVisualizationAgent


class CharityMatchingAI:
    """Main orchestrating agent that coordinates all other agents"""

    def __init__(self):
        self.charity_db = CharityDatabase()
        self.onboarding_agent = OnboardingAgent()
        self.curation_agent = CurationAgent(self.charity_db)
        self.planning_agent = DonationPlanningAgent()
        self.impact_agent = ImpactVisualizationAgent()

    def run_full_process(self, user_responses: Dict[str, any]) -> ImpactReport:
        """Run the complete charity matching and donation process"""

        print("Welcome to AI-Powered Charity Matching!")
        print("=" * 50)

        # Step 1: Analyze interests through onboarding
        print("\nStep 1: Analyzing Your Interests...")
        user_profile = self.onboarding_agent.conduct_onboarding(user_responses)
        print(f"Profile created for {user_profile.name}!")

        # Step 2: Curate perfect match
        print("\nStep 2: Finding Your Perfect Charity Match...")
        perfect_match = self.curation_agent.find_perfect_match(user_profile)

        if not perfect_match:
            print("No suitable matches found. Please try adjusting your preferences.")
            return None

        # Step 3: Propose feel-good plan
        print("\nStep 3: Creating Your Personalized Donation Plan...")
        donation_plan = self.planning_agent.create_plan(user_profile, perfect_match)

        # Step 4: Simulate donation and show impact
        print("\nStep 4: Generating Your Impact Report...")
        print("Simulating 6 months of donations...")

        impact_report = self.impact_agent.generate_impact_report(donation_plan, months_donated=6)

        print(f"\nProcess Complete! You're now connected with {perfect_match.name}")
        print("Your donations are making a real difference in the world! 🌍")

        return impact_report


# Example usage and testing
def main():
    """Demonstrate the complete AI charity matching system"""

    # Sample user responses (in a real system, this would come from a UI)
    sample_responses = {
        'name': 'Mehak Salil',
        'free_text_interests': 'I like the concept of providing mid day meals to children and ensuring education for all girls.',
        'interests': ['sustainability', 'children', 'literacy', 'nutrition', 'rescue'],
        'causes': ['Education', 'Nutrition'],
        'income': 3,  # Index for $4000-6000 range
        'comfort_level': 'Just starting out',
        'frequency': 'Weekly',
        'geography': 'National'
    }

    # Initialize and run the AI system
    charity_ai = CharityMatchingAI()

    print("Sample User Responses:")
    for key, value in sample_responses.items():
        print(f"• {key}: {value}")

    # Run the complete process
    impact_report = charity_ai.run_full_process(sample_responses)

    return impact_report


if __name__ == "__main__":
    # Run the demonstration
    report = main()