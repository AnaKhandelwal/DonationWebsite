import random
from typing import List, Tuple
from models import UserProfile, Charity
from ml_engine import MLEngine


class CharityDatabase:
    """Simulated charity database with matching capabilities"""

    def __init__(self):
        self.charities = self._initialize_charities()
        self.ml_engine = MLEngine()

    def _initialize_charities(self) -> List[Charity]:
        """Initialize sample charity database"""
        charities = [
            Charity(
                id="water_org_001",
                name="Clean Water Global",
                category="water_sanitation",
                description="Provides clean water access to rural communities worldwide",
                location="global",
                efficiency_score=92.5,
                tags=["water", "health", "global", "sustainability", "children"],
                min_donation=5.0,
                impact_metrics={
                    "$5": "provides clean water for 2 people for 1 week",
                    "$25": "maintains a water pump for 1 month",
                    "$100": "contributes to building a new well"
                }
            ),
            Charity(
                id="edu_future_002",
                name="Education for Tomorrow",
                category="education",
                description="Funds educational programs and supplies for underprivileged children",
                location="national",
                efficiency_score=88.3,
                tags=["education", "children", "literacy", "opportunity", "local"],
                min_donation=10.0,
                impact_metrics={
                    "$10": "provides school supplies for 1 child for 1 month",
                    "$50": "sponsors a child's education for 1 month",
                    "$200": "funds a teacher's salary for 1 week"
                }
            ),
            Charity(
                id="green_earth_003",
                name="Green Earth Initiative",
                category="environment",
                description="Forest conservation and renewable energy projects",
                location="global",
                efficiency_score=85.7,
                tags=["environment", "climate", "forests", "renewable", "future"],
                min_donation=8.0,
                impact_metrics={
                    "$8": "plants and maintains 2 trees for 1 year",
                    "$40": "powers a rural home with solar for 1 month",
                    "$160": "protects 1 acre of rainforest"
                }
            ),
            Charity(
                id="hungry_no_more_004",
                name="Hungry No More",
                category="hunger",
                description="Provides meals and nutrition programs for food-insecure families",
                location="local",
                efficiency_score=94.2,
                tags=["hunger", "nutrition", "families", "local", "emergency"],
                min_donation=3.0,
                impact_metrics={
                    "$3": "provides 1 nutritious meal",
                    "$15": "feeds a family of 4 for 1 day",
                    "$90": "provides weekly groceries for a family for 1 month"
                }
            ),
            Charity(
                id="animal_rescue_005",
                name="Wildlife Protection Society",
                category="animals",
                description="Rescues and rehabilitates endangered wildlife",
                location="global",
                efficiency_score=87.9,
                tags=["animals", "wildlife", "conservation", "rescue", "habitat"],
                min_donation=12.0,
                impact_metrics={
                    "$12": "provides medical care for 1 rescued animal",
                    "$60": "maintains habitat protection for 1 month",
                    "$300": "funds a wildlife rescue operation"
                }
            )
        ]

        # Initialize ML fields for each charity
        for charity in charities:
            charity.semantic_keywords = []
            charity.description_embedding = [random.random() for _ in range(50)]
            charity.donor_retention_rate = random.uniform(0.7, 0.95)
            charity.predicted_impact_score = random.uniform(0.8, 1.0)
            charity.success_stories = [
                f"Thanks to donations, we helped {random.randint(100, 1000)} people this month",
                f"Your support made possible {random.randint(10, 50)} new projects"
            ]

        return charities

    def find_matches(self, user_profile: UserProfile) -> List[Tuple[Charity, float]]:
        """Enhanced charity matching using ML and NLP"""
        matches = []

        for charity in self.charities:
            # Traditional compatibility score
            base_score = self._calculate_compatibility(user_profile, charity)

            # ML enhancement: semantic similarity
            semantic_score = 0.0
            if user_profile.extracted_keywords:
                user_text = ' '.join(user_profile.extracted_keywords)
                semantic_score = self.ml_engine.calculate_semantic_similarity(
                    user_text, charity.description
                )

            # ML enhancement: predicted engagement
            engagement_bonus = user_profile.predicted_engagement_score * 0.1

            # ML enhancement: donor retention rate
            retention_bonus = charity.donor_retention_rate * 0.05

            # Combined ML-enhanced score
            final_score = (base_score * 0.7 +  # Traditional matching (70%)
                           semantic_score * 0.2 +  # Semantic similarity (20%)
                           engagement_bonus +  # User engagement prediction
                           retention_bonus)  # Charity retention rate

            if final_score > 0.3:  # Minimum threshold
                matches.append((charity, final_score))

        return sorted(matches, key=lambda x: x[1], reverse=True)

    def _calculate_compatibility(self, profile: UserProfile, charity: Charity) -> float:
        """Calculate compatibility score between user and charity"""
        score = 0.0

        # Interest matching (40% weight)
        interest_overlap = len(set(profile.interests) & set(charity.tags)) / len(profile.interests)
        score += interest_overlap * 0.4

        # Cause alignment (30% weight)
        if charity.category in [cause.lower().replace(" ", "_") for cause in profile.causes]:
            score += 0.3

        # Geographic preference (20% weight)
        if profile.geographic_preference == charity.location or charity.location == "global":
            score += 0.2

        # Efficiency score (10% weight)
        score += (charity.efficiency_score / 100) * 0.1

        return min(score, 1.0)