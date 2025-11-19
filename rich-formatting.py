# package rich

from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="Sales Summary")
table.add_column("Region", justify="center")
table.add_column("Total Sales", justify="right")

data = [("North", "12000"),("South", "8900")]

for region, total in data:
    table.add_row(region, total)

console.print(table)
