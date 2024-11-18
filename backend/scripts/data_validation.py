import json
import hashlib
from datetime import datetime, timedelta

def validate_format(data, expected_format):
    try:
        if expected_format == 'json':
            json.loads(data)
            return True
        return False
    except json.JSONDecodeError:
        return False

def compute_checksum(data, algorithm='sha256'):
    hash_func = hashlib.sha256()
    hash_func.update(data.encode('utf-8'))
    return hash_func.hexdigest()

def validate_checksum(data, expected_checksum, algorithm='sha256'):
    computed_checksum = compute_checksum(data, algorithm)
    return computed_checksum == expected_checksum

def validate_recency(timestamp, threshold_days=30):
    dataset_date = datetime.strptime(timestamp, '%Y-%m-%d')
    current_date = datetime.now()
    return (current_date - dataset_date) <= timedelta(days=threshold_days)

def validate_dataset(data, expected_format, expected_checksum, timestamp, recency_threshold_days=30):
    return (
        validate_format(data, expected_format) and
        validate_checksum(data, expected_checksum) and
        validate_recency(timestamp, recency_threshold_days)
    )
