
import os
import sqlite3
import json
from datetime import datetime, timedelta

def get_edge_history():
    # Edge history database path
    edge_path = os.path.expandvars(r'%LOCALAPPDATA%\Microsoft\Edge\User Data\Profile 1\History')
    
    # Connect to the SQLite database
    conn = sqlite3.connect(edge_path)
    cursor = conn.cursor()
    
    # Query to fetch the browsing history
    query = """
    SELECT urls.url, urls.title, urls.visit_count, urls.last_visit_time
    FROM urls
    ORDER BY urls.last_visit_time DESC
    LIMIT 100
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Process and print the results
    for row in results:
        url, title, visit_count, last_visit_time = row
        # Convert the timestamp to a readable format
        last_visit_datetime = datetime(1601, 1, 1) + timedelta(microseconds=last_visit_time)
        
        print(f"URL: {url}")
        print(f"Title: {title}")
        print(f"Visit Count: {visit_count}")
        print(f"Last Visit: {last_visit_datetime}")
        print("-" * 50)
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    get_edge_history()
