"""
Module to manage HTML report files.

This module provides functions to manage HTML report files generated from XML data.
It includes functions to retrieve, delete, and regenerate HTML reports.

Functions:
- get_report_files(): Retrieves a list of HTML report filenames present in the configured reports directory.
- delete_report_files(): Deletes all HTML report files (excluding those in the 'assets' subdirectory) from the configured reports directory.
- generate_report_files(): Deletes existing HTML report files and generates new reports using XML data.

Usage Example:
    from report_management import get_report_files, delete_report_files, generate_report_files
"""

import os
from .XML_to_HTML import run_xml_to_html
from .configuration import reports_dir

def get_report_file_names():
    """
    Retrieves a list of HTML report filenames present in the configured reports directory.

    Returns:
        list: A list of strings representing HTML report filenames.
    """
    report_files = []
    for filename in os.listdir(reports_dir):
        if filename.endswith(".html"):
            report_files.append(filename)
    return report_files

def delete_report_files():
    """
    Deletes all HTML report files (excluding those in the 'assets' subdirectory)
    from the configured reports directory.
    """
    if not os.path.exists(reports_dir) or not os.path.isdir(reports_dir):
        return
    for filename in os.listdir(reports_dir):
        file_path = os.path.join(reports_dir, filename)
        if filename.endswith(".html") and os.path.isfile(file_path) and not filename.startswith("assets"):
            os.unlink(file_path)

def generate_report_files():
    """
    Deletes existing HTML report files and generates new reports using XML data.
    """
    delete_report_files()
    run_xml_to_html()