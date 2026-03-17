import os, json
from flask.cli import load_dotenv
from openai import OpenAI

# Use mock LLM response for testing before incurring charges with OpenAI API
load_dotenv()
USE_MOCK_LLM = os.getenv("USE_MOCK_LLM", "false").lower() == "true"

def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set")
    return OpenAI(api_key=api_key)

def generate_reconciliation_reasoning(patient_context, sources):
    if USE_MOCK_LLM or os.getenv("OPENAI_API_KEY") is None:
        return {
            "reconciled_medication": "Metformin 500mg twice daily",
            "confidence_score": 0.88,
            "reasoning": "Primary care record is most recent clinical encounter. Dose reduction appropriate given declining kidney function (eGFR 45). Pharmacy fill may reflect old prescription.",
            "recommended_actions": ["Update Hospital EHR to 500mg twice daily", "Verify with pharmacist that correct dose is being filled"],
            "clinical_safety_check": "PASSED"
        }
    
    client = get_client()

    system_prompt = "You are a helpful assistant that reconciles patient data, detects implausible data (e.g., drug-disease mismatches), and provides explanations."

    user_prompt = f"""
    Given the patient context and sources, determine the likeliest medication, provide a confidence score, generate a brief reasoning for reconciliation, determine recommended actions, and designate whether the reconciliation is safe.

    Patient context: {patient_context}
    Sources: {sources}

    Return a JSON object with the following structure:
    {
        "reconciled_medication": "...",
        "confidence_score": 0.0 - 1.0,
        "reasoning": "...",
        "recommended_actions": ["..."],
        "clinical_safety_check": "PASSED or FLAGGED"
    }
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )
    
    llm_reconciliation_response = response.choices[0].message.content

    try:
        llm_reconciliation_result = json.loads(llm_reconciliation_response)
    except json.JSONDecodeError:
        # If the response is not valid JSON, return the raw response
        llm_reconciliation_result = {"reconciliation_response": llm_reconciliation_response}

    return llm_reconciliation_result

def generate_data_quality_scores(patient_record):
    if USE_MOCK_LLM or os.getenv("OPENAI_API_KEY") is None:
        return {
            "overall_score": 62,
            "breakdown": {
                "completeness": 60,
                "accuracy": 50,
                "timeliness": 70,
                "clinical_plausibility": 40
            },
            "issues_detected": [
                {
                    "field": "allergies",
                    "issue": "No allergies documented - likely incomplete",
                    "severity": "medium"
                },
                {
                    "field": "vital_signs.blood_pressure",
                    "issue": "Blood pressure 340/180 is physiologically implausible",
                    "severity": "high"
                },
                {
                    "field": "last_updated",
                    "issue": "Data is 7+ months old",
                    "severity": "medium"
                }
            ]
        }
    
    client = get_client()

    system_prompt = "You are a helpful assistant that evaluates the quality of patient data, detects implausible data (e.g., impossible vital signs), and provides scores."

    user_prompt = f"""
    Given the patient's record, determine the overall data quality score (0-100) along with a scores (0-100) for completeness, accuracy, timeliness, and clinical plausibility. Identify any issues detected in the data and rate their severity.
    Demographics: {patient_record.get('demographics')}
    Medications: {patient_record.get('medications')}
    Allergies: {patient_record.get('allergies')}
    Conditions: {patient_record.get('conditions')}
    Vital Signs: {patient_record.get('vital_signs')}
    Last Updated: {patient_record.get('last_updated')}

    Return a JSON object with the following structure:
    {
        "overall_score": 0 - 100,
        "breakdown": {
            "completeness": 0 - 100,
            "accuracy": 0 - 100,
            "timeliness": 0 - 100,
            "clinical_plausibility": 0 - 100
        },
        "issues_detected": [
            {
                "field": "...",
                "issue": "...",
                "severity": "low, medium, or high"
            }
        ]
    }
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )
    
    llm_validation_response = response.choices[0].message.content

    try:
        llm_validation_result = json.loads(llm_validation_response)
    except json.JSONDecodeError:
        llm_validation_result = {"validation_response": llm_validation_response}

    return llm_validation_result
