import os

def analyze_log(log_entry):
    """
    A placeholder function for your AI Agent logic.
    In the next lesson, we will connect this to an LLM like Llama-3 or GPT-4o.
    """
    print(f"--- Analyzing Incident Log ---")
    print(f"Log Received: {log_entry}")
    
    # Logic to identify 'ERROR' or 'CRITICAL' levels
    if "ERROR" in log_entry.upper():
        return "Action Required: Potential system crash detected."
    return "Status: System Healthy."

if __name__ == "__main__":
    sample_log = "2026-04-09 10:00:00 - ERROR - Database connection timeout"
    result = analyze_log(sample_log)
    print(result)
