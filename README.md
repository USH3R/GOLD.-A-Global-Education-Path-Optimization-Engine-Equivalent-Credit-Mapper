![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![HTML](https://img.shields.io/badge/Frontend-HTML/CSS-orange)
![JSON](https://img.shields.io/badge/Data-JSON-green)
![Education](https://img.shields.io/badge/Domain-Education-blue)
![EdTech](https://img.shields.io/badge/Category-EdTech-purple)
![Credit Mapping](https://img.shields.io/badge/Focus-Credit%20Mapping-green)
![Optimization](https://img.shields.io/badge/Engine-Path%20Optimization-orange)
![Career Mobility](https://img.shields.io/badge/Impact-Career%20Mobility-brightgreen)
![Cost Reduction](https://img.shields.io/badge/Goal-Reduce%20Education%20Cost-red)
![Time Efficiency](https://img.shields.io/badge/Goal-Minimize%20Time-yellow)
![Accessibility](https://img.shields.io/badge/Impact-Accessible%20Education-lightgrey)
  
**Files Structure**  
  
/GOLD.-A-Global-Education-Path-Optimization-Engine-Equivalent-Credit-Mapper  
│  
├── README.md                 # Architecture, workflow, tech stack, modules, example data  
├── app.py                    # Flask web application (UI + backend)  
├── crawler.py                # Crawls MOOCs, ACE/NCCRS, CLEP, Study.com, Saylor, etc.  
├── degree_parser.py          # Loads degree requirements & normalizes course names  
├── mapper.py                 # Maps courses to degree requirements, calculates credits  
├── optimizer.py              # Path optimization: max credits, min cost, min time  
├── config.json               # Configuration file: user constraints, API keys, settings  
├── static/  
│   ├── style.css             # UI styling for web dashboard  
│   └── script.js             # Frontend interactivity  
└── data/  
    ├── degrees.json          # Standardized degree JSON for mapper and parser  
    └── example_courses.json  # Sample JSON output from crawler for testing  

**File Purposes**  
    1. README.md – Provides overview:  
      - Project title & description  
      - Architecture diagram (modules & data flow)  
      - Folder organization  
      - Example JSON structures for courses and degrees  
      - Tech stack  
      - Instructions to run  
    2. crawler.py – Collects courses from:  
      - MOOCs: Coursera, edX, Study.com  
      - ACE/NCCRS credit equivalence  
      - CLEP/DSST  
      - Optional: international universities with translation  
    3. degree_parser.py – Loads degree requirements:  
      - University catalogs, program pages  
      - Normalizes course names & credit requirements  
      - Produces standard JSON for mapping  
    4. mapping.py – Maps courses to degree requirements:  
      - Matches user’s available courses to degree needs  
      - Tracks transferable credits, cost, and duration  
    5. optimizer.py – Builds optimized education paths:  
      - Ranks paths by max transferable credits, minimal cost, shortest time  
      - Handles constraints: budget, duration, preferred institutions  
    6. ui.py – Web dashboard (Flask/FastAPI) or CLI interface:  
      - Input: target degree, user constraints  
      - Output: ranked degree paths  
      - Connects frontend static files (style.css + script.js)  
    7. config.json – Settings:  
      - User preferences: budget, max duration  
      - API keys (if needed)  
      - International translation toggle  
      - Default degree search filters  
    8. static/style.css – Minimal CSS for web dashboard:  
      - Tables, buttons, input fields  
      - Clean and functional, not aesthetic-heavy  
    9. static/script.js – Basic frontend interactivity:  
      - Handles form submission  
      - Displays JSON results or formatted tables  
    10. data/example_courses.json – Optional test data:  
      - JSON output for prototyping  
      - Sample courses for testing mapping & optimization modules  
    
**Folder Diagram Flow (Proposal)**  
+ gold/  
  |  
  +-- crawler.py      -> Scrapes courses (JSON output)  
  +-- degree_parser.py-> Loads degrees (JSON output)  
  +-- mapping.py      -> Matches courses to degrees  
  +-- optimizer.py    -> Calculates optimized paths  
  +-- ui.py           -> Provides interface for user interaction  
  +-- config.json     -> Holds settings and constraints  
  +-- static/         -> CSS & JS for web UI  
  +-- data/           -> Example course and degree data  
  +-- README.md       -> Documentation, architecture, instructions  
  
**Tech Stack**  
Python 3.11+  
Requests + BeautifulSoup → Web scraping  
Pandas / NumPy → Data processing  
JSON / SQLite → Storage & caching  
Flask or FastAPI → Web dashboard  
Optional: Google Translate API for foreign universities  
  
**Next Steps (Stage 1)**  
    1. Prototype crawler (start with Coursera or ACE).  
    2. Build sample degree JSON.  
    3. Map courses → degree requirements.  
    4. Simple optimizer: rank by transferable credits.  
    5. UI prototype: CLI or minimal Flask app.  
    6. Test locally with example_courses.json.  
    7. Expand crawler to multiple sources (international + MOOCs).  

🏃‍♂️ How to Run the GOLD Mapper  

Run in GitHub Codespaces (Recommended)  
Open this repository on GitHub.  
Click Code → Codespaces → Create Codespace on main.  
Wait for the environment to load.  
Open the terminal inside Codespaces.  
Run: bash run.sh  
  
Run Manually Inside the Repository (Local Machine)  
If you downloaded or cloned the repository:  
Open a terminal.  
Navigate to the project folder.  
Example: cd GOLD.-A-Global-Education-Path-Optimization-Engine-Equivalent-Credit-Mapper  
Run the launcher: bash run.sh  
  
If You Are Using a Random Public Terminal  
Public terminals do not automatically have this project. You must first download or clone the repository.  
A. Option A — Clone with Git  
Type:  
    git clone https://github.com/USH3R/GOLD.-A-Global-Education-Path-Optimization-Engine-Equivalent-Credit- Mapper.git  
    cd GOLD.-A-Global-Education-Path-Optimization-Engine-Equivalent-Credit-Mapper  
    bash run.sh  
B. Option B — Download ZIP  
Click Code → Download ZIP on GitHub.  
Extract the folder from the ZIP file. Then,  
Open a terminal in that folder. Run / Type: bash run.sh  

Quick Start Command  
This command is only for use inside a Terminal (like the one in Codespaces, terminal, or on your local machine).  
Verify Your Location: Ensure your terminal is currently pointed at the project directory;  
You should see GOLD.-A-Global-Education-Path-Optimization-Engine-Equivalent-Credit-Mapper in your command prompt.  
If you have already performed the setup in steps 1, 2, or 3 and just need to restart the application, type:      bash run.sh  
