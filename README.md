# GenEZ: AI-Powered Social Media Campaign Generator

GenEZ is an AI-powered tool designed to automate the creation of social media content. It uses a multi-agent architecture to research trends, write engaging content, and generate visual assets.

## Features

- **Trend Scouting**: Research trending topics (currently simulated).
- **Content Writing**: Generate creative text captions and posts.
- **Visual Remix**: Create AI-generated images for campaigns.
- **CLI Interface**: Easy-to-use command line interface.

## Architecture

The project consists of an Orchestrator that manages specialized Agents:\

- **Orchestrator**: Coordinates the workflow.
- **TrendScoutAgent**: Finds trends.
- **ContentWriterAgent**: Drafts text.
- **VisualRemixAgent**: Generates images.

## Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Saketh875/Content-Gen-Agent.git
    cd Content-Gen-Agent
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables**:
    Copy `.env.template` to `.env` and fill in your API keys.

## Usage

Run the application with a topic:

```bash
python main.py --topic "Artificial Intelligence"
```
