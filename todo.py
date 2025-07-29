import click
import json
from pathlib import Path

@click.group()
def cli():
    """Manage to-do list from the command line."""
    pass

# Function to load tasks from JSON file
def load_tasks():
    task_file = Path('tasks.json')
    if task_file.exists():
        with open(task_file, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)
    
@cli.command()
@click.argument('task_text')
def add(task_text):
    tasks = load_tasks()
    new_id = max([task['id'] for task in tasks] + [0]) + 1
    tasks.append({'id': new_id, 'task': task_text, 'done': False})
    save_tasks(tasks)
    click.echo(f"Added task {new_id}: {task_text}")
    
@cli.command()
def list():
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return
    for task in tasks:
        status = "✔" if task["done"] else "✖"
        click.echo(click.style(f"{task['id']}: [{status}] {task['task']}", fg="green"))
        
@cli.command()
@click.argument('task_id', type=int)
def done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = True
            save_tasks(tasks)
            click.echo(f"Marked task {task_id} as done.")
            return
    click.echo(f"Task {task_id} not found.")
    
@cli.command()
@click.argument("task_id", type=int)
def delete(task_id):
    tasks = load_tasks()
    initial_length = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) < initial_length:
        save_tasks(tasks)
        click.echo(f"Deleted task: {task_id}.")
    else:
        click.echo(f"Task {task_id} not found.")

if __name__ == "__main__":
    cli()