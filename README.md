# Python Job Scraper

This Python Job Scraper is a mini project that scrapes Python-related job listings from the TimesJobs website, filtering them based on recent postings. The results are saved to a text file for easy reference.

## Features

- **Scrapes job listings** for Python developer roles from TimesJobs.
- **Filters job listings** to show only jobs posted today or one day ago.
- **Extracts key details** like company name, required skills, and job posting date.
- **Writes job details to a file** in a neatly formatted text document.

## Project Structure

- **`main.py`**: Main script to run the job scraping process.
- **`get_html.py`**: Fetches HTML content from the TimesJobs website and extracts job listings.
- **`list_jobs.py`**: Processes the job listings to extract relevant details.
- **`write_to_file.py`**: Writes the extracted job details into a text file, organized by date.

## Prerequisites

- Python 3.x installed on your system.
- Required packages:
  - `beautifulsoup4`
  
  Install using:
  ```bash
  pip install beautifulsoup4

## Contributing
Feel free to fork this repository, make enhancements, and submit pull requests. All contributions are welcome!

## Contact
For any inquiries or issues, please open an issue in this repository or contact me directly.