![Screenshot 2025-03-01 104252](https://github.com/user-attachments/assets/c67bcaf5-8890-4a76-83ab-e358c20715cf)
![Screenshot 2025-03-01 104352](https://github.com/user-attachments/assets/5a71bd1f-8783-4a55-877b-b63718b7f394)
![Screenshot 2025-03-01 104422](https://github.com/user-attachments/assets/1cd3fa8d-0343-409e-9d7d-03a8756e6644)


# POC
This challenge needs a good intuition and some stego skills (well not really, hehe), i mean like the clues are scattered accross files and we were forced to be a detective and remember all small clues in order to solve this challenge.


Initially we're given with 2 files, they are _**Readme.txt**_ and _**Start.jpg**_.

_**Readme.txt**_:
```text
Refer to the image to start your challenge.
```

_**Start.jpg**_: \
![image](https://github.com/user-attachments/assets/c11470f9-bbf9-463c-8587-d3a61756d545) \
There's indeed a clue in the metadata.

_**Start.jpg**_'s metadata: \
(I used _**exiftool**_) \
![image](https://github.com/user-attachments/assets/02cb3f3b-2d35-4e7c-be23-bd1c882c7b19)
> Note:
> Two hints were released a couple hours before the event ended, and it does mentioned about the '**?**' sign. Which is used for the password later on.

But you might wonder what **password** has to do here? Well if we run [**_steghide_**](https://steghide.sourceforge.net/) with correct password on **_Start.jpg_** we'd get another file. More information below.

‎Looking at the hint we could assume that if we multiply the **height** and **width** of the image and then add with some value will give us the password of the image. Now what's the value of '?' ? It's actually the value **6467** which is on the challenge title itself or in the file _**Start.jpg**_. So now we got our final password which is 1587 * 1590 + 6467. \
Password for _**Start.jpg**_ = 2529797 \

Now let's run _**steghide**_ on it:
```bash
steghide extract -sf Start.jpg -p 2529797
```
Running this command will give us a file named _**message.txt**_, below is the content of it:
```text
Jvunyhabshapvuz fvb bujvclylk aol alea, uvd mvssvd aopz spur mvy fvby ulea zalw vm aol wbggsl.
oaawz://kypcl.nvvnsl.jvt/mpsl/k/1HMWOhQ0dGTGDFKrB-RepDb9g5hATz6LV/cpld?bzw=zohypun
```
A simple ROT-7 needed here to decode its original value, below is the original content:\
```text
Congratulations you uncovered the text, now follow this link for your next step of the puzzle.
https://drive.google.com/file/d/1AFPHaJ0wZMZWYDkU-KxiWu9z5aTMs6EO/view?usp=sharing
```
>Note : That google drive link is actually not working now, but it did gave us an image file named **_RickRoll.jpg_**

As ususal let's run _**exiftool**_ to check its metadata: \
![Screenshot 2025-03-01 111118](https://github.com/user-attachments/assets/2f55facb-ff73-400f-b8b4-e6e58c5f6b11)
Just a simple binary encoding which translates to:
```text
HahaKeepTrying
```

Same stuff as before we run _**steghide**_ to extract hidden file embedded within that _**image**_. And we got a file named _**password.txt**_. Here's the content of _**password.txt**_:
```text
Fob hkzi hntamfymusli yrrhmczrj ahps wiwhtxc. Kbtnrhtepeibfla, oaa im yyy xwbei buga whs dli tgu rprt fob mskli uv tmee drvnq. 
lxiij://eqgnbb.jow/srtlyfp/ouvk
```
>Note : We were pulling out our hair when looking for the password for this image since there is no clue for the password of this image.
> My friend was bruteforcing the password for this file for us. (Some manual bruteforce actually :v)

Turn out the password is not a number of some mathematical operation but it's literally just **259x194**.\
This is actually just the **width** and **height** value with 'x' sign added in the middle of it. (Who would've thought).


Now we got new file let's check its content:\
```text
Fob hkzi hntamfymusli yrrhmczrj ahps wiwhtxc. Kbtnrhtepeibfla, oaa im yyy xwbei buga whs dli tgu rprt fob mskli uv tmee drvnq. 
lxiij://eqgnbb.jow/srtlyfp/ouvk
```
(Gosh!! another encrypted file)\

But let's recall what information we've had previously. Yup, there's this string (**HahaKeepTrying**) that we haven't used. This file's content is actually encrypted by a **Vigenère Cipher** (was a blind guess from me). And yesss **Vigenère** was the cipher used to encode the content. Let's use **HahaKeepTrying** as the key. Here's the original content of **password.txt**:
```text
You have successfully uncovered this message. Congratulations, but if you think that was the end then you might be very wrong. 
https://github.com/oneshhh/book
```

[https://github.com/oneshhh/book](https://github.com/oneshhh/book) directed us to a github repo, there's a **.docx** file and if we download it, it gives us a book. Almost the whole content is not important, but if we do a search with **Ctrl+F** and search for the string **_ACECTF_**, we would get into the book part with that string, take a look at the image below:\
![Screenshot 2025-03-01 114219](https://github.com/user-attachments/assets/d9119f14-02fe-4f45-b408-bd667a7df7cd)


Yup that's it, that's the flag. Just need a little bit formatting and we end this suffering.
FLAG = ACECTF{}
