# The Symphony of Greatness - CTF Challenge Writeup


## Challenge Description
In this challenge, we are presented with a narrative from a user called "modernlouis" who describes their journey exploring music outside their native language. The description includes several clues about their musical preferences, including admiration for musicians with "raw vocal talent" who "blend different genres" and have a "signature sound that was instantly recognizable and highly danceable." 

The challenge task is to determine which band the user is referring to, with a hint indicated by "**Me...**" (suggesting a connection to the username itself). The flag format requires the band's name followed by their most streamed song, converted to leet speak (where letters are replaced with similar-looking numbers and symbols): ACECTF{band_name_song_name}

Original challenge:
```
Hey everyone, myself *modernlouis*. I remember starting to explore music outside of my native language years ago. Back then, I was just a kid, trying something completely new and unfamiliar. At first, I did it to feel included with others who were effortlessly singing along to the most popular songs of the time.
Over the years, I listened to a *lot of artists*, but for a long time, I couldn't settle on an all-time favorite. That changed during the recent pandemic. With all the extra time on my hands, I dove deeper into my love for music. Slowly and without even realizing it, I found myself drawn to a specific kind of sound.
What kind of music, you ask? Well, not the ones filled with meaningless words just to make rhymes. Not the albums entirely focused on heartbreak stories. And definitely not the tracks made just to curse or diss someone—come on, let's move past that.
*I admire musicians who showcase raw vocal talent, seamlessly blend different genres, and have a a signature sound that was instantly recognizable and highly danceable.*
Now, here's the challenge: Your task is to figure out which band I'm talking about. The biggest hint? **Me...**
```

## Solution Process

### 1. Initial Username Analysis

The first clue in the challenge is the username "modernlouis." This appears to be our starting point for investigation. The challenge description emphasizes this username by formatting it with asterisks as *modernlouis*, and the hint "**Me...**" suggests that the username itself is significant to solving the challenge.

### 2. Username Search Across Platforms

To find where this username exists online, we can use whatsmyname.app, which searches for usernames across multiple platforms:

```
https://whatsmyname.app/
```

Entering "modernlouis" into this tool reveals several accounts, including a YouTube account with the username @modernlouis.


### 3. YouTube Account Investigation

When accessing the YouTube account, we discover a link to another platform in the profile:

```
makromusic.com/u/modernlouis
```

This link points to a profile on a music platform called Ma Music, giving us another avenue to explore.

### 4. Ma Music Profile Analysis

Visiting the linked profile on makromusic.com reveals a crucial additional clue in the account description:

```
"Ok, I guess we're all 'Genius'. So if you haven't solved yet, here's the hint - 'Maybe they're technically not a band after all'."
```

This provides important context to help identify the musical act - suggesting that while they might be commonly referred to as a band, they might technically be a duo, trio, or some other configuration.

### 5. Making the Connection

At this point, we need to connect the dots between all our clues:
- Username: modernlouis
- Hint from the profile description: "not a band after all"
- Musical preferences: blend of genres, recognizable sound, danceable
- The emphasis on "**Me...**" pointing to the username itself

The key insight comes from analyzing the username: "modernlouis" bears a striking resemblance to "Modern Talking," a German duo from the 1980s known for their dance-pop sound that blended multiple genres. While technically a duo rather than a band (matching the hint "not a band after all"), they're often referred to as a band.

The connection between "modernlouis" and "Modern Talking" becomes even more apparent when we consider:
- "modern" is directly in the name
- "louis" could be a play on words related to "talking" (as in speaking/talking)

### 6. Verifying the Most Streamed Song

Once we've identified Modern Talking as the likely answer, we need to find their most streamed song on Spotify. A search reveals that "Cheri Cheri Lady" is their most popular track with the highest stream count.

### 7. Constructing the Flag

The final step is to format the flag according to the requirements: the band name followed by the song name, converted to leet speak (replacing letters with similar-looking numbers and symbols).

Band: Modern Talking → m0d3rn_74lk1n6
Song: Cheri Cheri Lady → ch3r1_ch3r1_l4dy

Putting it all together, we get:

```
ACECTF{m0d3rn_74lk1n6_ch3r1_ch3r1_l4dy}
```
