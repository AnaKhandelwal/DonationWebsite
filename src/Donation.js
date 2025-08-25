import React, { useState } from 'react';
import { Search, User, Wallet, Compass, Award, Gift, Zap, Target, Trophy, Star, TrendingUp, Calendar, DollarSign, Menu, X, ChevronLeft, ChevronRight, Heart, Users, Globe, Shield, ArrowRight, Mail, Phone, MapPin, Settings, Home, LogOut } from 'lucide-react';

// Simple Router Context
const RouterContext = React.createContext();

const Router = ({ children }) => {
  const [currentPage, setCurrentPage] = useState('landing');
  
  const navigate = (page) => {
    setCurrentPage(page);
  };
  
  return (
    <RouterContext.Provider value={{ currentPage, navigate }}>
      {children}
    </RouterContext.Provider>
  );
};

const useRouter = () => {
  const context = React.useContext(RouterContext);
  if (!context) {
    throw new Error('useRouter must be used within a Router');
  }
  return context;
};

// Landing Page Component
const LandingPage = () => {
  const { navigate } = useRouter();

  const handleSignIn = () => {
    navigate('preferences');
  };

  return (
    <div className="min-h-screen bg-white">
        <script src="https://cdn.tailwindcss.com"></script>
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 z-20 p-2 backdrop-blur-md">
        <div className="max-w-2xl mx-auto flex justify-between items-center">
          <div className="bg-white px-6 py-3 rounded-full shadow-lg">
            <span className="text-lg font-bold text-gray-800 tracking-wide">NIVA</span>
          </div>
          <button
            onClick={handleSignIn}
            className="bg-white bg-opacity-20 backdrop-blur-sm text-white border border-white border-opacity-30 px-6 py-3 rounded-full font-medium hover:bg-opacity-30 transition-all duration-300"
          >
            Sign In
          </button>
        </div>
      </header>

      {/* Hero Section */}
      <div className="relative min-h-screen flex items-center">
        {/* Background with multiple layers */}
        <div className="absolute inset-0">
          <div 
            className="absolute inset-0 bg-cover bg-center"
            style={{
             backgroundImage: "url('https://images.unsplash.com/photo-1582213782179-e0d53f98f2ca?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80')",
            }}
          />
          <div className="absolute inset-0 bg-gradient-to-br from-slate-900 via-blue-900 to-slate-800 opacity-85" />
          <div className="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent opacity-40" />
        </div>
        
        {/* Floating elements */}
        <div className="absolute top-1/4 left-10 w-2 h-2 bg-blue-400 rounded-full animate-pulse opacity-60" />
        <div className="absolute top-1/3 right-20 w-1 h-1 bg-white rounded-full animate-pulse opacity-40" />
        <div className="absolute bottom-1/3 left-1/4 w-1 h-1 bg-blue-300 rounded-full animate-pulse opacity-50" />
        
        {/* Hero Content */}
        <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
          <div className="mb-6">
            <span className="inline-block bg-blue-500 bg-opacity-20 backdrop-blur-sm text-blue-200 px-4 py-2 rounded-full text-sm font-medium border border-blue-400 border-opacity-30">
              Join 12,000+ changemakers
            </span>
          </div>
          <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold text-white mb-6 leading-tight">
            Small acts.
            <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-300 to-blue-100">
              Big change.
            </span>
          </h1>
          <p className="text-xl md:text-2xl text-slate-200 max-w-2xl mx-auto mb-8 font-light">
            Your $5 becomes someone's meal. Your $20 becomes a child's education. 
            Start making an impact that matters.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <button
              onClick={handleSignIn}
              className="bg-blue-500 hover:bg-blue-600 text-white px-8 py-4 rounded-lg font-semibold text-lg transition-all duration-300 transform hover:scale-105 shadow-xl flex items-center"
            >
              Start giving today
              <ArrowRight className="ml-2 w-5 h-5" />
            </button>
          </div>
          <p className="text-slate-300 text-sm mt-4">No signup fees • Cancel anytime • 100% transparent</p>
        </div>
      </div>

      {/* Real impact stories */}
      <section className="py-20 px-4 bg-slate-50">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-slate-800 mb-4">
              Real stories. Real impact.
            </h2>
            <p className="text-lg text-slate-600 max-w-2xl mx-auto">
              We connect your generosity with verified causes worldwide. Here's what your donations make possible.
            </p>
          </div>

          <div className="overflow-x-auto">
            <div className="flex gap-6 min-w-max md:grid md:grid-cols-3 md:min-w-0">
              <div className="bg-white rounded-xl p-6 shadow-sm hover:shadow-lg transition-all duration-300 border border-slate-100 min-w-80 md:min-w-0">
                <div className="w-10 h-10 bg-emerald-100 rounded-lg flex items-center justify-center mb-4">
                  <Target className="w-5 h-5 text-emerald-600" />
                </div>
                <h3 className="text-lg font-semibold text-slate-800 mb-2">Maria's Water Well</h3>
                <p className="text-slate-600 mb-3 text-sm">
                  "Thanks to 47 donors, our village now has clean water. My daughter doesn't miss school anymore to walk 3 hours for water."
                </p>
                <div className="text-xs text-slate-500">
                  🇰🇪 Kenya • Funded in 23 days
                </div>
              </div>

              <div className="bg-white rounded-xl p-6 shadow-sm hover:shadow-lg transition-all duration-300 border border-slate-100 min-w-80 md:min-w-0">
                <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                  <Users className="w-5 h-5 text-blue-600" />
                </div>
                <h3 className="text-lg font-semibold text-slate-800 mb-2">Local Food Bank</h3>
                <p className="text-slate-600 mb-3 text-sm">
                  "We fed 200 families last month. Every $10 provides groceries for a week. The community support has been incredible."
                </p>
                <div className="text-xs text-slate-500">
                  🇺🇸 Detroit • Ongoing support
                </div>
              </div>

              <div className="bg-white rounded-xl p-6 shadow-sm hover:shadow-lg transition-all duration-300 border border-slate-100 min-w-80 md:min-w-0">
                <div className="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center mb-4">
                  <Heart className="w-5 h-5 text-purple-600" />
                </div>
                <h3 className="text-lg font-semibold text-slate-800 mb-2">School Library</h3>
                <p className="text-slate-600 mb-3 text-sm">
                  "152 donors helped us buy books and tablets. Reading scores improved 40%. These kids now dream of college."
                </p>
                <div className="text-xs text-slate-500">
                  🇲🇽 Mexico • Completed last month
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* How it works - simplified */}
      <section className="py-16 px-4 bg-white">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl font-bold text-slate-800 mb-12">Three steps. Maximum impact.</h2>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="w-16 h-16 bg-blue-500 rounded-2xl flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl font-bold text-white">1</span>
              </div>
              <h3 className="text-lg font-semibold text-slate-800 mb-2">Choose your cause</h3>
              <p className="text-slate-600">Pick what matters to you most. We'll match you with vetted projects.</p>
            </div>
            
            <div className="text-center">
              <div className="w-16 h-16 bg-blue-500 rounded-2xl flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl font-bold text-white">2</span>
              </div>
              <h3 className="text-lg font-semibold text-slate-800 mb-2">Set your amount</h3>
              <p className="text-slate-600">Start with $5/month or give what feels right. Every dollar counts.</p>
            </div>
            
            <div className="text-center">
              <div className="w-16 h-16 bg-blue-500 rounded-2xl flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl font-bold text-white">3</span>
              </div>
              <h3 className="text-lg font-semibold text-slate-800 mb-2">See your impact</h3>
              <p className="text-slate-600">Get updates, photos, and stories from the communities you're helping.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Quick stats */}
      <section className="py-12 px-4 bg-gradient-to-r from-slate-800 to-slate-900">
        <div className="max-w-3xl mx-auto">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
            <div>
              <div className="text-2xl md:text-3xl font-bold text-white mb-1">$2.4M</div>
              <div className="text-slate-300 text-sm">donated this year</div>
            </div>
            <div>
              <div className="text-2xl md:text-3xl font-bold text-white mb-1">12,847</div>
              <div className="text-slate-300 text-sm">active donors</div>
            </div>
            <div>
              <div className="text-2xl md:text-3xl font-bold text-white mb-1">89</div>
              <div className="text-slate-300 text-sm">projects funded</div>
            </div>
            <div>
              <div className="text-2xl md:text-3xl font-bold text-white mb-1">23</div>
              <div className="text-slate-300 text-sm">countries reached</div>
            </div>
          </div>
        </div>
      </section>

      {/* Final CTA */}
      <section className="py-20 px-4 bg-blue-600">
        <div className="max-w-3xl mx-auto text-center">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
            Ready to make a difference?
          </h2>
          <p className="text-xl text-blue-100 mb-8">
            Join thousands of people creating positive change, one donation at a time.
          </p>
          <button
            onClick={handleSignIn}
            className="bg-white text-blue-600 px-8 py-4 rounded-lg font-semibold text-lg hover:bg-slate-50 transition-colors shadow-lg"
          >
            Get started now
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-900 text-white py-12 px-4">
        <div className="max-w-4xl mx-auto">
          <div className="grid md:grid-cols-3 gap-8 mb-8">
            <div>
              <h3 className="text-xl font-bold mb-4">Niva</h3>
              <p className="text-slate-400 text-sm mb-4">
                Connecting generous hearts with meaningful causes worldwide.
              </p>
              <div className="text-sm text-slate-500">
                🔒 Secure platform • 📊 Full transparency • 🌍 Global reach
              </div>
            </div>

            <div>
              <h4 className="font-semibold mb-3">Support</h4>
              <ul className="space-y-2 text-slate-400 text-sm">
                <li><a href="#" className="hover:text-white transition-colors">How it works</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Find projects</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Help center</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Contact us</a></li>
              </ul>
            </div>

            <div>
              <h4 className="font-semibold mb-3">Get in touch</h4>
              <div className="space-y-3 text-slate-400 text-sm">
                <div className="flex items-center">
                  <Mail className="w-4 h-4 mr-2" />
                  <span>hello@niva.org</span>
                </div>
                <div className="flex items-center">
                  <Phone className="w-4 h-4 mr-2" />
                  <span>(555) 123-4567</span>
                </div>
              </div>
            </div>
          </div>

          <div className="border-t border-slate-800 pt-6 text-center">
            <p className="text-slate-500 text-sm">
              © 2025 Niva • Made with care for a better world
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
};

// Preferences Page Component
const PreferencesPage = () => {
  const { navigate } = useRouter();
  const [formData, setFormData] = useState({
    name: '',
    free_text_interests: '',
    interests: [],
    causes: [],
    income: '',
    comfort_level: '',
    frequency: '',
    geography: ''
  });

  const interestOptions = [
    'health', 'education', 'environment', 'animals', 'technology',
    'arts', 'sports', 'children', 'elderly', 'community'
  ];

  const causeOptions = [
    'Water & Sanitation', 'Education', 'Environment', 'Hunger Relief',
    'Animal Welfare', 'Healthcare', 'Disaster Relief', 'Human Rights'
  ];

  const incomeRanges = [
    { label: '$0 - $2,000', value: '0-2000' },
    { label: '$2,000 - $4,000', value: '2000-4000' },
    { label: '$4,000 - $6,000', value: '4000-6000' },
    { label: '$6,000 - $10,000', value: '6000-10000' },
    { label: '$10,000+', value: '10000+' }
  ];

  const comfortLevels = ['Just starting out', 'Occasional donor', 'Regular supporter'];
  const frequencies = ['Weekly', 'Monthly', 'Quarterly'];
  const geographies = ['Local community', 'National', 'Global'];

  const handleInputChange = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
  };

  const handleMultiSelect = (field, option) => {
    setFormData(prev => ({
      ...prev,
      [field]: prev[field].includes(option)
        ? prev[field].filter(item => item !== option)
        : [...prev[field], option]
    }));
  };

  const handleSubmit = () => {
    console.log('Form submitted:', formData);
    navigate('homepage');
  };

  const handleBack = () => {
    navigate('landing');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-slate-100">
      <div className="max-w-2xl mx-auto px-4 py-8">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-sm p-6 mb-6">
          <div className="flex items-center mb-4">
            <button onClick={handleBack} className="flex items-center hover:text-blue-800 transition-colors">
              <ChevronLeft className="w-6 h-6 text-blue-600 mr-3" />
            </button>
            <h1 className="text-2xl font-semibold text-gray-800">Preferences</h1>
          </div>
          <p className="text-gray-600">Help us personalize your donation experience. This information helps us suggest causes and amounts that align with your interests.</p>
        </div>

        <div className="space-y-6">
          {/* Name */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="flex items-center mb-4">
              <Heart className="w-5 h-5 text-blue-600 mr-2" />
              <h2 className="text-lg font-medium text-gray-800">Personal Information</h2>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                What's your name? *
              </label>
              <input
                type="text"
                required
                value={formData.name}
                onChange={(e) => handleInputChange('name', e.target.value)}
                className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors"
                placeholder="Enter your name"
              />
            </div>
          </div>

          {/* Free Text Interests */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="flex items-center mb-4">
              <Globe className="w-5 h-5 text-blue-600 mr-2" />
              <h2 className="text-lg font-medium text-gray-800">Tell Us About Yourself</h2>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Tell me about what you're passionate about and what drives you to want to make a difference *
              </label>
              <textarea
                required
                value={formData.free_text_interests}
                onChange={(e) => handleInputChange('free_text_interests', e.target.value)}
                rows={4}
                className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors resize-none"
                placeholder="Share your passions and motivations..."
              />
            </div>
          </div>

          {/* Interests */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <h2 className="text-lg font-medium text-gray-800 mb-4">What are you passionate about? (Select all that apply) *</h2>
            <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
              {interestOptions.map((interest) => (
                <button
                  key={interest}
                  type="button"
                  onClick={() => handleMultiSelect('interests', interest)}
                  className={`px-4 py-3 rounded-full text-sm font-medium transition-colors ${
                    formData.interests.includes(interest)
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-100 text-gray-700 hover:bg-blue-50'
                  }`}
                >
                  {interest.charAt(0).toUpperCase() + interest.slice(1)}
                </button>
              ))}
            </div>
          </div>

          {/* Causes */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <h2 className="text-lg font-medium text-gray-800 mb-4">Which causes matter most to you? *</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {causeOptions.map((cause) => (
                <button
                  key={cause}
                  type="button"
                  onClick={() => handleMultiSelect('causes', cause)}
                  className={`px-4 py-3 rounded-full text-sm font-medium transition-colors ${
                    formData.causes.includes(cause)
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-100 text-gray-700 hover:bg-blue-50'
                  }`}
                >
                  {cause}
                </button>
              ))}
            </div>
          </div>

          {/* Income */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="flex items-center mb-4">
              <DollarSign className="w-5 h-5 text-blue-600 mr-2" />
              <h2 className="text-lg font-medium text-gray-800">Financial Information</h2>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                What's your approximate monthly income? (This helps us suggest appropriate amounts) *
              </label>
              <select
                required
                value={formData.income}
                onChange={(e) => handleInputChange('income', e.target.value)}
                className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors"
              >
                <option value="">Select income range</option>
                {incomeRanges.map((range) => (
                  <option key={range.value} value={range.value}>
                    {range.label}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* Comfort Level */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <h2 className="text-lg font-medium text-gray-800 mb-4">How comfortable are you with regular donations? *</h2>
            <div className="space-y-3">
              {comfortLevels.map((level) => (
                <label key={level} className="flex items-center">
                  <input
                    type="radio"
                    name="comfort_level"
                    value={level}
                    checked={formData.comfort_level === level}
                    onChange={(e) => handleInputChange('comfort_level', e.target.value)}
                    className="w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500"
                  />
                  <span className="ml-3 text-gray-700">{level}</span>
                </label>
              ))}
            </div>
          </div>

          {/* Frequency */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="flex items-center mb-4">
              <Calendar className="w-5 h-5 text-blue-600 mr-2" />
              <h2 className="text-lg font-medium text-gray-800">Donation Frequency</h2>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                How often would you prefer to donate? *
              </label>
              <div className="grid grid-cols-3 gap-3">
                {frequencies.map((freq) => (
                  <button
                    key={freq}
                    type="button"
                    onClick={() => handleInputChange('frequency', freq)}
                    className={`px-4 py-3 rounded-lg text-sm font-medium transition-colors ${
                      formData.frequency === freq
                        ? 'bg-blue-600 text-white'
                        : 'bg-gray-100 text-gray-700 hover:bg-blue-50'
                    }`}
                  >
                    {freq}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Geography */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <div className="flex items-center mb-4">
              <MapPin className="w-5 h-5 text-blue-600 mr-2" />
              <h2 className="text-lg font-medium text-gray-800">Impact Scope</h2>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Where would you like your impact to be? *
              </label>
              <div className="grid grid-cols-3 gap-3">
                {geographies.map((geo) => (
                  <button
                    key={geo}
                    type="button"
                    onClick={() => handleInputChange('geography', geo)}
                    className={`px-4 py-3 rounded-lg text-sm font-medium transition-colors ${
                      formData.geography === geo
                        ? 'bg-blue-600 text-white'
                        : 'bg-gray-100 text-gray-700 hover:bg-blue-50'
                    }`}
                  >
                    {geo}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Submit Button */}
          <div className="bg-white rounded-lg shadow-sm p-6">
            <button
              type="button"
              onClick={handleSubmit}
              className="w-full bg-blue-600 text-white py-4 px-6 rounded-lg font-medium hover:bg-blue-700 transition-colors focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            >
              Save Preferences
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

// Homepage Component
const Homepage = () => {
  const { navigate } = useRouter();
  
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
  const [rightPanelCollapsed, setRightPanelCollapsed] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [activeTab, setActiveTab] = useState('profile');

  const Header = () => {
    const searchResults = [
      { id: 1, title: 'Education for All', category: 'Education', match: 95 },
      { id: 2, title: 'Clean Water Initiative', category: 'Environment', match: 88 },
      { id: 3, title: 'Healthcare Access', category: 'Health', match: 92 }
    ];

    return (
      <header className="bg-white border-b border-gray-200 px-6 py-4 sticky top-0 z-40">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-sm">N</span>
            </div>
            <h1 className="text-xl font-semibold text-gray-900 tracking-tight">NIVA</h1>
            <span className="bg-gray-100 text-gray-600 text-xs px-2 py-1 rounded-full">AI Powered</span>
          </div>

          <div className="flex-1 max-w-md mx-8 relative">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" />
              <input
                type="text"
                placeholder="Discover causes that match your values..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full pl-10 pr-4 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors"
              />
            </div>
            
            {searchQuery && (
              <div className="absolute top-full mt-2 w-full bg-white border border-gray-200 rounded-lg shadow-lg z-50 p-2">
                <div className="text-xs text-gray-500 mb-2 px-2">AI Suggested Matches</div>
                {searchResults.map((result) => (
                  <div 
                    key={result.id} 
                    className="flex items-center justify-between p-3 rounded-lg hover:bg-gray-50 cursor-pointer"
                  >
                    <div>
                      <div className="font-medium text-sm text-gray-900">{result.title}</div>
                      <div className="text-xs text-gray-500">{result.category}</div>
                    </div>
                    <div className="flex items-center gap-2">
                      <div className="text-xs text-blue-600 font-medium">{result.match}% match</div>
                      <div className="w-2 h-2 bg-blue-600 rounded-full"></div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          <div className="flex items-center gap-6">
            <div className="flex items-center gap-2 bg-yellow-50 text-yellow-700 px-3 py-2 rounded-lg">
              <Zap className="w-4 h-4" />
              <span className="text-sm font-medium">12 day streak</span>
            </div>
            <div className="flex items-center gap-2 bg-blue-50 text-blue-700 px-3 py-2 rounded-lg">
              <Star className="w-4 h-4" />
              <span className="text-sm font-medium">2,847 points</span>
            </div>
            <button 
              onClick={() => navigate('preferences')}
              className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
              title="Settings"
            >
              <Settings className="w-5 h-5 text-gray-500" />
            </button>
            <button 
              onClick={() => navigate('landing')}
              className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
              title="Logout"
            >
              <LogOut className="w-5 h-5 text-gray-500" />
            </button>
          </div>
        </div>
      </header>
    );
  };

  const Sidebar = ({ isCollapsed, toggleSidebar }) => {
    const menuItems = [
      { id: 'profile', label: 'Profile', icon: User },
      { id: 'wallet', label: 'Wallet', icon: Wallet },
      { id: 'discover', label: 'Discover', icon: Compass }
    ];

    return (
      <aside className={`bg-white border-r border-gray-200 transition-all duration-300 relative z-30 ${
        isCollapsed ? 'w-16' : 'w-80'
      }`}>
        <div className="p-4 border-b border-gray-200">
          <button
            onClick={toggleSidebar}
            className={`w-full flex items-center p-2 rounded-lg hover:bg-gray-50 transition-colors ${
              isCollapsed ? 'justify-center' : 'justify-between'
            }`}
          >
            {isCollapsed ? (
              <Menu className="w-5 h-5 text-gray-500" />
            ) : (
              <>
                <span className="font-medium text-gray-700">Menu</span>
                <ChevronLeft className="w-5 h-5 text-gray-500" />
              </>
            )}
          </button>
        </div>

        <div className="p-4">
          <nav className="space-y-2">
            {menuItems.map((item) => {
              const Icon = item.icon;
              const isActive = activeTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => setActiveTab(item.id)}
                  className={`w-full flex items-center gap-3 p-3 rounded-lg text-sm font-medium transition-colors ${
                    isActive 
                      ? 'bg-blue-50 text-blue-700 border border-blue-200' 
                      : 'text-gray-600 hover:bg-gray-50'
                  } ${isCollapsed ? 'justify-center' : ''}`}
                  title={isCollapsed ? item.label : ''}
                >
                  <Icon className="w-5 h-5" />
                  {!isCollapsed && <span>{item.label}</span>}
                </button>
              );
            })}
          </nav>

          {!isCollapsed && (
            <div className="mt-8 p-4 bg-gray-50 rounded-lg">
              <h3 className="text-sm font-semibold text-gray-700 mb-3">This Month</h3>
              <div className="space-y-3">
                <div className="flex justify-between items-center">
                  <span className="text-sm text-gray-600">Total Donated</span>
                  <span className="text-sm font-semibold text-gray-900">$347</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-sm text-gray-600">Causes Supported</span>
                  <span className="text-sm font-semibold text-gray-900">8</span>
                </div>
                <div className="flex justify-between items-center">
                  <span className="text-sm text-gray-600">Impact Score</span>
                  <span className="text-sm font-semibold text-blue-700">94</span>
                </div>
              </div>
            </div>
          )}
        </div>
      </aside>
    );
  };

  const MainContent = () => {
    const posts = [
      {
        id: 1,
        user: 'Education Foundation',
        avatar: '📚',
        time: '2 hours ago',
        content: 'Thanks to your donations, we have built 3 new schools in rural areas this month! 🎉',
        image: 'https://images.unsplash.com/photo-1497486751825-1233686d5d80?w=500&h=300&fit=crop',
        likes: 234,
        comments: 18,
        category: 'Education'
      },
      {
        id: 2,
        user: 'Clean Water Initiative',
        avatar: '💧',
        time: '4 hours ago',
        content: 'Your contribution helped us install 15 water purifiers in villages across Maharashtra.',
        image: 'https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=500&h=300&fit=crop',
        likes: 189,
        comments: 12,
        category: 'Environment'
      },
      {
        id: 3,
        user: 'Healthcare Heroes',
        avatar: '🏥',
        time: '6 hours ago',
        content: 'Mobile health camps reached 500+ families this week. Your support makes it possible!',
        image: 'https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=500&h=300&fit=crop',
        likes: 167,
        comments: 9,
        category: 'Health'
      }
    ];

    return (
      <main className="flex-1 p-6 max-w-4xl overflow-y-auto">
        <div className="space-y-6">
          {/* Welcome Section */}
          <div className="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-200 rounded-2xl p-6">
            <h1 className="text-2xl font-semibold text-gray-900 mb-2">Welcome back! 👋</h1>
            <p className="text-gray-600 mb-4">Your donations have made an impact on 127 lives this month.</p>
            <div className="flex gap-4">
              <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg text-sm font-medium transition-colors">
                Make a Donation
              </button>
              <button className="bg-white hover:bg-blue-50 text-blue-600 border border-blue-200 px-4 py-2 rounded-lg text-sm font-medium transition-colors">
                View Impact Report
              </button>
            </div>
          </div>

          <h2 className="text-lg font-semibold text-gray-900">Recent Updates</h2>
          
          {posts.map((post) => (
            <div key={post.id} className="bg-white rounded-2xl p-6 border border-gray-200 hover:shadow-sm transition-shadow">
              <div className="flex items-center gap-3 mb-4">
                <div className="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center text-lg">
                  {post.avatar}
                </div>
                <div className="flex-1">
                  <h3 className="font-medium text-gray-900">{post.user}</h3>
                  <div className="flex items-center gap-2">
                    <span className="text-xs text-gray-500">{post.time}</span>
                    <span className="text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded-full">
                      {post.category}
                    </span>
                  </div>
                </div>
              </div>
              
              <p className="text-gray-700 mb-4">{post.content}</p>
              
              <img 
                src={post.image} 
                alt="Impact" 
                className="w-full h-48 object-cover rounded-lg mb-4" 
              />
              
              <div className="flex items-center gap-6 text-sm text-gray-500">
                <button className="flex items-center gap-2 hover:text-gray-700 transition-colors">
                  <Star className="w-4 h-4" />
                  <span>{post.likes} likes</span>
                </button>
                <button className="hover:text-gray-700 transition-colors">
                  {post.comments} comments
                </button>
                <button className="hover:text-gray-700 transition-colors">
                  Share
                </button>
              </div>
            </div>
          ))}
        </div>
      </main>
    );
  };

  const RightPanel = ({ isCollapsed, togglePanel }) => {
    const plans = [
      { id: 1, name: 'Education Fund', amount: 50, frequency: 'monthly', progress: 75, nextDonation: '3 days' },
      { id: 2, name: 'Clean Water Project', amount: 25, frequency: 'weekly', progress: 60, nextDonation: '2 days' },
    ];

    const badges = [
      { id: 1, name: 'First Donor', icon: '🎯', earned: true },
      { id: 2, name: 'Consistent Giver', icon: '⭐', earned: true },
      { id: 3, name: 'Education Champion', icon: '📚', earned: true },
      { id: 4, name: 'Monthly Hero', icon: '🏆', earned: false }
    ];

    const incentives = [
      { id: 1, type: 'cashback', amount: 15.30, description: '2% cashback earned' },
      { id: 2, type: 'points', amount: 250, description: 'Bonus points for streak' },
      { id: 3, type: 'voucher', amount: 10, description: 'Partner store voucher' }
    ];

    const totalEarnings = incentives.reduce((sum, item) => 
      item.type === 'cashback' ? sum + item.amount : sum, 0
    );

    if (isCollapsed) {
      return (
        <div className="w-16 bg-gray-50 border-l border-gray-200 relative overflow-y-auto">
          <button
            onClick={togglePanel}
            className="absolute -left-3 top-1/2 transform -translate-y-1/2 w-6 h-6 bg-white border border-gray-200 rounded-full flex items-center justify-center z-10"
          >
            <ChevronLeft className="w-4 h-4 text-gray-500" />
          </button>
          <div className="flex flex-col items-center gap-4 p-4 mt-5">
            <div className="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center">
              <Target className="w-4 h-4 text-blue-600" />
            </div>
            <div className="w-8 h-8 bg-purple-100 rounded-lg flex items-center justify-center">
              <Award className="w-4 h-4 text-purple-600" />
            </div>
            <div className="w-8 h-8 bg-green-100 rounded-lg flex items-center justify-center">
              <Gift className="w-4 h-4 text-green-600" />
            </div>
          </div>
        </div>
      );
    }

    return (
      <div className="w-80 bg-gray-50 border-l border-gray-200 p-4 overflow-y-auto relative">
        <button
          onClick={togglePanel}
          className="absolute -left-3 top-1/2 transform -translate-y-1/2 w-6 h-6 bg-white border border-gray-200 rounded-full flex items-center justify-center z-10"
        >
          <ChevronRight className="w-4 h-4 text-gray-500" />
        </button>

        <div className="space-y-6">
          {/* Your Plans */}
          <div className="bg-white rounded-2xl p-4 border border-gray-200">
            <div className="flex items-center justify-between mb-4">
              <h2 className="font-semibold text-gray-900">Your Plans</h2>
              <button className="text-xs text-blue-600 font-medium hover:text-blue-700">
                Manage
              </button>
            </div>
            <div className="space-y-3">
              {plans.map((plan) => (
                <div key={plan.id} className="p-3 bg-gray-50 rounded-lg">
                  <div className="flex justify-between items-start mb-2">
                    <div>
                      <h3 className="font-medium text-sm text-gray-900">{plan.name}</h3>
                      <p className="text-xs text-gray-600">${plan.amount}/{plan.frequency}</p>
                    </div>
                    <div className="text-right">
                      <div className="text-xs text-gray-500">Next in {plan.nextDonation}</div>
                    </div>
                  </div>
                  
                  <div className="space-y-1">
                    <div className="flex justify-between text-xs">
                      <span className="text-gray-600">Progress</span>
                      <span className="text-gray-700 font-medium">{plan.progress}%</span>
                    </div>
                    <div className="w-full h-1.5 bg-gray-200 rounded-full overflow-hidden">
                      <div 
                        className="h-full bg-blue-600 transition-all duration-300"
                        style={{ width: `${plan.progress}%` }}
                      />
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Achievements */}
          <div className="bg-white rounded-2xl p-4 border border-gray-200">
            <div className="flex items-center justify-between mb-4">
              <h2 className="font-semibold text-gray-900">Achievements</h2>
              <div className="text-xs text-gray-500">
                {badges.filter(b => b.earned).length}/{badges.length}
              </div>
            </div>
            <div className="grid grid-cols-2 gap-2">
              {badges.map((badge) => (
                <div 
                  key={badge.id} 
                  className={`p-3 rounded-lg border text-center ${
                    badge.earned 
                      ? 'bg-gradient-to-b from-blue-50 to-indigo-50 border-blue-200' 
                      : 'bg-gray-50 border-gray-200 opacity-60'
                  }`}
                >
                  <div className="text-lg mb-1">{badge.icon}</div>
                  <h3 className={`text-xs font-medium ${
                    badge.earned ? 'text-gray-900' : 'text-gray-500'
                  }`}>
                    {badge.name}
                  </h3>
                </div>
              ))}
            </div>
          </div>

          {/* Incentives */}
          <div className="bg-white rounded-2xl p-4 border border-gray-200">
            <div className="flex items-center justify-between mb-4">
              <h2 className="font-semibold text-gray-900">Incentives</h2>
              <button className="text-xs text-blue-600 font-medium hover:text-blue-700">
                Redeem
              </button>
            </div>

            <div className="bg-gradient-to-r from-green-50 to-emerald-50 border border-green-200 rounded-lg p-3 mb-4">
              <div className="flex items-center gap-2">
                <div className="w-8 h-8 bg-green-600 rounded-full flex items-center justify-center">
                  <DollarSign className="w-4 h-4 text-white" />
                </div>
                <div>
                  <div className="font-semibold text-gray-900">${totalEarnings.toFixed(2)}</div>
                  <div className="text-xs text-gray-600">Available</div>
                </div>
              </div>
            </div>

            <div className="space-y-2">
              {incentives.slice(0, 2).map((incentive) => (
                <div key={incentive.id} className="flex items-center justify-between p-2 bg-gray-50 rounded-lg">
                  <div className="flex items-center gap-2">
                    <div className={`w-6 h-6 rounded-full flex items-center justify-center ${
                      incentive.type === 'cashback' ? 'bg-green-100' :
                      incentive.type === 'points' ? 'bg-blue-100' : 'bg-purple-100'
                    }`}>
                      {incentive.type === 'cashback' && <DollarSign className="w-3 h-3 text-green-600" />}
                      {incentive.type === 'points' && <Star className="w-3 h-3 text-blue-600" />}
                      {incentive.type === 'voucher' && <Gift className="w-3 h-3 text-purple-600" />}
                    </div>
                    <div>
                      <div className="text-xs font-medium text-gray-900">
                        {incentive.type === 'cashback' && `${incentive.amount}`}
                        {incentive.type === 'points' && `${incentive.amount} pts`}
                        {incentive.type === 'voucher' && `${incentive.amount} voucher`}
                      </div>
                      <div className="text-xs text-gray-500">{incentive.description}</div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      <Header />
      <div className="flex flex-1 overflow-hidden">
        <Sidebar 
          isCollapsed={sidebarCollapsed} 
          toggleSidebar={() => setSidebarCollapsed(!sidebarCollapsed)} 
        />
        <MainContent />
        <RightPanel 
          isCollapsed={rightPanelCollapsed} 
          togglePanel={() => setRightPanelCollapsed(!rightPanelCollapsed)} 
        />
      </div>
    </div>
  );
};

// Main App Component with Router
const App = () => {
  const { currentPage } = useRouter();
  
  const renderPage = () => {
    switch(currentPage) {
      case 'landing':
        return <LandingPage />;
      case 'preferences':
        return <PreferencesPage />;
      case 'homepage':
        return <Homepage />;
      default:
        return <LandingPage />;
    }
  };

  return renderPage();
};

// Root Component
const UnifiedDonationApp = () => {
  return (
    <Router>
      <App />
    </Router>
  );
};

export default UnifiedDonationApp;