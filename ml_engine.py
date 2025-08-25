import numpy as np
from typing import Dict, List
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from collections import defaultdict
from models import UserProfile


class MLEngine:
    """Machine Learning engine for predictions and optimization"""

    def __init__(self):
        self.engagement_model = None
        self.donation_amount_model = None
        self.user_embeddings = {}
        self.charity_embeddings = {}
        self._initialize_models()

    def _initialize_models(self):
        """Initialize ML models with synthetic training data"""
        # Generate synthetic training data for demo
        # In production, this would use real historical data

        # Engagement prediction model
        X_engagement = np.random.rand(1000, 8)  # 8 features
        y_engagement = np.random.rand(1000)  # Engagement scores

        self.engagement_model = RandomForestRegressor(n_estimators=50, random_state=42)
        self.engagement_model.fit(X_engagement, y_engagement)

        # Donation amount prediction model
        X_donation = np.random.rand(1000, 6)  # 6 features
        y_donation = np.random.rand(1000) * 100  # Donation amounts

        self.donation_amount_model = RandomForestRegressor(n_estimators=50, random_state=42)
        self.donation_amount_model.fit(X_donation, y_donation)

    def predict_engagement_score(self, user_profile: UserProfile) -> float:
        """Predict how likely user is to continue donating using ML"""

        # Extract features from user profile
        features = self._extract_user_features(user_profile)

        # Predict engagement score
        predicted_score = self.engagement_model.predict([features])[0]

        # Normalize to 0-1 range
        return max(0, min(1, predicted_score))

    def optimize_donation_amount(self, user_profile: UserProfile, base_amount: float) -> float:
        """Use ML to optimize donation amount for maximum engagement"""

        # Extract features
        features = self._extract_donation_features(user_profile, base_amount)

        # Predict optimal amount
        predicted_amount = self.donation_amount_model.predict([features])[0]

        # Ensure reasonable bounds
        min_amount = max(3.0, base_amount * 0.5)
        max_amount = base_amount * 2.0

        return max(min_amount, min(max_amount, predicted_amount))

    def calculate_semantic_similarity(self, user_text: str, charity_description: str) -> float:
        """Calculate semantic similarity between user interests and charity"""

        # Simple implementation using word overlap
        # In production, would use word embeddings or transformer models

        user_words = set(user_text.lower().split())
        charity_words = set(charity_description.lower().split())

        if len(user_words) == 0 or len(charity_words) == 0:
            return 0.0

        intersection = len(user_words & charity_words)
        union = len(user_words | charity_words)

        return intersection / union if union > 0 else 0.0

    def cluster_user_behavior(self, user_profiles: List[UserProfile]) -> Dict[int, List[str]]:
        """Cluster users by behavior patterns for personalized recommendations"""

        if len(user_profiles) < 3:
            return {0: [profile.name for profile in user_profiles]}

        # Extract features for clustering
        features = []
        names = []

        for profile in user_profiles:
            feature_vector = self._extract_user_features(profile)
            features.append(feature_vector)
            names.append(profile.name)

        # Perform K-means clustering
        n_clusters = min(3, len(user_profiles))
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(features)

        # Group users by cluster
        cluster_groups = defaultdict(list)
        for i, cluster_id in enumerate(clusters):
            cluster_groups[cluster_id].append(names[i])

        return dict(cluster_groups)

    def _extract_user_features(self, profile: UserProfile) -> List[float]:
        """Extract numerical features from user profile for ML"""

        features = [
            profile.monthly_income / 10000,  # Normalized income
            len(profile.interests) / 10,  # Interest diversity
            len(profile.causes) / 8,  # Cause diversity
            1.0 if profile.donation_comfort_level == 'high' else 0.5 if profile.donation_comfort_level == 'medium' else 0.0,
            1.0 if profile.preferred_frequency == 'weekly' else 0.5 if profile.preferred_frequency == 'monthly' else 0.0,
            1.0 if profile.geographic_preference == 'global' else 0.5 if profile.geographic_preference == 'national' else 0.0,
            profile.giving_history_sentiment,
            sum(profile.personality_traits.values()) / len(
                profile.personality_traits) if profile.personality_traits else 0.0
        ]

        return features

    def _extract_donation_features(self, profile: UserProfile, base_amount: float) -> List[float]:
        """Extract features for donation amount optimization"""

        features = [
            profile.monthly_income / 10000,
            base_amount / 100,
            len(profile.interests) / 10,
            1.0 if profile.donation_comfort_level == 'high' else 0.5 if profile.donation_comfort_level == 'medium' else 0.0,
            profile.giving_history_sentiment,
            profile.predicted_engagement_score
        ]

        return features