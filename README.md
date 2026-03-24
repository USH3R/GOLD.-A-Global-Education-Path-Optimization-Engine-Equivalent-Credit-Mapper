**Nine Files / Structure**  
  
/GOLD.-A-Global-Education-Path-Optimization-Engine-Equivalent-Credit-Mapper  
gold/  
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
    
**Folder Diagram Flow**  
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
