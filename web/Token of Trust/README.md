# Token of Trust - CTF Challenge Writeup

![image](https://github.com/user-attachments/assets/f065a44d-3248-4082-bbb4-9a7c4d063af4)


## Challenge Information
> Name: Token of Trust  
Description: At first, this web app seems straightforward, but there's something more lurking beneath the surface. It relies on a token for user authentication, but not everything is as secure as it seems. Look closely, and you might discover that the system's trust can be manipulated. The secret is hidden within the way this token is used. Can you find the key to unlock what's been concealed?  
Target: http://34.131.133.224:9999/

## Challenge Overview
This challenge presents a web application that uses token-based authentication for controlling access. At first glance, the application appears to be a standard login system, but there's a security flaw in how it handles and validates authentication tokens.

The challenge hints that the system's "trust can be manipulated," suggesting that the token validation mechanism is vulnerable. Our goal is to exploit this vulnerability to access protected resources and retrieve the hidden flag.

## Solution Walkthrough

### Step 1: Initial Reconnaissance
Upon visiting the main page at http://34.131.133.224:9999/, we see the following message:

![image](https://github.com/user-attachments/assets/cda6af83-25af-442f-82d4-cfdf382020b1)

```
Welcome to the main page!
To log in, visit /login. But remember, POST requests are my love language. ❤️
PS: Don't forget to set your headers for JSON, or I'll just ignore you. 😉
```

This gives us clear instructions:
- We need to visit the `/login` endpoint
- We should use POST requests
- We need to set appropriate JSON headers

### Step 2: Exploring the Login Endpoint
When accessing the `/login` endpoint, we receive the following response:

![image](https://github.com/user-attachments/assets/53cf55fd-49f4-408a-80d5-d0cc48055f7b)


```
Oops! Wrong approach.
You can't just walk in here without a proper POST request.
Try sending a JSON payload like this: {"user":"ace","pass":"ctf"}.
Hint: I only care about your request format, not your credentials. 😉
```

This confirms we need to send a POST request with a JSON payload, and interestingly, the hint suggests that the actual credentials don't matter - only the format.

### Step 3: Authentication and JWT Analysis
Next, we send a POST request to the `/login` endpoint with the suggested JSON payload:

![image](https://github.com/user-attachments/assets/ec0c243d-ce76-4452-9740-42a9e22cebc2)


The server responds with a JWT (JSON Web Token). To analyze this token, we use the JWT decoder at https://fusionauth.io/dev-tools/jwt-decoder.

![image](https://github.com/user-attachments/assets/53a055ac-35cf-4558-97f4-12ef9a1fb941)

When decoded, we can see the token consists of three parts:
1. **Header**: Contains the token type and signing algorithm (HS256)
   ```json
   {
     "alg": "HS256",
     "typ": "JWT"
   }
   ```
2. **Payload**: Contains the claims
   ```json
   {
     "user": "guest"
   }
   ```
3. **Signature**: Used to verify the token hasn't been tampered with

### Step 4: JWT Manipulation
The key vulnerability here is related to the JWT's algorithm. JWT supports multiple algorithms for signing, including an algorithm called "none" which effectively means "no signature verification."

In a secure implementation, the server should reject tokens with the "none" algorithm. However, many JWT libraries had vulnerabilities where they would accept "none" algorithm tokens, effectively bypassing signature verification.

We modify the JWT by changing the algorithm in the header from "HS256" to "none" and removing the signature part:

![image](https://github.com/user-attachments/assets/a64869e5-b921-432b-b369-aebf368adc24)

Original header:
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

Modified header:
```json
{
  "alg": "none",
  "typ": "JWT"
}
```

**Payload**: Contains the claims
   ```json
   {
     "user": "admin"
   }
   ```

### Step 5: Discovering Hidden Endpoints
Now we need to find where to use our manipulated token. A common technique in web application reconnaissance is checking the robots.txt file, which often contains information about restricted areas of a website.

![image](https://github.com/user-attachments/assets/7002fe6c-edec-4d13-b621-f2159e3ea843)

When checking `http://34.131.133.224:9999/robots.txt`, we discover a disallowed endpoint: `/flag`.

### Step 6: Accessing the Protected Resource
With our manipulated JWT and the knowledge of the `/flag` endpoint, we can now try to access this protected resource

### Step 7: Flag Retrieval
The server accepts our manipulated token with the "none" algorithm and processes our request as if we were authenticated with valid credentials. The server responds with the flag:

```
ACECTF{jwt_cr4ck3d_4dm1n_4cce55_0bt41n3d!}
```

## Flag
`ACECTF{jwt_cr4ck3d_4dm1n_4cce55_0bt41n3d!}`
