# Architecture Decisions Document

<strong>Stack overview: </strong>
<ul>
  <li>React frontend</li>
  <li>Flask backend</li>
  <li>REST API communication</li>
  <li>JSON input/output</li>
</ul>

<br>

<strong>Architectural decisions: </strong>
<ul>
  <li>I used React + Flask in my capstone project, so I was already familiar with the stack and wanted to continue building my skills with it.</li>
  <li>In the backend, services (i.e., core logic) and routes are separated into folders. The app is built from an __init__.py file in a separate "app" folder that app.py (from the backend root) uses to create the app with. My goal in all of this separation was to define a package structure for creating distinct modules within.</li>
  <li>In the frontend, assets, components, and pages received their own folders. Further, components like the generic "button" received their own folders for their JSX and CSS files. A frontend gets unwieldy fast, so I wanted to compartmentalize components as much as possible for quick navigation.</li>
  <li>Tests per file were organized in a root directory "tests" folder. A conftest file was implemented to reduce redundancy throughout each individual file. Finally, I included sample data (pulled from the project instructions) in this folder to produce a mock LLM response with.</li>
  <li>I implemented OpenAI's API because it has extensive documentation and a lot of models to choose from. For the sake of this demo, I set up the prompt and response code but chose to use a mock response to avoid incurring charges. The API calls are functional with the mock response, and the actual LLM response is ready for use with a little tweaking.</li>
</ul>
