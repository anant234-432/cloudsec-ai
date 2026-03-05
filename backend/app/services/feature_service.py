import re
import numpy as np

SQL_KEYWORDS = [
    "select", "insert", "update", "delete", "drop", "union",
    "or 1=1", "xp_cmdshell", "exec"
]

ERROR_KEYWORDS = [
    "error", "failed", "exception", "unauthorized", "denied"
]

def has_ip_address(message: str) -> int:
    pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    return 1 if re.search(pattern, message) else 0

def has_sql_keywords(message: str) -> int:
    msg=message.lower()
    return 1 if any(keyword in msg for keyword in SQL_KEYWORDS) else 0

def has_error_keywords(message: str) -> int:
    msg=message.lower()
    return 1 if any(keyword in msg for keyword in ERROR_KEYWORDS) else 0

def special_char_count(message: str) -> int:
    return len(re.findall(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", message))

def uppercase_ratio(message: str) -> float:
    if len(message) == 0:
        return 0.0
    upper = sum(1 for c in message if c.isupper())
    return upper / len(message)

def extract_log_features(message: str) -> np.ndarray:

    message_length = len(message)

    error_flag = has_error_keywords(message)

    sql_flag = has_sql_keywords(message)

    ip_flag = has_ip_address(message)

    special_chars = special_char_count(message)

    upper_ratio = uppercase_ratio(message)

    return np.array([
        message_length,
        error_flag,
        sql_flag,
        ip_flag,
        special_chars,
        upper_ratio
    ])

