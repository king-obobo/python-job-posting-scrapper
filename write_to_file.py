from datetime import date
today = date.today()
file_name = today.strftime('%d-%m')

def write_to_file(jobs):
    with open(f'./jobs/{file_name}-jobs.txt', 'a') as f:
        for job in jobs:
            f.write(f"Company name: {job['company_name']} \n")
            f.write(f"Required Skills: {job['skillset']} \n")
            f.write(f"More Info: {job['more_info']} \n")
            f.write(f"When Posted: {job['when_posted']} \n")
            f.write('-'*30)
            f.write('\n')
    