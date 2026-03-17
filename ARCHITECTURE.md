# Architecture Decisions Document (ADD)

<strong>Stack overview</strong>
<ul>
  <li>React frontend</li>
  <li>Flask backend</li>
  <li>REST API communication</li>
  <li>JSON input/output</li>
</ul>
<br>
<strong>Architectural decisions</strong>
<ul>
  <li>I used React + Flask in my capstone project, so I was already familiar with the stack and wanted to continue building my skills with it.</li>
  <li>In the backend, services (i.e., core logic) and routes are separated into folders. The app is built from an __init__.py file in a separate "app" folder that app.py (from backend root) uses to create the app with. My goal in all of this separation was to define a package structure for creating distinct modules within.</li>
  <li>In the frontend, assets, components, and pages received their own folders. Further, components like the generic "button" received its own folder for its JSX and CSS files. A frontend gets unwieldy fast, so I wanted to compartmentalize components as much as possible for quick navigation.</li>
</ul>
