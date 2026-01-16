# GenEZ: AI-Powered Social Media Campaign Generator

**GenEZ** is a cutting-edge AI automation tool designed to streamline the creation of social media marketing campaigns. By leveraging a multi-agent architecture, GenEZ orchestrates the entire content lifecycle—from identifying trending topics to generating engaging copy and creating stunning visual assets.

## 🚀 Key Features

*   **Trend Scouting**: Automatically researches specific topics to identify current trends and relevant sub-topics.
*   **Intelligent Content Writing**: Generates tailored social media captions, blog posts, and taglines based on researched insights.
*   **Visual Generation**: "Visual Remix" agent creates custom, high-quality images using AI image generation tools (e.g., Google Imagen) to match the text content.
*   **Orchestration**: A central brain manages the workflow, ensuring seamless data flow between agents.
*   **CLI Interface**: Simple command-line interface for quick campaign generation.

## 🏗️ Architecture

GenEZ is built on a modular **Multi-Agent System** where each agent specializes in a specific task.

### Core Components

1.  **Orchestrator (`orchestrator.py`)**
    *   The central controller of the application.
    *   Initializes all agents.
    *   Manages the sequence of operations: `Input -> Trend Scouting -> Content Writing -> Visual Generation -> Output`.

2.  **Agents (`agents/`)**
    *   **TrendScoutAgent**: Queries external sources (like Google Search) to gather intelligence on a given topic.
    *   **ContentWriterAgent**: Processes the data from the Trend Scout to draft compelling marketing copy.
    *   **VisualRemixAgent**: Takes the creative direction from the content and prompts AI models to generate accompanying visuals.

3.  **Tools (`tools/`)**
    *   **GoogleSearchTool**: Provides agents with real-time web search capabilities.
    *   **ImagenClient**: Interfaces with Google's Vertex AI (Imagen) for state-of-the-art image synthesis.

## 📂 Project Structure

```
ADK@2/
├── agents/                 # Agent implementations
│   ├── content_writer.py
│   ├── trend_scout.py
│   └── visual_remix.py
├── tools/                  # Interface tools for APIs
│   ├── google_search.py
│   └── imagen_client.py
├── main.py                 # CLI Entry point
├── orchestrator.py         # Workflow manager
├── requirements.txt        # Python dependencies
├── .env.template           # Template for environment variables
└── README.md               # Project documentation
```

## 🛠️ Setup & Installation

Follow these steps to get GenEZ running on your local machine.

### Prerequisites
*   Python 3.8 or higher
*   Git

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Saketh875/Content-Gen-Agent.git
    cd Content-Gen-Agent
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    
    # Windows
    .\venv\Scripts\activate
    
    # Mac/Linux
    # source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration**
    *   Duplicate `.env.template` and rename it to `.env`.
    *   Open `.env` and add your API keys (e.g., Google Cloud Project ID, API Keys).

## 🖥️ Usage

To start a new campaign generation, run the `main.py` script with your desired topic:

```bash
python main.py --topic "Sustainable Fashion"
```

The system will:
1.  Scout for trends in "Sustainable Fashion".
2.  Draft posts based on those trends.
3.  Generate images to match the posts.
4.  Output the final campaign assets.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a Pull Request with your improvements.
