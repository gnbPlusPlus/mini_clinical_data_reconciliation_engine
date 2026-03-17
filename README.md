# Mini Clinical Data Reconciliation Engine README

<strong>About:</strong> A mini clinical data reconciliation engine that demonstrates how OpenAI API can be used to reconcile conflicting medical records. Built for an internship pre-assessment.

<br>

<strong>Estimated time spent: </strong> ~20 hours

<br>

<strong>Stack overview: </strong>
<ul>
  <li>React frontend</li>
  <li>Flask backend</li>
  <li>REST API communication (2 POST endpoints)</li>
  <li>JSON input/output</li>
</ul>

<br>

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

<br>

<strong>Architectural decisions: </strong>
<ul>
  <li>I used React + Flask in my capstone project, so I was already familiar with the stack and wanted to continue building my skills with it.</li>
  <li>In the backend, services (i.e., core logic) and routes are separated into folders. The app is built from an __init__.py file in a separate "app" folder that app.py (from the backend root) uses to create the app with. My goal in all of this separation was to define a package structure for creating distinct modules within.</li>
  <li>In the frontend, assets, components, and pages received their own folders. Further, components like the generic "button" received their own folders for their JSX and CSS files. A frontend gets unwieldy fast, so I wanted to compartmentalize components as much as possible for quick navigation.</li>
  <li>Tests per file were organized in a root directory "tests" folder. A conftest file was implemented to reduce redundancy throughout each individual file. Finally, I included sample data (pulled from the project instructions) in this folder to produce a mock LLM response with.</li>
  <li>I implemented OpenAI's API because it has extensive documentation and a lot of models to choose from. For the sake of this demo, I set up the prompt and response code but chose to use a mock response to avoid incurring charges. The API calls are functional with the mock response, and the actual LLM response is ready for use with a little tweaking.</li>
</ul>

<br>

<strong>Tradeoffs, what I'd improve with more time: </strong>
<ul>
  <li>I opted for an in-memory solution for storing approved reconciliation/validation results. This storage persists during a session (see below image) but wipes between refreshes, meaning it's not viable for production. I did this in the interest of time.</li>
  
  <br>
  <figure>
    <img src="/frontend/src/assets/images/local_storage.PNG">
  </figure>
  <br>
  
  <li>As aforementioned, the "LLM response" currently in use is actually a mock response meant for testing the app's functionality. I did this to avoid spending money on actual LLM responses.</li>
  <li>The frontend is very basic, and I'd like to implement a more aesthetically-pleasing design with more time. Also, if an invalid file is uploaded, the modal is simply blank (see below image). Some kind of error message would be more appropriate.</li>
  
  <br>
  <figure>
    <img src="/frontend/src/assets/images/blank_modal.PNG">
  </figure>
</ul>

<br>

<strong>Pytest results: </strong>
<ul>
  <li>The test files can be viewed in the tests folder.</li>
  <li>Tests can be run with "pytest -v" in the terminal from the root folder.</li>
</ul>
<br>
<img src="/frontend/src/assets/images/tests_passed.PNG">

