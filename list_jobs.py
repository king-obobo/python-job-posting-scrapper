# A simple function to get my list of jobs


def list_jobs(jobs):

    job_details = []
    

    for job in jobs:
        when_posted = job.find('span', {'class': 'sim-posted'}).text.strip().lower()
        if when_posted == 'posted today'.lower() or when_posted == 'Posted 1 day ago'.lower():
            company_el = job.find('h3', {'class': 'joblist-comp-name'})
            company_name = company_el.text.replace(' ', '').strip() if company_el else 'N/A'
            skillset_el = job.find('span', {'class': 'srp-skills'})
            skillset = skillset_el.text.replace('\n', ' ').strip().replace(' ', ',') if skillset_el else 'N/A'
            more_info_el = job.h2.a['href']
            more_info = more_info_el if more_info_el else 'N/A'
            when_posted_el = job.find('span', {'class': 'sim-posted'})
            when_posted = when_posted_el.text.lower() if when_posted_el else 'N/A'

            job_details.append({
                'company_name': company_name,
                'skillset' : skillset,
                'more_info' : more_info,
                'when_posted': when_posted

            })
            
    return job_details
