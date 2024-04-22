import time
import signal
import logging
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to handle keyboard interrupt
def signal_handler(sig, frame):
    logging.info("Monitoring stopped.")
    exit(0)

# Function to monitor log file
def monitor_log(log_file):
    try:
        logging.info("Monitoring log file: {}".format(log_file))
        word_counter = Counter()

        with open(log_file, 'r') as file:
            while True:
                where = file.tell()
                line = file.readline()
                if not line:
                    time.sleep(1)
                    file.seek(where)
                else:
                    logging.info(line.strip())
                    # Basic log analysis - counting occurrences of words
                    words = line.strip().split()
                    word_counter.update(words)

    except FileNotFoundError:
        logging.error("Log file '{}' not found.".format(log_file))
        exit(1)
    except Exception as e:
        logging.error("An error occurred: {}".format(str(e)))
        exit(1)

# Main function
def main():
    signal.signal(signal.SIGINT, signal_handler)  # Register signal handler for Ctrl+C
    log_file = "sample.log"  # Change this to the path of your log file
    monitor_log(log_file)

if __name__ == "__main__":
    main()
