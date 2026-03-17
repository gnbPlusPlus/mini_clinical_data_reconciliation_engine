# Mini Clinical Data Reconciliation Engine README

<strong>About:</strong> (React + Flask) A mini clinical data reconciliation engine that demonstrates how OpenAI API can be used to reconcile conflicting medical records. Built for an internship pre-assessment.

<strong>Images of app in-use:</strong>
<br>
<figure>
  <img src="/frontend/src/assets/images/the_mini_reconciler_example_zoomed_out.PNG">
  <!--figcaption>Dashboard (zoomed out 75%)</figcaption-->
</figure>
<figure>
  <img src="/frontend/src/assets/images/the_mini_reconciler_reconciliation_results.PNG">
  <!--figcaption>Reconciliation results modal</figcaption-->
</figure>
<figure>
  <img src="/frontend/src/assets/images/the_mini_reconciler_validation_results.PNG">
  <!--figcaption>Validation results modal</figcaption-->
</figure>
<br>

<strong>Video walkthrough:</strong>
<br>
<!-- embedded video here -->
<br>

<strong>Local setup instructions (I use VS Code & its terminal):</strong>
<ol>
  <li>
    <strong>Clone the repository:</strong>
    <ul>
      <li>git clone https://github.com/gnbPlusPlus/mini_clinical_data_reconciliation_engine.git</li>
      <li>cd mini_clinical_data_reconciliation_engine <em>(NOTE: this is the root folder)</em></li>
    </ul>
  </li>
  <br>
  <li>
    <strong>Create a virtual environment (venv or myenv):</strong>
    <ul>
      <li>python -m venv venv</li>
    </ul>
  </li>
   <br>
  <li>
    <strong>Activate the virtual environment (Windows):</strong>
    <ul>
      <li>.\venv\Scripts\activate</li>
    </ul>
  </li>
   <br>
  <li>
    <strong>Install Python dependencies:</strong>
    <ul>
      <li>pip install -r requirements.txt</li>
    </ul>
  </li>
   <br>
  <li>
    <strong>Run the backend (Flask server) from the root folder:</strong>
    <ul>
      <li>python -m backend.app</li>
    </ul>
  </li>
   <br>
  <li>
    <strong>Run the frontend (React) from the frontend folder:</strong>
    <ul>
      <li>cd frontend</li>
      <li>npm install <em>(NOTE: you only need to do this once)</em></li>
      <li>npm run dev</li>
    </ul>
  </li>
  <br>
  <li>
    <strong>Visit localhost URL for frontend to interact with app:</strong>
    <ul>
      <li>Likely frontend URL: http://localhost:5173/</li>
      <li>Press F12 to monitor file uploads, file approvals, and blocked (status 400) requests.</li>
    </ul>
  </li>
</ol>
