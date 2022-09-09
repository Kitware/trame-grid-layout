from pathlib import Path

# Compute local path to serve
serve_path = str(Path(__file__).with_name("serve").resolve())

# Serve directory for JS/CSS files
serve = {"__grid": serve_path}

# List of JS files to load (usually from the serve path above)
scripts = ["__grid/vue-grid-layout.js"]
