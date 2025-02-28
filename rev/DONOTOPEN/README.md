## POC
This challenge is about reverse engineering a self-extracting archive. The bash file uses a marker (`__ARCHIVE_BELOW__`) to indicate where the compressed Python script begins.
A single command employing `awk` and `tail` extracts the script, decompressing it via `gzip` into a file (extract.py).

After extraction, the bash script computes an MD5 checksum to verify the integrity of the embedded Python code before executing it. 
The Python script itself contains several flag variables and a PIN check that hashes the provided PIN to generate a final flag. 
The goal is to extract the Python script, analyze its logic, and figure out the correct PIN to unlock the final flag.


# NOTE
We don't have to patch the script, just straight up run this command below:
```bash
tail -n +$(awk '/^__ARCHIVE_BELOW__/ {print NR+1; exit}' script.sh) script.sh | gzip -d > extract.py
```
This will give us the extracted python script and output it into _**extract.py**_

From here, we can run _**extract.py**_ and input the code/pin that is available in the _**if**_ statement of _**extract.py**_
The flag format would be slightly different than the usual flag on the event.

FLAG = ACE{e2e3619b630b3be9de762910fd58dba7}
