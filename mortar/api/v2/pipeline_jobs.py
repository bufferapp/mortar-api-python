import time

def post_pipeline_job(api, project_name, luigiscript_name, git_ref='master', parameters=None):
    body = {'project_name': project_name,
            'luigiscript_name': luigiscript_name,
            'git_ref': git_ref,
            'parameters': parameters or {}
    }

    return api.post('pipeline_jobs', body)['pipeline_job_id']
