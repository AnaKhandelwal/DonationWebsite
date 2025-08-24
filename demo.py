# Charity AI Matching Platform - Complete Implementation

import json
import sqlite3
import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random


# Data Models
@dataclass
class Charity:
    id: int
    name: str
    category: str
    description: str
    efficiency_rating: float  # 0-100
    location: str
    impact_metric: str  # e.g., "meals provided", "trees planted"
    cost_per_impact: float  # cost per unit of impact


@dataclass
class UserProfile:
    interests: List[str]
    income_range: str
    donation_frequency: str
    causes_passionate_about: List[str]
    geographic_preference: str


@dataclass
class DonationPlan:
    charity: Charity
    monthly_amount: float
    impact_per_month: float
    total_annual_impact: float
    confidence_score: float


class CharityDatabase:
    """Manages charity data and provides search functionality"""

    def _init_(self):
        self.charities = self._load_sample_charities()
        self.embeddings = None
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self._generate_embeddings()

    def _load_sample_charities(self) -> List[Charity]:
        """Load sample charity data"""
        sample_data = [
            Charity(1, "Clean Water Initiative", "Water & Sanitation",
                    "Provides clean water access to rural communities through well drilling and filtration systems",
                    92.5, "Global", "people with clean water access", 25.0),

            Charity(2, "Forest Restoration Project", "Environment",
                    "Plants native trees to restore deforested areas and combat climate change",
                    88.3, "Global", "trees planted", 2.5),

            Charity(3, "Girls Education Fund", "Education",
                    "Provides scholarships and educational resources to girls in developing countries",
                    94.2, "Africa, Asia", "girls educated for 1 year", 120.0),

            Charity(4, "Mental Health Support Network", "Health",
                    "Offers counseling and mental health services to underserved communities",
                    87.9, "United States", "therapy sessions provided", 45.0),

            Charity(5, "Urban Food Bank", "Hunger",
                    "Distributes nutritious meals to homeless and low-income families",
                    91.7, "Local", "meals provided", 1.5),

            Charity(6, "Tech Skills Training", "Education",
                    "Teaches coding and digital literacy to unemployed youth",
                    85.4, "Urban areas", "people trained", 200.0),

            Charity(7, "Animal Rescue Coalition", "Animal Welfare",
                    "Rescues, rehabilitates and rehomes abandoned animals",
                    89.1, "Regional", "animals rescued", 75.0),

            Charity(8, "Elderly Care Program", "Health",
                    "Provides home care and companionship for isolated seniors",
                    93.6, "Local", "seniors supported monthly", 80.0),
        ]
        return sample_data

    def _generate_embeddings(self):
        """Generate embeddings for all charities"""
        descriptions = [f"{c.name} {c.category} {c.description}" for c in self.charities]
        self.embeddings = self.model.encode(descriptions)

    def find_best_match(self, user_profile: UserProfile) -> Tuple[Charity, float]:
        """Find the best charity match for user profile"""
        user_text = " ".join(user_profile.interests + user_profile.causes_passionate_about)
        user_embedding = self.model.encode([user_text])

        similarities = cosine_similarity(user_embedding, self.embeddings)[0]

        # Apply additional scoring factors
        scored_charities = []
        for i, charity in enumerate(self.charities):
            base_score = similarities[i]

            # Boost score for geographic preference
            if user_profile.geographic_preference.lower() in charity.location.lower():
                base_score *= 1.2

            # Boost score for high efficiency
            efficiency_boost = (charity.efficiency_rating / 100) * 0.1
            final_score = base_score + efficiency_boost

            scored_charities.append((charity, final_score))

        # Return best match
        best_charity, best_score = max(scored_charities, key=lambda x: x[1])
        return best_charity, best_score


class OnboardingAgent:
    """Handles user onboarding and profile creation"""

    def _init_(self):
        self.questions = [
            "What activities do you enjoy in your free time?",
            "Which global issues concern you most?",
            "Do you prefer helping locally or globally?",
            "What's your monthly discretionary spending range?",
            "How often would you like to contribute?"
        ]

    def create_profile_from_responses(self, responses: List[str]) -> UserProfile:
        """Convert user responses into structured profile"""
        # Extract interests (simplified NLP)
        interests = self._extract_interests(responses[0])
        causes = self._extract_causes(responses[1])
        geographic_pref = responses[2] if len(responses) > 2 else "Global"
        income_range = responses[3] if len(responses) > 3 else "moderate"
        frequency = responses[4] if len(responses) > 4 else "monthly"

        return UserProfile(
            interests=interests,
            income_range=income_range,
            donation_frequency=frequency,
            causes_passionate_about=causes,
            geographic_preference=geographic_pref
        )

    def _extract_interests(self, text: str) -> List[str]:
        """Extract interests from user response"""
        interest_keywords = {
            'environment': ['nature', 'outdoors', 'hiking', 'gardening', 'climate'],
            'education': ['reading', 'learning', 'teaching', 'books', 'school'],
            'technology': ['coding', 'programming', 'computers', 'tech', 'gaming'],
            'health': ['fitness', 'running', 'wellness', 'medicine', 'healthcare'],
            'animals': ['pets', 'dogs', 'cats', 'wildlife', 'animals'],
            'arts': ['music', 'painting', 'art', 'creative', 'design']
        }

        detected_interests = []
        text_lower = text.lower()

        for interest, keywords in interest_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                detected_interests.append(interest)

        return detected_interests or ['general']

    def _extract_causes(self, text: str) -> List[str]:
        """Extract causes from user response"""
        cause_keywords = {
            'poverty': ['poverty', 'hunger', 'homeless', 'food'],
            'education': ['education', 'literacy', 'school', 'learning'],
            'environment': ['climate', 'environment', 'pollution', 'conservation'],
            'health': ['health', 'disease', 'medical', 'wellness'],
            'human_rights': ['rights', 'equality', 'justice', 'discrimination']
        }

        detected_causes = []
        text_lower = text.lower()

        for cause, keywords in cause_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                detected_causes.append(cause)

        return detected_causes or ['general']


class DonationPlanningAI:
    """Creates personalized donation plans"""

    def _init_(self):
        self.income_ranges = {
            'low': (0, 30000),
            'moderate': (30000, 70000),
            'high': (70000, 150000),
            'very_high': (150000, float('inf'))
        }

    def create_donation_plan(self, charity: Charity, user_profile: UserProfile,
                             confidence_score: float) -> DonationPlan:
        """Create a personalized donation plan"""

        # Determine donation capacity based on income
        monthly_capacity = self._calculate_monthly_capacity(user_profile.income_range)

        # Apply psychological nudging for comfort
        suggested_amount = monthly_capacity * 0.7  # Start conservatively

        # Calculate impact
        monthly_impact = suggested_amount / charity.cost_per_impact
        annual_impact = monthly_impact * 12

        return DonationPlan(
            charity=charity,
            monthly_amount=suggested_amount,
            impact_per_month=monthly_impact,
            total_annual_impact=annual_impact,
            confidence_score=confidence_score
        )

    def _calculate_monthly_capacity(self, income_range: str) -> float:
        """Calculate reasonable monthly donation capacity"""
        capacity_map = {
            'low': 15.0,
            'moderate': 35.0,
            'high': 75.0,
            'very_high': 150.0
        }
        return capacity_map.get(income_range.lower(), 25.0)


class ImpactVisualizer:
    """Creates visualizations of donation impact"""

    def _init_(self):
        pass

    def create_impact_dashboard(self, donation_plan: DonationPlan) -> Dict:
        """Create comprehensive impact visualization"""

        # Generate monthly impact projection
        months = list(range(1, 13))
        cumulative_impact = [donation_plan.impact_per_month * m for m in months]
        cumulative_donations = [donation_plan.monthly_amount * m for m in months]

        # Create main impact chart
        fig_impact = go.Figure()
        fig_impact.add_trace(go.Scatter(
            x=months,
            y=cumulative_impact,
            mode='lines+markers',
            name=f'Cumulative {donation_plan.charity.impact_metric}',
            line=dict(color='#2E86AB', width=3),
            marker=dict(size=8)
        ))

        fig_impact.update_layout(
            title=f'Your Impact Over Time with {donation_plan.charity.name}',
            xaxis_title='Month',
            yaxis_title=f'Total {donation_plan.charity.impact_metric}',
            template='plotly_white',
            height=400
        )

        # Create donation breakdown pie chart
        fig_pie = go.Figure(data=[go.Pie(
            labels=['Direct Impact', 'Administrative Costs'],
            values=[donation_plan.charity.efficiency_rating, 100 - donation_plan.charity.efficiency_rating],
            hole=0.4,
            marker_colors=['#2E86AB', '#A23B72']
        )])

        fig_pie.update_layout(
            title='How Your Donation Is Used',
            template='plotly_white',
            height=300
        )

        # Generate impact statements
        impact_statements = self._generate_impact_statements(donation_plan)

        return {
            'impact_chart': fig_impact,
            'efficiency_chart': fig_pie,
            'statements': impact_statements,
            'monthly_impact': donation_plan.impact_per_month,
            'annual_impact': donation_plan.total_annual_impact
        }

    def _generate_impact_statements(self, donation_plan: DonationPlan) -> List[str]:
        """Generate compelling impact statements"""
        charity = donation_plan.charity
        monthly_impact = int(donation_plan.impact_per_month)
        annual_impact = int(donation_plan.total_annual_impact)

        statements = [
            f"Your ${donation_plan.monthly_amount:.0f} monthly contribution will provide {monthly_impact} {charity.impact_metric}",
            f"In just one year, you'll have helped achieve {annual_impact} {charity.impact_metric}",
            f"Your donation is {charity.efficiency_rating:.1f}% efficient - among the best in the sector",
            f"You're joining thousands of donors making a real difference through {charity.name}"
        ]

        # Add contextual comparisons
        if "meals" in charity.impact_metric.lower():
            statements.append(f"That's enough meals to feed a family of 4 for {monthly_impact // 4} days each month")
        elif "trees" in charity.impact_metric.lower():
            co2_offset = monthly_impact * 48  # rough kg CO2 per tree per year
            statements.append(f"These trees will offset approximately {co2_offset:.0f} kg of CO2 annually")

        return statements


# Main Application Class
class CharityMatchingApp:
    """Main application orchestrator"""

    def _init_(self):
        self.db = CharityDatabase()
        self.onboarding = OnboardingAgent()
        self.planner = DonationPlanningAI()
        self.visualizer = ImpactVisualizer()

    def run_full_pipeline(self, user_responses: List[str]) -> Dict:
        """Execute complete charity matching pipeline"""

        # Step 1: Create user profile
        user_profile = self.onboarding.create_profile_from_responses(user_responses)

        # Step 2: Find best charity match
        best_charity, confidence_score = self.db.find_best_match(user_profile)

        # Step 3: Create donation plan
        donation_plan = self.planner.create_donation_plan(
            best_charity, user_profile, confidence_score
        )

        # Step 4: Generate impact visualization
        impact_data = self.visualizer.create_impact_dashboard(donation_plan)

        return {
            'user_profile': user_profile,
            'matched_charity': best_charity,
            'donation_plan': donation_plan,
            'impact_visualization': impact_data,
            'confidence_score': confidence_score
        }


# Streamlit UI Implementation
def create_streamlit_app():
    """Create Streamlit interface for the charity matching app"""

    st.set_page_config(
        page_title="AI Charity Matcher",
        page_icon="💝",
        layout="wide"
    )

    st.title("🤖 AI-Powered Charity Matching Platform")
    st.markdown("Find your perfect charity match and see your impact in real-time")

    # Initialize app
    if 'app' not in st.session_state:
        st.session_state.app = CharityMatchingApp()

    # Onboarding Section
    st.header("📋 Tell Us About Yourself")

    col1, col2 = st.columns(2)

    with col1:
        interests = st.text_area(
            "What activities do you enjoy in your free time?",
            placeholder="e.g., hiking, reading, cooking, programming..."
        )

        causes = st.text_area(
            "Which global issues concern you most?",
            placeholder="e.g., climate change, education inequality, poverty..."
        )

    with col2:
        geography = st.selectbox(
            "Do you prefer helping locally or globally?",
            ["Local", "Regional", "Global", "No preference"]
        )

        income = st.selectbox(
            "What's your monthly discretionary spending range?",
            ["low", "moderate", "high", "very_high"]
        )

        frequency = st.selectbox(
            "How often would you like to contribute?",
            ["monthly", "quarterly", "annually"]
        )

    if st.button("🔍 Find My Perfect Charity Match", type="primary"):
        if interests and causes:
            responses = [interests, causes, geography, income, frequency]

            with st.spinner("🤖 AI is analyzing your profile and finding the perfect match..."):
                results = st.session_state.app.run_full_pipeline(responses)

            # Display Results
            st.success("✨ Perfect Match Found!")

            # Charity Information
            charity = results['matched_charity']
            plan = results['donation_plan']

            st.header(f"🎯 Your Match: {charity.name}")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Efficiency Rating", f"{charity.efficiency_rating:.1f}%")
            with col2:
                st.metric("Confidence Score", f"{results['confidence_score']:.1f}%")
            with col3:
                st.metric("Category", charity.category)

            st.markdown(f"*Description:* {charity.description}")
            st.markdown(f"*Location:* {charity.location}")

            # Donation Plan
            st.header("💡 Your Personalized Giving Plan")

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Suggested Monthly Donation", f"${plan.monthly_amount:.0f}")
                st.metric("Monthly Impact", f"{plan.impact_per_month:.0f} {charity.impact_metric}")

            with col2:
                st.metric("Annual Impact", f"{plan.total_annual_impact:.0f} {charity.impact_metric}")
                st.metric("Cost Per Impact", f"${charity.cost_per_impact:.2f}")

            # Impact Visualization
            st.header("📊 Your Impact Visualization")

            impact_viz = results['impact_visualization']

            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(impact_viz['impact_chart'], use_container_width=True)
            with col2:
                st.plotly_chart(impact_viz['efficiency_chart'], use_container_width=True)

            # Impact Statements
            st.header("🌟 Your Impact Story")
            for statement in impact_viz['statements']:
                st.markdown(f"• {statement}")

            # Simulate Donation Button
            if st.button("🎉 Simulate Donation", type="secondary"):
                st.balloons()
                st.success(
                    f"🎊 Congratulations! You've just made a simulated ${plan.monthly_amount:.0f} donation to {charity.name}!")
                st.markdown(
                    f"*Immediate Impact:* You've just provided {plan.impact_per_month:.0f} {charity.impact_metric}!")
        else:
            st.warning("Please fill in your interests and causes to get started!")


# Demo Runner
def run_demo():
    """Run a simple demo of the system"""
    app = CharityMatchingApp()

    # Sample user responses
    demo_responses = [
        "I love hiking, photography, and spending time in nature",
        "I'm most concerned about climate change and environmental destruction",
        "Global",
        "moderate",
        "monthly"
    ]

    print("🤖 Running Charity AI Demo...")
    print("=" * 50)

    results = app.run_full_pipeline(demo_responses)

    print(f"✅ Best Match: {results['matched_charity'].name}")
    print(f"📊 Confidence: {results['confidence_score']:.1f}%")
    print(f"💰 Suggested Donation: ${results['donation_plan'].monthly_amount:.0f}/month")
    print(
        f"🎯 Monthly Impact: {results['donation_plan'].impact_per_month:.0f} {results['matched_charity'].impact_metric}")
    print("=" * 50)


if _name_ == "_main_":
    # For Streamlit: streamlit run charity_ai.py
    create_streamlit_app()

    # For demo: python charity_ai.py
    # run_demo()