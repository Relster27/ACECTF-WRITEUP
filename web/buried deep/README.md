# CTF Writeup: Buried Deep

![image](https://github.com/user-attachments/assets/23857c7b-ca94-4544-915a-db850ecb8a24)

## Challenge Description
The challenge presents itself with a cryptic message:

> "I'm not a hacker. I'm just someone who wants to make the world a little better. But the world isn't going to change itself."

Players are instructed to submit their answer in the format ACECTF{3x4mpl3_fl4g}, with the content using lowercase letters only. The challenge is hosted at http://34.131.133.224:9998/.

Upon initial access, we're greeted with a webpage that uses metaphors about digging deep, uncovering layers, and finding what's hidden beneath the surface – all hinting at the exploration-based nature of this challenge.

## Solution Process

![image](https://github.com/user-attachments/assets/67bb5d2a-5247-4bb6-803b-46ffd3c85039)

### Step 1: Initial Reconnaissance
When first accessing the website, we're presented with a page containing philosophical text about seeking truth and finding things that are "buried deep." This immediately suggests we need to look beyond what's immediately visible.

A standard first step in web application testing is to check for the presence of a robots.txt file:

![image](https://github.com/user-attachments/assets/38cd25b0-f917-44f2-bbe2-a4d15e479edd)

```
http://34.131.133.224:9998/robots.txt
```

This reveals multiple disallowed directories:

```
Disallow: /secret/
Disallow: /hidden/
Disallow: /cryptic/
Disallow: /forbidden/
Disallow: /stealth/
Disallow: /buried/
Disallow: /underground/
Disallow: /secret_path/
Disallow: /hidden_flag/
Disallow: /deep_web/
Disallow: /encrypted/
```

This is a goldmine of information – robots.txt is designed to tell search engines which parts of a site not to index, but it's often used in CTF challenges to tell players exactly where to look!

### Step 2: Directory Exploration

![image](https://github.com/user-attachments/assets/1154fe90-ab62-463e-9a45-a68eb234b5a4)

After discovering these directories, we need to systematically explore each one. Let's start with `/buried`:

```
http://34.131.133.224:9998/buried
```

This page contains what appears to be encoded text:
```
49 115 116 32 80 97 114 116 32 111 102 32 116 104 101 32 70 108 97 103 32 105 115 32 58 32 65 67 69 67 84 70 123 49 110 102 49 108 55 114 52 55 49 110 103 95 55 104 51 95 53 121 53 55 51 109 95
```

### Step 3: Decoding the First Fragment
These numbers represent ASCII values. When converted from decimal to ASCII, we get:

![image](https://github.com/user-attachments/assets/d32ffcce-c4d0-4571-be74-70632e3b8a07)


```
1st Part of the Flag is : ACECTF{1nf1l7r471ng_7h3_5y573m_
```

Great! We have the beginning of our flag. Let's continue exploring the directories.

### Step 4: Finding the Second Fragment

![image](https://github.com/user-attachments/assets/16ebc0b6-ef99-44d4-b728-cad278e3626c)

Moving on to `/secret_path`:

```
http://34.131.133.224:9998/secret_path
```

Here we find morse code:
```
..--- -. -..
.--. .- .-. -
--- ..-.
- .... .
..-. .-.. .- --.
.. ...
---...
.---- ..... ..--.- ...-- ....- ..... -.-- ..--.- .-- .... ...-- -. ..--.- -.-- ----- ..- ..--.- -.- -. ----- .-- ..--.- .-- .... ...-- .-. ...-- ..--.-
```

### Step 5: Decoding the Morse Code
When decoded, the morse code translates to:

![image](https://github.com/user-attachments/assets/7bc31653-bb11-42e8-baaa-52ff7d8e1149)

```
2ND PART OF THE FLAG IS : 15_345Y_WH3N_Y0U_KN0W_WH3R3_
```

This gives us the middle section of our flag. Now we need the final part.

### Step 6: Finding the Last Fragment
The solution mentions that the final part of the flag is in the CSS. Let's examine the `/encrypted/` directory first, as it might provide a hint:

![image](https://github.com/user-attachments/assets/52148c44-d563-4ffd-bd1d-aea45a0c025d)

```
http://34.131.133.224:9998/encrypted/
```

This page contains a hint that the last part of the flag is in the CSS. Checking the page source or directly accessing:

```
http://34.131.133.224:9998/static/css/style.css
```

We find this unusual CSS rule:

![image](https://github.com/user-attachments/assets/6151ef25-0e63-4e57-9487-ab3ffbf3cfdd)

```css
#flag {
    display: none;
    content: "bC5 !2CE @7 E96 u=28 :D i f9b0db4CbEd0cCb03FC`b5N"; 
}
```

### Step 7: Decoding the CSS Content
This text appears to be encoded with some form of cipher. When properly decoded, it reveals:

![image](https://github.com/user-attachments/assets/5d54fdbd-4a32-430f-bd45-ba8adbce0392)

```
LAST PART 7h3_53cr3t5_4r3_bur13d}
```

### Step 8: Assembling the Complete Flag
Now we can combine all three parts:

1. First part: `ACECTF{1nf1l7r471ng_7h3_5y573m_`
2. Middle part: `15_345Y_WH3N_Y0U_KN0W_WH3R3_`
3. Last part: `7h3_53cr3t5_4r3_bur13d}`

This gives us the complete flag:
```
ACECTF{1nf1l7r471ng_7h3_5y573m_15_345y_wh3n_y0u_kn0w_wh3r3_7h3_53cr3t5_4r3_bur13d}
```
