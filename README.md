# Mini Clinical Data Reconciliation Engine README
About: (React + Flask) A mini clinical data reconciliation engine that demonstrates how OpenAI API can be used to reconcile conflicting medical records. Built for an internship pre-assessment.

Local setup instructions (I use VS Code & its terminal):
<ol>
  <li>
    Clone the repository:
    <ul>
      <li>git clone https://github.com/gnbPlusPlus/mini_clinical_data_reconciliation_engine.git</li>
      <li>cd mini_clinical_data_reconciliation_engine <em>(NOTE: this is the root folder)</em></li>
    </ul>
  </li>
  <li>
    Create a virtual environment (venv or myenv):
    <ul>
      <li>python -m venv venv</li>
    </ul>
  </li>
  <li>
    Activate the virtual environment (Windows):
    <ul>
      <li>.\venv\Scripts\activate</li>
    </ul>
  </li>
  <li>
    Install Python dependencies:
    <ul>
      <li>pip install -r requirements.txt</li>
    </ul>
  </li>
  <li>
    Run the backend (Flask server) from the root folder:
    <ul>
      <li>python -m backend.app</li>
    </ul>
  </li>
  <li>
    Run the frontend (React) from the frontend folder:
    <ul>
      <li>cd frontend</li>
      <li>npm install <em>(NOTE: you only need to do this once)</em></li>
      <li>npm run dev</li>
    </ul>
  </li>
</ol>
