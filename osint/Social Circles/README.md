# Social Circles

![image](https://github.com/user-attachments/assets/1fd75316-c190-4f46-84d1-3792c7a48280)

## Challenge Description

> Hey guys, my friend is starting a gaming channel—go sub to @AhjussiPlayz on Youtube!


## Solution Walkthrough

### Step 1: Initial YouTube Investigation

First, we need to visit the YouTube channel mentioned in the challenge description:

![image](https://github.com/user-attachments/assets/f892ac53-ce9b-493d-8950-38bcf92bbf19)


```
YouTube Channel: @AhjussiPlayz
```

This is our starting point, and we need to carefully examine the channel's content for any potential clues.

### Step 2: Investigating Video Subtitles/Captions

When watching videos on the channel, we should check for subtitles/closed captions. At approximately the 0:07 timestamp in a video, there's a subtitle option available.

When using English subtitles, we see:

![image](https://github.com/user-attachments/assets/7ad2e1ad-02af-4a6e-9de9-64346b5f106f)


```
"Nothing to see here >:D"
```

This suspicious message with a mischievous expression (>:D) suggests something is being hidden.

### Step 3: Changing Subtitle Language

An important detail to notice is that the YouTube channel name "AhjussiPlayz" contains the Korean term "Ahjussi" (아저씨), which means "middle-aged man" in Korean. This subtle hint suggests trying Korean subtitles.

When switching to Korean subtitles at the same timestamp, we discover:

![image](https://github.com/user-attachments/assets/9c472949-9c44-404e-9e94-d79fb56252c7)


```
"PS 인트로 제작에 도움을 준 나의 좋은 친구 "wimebix884" 에게 큰 감사를 드립니다. 떠오르는 신예 가수, 그의 신곡을 만나보세요!"
```

### Step 4: Translating the Korean Message

Using a translation service to convert the Korean text to English:

```
"PS A big thank you to my good friend "wimebix884" for helping me create the intro. Meet the rising new singer, his new song!"
```

This reveals crucial information:
1. A username: "wimebix884"
2. Context that this person is a "rising new singer"

### Step 5: Username Reconnaissance

With this new information, we need to track down the username "wimebix884" across various platforms. A specialized OSINT tool called "whatsmyname.app" (https://whatsmyname.app/#) is helpful for this task.

```
Search query: wimebix884
```

The tool searches numerous social platforms for accounts with this username.

### Step 6: Discovering the Smule Account

Among the results, we find an account on Smule, a social singing platform, which aligns with the clue that "wimebix884" is a singer:

![image](https://github.com/user-attachments/assets/c4064b0b-467d-40be-a72f-c1a600137c7b)


```
Smule profile: https://www.smule.com/wimebix884
```

### Step 7: Investigating the Smule Profile

Upon accessing the Smule profile, we discover a song titled "ACE" with a subtitle "Flag Debauchery" - the word "Flag" being a clear indicator that we're on the right track.

![image](https://github.com/user-attachments/assets/b0530f7c-f990-4ed2-8b18-b4c43c15a810)

The description of the song contains crucial information:

![image](https://github.com/user-attachments/assets/d8aac091-9906-4e6d-b708-f87608d03dbe)

```
In case you don't have the mobile app,
you can also listen to my song here:
https://drive.google.com/file/d/1093uvDYSVWke8ze2jdgJ1rVehz51Jx00
Contact omniRex on Discord in case you have a disability.
```

### Step 8: Accessing the Google Drive File

Following the provided Google Drive link:

```
https://drive.google.com/file/d/1093uvDYSVWke8ze2jdgJ1rVehz51Jx00
```

We find an audio file. The mention of contacting someone "in case you have a disability" is a hint that the flag is contained in audio format

![image](https://github.com/user-attachments/assets/53765c82-f739-42ad-b0c2-ef1fecbaa661)

## FLAG Retrieval

Upon listening to the audio file from Google Drive, we hear the flag being spelled out verbally:

```
ACECTF{mu171m3d14_f146}
```
