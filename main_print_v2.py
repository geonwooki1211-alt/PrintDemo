# rich 출력 모듈입니다.
# pip install rich 로 설치하세요.

from rich import print as rprint
from rich.table import Table
from rich.panel import Panel

name = "Alice"
age = 20
score = 95.5
data = {"name": name, "age": age, "score": score}

# rprint로 컬러 출력 예제 (f-string)
rprint(f"[bold green]Hello, [name]{name}[/]! Your score is [cyan]{score:.2f}[/].")

# Panel(패널)로 정보 출력
panel_text = f"""
[bold]Student Info[/]
Name: [yellow]{name}[/]
Age: [yellow]{age}[/]
Score: [cyan]{score:.2f}[/]
"""

panel = Panel(panel_text, title="Profile", border_style="blue")
rprint(panel)

# Table을 이용한 출력 (터미널에서 테이블 보기 좋게 출력)
table = Table(title="Records")
table.add_column("Key", style="bold")
table.add_column("Value")

for k, v in data.items():
    table.add_row(k, str(v))

rprint(table)

# sep, end 예제 (기본 print 함수와 동일하게 동작)
print("2025", "09", "23", sep="-", end="\n")
