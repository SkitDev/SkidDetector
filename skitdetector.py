#!/usr/bin/env python3

import os
import sys
from pathlib import Path
from typing import List, Optional
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich import print as rprint
import typer
from dotenv import load_dotenv

# ts the main app fr fr
app = typer.Typer(help="SkitDetector - AI-powered code analysis tool")

# console lookin clean af
console = Console()

# get that api key or we dead fr
load_dotenv()

# no api key = no vibes
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    console.print("[red]Error: GEMINI_API_KEY not found in environment variables[/red]")
    sys.exit(1)

# setup that ai ts
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

def analyze_code(code: str) -> dict:
    """let the ai do its thing fr fr"""
    prompt = """
    Analyze this code and determine if it appears to be skidded (copied without understanding).
    Consider the following factors:
    1. Code quality and consistency
    2. Variable naming patterns
    3. Comment quality and relevance
    4. Overall code structure
    5. Presence of common skid patterns
    
    Provide a detailed analysis with:
    - Skid probability (0-100%)
    - Key indicators
    - Specific examples from the code
    - Recommendations for improvement
    
    Format the response as a structured analysis.
    """
    
    try:
        response = model.generate_content([prompt, code])
        return {
            "success": True,
            "analysis": response.text
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def scan_file(file_path: Path) -> dict:
    """read that file or we dead fr"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        return analyze_code(code)
    except Exception as e:
        return {
            "success": False,
            "error": f"Error reading file: {str(e)}"
        }

def display_results(file_path: str, results: dict):
    """make it look clean af"""
    if not results["success"]:
        console.print(f"[red]Error analyzing {file_path}: {results['error']}[/red]")
        return

    # table lookin fire ngl
    table = Table(title=f"Analysis Results for {file_path}")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    # add that analysis ts
    analysis = results["analysis"]
    table.add_row("Analysis", analysis)

    # show that fire
    console.print(Panel(table, title="[bold blue]SkitDetector Analysis[/bold blue]"))

@app.command()
def scan(
    path: str = typer.Argument(..., help="File or directory to scan"),
    recursive: bool = typer.Option(False, "--recursive", "-r", help="Scan directories recursively")
):
    """scan that code or we dead fr"""
    path = Path(path)
    
    if not path.exists():
        console.print(f"[red]Error: Path {path} does not exist[/red]")
        sys.exit(1)

    if path.is_file():
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task(f"Analyzing {path}...", total=None)
            results = scan_file(path)
            progress.update(task, completed=True)
            display_results(str(path), results)
    
    elif path.is_dir():
        files = []
        if recursive:
            files = list(path.rglob("*.py"))
        else:
            files = list(path.glob("*.py"))
        
        if not files:
            console.print("[yellow]No Python files found to analyze[/yellow]")
            return

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            for file in files:
                task = progress.add_task(f"Analyzing {file}...", total=None)
                results = scan_file(file)
                progress.update(task, completed=True)
                display_results(str(file), results)

if __name__ == "__main__":
    app() 