# pyrefly: ignore [missing-import]
from rich.console import Console
# pyrefly: ignore [missing-import]
from rich.table import Table
# pyrefly: ignore [missing-import]
from rich.panel import Panel

console = Console()

def display_dashboard():
    """
    Demonstrates modern terminal formatting with Rich.
    """
    # 1. Panel
    console.print(Panel("[bold cyan]Library Dashboard[/bold cyan]", subtitle="v1.0"))
    
    # 2. Table
    table = Table(title="Top Python Libraries (2024)")
    
    table.add_column("Library", justify="right", style="cyan", no_wrap=True)
    table.add_column("Domain", style="magenta")
    table.add_column("Popularity", justify="right", style="green")
    
    table.add_row("Pandas", "Data Science", "⭐⭐⭐⭐⭐")
    table.add_row("Requests", "Networking", "⭐⭐⭐⭐⭐")
    table.add_row("TensorFlow", "ML/AI", "⭐⭐⭐⭐")
    table.add_row("FastAPI", "Web APIs", "⭐⭐⭐⭐")
    
    console.print(table)
    
    # 3. Styled text
    console.print("\n[bold red]Alert:[/bold red] System looks [italic green]perfect[/italic green]! 🚀")

if __name__ == "__main__":
    display_dashboard()
