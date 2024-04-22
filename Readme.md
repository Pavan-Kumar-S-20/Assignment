To fulfill the requirements outlined in the assessment, I'll create a Python script named log-monitor.py 
that will continuously monitor a specified log file for new entries and perform basic log analysis.
 

This script continuously monitors the specified log file (sample.log by default) for new entries, displaying them in real-time.
 It also performs basic log analysis by counting occurrences of words in each log entry. 
Error handling is implemented to catch file not found errors or any other unexpected exceptions. 
Additionally, a signal handler is registered to gracefully handle a keyboard interrupt (Ctrl+C) to stop the monitoring loop.

