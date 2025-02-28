#!/usr/bin/env python

import socket
import time

HOST = "34.131.133.224"
PORT = 5000

def submit_guess(guess_hash):
    """
    Connects to the server, sends the guess_hash, and returns the feedback.
    The feedback should tell you how many characters (and positions) match.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.recv(4096)
        s.sendall((guess_hash + "\n").encode())
        response = s.recv(4096).decode()
        return response

def parse_feedback(response):
    """
    Parses the server's response to extract:
      - total number of characters in the target hash that appear in your guess, and
      - number of characters in the correct positions.
    For example, if the server returns "Characters matched: X/32" and "Characters in correct positions: Y/32",
    then return (X, Y) as integers.
    """
    lines = response.splitlines()
    matched = correct = 0
    for line in lines:
        if "Characters matched:" in line:
            matched = int(line.split(":")[1].strip().split("/")[0])
        if "Characters in correct positions:" in line:
            correct = int(line.split(":")[1].strip().split("/")[0])
    return matched, correct

def improve_hash(initial_guess):
    """
    Uses a simple greedy algorithm:
      For each position in the 32-character hash,
      try all 16 hex digits and keep the one that improves the number of correct positions.
      (You may also use the total matched count.)
    """
    current = list(initial_guess)
    best_score = 0
    # Get initial score
    response = submit_guess("".join(current))
    best_score = parse_feedback(response)[1]  # using correct positions count
    print(f"Starting guess {''.join(current)} with {best_score}/32 correct positions")
    
    hex_chars = "0123456789abcdef"
    changed = True
    while changed and best_score < 32:
        changed = False
        for i in range(32):
            original = current[i]
            for ch in hex_chars:
                if ch == original:
                    continue
                current[i] = ch
                candidate = "".join(current)
                response = submit_guess(candidate)
                _, score = parse_feedback(response)

                if score > best_score:
                    best_score = score
                    changed = True
                    print(f"Improved position {i} to '{ch}': {best_score}/32")
                    break
                else:
                    current[i] = original
                time.sleep(0.1)

    return "".join(current)

if __name__ == "__main__":
    
    # I've tried the bruteforce-way but it's taking so long so i cancelled it and take my current string's hash
    # and plug it down here
    initial_candidate = "8276ec2bcbe26768d5e69ac354780e5a"  # This matches 9/32 (if i recall correctly)
    final_hash = improve_hash(initial_candidate)
    print(f"Final hash: {final_hash}")

# NOTE:
# Instead of bruteforce every string in rockyou.txt, my idea here is to modify 1 hex at a time.

# This script might not run remotely because the server have been closed (i guess).
# But the idea remains the same.
