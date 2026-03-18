---
name: awesome-gcp-ai
description: Sets up Google Cloud AI development environment by dynamically installing MCP servers, extensions, and agent skills based on requested products.
---
# Awesome GCP AI Setup Skill

This skill acts as your AI-powered companion for setting up a Google Cloud development environment. Rather than manually installing individual plugins, you can tell the agent which GCP products you intend to use, and it will automatically provision the necessary tools.

## Instructions
1. When the user asks to set up their environment for specific Google Cloud products (e.g. "I want to use Firebase and Cloud Run"), use the `scripts/setup_env.py` script provided in this repository to find all required dependencies.
   - Execute: `python3 scripts/setup_env.py "firebase" "cloud run"`
2. The script will output a JSON object containing the required `mcp_servers`, `extensions`, and `agent_skills`.
3. **CRITICAL:** Present the required installations from the JSON output to the user. You MUST explicitly ask the user for confirmation and ensure they understand that you will be installing new software on their system before proceeding. 
4. Upon user confirmation, perform the following installations:
   - **MCP Servers**: Configure the MCP servers (if tools are available to configure MCPs, or output instructions).
   - **Gemini CLI Extensions**: Install the extensions (e.g., `gemini extensions install <url>`).
   - **Agent Skills**: Fetch and install the agent skills (e.g., clone the repo or use `gemini skills install <url>`).
5. Once all tools are configured or the steps are generated, provide a comprehensive summary to the user outlining what was installed and that the workspace is ready for development.

## Resources
- `data/maad_stack.csv`: The database containing the mapping of products to dependencies.
- `scripts/setup_env.py`: The helper script to parse the CSV safely.
