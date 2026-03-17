from backend.services.llm_service import generate_reconciliation_reasoning

# Function that accepts patient context and sources, and returns a reconciliation report
def reconcile_medication(patient_context, sources):
    extracted_sources = []

    # Extract information from each source to pass to the LLM
    for source in sources:
        system = source["system"]
        medication = source["medication"]
        reliability = source["source_reliability"]

        if "last_updated" in source:
            timestamp = source["last_updated"]
        elif "last_filled" in source:
            timestamp = source["last_filled"]
        else:
            timestamp = "unknown"

        # Add a new dict to the list for each source
        extracted_sources.append({
            "system": system,
            "medication": medication,
            "timestamp": timestamp,
            "reliability": reliability
        })

    reconciliation_report = generate_reconciliation_reasoning(patient_context, extracted_sources)

    return reconciliation_report