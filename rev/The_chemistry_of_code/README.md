This challenge just required basic programming knowledge, we don't actually know how to program in rust to solve this actually. \

We can actually solve this challenge by just doing some simple _static analysis_ on **main.rs** which located in the _src/_ directory. \
Step: \
1. Make _chemistryofcode_ executable (this binary is located at __target/debug/__)
2. Read _main.rs_ source code, from there we can see a string like _**AdminFeroxide**_ which is the value of the variable _const FERROUS_OXIDE_USERNAME: &str_
3. Under the _**AdminFeroxide**_ we can see there's a base64 string in which when we decode it to ASCII, it'll give us a hex string which we will also convert that hex to ASCII back and the value is something like _**d3ru571fy1n6**_
4. Now just run the binary and input those 2 strings that we've obtained above

FLAG = ACECTF{4ppr3n71c3_w4l73r_wh1t3}
