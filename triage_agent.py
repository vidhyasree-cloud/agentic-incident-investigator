# triage_agent.py

"""
AGENT ROLE: Senior Azure Incident Investigator
OBJECTIVE: Analyze IcM logs, generate KQL queries, and identify Root Cause.
"""

def agent_workflow(icm_log):
    # STEP 1: ANALYSIS
    # The AI reads the log and identifies the service (e.g., Compute, Storage, Networking).
    print("AI is analyzing log signature...")

    # STEP 2: TOOL CALLING (The most important part!)
    # The AI decides which KQL table to query based on the log.
    # Example: If 'Timeout' is found, query 'Requests' table.
    kql_query = generate_kql_tool(icm_log)
    print(f"Generated KQL: {kql_query}")

    # STEP 3: REASONING
    # The AI looks at the 'data' (simulated for now) and writes the summary.
    root_cause = generate_summary_tool(kql_query)
    return root_cause

def generate_kql_tool(log_text):
    # Logic to map error patterns to KQL queries
    return "Requests | where ResultCode == '500' | summarize count() by bin(Timestamp, 1h)"

def generate_summary_tool(data):
    return "Root Cause: High 500-error spike detected in West US region due to capacity bottleneck."

# Test the agent
print(agent_workflow("Error: DependencyTimeout in AzureSQL"))
