---
name: awesome-gcp-ai
description: Sets up the Gemini CLI or Antigravity agentic development environment by dynamically installing MCP servers, extensions, and agent skills based on requested products.
---
# Awesome GCP AI Setup Skill

This skill acts as your AI-powered companion for setting up a Google Cloud development environment. Rather than manually installing individual plugins, you can tell the agent which GCP products you intend to use, and it will automatically provision the necessary tools.

## Instructions
1. When the user asks to set up their environment for specific Google Cloud products (e.g. "I want to use Firebase and Cloud Run"), directly consult the `references/maad_stack.csv` file in this repository to find all required dependencies.
2. Cross-reference the user's requested products with the `Product` column in the CSV to identify the required `MCP Server (GitHub)`, `Gemini CLI Extension`, and `Agent Skills`.
3. **CRITICAL:** Present the required installations derived from the CSV to the user. You MUST explicitly ask the user for confirmation and ensure they understand that you will be installing new software on their system before proceeding. 
4. Upon user confirmation, perform the following installations:
   - **MCP Servers**: Configure the MCP servers (if tools are available to configure MCPs, or output instructions).
   - **Gemini CLI Extensions**: Install the extensions (e.g., `gemini extensions install <url>`).
   - **Agent Skills**: Fetch and install the agent skills (e.g., clone the repo or use `gemini skills install <url>`).
5. Once all tools are configured or the steps are generated, provide a comprehensive summary to the user outlining what was installed and that the workspace is ready for development.

## Resources
- `references/maad_stack.csv`: The CSV reference file containing the mapping of products to dependencies.
