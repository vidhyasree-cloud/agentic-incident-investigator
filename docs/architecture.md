# 🏛️ System Architecture: Agentic Incident Investigator

This project uses an **Agentic RAG** (Retrieval-Augmented Generation) workflow.

### The Workflow:
1. **Ingestion:** The system monitors raw system logs.
2. **Analysis:** An AI Agent (Llama-3/GPT-4o) parses the log for root causes.
3. **Action:** The agent suggests a CLI command or a fix to resolve the incident.
