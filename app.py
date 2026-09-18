from flask import Flask, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Docker", "completed": False},
    {"id": 2, "title": "Create GitHub Actions workflow", "completed": False},
]


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Task Manager</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                margin: 0;
                padding: 40px;
            }

            .container {
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }

            h1 {
                text-align: center;
                color: #333;
            }

            form {
                display: flex;
                gap: 10px;
                margin-bottom: 25px;
            }

            input {
                flex: 1;
                padding: 12px;
                border: 1px solid #ccc;
                border-radius: 6px;
            }

            button {
                padding: 12px 20px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
            }

            ul {
                padding: 0;
                list-style: none;
            }

            li {
                background: #f1f3f5;
                padding: 12px;
                margin-bottom: 10px;
                border-radius: 6px;
            }

            .status {
                text-align: center;
                margin-top: 20px;
                color: green;
            }
        </style>
    </head>

    <body>
        <div class="container">

            <h1>📋 DevOps Task Manager</h1>

            <form method="POST" action="/add">
                <input
                    type="text"
                    name="title"
                    placeholder="Enter a new task"
                    required
                >
                <button type="submit">Add Task</button>
            </form>

            <ul>
                {%TASKS%}
            </ul>

            <div class="status">
                Application is running successfully 🚀
            </div>

        </div>
    </body>
    </html>
    """.replace(
        "{%TASKS%}",
        "".join(
            f"<li>{'✅' if task['completed'] else '⬜'} {task['title']}</li>"
            for task in tasks
        ),
    )


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")

    if title:
        tasks.append({
            "id": len(tasks) + 1,
            "title": title,
            "completed": False
        })

    return redirect(url_for("home"))


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)