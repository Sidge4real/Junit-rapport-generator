import configparser
from fastapi.templating import Jinja2Templates
from modules.configuration import reports_dir, host, port, logs_dir
from fastapi import FastAPI, Form, Path, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
import os
from fastapi.staticfiles import StaticFiles
from modules.report_management import get_report_file_names

app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")

templates = Jinja2Templates(directory="template")
config_file_path = 'settings.cfg'

@app.get("/", response_class=HTMLResponse)
async def get_list_of_reports():
    # Get list of report file names
    report_files = get_report_file_names()

    # Generate HTML content to display the list of reports
    html_content = "<h1>List of Reports</h1>\n<ul>"
    for filename in report_files:
        link_name = filename.replace(".html", "")
        html_content += f'<li><a href="/file/{link_name}">{link_name}</a></li>'
    html_content += "</ul>"
    return HTMLResponse(content=html_content)

@app.get("/file/{file_name}", response_class=HTMLResponse)
async def get_report_files(file_name: str = Path(..., description="The name of the HTML report file")):
    # Construct the file path
    file_path = os.path.join(reports_dir, f"{file_name}.html")

    # Check if the file exists
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Report file not found")

    # Return the HTML file as a response
    return FileResponse(file_path)

@app.get("/file/public/css/style.css", response_class=FileResponse)
async def get_css_file():
    css_file_path = os.path.join(os.getcwd(), "public/css", "style.css")
    
    # Controleer of het bestand bestaat
    if not os.path.exists(css_file_path):
        raise HTTPException(status_code=404, detail="CSS file not found")
    
    return css_file_path

@app.get("/file/public/css/colors.css", response_class=FileResponse)
async def get_colors_css_file():
    css_file_path = os.path.join(os.getcwd(), "public/css", "colors.css")
    
    if not os.path.exists(css_file_path):
        raise HTTPException(status_code=404, detail="CSS file not found")
    
    return css_file_path

@app.get("/file/public/script.js", response_class=FileResponse)
async def get_script_js_file():
    js_file_path = os.path.join(os.getcwd(), "public", "script.js")
    
    if not os.path.exists(js_file_path):
        raise HTTPException(status_code=404, detail="JS file not found")
    
    return js_file_path

@app.get("/settings", response_class=HTMLResponse)
async def get_settings(request: Request):
    return templates.TemplateResponse("settings.html", {"request":request, "reports_dir":reports_dir, "logs_dir":logs_dir})

# Function to determine if a path is within the project directory
def is_within_project_dir(path):
    project_dir = Path(__file__).resolve().parent
    input_path = Path(path).resolve()
    return input_path.parts[:len(project_dir.parts)] == project_dir.parts

@app.post("/update-logs-dir")
async def update_logs_dir(new_logs_dir: str = Form(...)):
    global logs_dir

    if is_within_project_dir(new_logs_dir):
        # Convert to relative path within project
        logs_dir = os.path.relpath(new_logs_dir, start=os.getcwd())
    else:
        # Use absolute path if outside project directory
        logs_dir = new_logs_dir

    # Update the configuration file
    config = configparser.ConfigParser()
    config.read(config_file_path)
    config.set('directories', 'logs_dir', logs_dir)

    with open(config_file_path, 'w') as configfile:
        config.write(configfile)

    return {"message": "Log directory updated successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=host, port=port)