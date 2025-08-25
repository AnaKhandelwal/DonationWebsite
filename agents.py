from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from models import UserProfile, Charity, DonationPlan, ImpactReport
from nlp_processor import NLPProcessor
from ml_engine import MLEngine
from charity_database import CharityDatabase


class OnboardingAgent:
    """Enhanced onboarding with NLP text analysis"""

    def __init__(self):
        self.questions = self._define_questions()
        self.nlp_processor = NLPProcessor()
        self.ml_engine = MLEngine()

    def _define_questions(self) -> List[Dict[str, any]]:
        """Define onboarding questions"""
        return [
            {
                "id": "name",
                "question": "What's your name?",
                "type": "text",
                "required": True
            },
            {
                "id": "free_text_interests",
                "question": "Tell me about what you're passionate about and what drives you to want to make a difference in the world. (Free text - be as detailed as you'd like!)",
                "type": "long_text",
                "required": True
            },
            {
                "id": "interests",
                "question": "What are you passionate about? (Select all that apply)",
                "type": "multiple_choice",
                "options": ["health", "education", "environment", "animals", "technology",
                            "arts", "sports", "children", "elderly", "community"],
                "required": True
            },
            {
                "id": "causes",
                "question": "Which causes matter most to you?",
                "type": "multiple_choice",
                "options": ["Water & Sanitation", "Education", "Environment", "Hunger Relief",
                            "Animal Welfare", "Healthcare", "Disaster Relief", "Human Rights"],
                "required": True
            },
            {
                "id": "income",
                "question": "What's your approximate monthly income? (This helps us suggest appropriate amounts)",
                "type": "range",
                "ranges": [(0, 2000), (2000, 4000), (4000, 6000), (6000, 10000), (10000, float('inf'))],
                "required": True
            },
            {
                "id": "comfort_level",
                "question": "How comfortable are you with regular donations?",
                "type": "single_choice",
                "options": ["Just starting out", "Occasional donor", "Regular supporter"],
                "required": True
            },
            {
                "id": "frequency",
                "question": "How often would you prefer to donate?",
                "type": "single_choice",
                "options": ["Weekly", "Monthly", "Quarterly"],
                "required": True
            },
            {
                "id": "geography",
                "question": "Where would you like your impact to be?",
                "type": "single_choice",
                "options": ["Local community", "National", "Global"],
                "required": True
            }
        ]

    def conduct_onboarding(self, responses: Dict[str, any]) -> UserProfile:
        """Enhanced onboarding with NLP analysis of free text"""

        # Traditional profile creation
        comfort_mapping = {
            "Just starting out": "low",
            "Occasional donor": "medium",
            "Regular supporter": "high"
        }

        frequency_mapping = {
            "Weekly": "weekly",
            "Monthly": "monthly",
            "Quarterly": "quarterly"
        }

        geo_mapping = {
            "Local community": "local",
            "National": "national",
            "Global": "global"
        }

        # Estimate income from range
        income_ranges = [(0, 2000), (2000, 4000), (4000, 6000), (6000, 10000), (10000, 20000)]
        income_range = income_ranges[responses['income']]
        estimated_income = (income_range[0] + income_range[1]) / 2

        # NEW: NLP Analysis of free text
        nlp_results = {}
        if 'free_text_interests' in responses and responses['free_text_interests']:
            print("Analyzing your passions using NLP...")
            nlp_results = self.nlp_processor.extract_interests_from_text(responses['free_text_interests'])
            print(f"Discovered personality traits: {list(nlp_results.get('personality_traits', {}).keys())}")
            print(f"Extracted keywords: {nlp_results.get('keywords', [])[:5]}")

        # Create enhanced profile
        profile = UserProfile(
            name=responses['name'],
            interests=responses['interests'],
            causes=responses['causes'],
            monthly_income=estimated_income,
            donation_comfort_level=comfort_mapping[responses['comfort_level']],
            preferred_frequency=frequency_mapping[responses['frequency']],
            geographic_preference=geo_mapping[responses['geography']],
            # NEW: NLP-enhanced fields
            personality_traits=nlp_results.get('personality_traits', {}),
            emotional_drivers=nlp_results.get('emotional_drivers', []),
            giving_history_sentiment=nlp_results.get('sentiment', 0.0),
            extracted_keywords=nlp_results.get('keywords', [])
        )

        # NEW: ML Prediction of engagement score
        profile.predicted_engagement_score = self.ml_engine.predict_engagement_score(profile)
        print(f"Predicted engagement score: {profile.predicted_engagement_score:.2f}")

        return profile


class CurationAgent:
    """Enhanced charity matching using ML and NLP"""

    def __init__(self, charity_db: CharityDatabase):
        self.charity_db = charity_db

    def find_perfect_match(self, user_profile: UserProfile) -> Optional[Charity]:
        """Find the single best charity match using ML-enhanced scoring"""
        matches = self.charity_db.find_matches(user_profile)

        if not matches:
            return None

        best_match, score = matches[0]

        print(f"AI-Enhanced Perfect Match Found!")
        print(f"Overall ML Score: {score:.1%}")
        print(f"Charity: {best_match.name}")
        print(f"Predicted Impact Score: {best_match.predicted_impact_score:.2f}")
        print(f"Donor Retention Rate: {best_match.donor_retention_rate:.1%}")

        # Enhanced explanation using NLP insights
        explanation = self._generate_ai_explanation(user_profile, best_match, score)
        print(f"AI Analysis: {explanation}")

        return best_match

    def _generate_ai_explanation(self, profile: UserProfile, charity: Charity, score: float) -> str:
        """Generate AI-powered explanation using NLP insights"""
        explanations = []

        # Traditional matching reasons
        common_interests = set(profile.interests) & set(charity.tags)
        if common_interests:
            explanations.append(f"interests alignment in {', '.join(common_interests)}")

        # NEW: NLP-based explanations
        if profile.personality_traits:
            top_trait = max(profile.personality_traits.items(), key=lambda x: x[1])
            if top_trait[1] > 0.3:
                explanations.append(f"matches your {top_trait[0]} personality")

        if profile.emotional_drivers:
            explanations.append(f"aligns with your emotional drivers: {', '.join(profile.emotional_drivers[:2])}")

        # NEW: ML-based explanations
        if charity.predicted_impact_score > 0.9:
            explanations.append("high predicted impact potential")

        if charity.donor_retention_rate > 0.85:
            explanations.append("excellent donor satisfaction history")

        return "; ".join(explanations) if explanations else "strong overall compatibility"


class DonationPlanningAgent:
    """ML-enhanced donation planning for optimal engagement"""

    def __init__(self):
        self.ml_engine = MLEngine()

    def create_plan(self, user_profile: UserProfile, charity: Charity) -> DonationPlan:
        """Create ML-optimized donation plan"""

        # Traditional calculation
        base_amount = self._calculate_suggested_amount(user_profile)

        # NEW: ML optimization for maximum engagement
        print("Optimizing donation amount using ML...")
        optimized_amount = self.ml_engine.optimize_donation_amount(user_profile, base_amount)

        # Ensure minimum requirements
        final_amount = max(optimized_amount, charity.min_donation)

        # Calculate annual total
        frequency_multiplier = {"weekly": 52, "monthly": 12, "quarterly": 4}
        annual_total = final_amount * frequency_multiplier[user_profile.preferred_frequency]

        # NEW: AI-generated impact description considering user psychology
        impact_desc = self._generate_personalized_impact_description(
            charity, final_amount, user_profile
        )

        plan = DonationPlan(
            charity=charity,
            amount=final_amount,
            frequency=user_profile.preferred_frequency,
            annual_total=annual_total,
            impact_description=impact_desc
        )

        print(f"\nML-Optimized Donation Plan")
        print(f"Original suggestion: ${base_amount:.2f}")
        print(f"ML-optimized amount: ${final_amount:.2f} {user_profile.preferred_frequency}")
        print(f"Annual Total: ${annual_total:.2f}")
        print(f"Personalized Impact: {impact_desc}")
        print(f"Engagement-optimized for your profile: {user_profile.predicted_engagement_score:.2f}")

        return plan

    def _generate_personalized_impact_description(self, charity: Charity, amount: float, profile: UserProfile) -> str:
        """Generate AI-personalized impact description based on user psychology"""

        # Base impact description
        base_impact = self._generate_impact_description(charity, amount, profile.preferred_frequency)

        # NEW: Personalization based on NLP insights
        if profile.personality_traits:
            top_trait = max(profile.personality_traits.items(), key=lambda x: x[1])

            if top_trait[0] == 'empathetic' and top_trait[1] > 0.3:
                # Add emotional connection for empathetic users
                base_impact += f" - directly touching lives in your community"
            elif top_trait[0] == 'analytical' and top_trait[1] > 0.3:
                # Add concrete metrics for analytical users
                efficiency = charity.efficiency_score
                base_impact += f" with {efficiency:.1f}% efficiency rating"
            elif top_trait[0] == 'activist' and top_trait[1] > 0.3:
                # Add change-focused language for activists
                base_impact += f" - driving systemic change"

        # NEW: Emotional driver personalization
        if profile.emotional_drivers:
            if 'hope' in profile.emotional_drivers:
                base_impact += f" building a better future"
            elif 'responsibility' in profile.emotional_drivers:
                base_impact += f" fulfilling your commitment to change"

        return base_impact

    def _calculate_suggested_amount(self, profile: UserProfile) -> float:
        """Calculate psychologically comfortable donation amount"""

        # Base percentage of monthly income
        comfort_percentages = {
            "low": 0.002,  # 0.2% of monthly income
            "medium": 0.005,  # 0.5% of monthly income
            "high": 0.01  # 1.0% of monthly income
        }

        base_amount = profile.monthly_income * comfort_percentages[profile.donation_comfort_level]

        # Adjust for frequency
        frequency_divisors = {"weekly": 4, "monthly": 1, "quarterly": 0.33}
        suggested = base_amount * frequency_divisors[profile.preferred_frequency]

        # Round to psychologically friendly amounts
        if suggested < 5:
            return 5
        elif suggested < 10:
            return round(suggested)
        else:
            return round(suggested / 5) * 5  # Round to nearest $5

    def _generate_impact_description(self, charity: Charity, amount: float, frequency: str) -> str:
        """Generate compelling impact description"""

        # Find the best matching impact metric
        impact_amounts = [float(key.replace(",", "").replace("$", "")) for key in charity.impact_metrics.keys()]
        closest_amount = min(impact_amounts, key=lambda x: abs(x - amount))

        base_impact = charity.impact_metrics[f"${closest_amount:.0f}"]

        # Scale for frequency
        frequency_text = {"weekly": "Every week", "monthly": "Every month", "quarterly": "Every quarter"}

        return f"{frequency_text[frequency]}, your ${amount:.2f} {base_impact}"


class ImpactVisualizationAgent:
    """Creates visual impact reports and proof of donation effectiveness"""

    def generate_impact_report(self, donation_plan: DonationPlan, months_donated: int = 6) -> ImpactReport:
        """Generate comprehensive impact report with visualizations"""

        # Calculate total impact over time
        frequency_multiplier = {"weekly": 4.33, "monthly": 1, "quarterly": 0.33}
        donations_per_month = frequency_multiplier[donation_plan.frequency]
        total_donated = donation_plan.amount * donations_per_month * months_donated

        # Generate impact metrics
        impact_metrics = self._calculate_impact_metrics(donation_plan.charity, total_donated)

        # Estimate beneficiaries helped
        beneficiaries = self._estimate_beneficiaries(donation_plan.charity, total_donated)

        # Create timeline
        timeline = self._generate_timeline(donation_plan, months_donated)

        report = ImpactReport(
            charity_name=donation_plan.charity.name,
            total_donated=total_donated,
            impact_metrics=impact_metrics,
            beneficiaries_helped=beneficiaries,
            timeline=timeline
        )

        # Generate visualizations
        self._create_visualizations(report)

        return report

    def _calculate_impact_metrics(self, charity: Charity, total_amount: float) -> Dict[str, float]:
        """Calculate concrete impact metrics"""

        metrics = {}

        if charity.category == "water_sanitation":
            metrics["people_served"] = total_amount / 2.5  # $2.50 per person per week
            metrics["weeks_of_access"] = total_amount / 2.5
            metrics["wells_supported"] = total_amount / 100  # $100 per well access point

        elif charity.category == "education":
            metrics["children_supported"] = total_amount / 50  # $50 per child per month
            metrics["school_supplies_provided"] = total_amount / 10  # $10 per child supplies
            metrics["teacher_hours_funded"] = total_amount / 28.57  # $200/week = $28.57/hour

        elif charity.category == "environment":
            metrics["trees_planted"] = total_amount / 4  # $4 per tree
            metrics["acres_protected"] = total_amount / 160  # $160 per acre
            metrics["solar_powered_days"] = total_amount / 1.33  # $40/month = $1.33/day

        elif charity.category == "hunger":
            metrics["meals_provided"] = total_amount / 3  # $3 per meal
            metrics["families_fed"] = total_amount / 15  # $15 per family per day
            metrics["grocery_weeks_funded"] = total_amount / 22.5  # $90/month = $22.5/week

        elif charity.category == "animals":
            metrics["animals_treated"] = total_amount / 12  # $12 per treatment
            metrics["habitat_protection_days"] = total_amount / 2  # $60/month = $2/day
            metrics["rescue_operations"] = total_amount / 300  # $300 per operation

        return metrics

    def _estimate_beneficiaries(self, charity: Charity, total_amount: float) -> int:
        """Estimate total number of beneficiaries helped"""

        beneficiary_rates = {
            "water_sanitation": 2.5,  # $2.50 per person
            "education": 50,  # $50 per child
            "environment": 100,  # $100 per community impacted
            "hunger": 15,  # $15 per family
            "animals": 12  # $12 per animal
        }

        rate = beneficiary_rates.get(charity.category, 25)  # Default rate
        return int(total_amount / rate)

    def _generate_timeline(self, plan: DonationPlan, months: int) -> List[Dict[str, any]]:
        """Generate donation timeline with milestones"""

        timeline = []
        current_date = datetime.now()

        frequency_days = {"weekly": 7, "monthly": 30, "quarterly": 90}
        days_between = frequency_days[plan.frequency]

        cumulative_amount = 0

        for i in range(months * (30 // days_between)):
            donation_date = current_date - timedelta(days=i * days_between)
            cumulative_amount += plan.amount

            # Add milestone events
            milestone = None
            if i % 5 == 4:  # Every 5th donation
                milestone = self._generate_milestone(plan.charity, cumulative_amount)

            timeline.append({
                "date": donation_date.strftime("%Y-%m-%d"),
                "amount": plan.amount,
                "cumulative": cumulative_amount,
                "milestone": milestone
            })

        return list(reversed(timeline))  # Chronological order

    def _generate_milestone(self, charity: Charity, cumulative_amount: float) -> str:
        """Generate milestone descriptions"""

        milestones = {
            "water_sanitation": [
                "Milestone: Provided clean water for 10 people for a month!",
                "Milestone: Supported maintenance of a water pump for a full month!",
                "Milestone: Contributed to building a new well access point!"
            ],
            "education": [
                "Milestone: Provided school supplies for an entire classroom!",
                "Milestone: Sponsored a child's education for a full semester!",
                "Milestone: Funded a week of teacher training!"
            ],
            "environment": [
                "Milestone: Planted a small forest of 25 trees!",
                "Milestone: Protected an acre of rainforest!",
                "Milestone: Powered a village with solar for a month!"
            ]
        }

        charity_milestones = milestones.get(charity.category, ["Milestone: Making a real difference!"])

        # Choose milestone based on amount
        if cumulative_amount > 200:
            return charity_milestones[-1]
        elif cumulative_amount > 100:
            return charity_milestones[-2] if len(charity_milestones) > 1 else charity_milestones[0]
        else:
            return charity_milestones[0]

    def _create_visualizations(self, report: ImpactReport):
        """Create visual impact charts"""

        # Create figure with subplots
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle(f'Your Impact with {report.charity_name}', fontsize=16, fontweight='bold')

        # 1. Cumulative donations over time
        dates = [item['date'] for item in report.timeline]
        cumulative = [item['cumulative'] for item in report.timeline]

        ax1.plot(range(len(dates)), cumulative, 'b-', linewidth=3, marker='o', markersize=4)
        ax1.set_title('Your Donations Over Time')
        ax1.set_xlabel('Donation Number')
        ax1.set_ylabel('Cumulative Amount ($)')
        ax1.grid(True, alpha=0.3)
        ax1.fill_between(range(len(dates)), cumulative, alpha=0.3)

        # 2. Impact metrics pie chart
        if report.impact_metrics:
            metrics_names = list(report.impact_metrics.keys())[:4]  # Top 4 metrics
            metrics_values = [report.impact_metrics[name] for name in metrics_names]

            # Clean up names for display
            clean_names = [name.replace('_', ' ').title() for name in metrics_names]

            ax2.pie(metrics_values, labels=clean_names, autopct='%1.0f', startangle=90)
            ax2.set_title('Impact Breakdown')

        # 3. Beneficiaries helped
        ax3.bar(['People Helped'], [report.beneficiaries_helped],
                color='green', alpha=0.7, width=0.5)
        ax3.set_title('Lives Impacted')
        ax3.set_ylabel('Number of Beneficiaries')

        # Add value labels on bars
        for i, v in enumerate([report.beneficiaries_helped]):
            ax3.text(i, v + 0.1, str(int(v)), ha='center', va='bottom', fontweight='bold')

        # 4. Donation frequency visualization
        donation_amounts = [item['amount'] for item in report.timeline]
        ax4.hist(donation_amounts, bins=10, color='purple', alpha=0.7, edgecolor='black')
        ax4.set_title('Donation Amount Distribution')
        ax4.set_xlabel('Donation Amount ($)')
        ax4.set_ylabel('Frequency')

        plt.tight_layout()
        plt.show()

        # Print summary statistics
        print(f"\nImpact Summary for {report.charity_name}")
        print(f"Total Donated: ${report.total_donated:.2f}")
        print(f"Beneficiaries Helped: {report.beneficiaries_helped:,}")
        print(f"Donations Made: {len(report.timeline)}")

        if report.impact_metrics:
            print(f"\nSpecific Impact:")
            for metric, value in report.impact_metrics.items():
                clean_name = metric.replace('_', ' ').title()
                print(f"• {clean_name}: {value:.1f}")