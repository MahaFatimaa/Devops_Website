import json
from models import Job
from db import db

def load_data(app):
    with app.app_context():
        # Check if the jobs table is empty
        if Job.query.first() is None:
            with open('jobs.json') as f:
                jobs = json.load(f)
                for job in jobs:
                    new_job = Job(
                        job_title=job['job_title'],
                        job_URL=job['job_URL'],
                        company_URL=job['company_URL'],
                        post_date=job['post_date']
                    )
                    db.session.add(new_job)
                db.session.commit()
            print("Data loaded successfully.")
        else:
            print("Data already exists in the database. Skipping loading.")
