import './Modal.css';

export default function Modal({ data, onClose, onApprove }) {
    // Helper functions to determine colors based on scores/severity
    const confidenceColor = (score) => {
        if (score >= 0.8) return 'green';
        if (score >= 0.5) return 'orange';
        return 'red';
    }
    const qualityColor = (rating) => {
        if (rating >= 80) return 'green';
        if (rating >= 50) return 'orange';
        return 'red';
    }
    const severityColor = (severity) => {
        switch (severity) {
            case 'low':
                return 'green';
            case 'medium':
                return 'orange';
            case 'high':
                return 'red';
            default:
                return 'black';
        }  
    }

    // Stop clicks inside the modal from closing it
    const handleContainerClick = (e) => e.stopPropagation();

    return (
        <div className="modal_overlay" onClick={onClose}>
            <div className="modal_container" onClick={handleContainerClick}>
                {/* Close button 'X' in top right corner of screen */}
                <button className="modal_close_button" onClick={onClose}>X</button>

                {/* Reconciliation Result */}
                {"confidence_score" in data && (
                    <>
                        <h2 style={{ textAlign: 'center' }}>Reconciliation Result</h2>
                        <hr style={{ border: '1px solid #ccc', margin: '1rem 0' }}></hr>
                        <p><strong>Medication: </strong>{data.reconciled_medication}</p>
                        <p><strong>Confidence Score:  <span style={{ color: confidenceColor(data.confidence_score) }}>{Math.round(data.confidence_score * 100)}%</span></strong></p>
                        <p><strong>Reasoning: </strong>{data.reasoning}</p>
                        <hr style={{ border: '1px solid #ccc', margin: '1rem 0' }}></hr>

                        {/* Accept/Reject buttons */}
                        <div className="modal_actions">
                            <button 
                                className="modal_action_button" style={{ backgroundColor: 'green', color: 'white' }} onClick={() => { onApprove(data); onClose(); }}>APPROVE</button>
                            <button className="modal_action_button" style={{ backgroundColor: 'red', color: 'white' }} onClick={onClose}>REJECT</button>
                        </div>
                    </>
                )}

                {/* Data Quality Validation Result */}
                {"overall_score" in data && (
                    <>
                        <h2 style={{ textAlign: 'center' }}>Data Quality Validation Result</h2>
                        <hr style={{ border: '1px solid #ccc', margin: '1rem 0' }}></hr>
                        <p><strong>Overall Score: <span style={{ color: qualityColor(data.overall_score) }}>{data.overall_score}</span></strong> / 100</p>
                        <p><strong>Breakdown: </strong></p>
                        <ul>
                            <li><strong>Completeness: <span style={{ color: qualityColor(data.breakdown.completeness) }}>{data.breakdown.completeness}</span></strong> / 100</li>
                            <li><strong>Accuracy: <span style={{ color: qualityColor(data.breakdown.accuracy) }}>{data.breakdown.accuracy}</span></strong> / 100</li>
                            <li><strong>Timeliness: <span style={{ color: qualityColor(data.breakdown.timeliness) }}>{data.breakdown.timeliness}</span></strong> / 100</li>
                            <li><strong>Clinical Plausibility: <span style={{ color: qualityColor(data.breakdown.clinical_plausibility) }}>{data.breakdown.clinical_plausibility}</span></strong> / 100</li>
                        </ul>
                        <p><strong>Issues Detected (with severity): </strong></p>
                        <ul>
                            {data.issues_detected?.map((issue, index) => (
                                <li key={index}>
                                    <strong><span style={{ color: severityColor(issue.severity) }}>{issue.severity.toUpperCase()}</span> - {issue.field}:</strong> {issue.issue}
                                </li>
                            ))}
                        </ul>
                        <hr style={{ border: '1px solid #ccc', margin: '1rem 0' }}></hr>

                        {/* Accept/Reject buttons */}
                        <div className="modal_actions">
                            <button className="modal_action_button" style={{ backgroundColor: 'green', color: 'white' }} onClick={() => { onApprove(data); onClose(); }}>APPROVE</button>
                            <button className="modal_action_button" style={{ backgroundColor: 'red', color: 'white' }} onClick={onClose}>REJECT</button>
                        </div>
                    </>
                )}
            </div>
        </div>
    );
}