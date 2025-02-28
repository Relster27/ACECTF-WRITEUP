# For The Fans - CTF Challenge Writeup

## Challenge Description
>Yo, I’ve lowkey always been a Drake fan, that’s why my username’s "DrakeSaltyOVO". It was literally everywhere on my dashboard until I had to take it down 'cause people just kept hating. But, like, that’s one thing I’ve always related to with my guy Drake, and honestly, I’ve been an even bigger fan ever since. 😂 Ya, laugh all you want, but I’m literally the only one with the flag fr, rofl!

In this challenge, we're given information about a user with the handle "DrakeSaltyOVO" who claims to be a Drake fan. The description suggests this username was previously visible on some kind of dashboard until the user had to remove it due to negative reactions. The user hints that they alone possess the flag, inviting us to track them down across the internet.

The challenge tests our ability to use Open Source Intelligence (OSINT) techniques to follow digital breadcrumbs across different social media platforms and decode hidden information.

## Solution Process

### Step 1: Username Reconnaissance
First, we need to locate where this username exists online. Since we have a specific username "DrakeSaltyOVO", we can use OSINT tools to find accounts across multiple platforms.

```
Tool used: https://whatsmyname.app/
Search term: DrakeSaltyOVO
```

This search reveals a Twitter (now X) account. Let's navigate to it:

```
https://x.com/DrakeSaltyOVO
```

### Step 2: Analyzing Twitter Content
On examining the Twitter profile, we find a critical tweet where the user mentions creating a blog:

> I really wanna put in a post about drake ngl, but this platform ain't cool yk, "so Imma blog somewhere, also twitter has a limit of 15 chars for username, who even does that. I don't like my username, finda new one ig. See ya at my "blog" babe, hope you drop in a note there!!! OVO"

This tweet contains several important clues:
1. The user plans to create a blog on another platform
2. They're unhappy with Twitter's username character limit
3. They'll be using a different username for their blog

### Step 3: Finding the Blog
Based on the tweet, we need to search for an alternative username on blogging platforms. Let's Google for related usernames:

```
Google search query: DrakeSaltyOVO blog alternative username
```

This search leads us to a Tumbig blog by a user named "salty-senpai-drake1":

```
https://www.tumbig.com/blog/salty-senpai-drake1
```

### Step 4: Examining Blog Content
The blog contains a post titled "Drake GOAT" with several paragraphs praising Drake. At the end of the post, we find:

1. A suspicious line: "I hope you ain't one of his haters though, only his fans 'were' allowed to read this!!!"
2. A long Base64-encoded string:

```
N3q8ryccAAQrDS+tIAAAAAAAAABqAAAAAAAAANGqpB7VL3HfX5dq2a0oNrtZRM2Hum9ExZnUSpeMMG2rzSg6lQEEBgABCSAABwsBAAIkBvEHARJTD3GIJuGJqEfIwbSE/71QeN8hIQEAAQAMIBwACAoBra6o3QAABQEZAQAREwBmAGwAYQBnAC4AdAB4AHQAAAAZABQKAQCfS+NlYELbARUGAQAgAAAAAAA=
```

### Step 5: Decoding the Base64 String
The long string appears to be Base64-encoded data. Let's decode it using Python:

```python
import base64

# The Base64 string found on the blog
data = "N3q8ryccAAQrDS+tIAAAAAAAAABqAAAAAAAAANGqpB7VL3HfX5dq2a0oNrtZRM2Hum9ExZnUSpeMMG2rzSg6lQEEBgABCSAABwsBAAIkBvEHARJTD3GIJuGJqEfIwbSE/71QeN8hIQEAAQAMIBwACAoBra6o3QAABQEZAQAREwBmAGwAYQBnAC4AdAB4AHQAAAAZABQKAQCfS+NlYELbARUGAQAgAAAAAAA="

# Decode the Base64 string to binary data
binary_data = base64.b64decode(data)

# Write the binary data to a file
with open("output.7z", "wb") as f:
    f.write(binary_data)
```

Running this script converts the Base64 string to binary data and saves it as a file named `output.7z`. The file extension suggests this is a 7-Zip archive.

### Step 6: Finding the Archive Password
Now we have a 7z archive file, but it's password-protected. Looking back at the Twitter profile for potential password clues, we notice a number: 2000914. This could be the password for the archive.

### Step 7: Extracting the Archive
We can use 7-Zip or a similar archive utility to extract the contents using the discovered password:

```bash
7z x output.7z
# When prompted for password
# Enter: 2000914
```

After successful extraction, we find a `flag.txt` file containing the challenge flag.

### Flag
```
ACECTF{y0u_b3773r_41nt_h4t3}
```
