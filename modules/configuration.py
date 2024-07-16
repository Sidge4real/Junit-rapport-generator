"""
Module configuration.py

This module handles the configuration settings for the FastAPI application.

It reads configuration values from the 'settings.cfg' file using configparser and initializes
variables for port, host, reports directory, and logs directory based on the configuration.

Attributes:
    port (int): The port number on which the FastAPI server will run.
    host (str): The host address (IP or domain) on which the FastAPI server will bind.
    reports_dir (str): The directory path where HTML report files are stored.
    logs_dir (str): The directory path where log files are stored.
"""

import configparser

# Read configuration from settings.cfg file
config = configparser.ConfigParser()
config.read('settings.cfg')

# Initialize configuration variables
port = int(config['server']['port'])
host = config['server']['host']
reports_dir = config['directories']['reports_dir']
logs_dir = config['directories']['logs_dir']