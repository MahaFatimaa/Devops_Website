from db import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(256), nullable=False)
    job_URL = db.Column(db.String(512), nullable=False)
    company_URL = db.Column(db.String(512), nullable=False)
    post_date = db.Column(db.String(64), nullable=False)

    def __init__(self, job_title, job_URL, company_URL, post_date):
        self.job_title = job_title
        self.job_URL = job_URL
        self.company_URL = company_URL
        self.post_date = post_date
