# Fall of 2022 - CTF Challenge Writeup

## Challenge Description
```
It was a peaceful time — schools were over, college admissions were delayed, and COVID was slowly on the decline. It seemed like the perfect time to relax and check my phone for her txts.
The funny thing is, I never got any. So I considered it just another gloomy year.
Anyways, here's the domain for this CTF: acectf.tech
What? You already knew this domain? Oh, I guess you'll have no trouble finding the flag then.
Good Luck!
```

The challenge presents a scenario referencing the Fall of 2022 as a time period of interest, with subtle wordplay around "txts" (text messages). Participants are given the domain `acectf.tech` and are told that if they already know the domain, they should have no trouble finding the flag.

This challenge tests participants' knowledge of DNS records, particularly TXT records, and their ability to access historical DNS data from a specific time period (Fall 2022). The hint about "checking my phone for her txts" is deliberately playful misdirection that actually points to DNS TXT records rather than SMS messages.

## Solution Process

### 1. Analyzing the Challenge Clues

The first step is to carefully analyze the challenge description for key clues:
- "Fall of 2022" suggests we need to look at historical data
- The reference to "txts" is a hint about TXT DNS records
- We're explicitly given the domain `acectf.tech`

### 2. Understanding DNS Records

DNS (Domain Name System) records contain various information about domains. Among these, TXT records are particularly useful for CTF challenges as they can contain arbitrary text data. They're commonly used for:
- Domain verification
- SPF (Sender Policy Framework) records for email
- DKIM (DomainKeys Identified Mail) information
- And sometimes, CTF flags!

### 3. DNS Lookup Tools

To solve this challenge, we need to look up the DNS records for `acectf.tech`. We can use various online DNS lookup tools such as:
- dnschecker.org
- mxtoolbox.com
- google's dig tool

For this challenge, I'll use dnschecker.org's comprehensive DNS lookup tool.

### 4. Retrieving Current DNS Records

First, I'll navigate to dnschecker.org/all-dns-records-of-domain.php and enter:
```
query=acectf.tech&type=TXT&dns=google
```

This gives us the current TXT records for the domain, but we need to specifically look at records from Fall 2022.

### 5. Finding Historical DNS Records

Looking at the current TXT records for `acectf.tech`, we see two entries:

1. `ACECTF{y0u_g07_7h3_73x7}`
2. `v=spf1 include:_spf.mx.cloudflare.net ~all`

### Flag
```
ACECTF{y0u_g07_7h3_73x7}
```


![image](https://github.com/user-attachments/assets/638caad8-c049-4af5-b241-b1147cf36ff2)




