from get_html import get_html
from list_jobs import list_jobs
from write_to_file import write_to_file

sequence_no = 1
pages_deep = 9


if __name__ == "__main__":
    # setting up my global variable to navigate pagination

    print('Please wait a second while I gather the results...')

    while sequence_no <= pages_deep:
        jobs = get_html(sequence_no = sequence_no)
        job_details = list_jobs(jobs)
        if job_details:
            write_to_file(job_details)
        sequence_no += 1
    print('-'*30)
    print('Done')