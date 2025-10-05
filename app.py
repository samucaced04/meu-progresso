from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Seus dados de exemplo - depois você altera!
    weekly_data = [
        {"week": 1, "problems_solved": 15},
        {"week": 2, "problems_solved": 22},
        {"week": 3, "problems_solved": 18},
        {"week": 4, "problems_solved": 25},
        {"week": 5, "problems_solved": 20},
        {"week": 6, "problems_solved": 28}
    ]
    
    stats = {
        "total": sum(item["problems_solved"] for item in weekly_data),
        "average": sum(item["problems_solved"] for item in weekly_data) / len(weekly_data),
        "best_week": max(item["problems_solved"] for item in weekly_data)
    }
    
    return render_template('index.html', 
                         weekly_data=weekly_data,
                         current_week=6,
                         stats=stats)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
