![Screenshot 2025-03-01 104252](https://github.com/user-attachments/assets/c67bcaf5-8890-4a76-83ab-e358c20715cf)
![Screenshot 2025-03-01 104352](https://github.com/user-attachments/assets/5a71bd1f-8783-4a55-877b-b63718b7f394)
![Screenshot 2025-03-01 104422](https://github.com/user-attachments/assets/1cd3fa8d-0343-409e-9d7d-03a8756e6644)


# POC
This challenge needs a good intuition (well not really, hehe), i mean like the clues are scattered accross files and we were forced to be a detective and remember all small clues in order to solve this challenge.


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
A simple ROT-7 needed here to decode it's original value, below is the original content:\
```text
Congratulations you uncovered the text, now follow this link for your next step of the puzzle.
https://drive.google.com/file/d/1AFPHaJ0wZMZWYDkU-KxiWu9z5aTMs6EO/view?usp=sharing
```
>Note : That google drive link is actually not working now, but it gave us an image file named **_RickRoll.jpg_**












