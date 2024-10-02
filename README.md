# CS-6320.002-Project - Travel Planning Assistant

## Overview

The **Travel Planning Assistant** is a conversational AI application designed to simplify your travel planning experience. It provides personalized travel advice, assists in booking accommodations, and generates customized itineraries based on your preferences. Leveraging advanced natural language processing and real-time data integration, it offers a seamless and eco-friendly approach to planning your next adventure.

## Table of Contents

- [Features](#features)
- [Team Members](#team-members)
- [Data Sources](#data-sources)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Conversational Interface**: Plan your travel through an intuitive chat-based system powered by GPT-4.
- **Intent Recognition**: Understands user intent to provide relevant travel recommendations.
- **Named Entity Recognition**: Extracts key information to manage conversation flow effectively.
- **Real-time Travel Data**: Retrieves up-to-date flight and accommodation information.
- **Eco-friendly Options**: Suggests environmentally friendly travel choices.
- **Personalized Itineraries**: Generates itineraries tailored to your interests and preferences.

## Team Members

- **Adam Uszynski**: Intent recognition and travel recommendations based on user input.
- **Rishi Villa**: Named Entity Recognition for key information extraction and conversation management.
- **Kyle Poulson**: API integration for travel data retrieval and eco-friendly option provision.

## Data Sources

- **Travel APIs**: For real-time flight and accommodation details.
- **Geographic Data**: Provides context such as points of interest.
- **Open Tourism Datasets**: Offers destination suggestions and activity recommendations.
- **OpenAI GPT-4**: Handles user input, maintains context, and generates responses.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/travel-planning-assistant.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd travel-planning-assistant
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your API keys:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   TRAVEL_API_KEY=your_travel_api_key
   ```

## Usage

1. **Run the Application**

   ```bash
   python app.py
   ```

2. **Start Planning**

   - Engage with the assistant through the conversational interface.
   - Provide your travel preferences and receive personalized recommendations.

## Contributing

We welcome contributions from the community. Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- **OpenAI GPT-4**: For powering our conversational AI.
- **Various Travel APIs**: For providing real-time travel data.
- **Open Tourism Datasets**: For enriching our destination and activity recommendations.