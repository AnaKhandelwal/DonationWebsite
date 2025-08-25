import re
from typing import Dict, List
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob


class NLPProcessor:
    """Handles all NLP operations for text understanding"""

    def __init__(self):
        self.tfidf = TfidfVectorizer(max_features=100, stop_words='english')
        self.personality_keywords = {
            'empathetic': ['care', 'help', 'compassion', 'support', 'kindness', 'love'],
            'analytical': ['data', 'research', 'evidence', 'facts', 'analysis', 'study'],
            'activist': ['change', 'fight', 'justice', 'rights', 'action', 'movement'],
            'community-oriented': ['together', 'community', 'local', 'neighborhood', 'family'],
            'global-minded': ['world', 'global', 'international', 'humanity', 'planet']
        }

    def extract_interests_from_text(self, text: str) -> Dict[str, any]:
        """Extract interests and personality from free text using NLP"""

        # Clean and process text
        cleaned_text = self._clean_text(text)
        blob = TextBlob(cleaned_text)

        # Sentiment analysis
        sentiment = blob.sentiment.polarity

        # Extract keywords using TF-IDF
        keywords = self._extract_keywords(cleaned_text)

        # Personality trait analysis
        personality_traits = self._analyze_personality(cleaned_text)

        # Emotional drivers
        emotional_drivers = self._extract_emotional_drivers(cleaned_text)

        # Map to charity categories using semantic similarity
        category_matches = self._map_to_charity_categories(keywords, cleaned_text)

        return {
            'keywords': keywords,
            'sentiment': sentiment,
            'personality_traits': personality_traits,
            'emotional_drivers': emotional_drivers,
            'category_matches': category_matches,
            'processed_text': cleaned_text
        }

    def _clean_text(self, text: str) -> str:
        """Clean and preprocess text"""
        # Remove special characters, normalize case
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text.lower().strip()

    def _extract_keywords(self, text: str) -> List[str]:
        """Extract important keywords using TF-IDF"""
        try:
            # Simple keyword extraction for demo
            words = text.split()
            # Remove common words and get meaningful terms
            meaningful_words = [w for w in words if len(w) > 3 and w not in
                                ['that', 'this', 'have', 'been', 'will', 'they', 'there']]
            return list(set(meaningful_words))[:10]  # Top 10 keywords
        except:
            return []

    def _analyze_personality(self, text: str) -> Dict[str, float]:
        """Analyze personality traits from text"""
        traits = {}

        for trait, keywords in self.personality_keywords.items():
            # Count keyword matches (normalized)
            matches = sum(1 for keyword in keywords if keyword in text)
            traits[trait] = matches / len(keywords)  # Normalize by total keywords

        return traits

    def _extract_emotional_drivers(self, text: str) -> List[str]:
        """Extract what emotionally motivates the user"""
        drivers = []

        emotional_patterns = {
            'injustice': ['unfair', 'wrong', 'injustice', 'inequality'],
            'empathy': ['feel', 'heart', 'compassion', 'care'],
            'hope': ['future', 'better', 'hope', 'change'],
            'responsibility': ['duty', 'should', 'must', 'responsibility']
        }

        for driver, patterns in emotional_patterns.items():
            if any(pattern in text for pattern in patterns):
                drivers.append(driver)

        return drivers

    def _map_to_charity_categories(self, keywords: List[str], text: str) -> Dict[str, float]:
        """Map extracted content to charity categories using semantic similarity"""

        category_themes = {
            'education': ['school', 'learn', 'student', 'teacher', 'education', 'literacy'],
            'health': ['health', 'medical', 'disease', 'treatment', 'wellness', 'care'],
            'environment': ['environment', 'climate', 'nature', 'green', 'planet', 'earth'],
            'poverty': ['poor', 'poverty', 'hunger', 'homeless', 'food', 'basic'],
            'animals': ['animal', 'wildlife', 'species', 'conservation', 'pets'],
            'water': ['water', 'clean', 'sanitation', 'wells', 'drinking']
        }

        matches = {}
        for category, themes in category_themes.items():
            # Calculate semantic overlap
            overlap = len(set(keywords) & set(themes))
            # Also check direct text mentions
            text_mentions = sum(1 for theme in themes if theme in text)
            matches[category] = (overlap + text_mentions) / len(themes)

        return matches