from flask import request, jsonify
from models import Job
from db import db

def get_jobs():
    keyword = request.args.get('keyword')
    posted_after = request.args.get('posted_after')

    query = Job.query

    if keyword:
        query = query.filter(Job.job_title.ilike(f'%{keyword}%'))

    if posted_after:
        query = query.filter(Job.post_date >= posted_after)

    jobs = query.all()  # Use the filtered query to get jobs
    return jsonify([{
        'id': job.id,  # Include job ID in the response
        'job_title': job.job_title,
        'job_URL': job.job_URL,
        'company_URL': job.company_URL,
        'post_date': job.post_date
    } for job in jobs])

def add_job():
    job_data = request.json  

    new_job = Job(
        job_title=job_data['job_title'],
        job_URL=job_data['job_URL'],
        company_URL=job_data['company_URL'],
        post_date=job_data['post_date']
    )
    db.session.add(new_job)
    db.session.commit()

    return jsonify({
        'id': new_job.id,  # Include the job ID assigned by the database
        'job_title': new_job.job_title,
        'job_URL': new_job.job_URL,
        'company_URL': new_job.company_URL,
        'post_date': new_job.post_date
    }), 201

def update_job(job_id):
    job = Job.query.get(job_id)
    
    if not job:
        return jsonify({'error': 'Job not found'}), 404
    
    job_data = request.json

    # Update the job details
    job.job_title = job_data.get('job_title', job.job_title)
    job.job_URL = job_data.get('job_URL', job.job_URL)
    job.company_URL = job_data.get('company_URL', job.company_URL)
    job.post_date = job_data.get('post_date', job.post_date)

    db.session.commit()

    return jsonify({
        'id': job.id,  # Include job ID in the response
        'job_title': job.job_title,
        'job_URL': job.job_URL,
        'company_URL': job.company_URL,
        'post_date': job.post_date
    }), 200

def delete_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    db.session.delete(job)
    db.session.commit()

    return jsonify({'message': f'Job {job_id} deleted successfully'}), 200