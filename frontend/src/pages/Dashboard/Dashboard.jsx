import { useState } from 'react';
import Button from '../../components/Button/Button';
import './Dashboard.css';
import reconcileExample from "../../assets/images/example_data_reconcile.PNG";
import validateExample from "../../assets/images/example_data_validate.PNG";
import Modal from '../../components/Modal/Modal';

export default function Dashboard() {
    // For uploading JSON file and displaying results
    const [uploadAction, setUploadAction] = useState(null);
    const [resultData, setResultData] = useState(null);
    const [showModal, setShowModal] = useState(false);

    // For local storage
    const [approvedReconciliations, setApprovedReconciliations] = useState([]);
    const [approvedValidations, setApprovedValidations] = useState([]);

    // Logic to handle file upload and call appropriate route
    const handleFileUpload = (event) => {
        if (event.target.files.length > 0) {
            const file = event.target.files[0];
            const reader = new FileReader();
            let endpoint = "";

            reader.onload = async (event) => {
                try {
                    const fileContent = JSON.parse(event.target.result);
                    console.log("File content:", fileContent);

                    const result = await fetch(endpoint, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(fileContent),
                    }).then((res) => res.json());

                    setResultData(result);
                    setShowModal(true);
                }
                catch (error) {
                    console.error("Error parsing file content:", error);
                }
            };

            if (uploadAction === "reconcile") {
                endpoint = "http://localhost:5000/api/reconcile/medication";
            } else if (uploadAction === "validate") {
                endpoint = "http://localhost:5000/api/validate/data-quality";
            }

            reader.readAsText(file);
            event.target.value = ""; // Reset the file input
        }
    };

    return (
        <div className="dashboard_container">

            <input 
                type="file"
                accept=".json"
                id="jsonUpload"
                style={{ display: 'none' }}
                onChange={handleFileUpload}
            />

            {/* Header and description */}
            <div className="dashboard_header">
                <h1>Clinical Data Reconciliation Engine (Mini Version)</h1>
            </div>

            <div className="dashboard_header_desc">
                <p>Healthcare providers often have conflicting information about the same patient across different systems.</p>
                <p>The mini engine helps by using generative AI to resolve these discrepancies.</p>
            </div>

            {/* Body - Reconciliation and validation containers */}
            <div className="dashboard_body_container">
                <div className="dashboard_reconciliation_container">
                    <h1>Reconcile</h1>
                    <p>Upload a patient's data in JSON format. GPT 4o-mini will determine the "most likely" truth from conflicting records based on context and sources.</p>
                    <p style={{ fontStyle: 'italic' }}>Example data upload with correct format: </p>
                    <img src={reconcileExample} alt="Reconciliation format example" className="image" />
                    <br></br>
                    <Button onClick={() => {
                        setUploadAction("reconcile");
                        document.getElementById('jsonUpload').click();
                    }}>UPLOAD</Button>
                </div>

                <div className="dashboard_validation_container">
                    <h1>Validate</h1>
                    <p>Upload a patient's record in JSON format. GPT 4o-mini will calculate data quality scores based on overall quality and specific dimensions.</p>
                    <p style={{ fontStyle: 'italic' }}>Example data upload with correct format: </p>
                    <img src={validateExample} alt="Validation format example" className="image" />
                    <br></br>
                    <Button onClick={() => {
                        setUploadAction("validate");
                        document.getElementById('jsonUpload').click();
                    }}>UPLOAD</Button>
                </div>
            </div>
            
            {/* Modal for displaying results after upload */}
            {showModal && (
                <Modal
                data={resultData}
                onClose={() => setShowModal(false)}
                onApprove={(approvedData) => {
                    if ("confidence_score" in approvedData) {
                        setApprovedReconciliations(prev => {
                            const approvalList = [...prev, approvedData];
                            localStorage.setItem('approvedReconciliations', JSON.stringify(approvalList));  // In-memory solution for approved responses
                            console.log("Approved Reconciliations:", approvalList);
                            return approvalList;
                        });
                    } else {
                        setApprovedValidations(prev => {
                            const approvalList = [...prev, approvedData];
                            localStorage.setItem('approvedValidations', JSON.stringify(approvalList));
                            console.log("Approved Validations:", approvalList);
                            return approvalList;
                        });
                    }
                }}
            />
            )}
        </div>
    );
    }