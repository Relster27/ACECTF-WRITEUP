# Webrypto CTF Challenge Writeup

## Challenge Description

The challenge presents us with a nostalgic reference to the classic cartoon Tom & Jerry, questioning whether their famous chases were genuine or if they were secretly friends all along. To settle this debate, the creator developed a web application containing the hidden truth.

Our task is to uncover this secret by exploiting vulnerabilities in the web application's parameter validation system. After examining the application, we discover it's built with PHP and implements specific validation checks on two URL parameters: 'tom' and 'jerry'.

The underlying PHP code reveals two critical conditions we need to satisfy simultaneously:
```php
if ($_GET['tom'] != $_GET['jerry']) {
    // First condition: tom and jerry must be different
    if (md5('ACECTF' . $_GET['tom']) == md5('ACECTF' . $_GET['jerry'])) {
        // Second condition: their MD5 hashes when concatenated with 'ACECTF' must be equal
        echo $FLAG;
    }
}
```

This presents an interesting paradox: we need to provide two parameters that are different, yet produce identical MD5 hashes when prefixed with 'ACECTF'. This is where our exploitation journey begins.

## Solution Process

### Step 1: Analyzing the Code Structure

The PHP code implements two nested conditions:
```php
if ($_GET['tom'] != $_GET['jerry']) {
    // First condition met
    if (md5('ACECTF' . $_GET['tom']) == md5('ACECTF' . $_GET['jerry'])) {
        // Second condition met
        echo $FLAG;
    }
}
```

Let's break down what these conditions require:
1. The GET parameters 'tom' and 'jerry' must be different values
2. When each parameter is prefixed with 'ACECTF' and hashed with MD5, the resulting hashes must be identical

This creates a seeming contradiction - how can two different values hash to the same result? At first glance, we might consider finding an MD5 collision, but that would be extremely difficult and likely not the intended solution for a CTF challenge.

### Step 2: Identifying PHP Type Juggling Vulnerabilities

A critical detail in the code is the use of the loose comparison operator (`==`) rather than the strict comparison operator (`===`). This distinction is significant in PHP as it involves type juggling, where PHP will attempt to convert compared values to a common type before comparison.

Additionally, we need to understand how PHP handles different data types in string operations and in the MD5 function. This leads us to a potential vulnerability:

When PHP functions like MD5 receive unexpected data types (like arrays), they behave in specific ways:
1. PHP will issue a warning (which doesn't stop execution)
2. It will attempt to convert arrays to strings, typically resulting in the string "Array"
3. Or in some cases, PHP might treat the array as NULL

### Step 3: Devising an Exploitation Strategy

Based on this understanding, we can exploit PHP's type handling behavior with the following approach:

1. Pass arrays as both 'tom' and 'jerry' parameters
2. The arrays will be different objects in memory, satisfying `$_GET['tom'] != $_GET['jerry']`
3. When PHP concatenates 'ACECTF' with each array parameter, it will convert both arrays to the same string representation
4. The MD5 hash of identical strings will be identical, satisfying the second condition

Let's craft a URL with array parameters:
```
https://chal.acectf.tech/Webrypto/?tom[]=1&jerry[]=2
```

This makes:
- `$_GET['tom']` an array containing `[1]`
- `$_GET['jerry']` an array containing `[2]`

### Step 4: Executing the Exploit and Understanding the Process

When we send this request to the server, here's what happens behind the scenes:

1. The server processes our request with the array parameters
2. For the first condition: `$_GET['tom'] != $_GET['jerry']`
   - PHP compares two different array objects
   - Since they are different arrays (one containing `1`, the other containing `2`), the comparison returns `true`
   - The first condition is satisfied

3. For the second condition: `md5('ACECTF' . $_GET['tom']) == md5('ACECTF' . $_GET['jerry'])`
   - PHP attempts to concatenate the string 'ACECTF' with the array `$_GET['tom']`
   - Unable to directly concatenate a string with an array, PHP converts the array to the string "Array"
   - This results in `md5('ACECTFArray')`
   - The same process happens with `$_GET['jerry']`, also resulting in `md5('ACECTFArray')`
   - Since the inputs to MD5 are identical, the hashes are identical
   - The second condition is satisfied

4. With both conditions satisfied, the server reveals the flag

When we submit our crafted URL:
```
https://chal.acectf.tech/Webrypto/?tom[]=1&jerry[]=2
```

The application returns:
```
Parameter 1 Met!ACECTF{70m_4nd_j3rry_4r3_4ll135}
```

We successfully retrieve the flag: `ACECTF{70m_4nd_j3rry_4r3_4ll135}`
