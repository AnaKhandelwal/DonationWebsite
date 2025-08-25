from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class UserProfile:
    """Enhanced user profile with NLP-extracted insights"""
    name: str
    interests: List[str]
    causes: List[str]
    monthly_income: float
    donation_comfort_level: str  # 'low', 'medium', 'high'
    preferred_frequency: str  # 'weekly', 'monthly', 'quarterly'
    geographic_preference: str  # 'local', 'national', 'global'
    # NEW: NLP-enhanced fields
    personality_traits: Dict[str, float] = None  # extracted from free text
    emotional_drivers: List[str] = None  # what motivates them
    giving_history_sentiment: float = 0.0  # sentiment about past giving
    extracted_keywords: List[str] = None  # NLP-extracted interests
    predicted_engagement_score: float = 0.0  # ML-predicted likelihood to continue


@dataclass
class Charity:
    """Enhanced charity data structure with ML features"""
    id: str
    name: str
    category: str
    description: str
    location: str
    efficiency_score: float  # 0-100
    tags: List[str]
    min_donation: float
    impact_metrics: Dict[str, str]  # e.g., {"$10": "feeds 3 children for a day"}
    # NEW: ML-enhanced fields
    description_embedding: List[float] = None  # NLP embedding of description
    success_stories: List[str] = None  # for sentiment analysis
    donor_retention_rate: float = 0.0  # historical ML feature
    predicted_impact_score: float = 0.0  # ML-predicted impact
    semantic_keywords: List[str] = None  # NLP-extracted keywords


@dataclass
class DonationPlan:
    """Micro-donation plan structure"""
    charity: Charity
    amount: float
    frequency: str
    annual_total: float
    impact_description: str


@dataclass
class ImpactReport:
    """Impact visualization data"""
    charity_name: str
    total_donated: float
    impact_metrics: Dict[str, float]
    beneficiaries_helped: int
    timeline: List[Dict[str, any]]