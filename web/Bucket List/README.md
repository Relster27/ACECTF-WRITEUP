# Bucket List - CTF Challenge Writeup

![image](https://github.com/user-attachments/assets/571f865d-861c-4273-a275-a567e6957022)

## Challenge Description
The challenge presents us with the following text:

> You know what's a bucketlist? In simple terms, it's just a list of wishes people want to achieve before the leavee this world. I found it to be very limiting & ironic because how can you know when you'll leave the world behind? It's better to enjoy every moment and take on every opportunity you can. One of my whishes though is to pet a cat, do you mind checking this one out. So cute.

The title "Bucket List" is a clever play on words - referring both to the common concept of a list of wishes to fulfill before one dies and hinting at the AWS S3 bucket that needs to be explored. The description provides some misdirection about a cat picture, which serves as the initial entry point to the challenge.

## Solution Process

### Step 1: Examining the Initial Link
We are given an initial link to what appears to be a JPEG image:
```
https://opening-account-acectf.s3.ap-south-1.amazonaws.com/fun/can_we_get_some_dogs/026.jpeg
```

This URL reveals several important pieces of information:
- We're dealing with an Amazon S3 bucket (indicated by the s3.ap-south-1.amazonaws.com domain)
- The bucket name is "opening-account-acectf"
- The image is stored in a path "/fun/can_we_get_some_dogs/"

### Step 2: Exploring the Bucket Root
The next logical step is to try accessing the root of the S3 bucket to see if directory listing is enabled:
```
https://opening-account-acectf.s3.ap-south-1.amazonaws.com/
```

In properly secured S3 buckets, this kind of access would be forbidden. However, if the bucket is misconfigured (as suggested by the challenge title), we might be able to list its contents.

### Step 3: Discovering Hidden Content
Upon accessing the bucket root, we need to examine the page for any clues. The page should display an XML listing of the bucket contents if directory listing is enabled.

When examining the contents of the bucket listing (you can use View Source or Ctrl+U in most browsers), we discover an interesting file entry:

```xml
<Contents>
<Key>cry-for-me/acectf/secret.txt</Key>
<LastModified>2025-02-21T16:03:50.000Z</LastModified>
<ETag>"f5c541d9b2015848ce307d8e1191de89"</ETag>
<ChecksumAlgorithm>CRC64NVME</ChecksumAlgorithm>
<ChecksumType>FULL_OBJECT</ChecksumType>
<Size>44</Size>
</Contents>
```

This XML snippet reveals a text file named "secret.txt" located in the "cry-for-me/acectf/" directory within the bucket, with a size of 44 bytes.

### Step 4: Accessing the Secret File
Now that we've discovered this hidden file, we can construct a URL to access it directly

```
https://opening-account-acectf.s3.ap-south-1.amazonaws.com/cry-for-me/acectf/secret.txt
```

Navigating to this URL gives us access to the content of the secret.txt file.

### Step 5: Decoding the Flag

![image](https://github.com/user-attachments/assets/cb459b39-43aa-4f3d-9926-4d45ae5215ab)

Accessing the secret.txt file reveals a Base64 encoded string:
```
QUNFQ1RGezdoM180dzVfMTVfbTE1YzBuZjE2dXIzZH0=
```

To decode this Base64 string, we can use various online tools or command-line utilities such as:
```bash
echo "QUNFQ1RGezdoM180dzVfMTVfbTE1YzBuZjE2dXIzZH0=" | base64 -d
```

After decoding, we get the flag:
```
ACECTF{7h3_4w5_15_m15c0nf16ur3d}
```
