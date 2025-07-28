# 🏢 CondoGPT

> AI-powered condo and real estate data analysis chatbot with natural language SQL queries

[![Flask](https://img.shields.io/badge/Flask-3.0.3-blue.svg)](https://flask.palletsprojects.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.2.11-green.svg)](https://langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)](https://postgresql.org/)

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [⚙️ Configuration](#️-configuration)
- [🖥️ Usage](#️-usage)
- [📂 Project Structure](#-project-structure)
- [🛠️ API Endpoints](#️-api-endpoints)
- [📊 Database Schema](#-database-schema)
- [🎨 UI Features](#-ui-features)
- [🤖 AI Capabilities](#-ai-capabilities)
- [🔧 Development](#-development)
- [📝 Environment Variables](#-environment-variables)
- [🚦 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🎯 Overview

CondoGPT is an intelligent real estate data analysis platform that combines the power of AI with comprehensive condo sales data. Users can ask natural language questions about real estate trends, sales data, building information, and market analysis, and receive accurate, data-driven answers through an intuitive web interface.

## ✨ Features

### 🤖 AI-Powered Analysis

- **Natural Language Queries**: Ask questions in plain English about real estate data
- **Intelligent SQL Generation**: Automatically converts questions to optimized PostgreSQL queries
- **Contextual Responses**: Maintains conversation history for follow-up questions
- **Multi-Model Support**: Works with OpenAI GPT models via OpenRouter API

### 🏢 Real Estate Intelligence

- **Condo Sales Analysis**: Comprehensive sales data with pricing trends
- **Building Information**: Detailed building profiles and characteristics
- **Market Insights**: Holding periods, price changes, and market dynamics
- **Geographic Data**: Location-based analysis with mapping capabilities

### 🎨 Modern Web Interface

- **Glass Morphism Design**: Beautiful, modern UI with backdrop blur effects
- **Responsive Layout**: Works seamlessly on desktop and mobile devices
- **Real-time Loading States**: Interactive feedback during AI processing
- **Conversation History**: Track and review previous interactions

### 📊 Data Visualization

- **Interactive Maps**: Google Maps integration for geographic visualization
- **Chart Support**: Chart.js integration for data visualization
- **Rich Formatting**: Proper display of complex query results

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Flask Server   │    │   AI Engine     │
│   (HTML/CSS/JS) │◄──►│   (Python)       │◄──►│   (LangChain)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
                       ┌──────────────────┐    ┌─────────────────┐
                       │   PostgreSQL     │    │   OpenRouter    │
                       │   Database       │    │   API           │
                       └──────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL database
- OpenRouter API key
- Google Maps API key (optional, for maps)

### 1. Clone the Repository

```bash
git clone https://github.com/zeelapatel/condo-gpt.git
cd condo-gpt
```

### 2. Set Up Virtual Environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate.bat
# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy and edit the environment variables in .venv/Scripts/activate.bat
set OPENROUTER_API_KEY=your_openrouter_api_key
set PG_USER=your_postgres_user
set PG_PASSWORD=your_postgres_password
set PG_HOST=localhost
set PG_PORT=5432
set PG_DB=condo_gpt
set FLASK_SECRET=your_secret_key
set GPLACES_API_KEY=your_google_api_key
```

### 5. Set Up Database

```bash
# Import the sample database
psql -U your_user -d condo_gpt -f sample_db.sql
```

### 6. Run the Application

```bash
python server.py
```

Visit `http://localhost:5000` to start using CondoGPT!

## 📦 Installation

### System Requirements

- **Operating System**: Windows 10+, macOS 10.15+, or Linux
- **Python**: 3.8 or higher
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Storage**: 2GB free space
- **Database**: PostgreSQL 12+

### Detailed Installation

1. **Clone Repository**

   ```bash
   git clone https://github.com/zeelapatel/condo-gpt.git
   cd condo-gpt
   ```

2. **Python Virtual Environment**

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate.bat

   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Python Dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Database Setup**

   ```bash
   # Create database
   createdb condo_gpt

   # Import sample data
   psql -d condo_gpt -f sample_db.sql
   ```

## ⚙️ Configuration

### Environment Variables

Create or modify `.venv/Scripts/activate.bat` (Windows) or `.venv/bin/activate` (Unix):

```bash
# API Keys
set OPENROUTER_API_KEY=sk-or-v1-your-key-here
set GPLACES_API_KEY=your-google-maps-api-key

# Database Configuration
set PG_USER=postgres
set PG_PASSWORD=your_password
set PG_HOST=localhost
set PG_PORT=5432
set PG_DB=condo_gpt

# Flask Configuration
set FLASK_SECRET=your-super-secret-key
```

### Database Configuration

The application expects a PostgreSQL database with the following tables:

- `core_condosale`: Sales transaction data
- `core_condounit`: Individual unit information
- `core_condobuilding`: Building details and metadata

## 🖥️ Usage

### Basic Queries

**Sales Analysis:**

```
"What is the most recent sale in the database?"
"Show me sales in Brickell from 2023"
"What's the average price per square foot in downtown?"
```

**Market Trends:**

```
"What is the holding period for condos in Brickell?"
"Show me price trends for 2-bedroom units"
"Which buildings have the highest appreciation?"
```

**Building Information:**

```
"Tell me about buildings on Biscayne Boulevard"
"What amenities do luxury buildings offer?"
"Show me buildings with ocean views"
```

### Advanced Features

**Follow-up Questions:**
The system maintains conversation context, allowing for natural follow-up questions.

**Complex Analysis:**
Ask multi-part questions involving joins across sales, units, and building data.

**Data Export:**
Results can be formatted for further analysis or reporting.

## 📂 Project Structure

```
condo-gpt/
├── 📁 .venv/                 # Virtual environment
│   └── Scripts/
│       ├── activate.bat      # Environment variables (Windows)
│       └── activate          # Environment variables (Unix)
├── 📁 templates/
│   └── index.html           # Main web interface
├── 📁 static/               # Static assets (CSS, JS, images)
├── 📄 main.py              # Core AI logic and database connection
├── 📄 server.py            # Flask web server
├── 📄 prefix.py            # SQL query prefix templates
├── 📄 boilerplate.py       # SQL boilerplate code
├── 📄 tools.py             # Utility functions and tools
├── 📄 sample_db.sql        # Database schema and sample data
├── 📄 requirements.txt     # Python dependencies
└── 📄 README.md           # This file
```

### Core Components

**main.py**

- Database connection management
- LangChain agent configuration
- AI query processing
- OpenRouter API integration

**server.py**

- Flask web application
- Session management
- Conversation history
- Request routing

**prefix.py**

- SQL query templates
- Database schema information
- Query optimization hints

**boilerplate.py**

- Reusable SQL code snippets
- Complex query patterns
- Data formatting functions

## 🛠️ API Endpoints

### Web Routes

| Method | Endpoint | Description                |
| ------ | -------- | -------------------------- |
| GET    | `/`      | Main application interface |
| POST   | `/`      | Process user questions     |
| POST   | `/`      | Clear conversation history |

### Request Format

**Question Submission:**

```json
{
  "question": "What is the average price in Brickell?"
}
```

**Clear History:**

```json
{
  "sign_out": "true"
}
```

## 📊 Database Schema

### Core Tables

**core_condosale**

- `id`: Unique sale identifier
- `condo_unit_id`: Reference to unit
- `closing_date`: Sale date
- `sale_price`: Transaction amount
- `price_per_sqft`: Calculated price per square foot

**core_condounit**

- `id`: Unique unit identifier
- `building_id`: Reference to building
- `unit_number`: Unit designation
- `bedrooms`: Number of bedrooms
- `bathrooms`: Number of bathrooms
- `square_feet`: Unit size

**core_condobuilding**

- `id`: Unique building identifier
- `name`: Building name
- `address`: Street address
- `city`: City location
- `zip_code`: Postal code
- `year_built`: Construction year

## 🎨 UI Features

### Design Elements

- **Glass Morphism**: Modern translucent design with backdrop blur
- **Gradient Backgrounds**: Beautiful color transitions
- **Smooth Animations**: Micro-interactions and hover effects
- **Responsive Grid**: Adapts to all screen sizes

### Interactive Components

- **Smart Search**: Auto-focus and loading states
- **Real-time Feedback**: Progress indicators during processing
- **Conversation Flow**: Organized Q&A history
- **Clear Actions**: Easy session management

### Accessibility

- **Keyboard Navigation**: Full keyboard support
- **Screen Reader Friendly**: Semantic HTML structure
- **High Contrast**: Readable color combinations
- **Mobile Optimized**: Touch-friendly interface

## 🤖 AI Capabilities

### Natural Language Processing

- **Intent Recognition**: Understands various question formats
- **Context Awareness**: Maintains conversation state
- **Error Handling**: Graceful handling of ambiguous queries
- **Query Optimization**: Efficient SQL generation

### Supported Query Types

- **Aggregations**: SUM, AVG, COUNT, MIN, MAX
- **Filtering**: Date ranges, price ranges, locations
- **Joins**: Cross-table analysis
- **Grouping**: Categorical breakdowns
- **Sorting**: Ordered results

### Model Configuration

- **Model**: OpenAI GPT-3.5-turbo (via OpenRouter)
- **Temperature**: 0.0 (deterministic responses)
- **Max Tokens**: 500 (optimized for responses)
- **Retries**: 2 (error resilience)

## 🔧 Development

### Setting Up Development Environment

1. **Install Development Dependencies**

   ```bash
   pip install -r requirements.txt
   pip install black flake8 pytest  # Additional dev tools
   ```

2. **Code Formatting**

   ```bash
   black *.py  # Format code
   flake8 *.py  # Check style
   ```

3. **Running Tests**
   ```bash
   pytest tests/  # Run test suite
   ```

### Adding New Features

**Custom SQL Templates:**

1. Add templates to `prefix.py`
2. Update boilerplate in `boilerplate.py`
3. Test with sample queries

**New AI Capabilities:**

1. Modify agent configuration in `main.py`
2. Add new tools in `tools.py`
3. Update prompt templates

**UI Enhancements:**

1. Modify `templates/index.html`
2. Add static assets to `static/`
3. Update Flask routes in `server.py`

### Debugging

**Enable Debug Mode:**

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

**Database Query Debugging:**

```python
# Add to main.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

**AI Response Debugging:**

```python
# Enable verbose output
toolkit = SQLDatabaseToolkit(db=db, llm=llm, verbose=True)
```

## 📝 Environment Variables

### Required Variables

| Variable             | Description                      | Example          |
| -------------------- | -------------------------------- | ---------------- |
| `OPENROUTER_API_KEY` | OpenRouter API key for AI models | `sk-or-v1-...`   |
| `PG_USER`            | PostgreSQL username              | `postgres`       |
| `PG_PASSWORD`        | PostgreSQL password              | `mypassword`     |
| `PG_HOST`            | Database host                    | `localhost`      |
| `PG_PORT`            | Database port                    | `5432`           |
| `PG_DB`              | Database name                    | `condo_gpt`      |
| `FLASK_SECRET`       | Flask session secret             | `supersecretkey` |

### Optional Variables

| Variable          | Description         | Default      |
| ----------------- | ------------------- | ------------ |
| `GPLACES_API_KEY` | Google Maps API key | None         |
| `FLASK_ENV`       | Flask environment   | `production` |
| `DEBUG`           | Enable debug mode   | `False`      |

## 🚦 Troubleshooting

### Common Issues

**Database Connection Error**

```bash
Error: could not connect to server
```

- Check PostgreSQL is running
- Verify connection parameters
- Ensure database exists

**API Key Error**

```bash
Error code: 401 - Unauthorized
```

- Verify OpenRouter API key is correct
- Check account credits/billing
- Ensure key has proper permissions

**Token Limit Exceeded**

```bash
Error code: 402 - Prompt tokens limit exceeded
```

- Upgrade OpenRouter account
- Use shorter queries
- Switch to GPT-3.5-turbo model

**Import Errors**

```bash
ModuleNotFoundError: No module named 'langchain'
```

- Activate virtual environment
- Install requirements: `pip install -r requirements.txt`
- Check Python version compatibility

## 🙏 Acknowledgments

- **LangChain** for the powerful AI framework
- **OpenAI** for GPT models via OpenRouter
- **Flask** for the web framework
- **PostgreSQL** for robust data storage
- **Chart.js** for data visualization
- **Google Maps** for geographic features
- **https://www.youtube.com/watch?v=ShEOoJLSLbI** Youtube video 
---

