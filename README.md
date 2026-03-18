# Awesome Google Cloud Agent Skill

An opinionated Agent Skill that configures your development environment for Google Cloud, Firebase, ADK, and Vertex AI. Instead of reading through a static list of tools and extensions, you simply install this skill and ask it to set up what you need.

## How It Works

This repository contains an Agent Skill (`SKILL.md`) mapped against `maad_stack.csv`. The CSV contains the latest references to:
- **MCP Servers** (Model Context Protocol)
- **Gemini CLI Extensions**
- **Agent Skills**

## Usage

1. **Install the Skill** into your agent or Gemini CLI workspace:
   ```bash
   gemini skills install https://github.com/estherwasatester/awesome-google-cloud-ai
   ```

2. **Prompt the Agent**:
   _"Set up my environment for Firebase Authentication and Cloud Run."_
3. The Agent will:
   - Query `data/maad_stack.csv` using the included `scripts/setup_env.py` helper script.
   - Dynamically identify the required MCPs, CLI extensions, and other Agent Skills.
   - Automatically fetch and install them for you!

## Available Tools & Resources

Below is a complete index of the unique capabilities this agent skill can automatically install for you. Each layer provides different capabilities to the Gemini CLI and Antigravity IDE:

### MCP Servers
MCP servers give your AI agents contextual access to tools and infrastructure data.
- **[Cloud Run MCP](https://github.com/GoogleCloudPlatform/cloud-run-mcp)**: Allows agents to manage, inspect, and deploy serverless applications.
- **[Firebase Tools (CLI)](https://github.com/firebase/firebase-tools)**: Essential CLI tools enabling agents to execute Firebase tasks and manage projects.
- **[Google Cloud MCP](https://github.com/googleapis/gcloud-mcp)**: The core MCP server for provisioning and fetching data from various Google Cloud services.
- **[Apigee MCP](https://github.com/GoogleCloudPlatform/apigee-mcp-server)**: Allows the agent to interface with and analyze Apigee API gateways directly.

### Gemini CLI Extensions
Extensions provide customized commands, agents, and native UI elements to the Gemini Developer Experience.
- **[BigQuery Data Analytics](https://github.com/gemini-cli-extensions/bigquery-data-analytics)**: Query, analyze, and visualize structured data via BigQuery in the CLI.
- **[gloud Integration](https://github.com/gemini-cli-extensions/gcloud)**: Execute broad Google Cloud management commands natively.
- **[Conductor](https://github.com/gemini-cli-extensions/conductor)**: Orchestrate complex tasks and integrate Spec-Driven Development directly into your prompt flows.
- **[Firebase Native](https://github.com/gemini-cli-extensions/firebase)**: Comprehensive ecosystem support for scaffolding and managing Firebase products.
- **[Firestore Native](https://github.com/gemini-cli-extensions/firestore-native)**: Native tooling for executing and displaying Cloud Firestore database queries.
- **[Flutter Agent Support](https://github.com/gemini-cli-extensions/flutter)**: Tools tailored for AI-assisted Flutter application development.
- **[Genkit Utilities](https://github.com/gemini-cli-extensions/genkit)**: Assistants for building structured AI logic using Firebase Genkit.
- **[Jules Assistant](https://github.com/gemini-cli-extensions/jules)**: Code assistance tools and rules leveraging the Jules AI.
- **[Stitch Integration](https://github.com/gemini-cli-extensions/stitch)**: Utilities for Google Stitch environment setups.

### Agent Skills
Agent skills are precise, step-by-step instructions that teach your AI *how* to use the underlying tools correctly according to best practices.
- **Firebase Initialization & Base Setup**:
  - [Firebase Basics](https://github.com/firebase/agent-skills/tree/main/skills/firebase-basics)
  - [Local Environment Setup (Emulators)](https://github.com/firebase/agent-skills/tree/main/skills/firebase-local-env-setup)
- **Firebase Backend Services**:
  - [Authentication Basics](https://github.com/firebase/agent-skills/tree/main/skills/firebase-auth-basics)
  - [Firestore Standard Mode](https://github.com/firebase/agent-skills/tree/main/skills/firebase-firestore-standard) & [Enterprise Native Mode](https://github.com/firebase/agent-skills/tree/main/skills/firebase-firestore-enterprise-native-mode)
  - [Hosting Basics](https://github.com/firebase/agent-skills/tree/main/skills/firebase-hosting-basics) & [App Hosting Integrations](https://github.com/firebase/agent-skills/tree/main/skills/firebase-app-hosting-basics)
  - [Data Connect Integrations](https://github.com/firebase/agent-skills/tree/main/skills/firebase-data-connect-basics)
- **Firebase AI & Logic Layers**:
  - [Firebase AI Logic Implementation Basics](https://github.com/firebase/agent-skills/tree/main/skills/firebase-ai-logic-basics)
  - Developing Genkit with [Dart](https://github.com/firebase/agent-skills/tree/main/skills/developing-genkit-dart) or [TypeScript/JS](https://github.com/firebase/agent-skills/tree/main/skills/developing-genkit-js)
- **Agentic Generation Systems**:
  - [ADK Base Instructions](https://github.com/google/adk-docs/tree/main/skills): Core skills and instructions for building new agents using Google's Agent Development Kit.

---

## Contributing

To add new references to the ecosystem:
1. Update `maad_stack.csv` with the new Product details, MCP Server, Extension, or Agent Skill.
2. Submit a Pull Request.

That's it! The agent will immediately be able to leverage your additions when setting up environments.
