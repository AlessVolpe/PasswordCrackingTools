# PasswordCrackingTools

A collection of script that I made while learning password cracking. Those tools are just for learning and used to complete an old university project of mine, don't use them for evil. All the tools require click, which can be installed with the following command:

```bash
pip install click
```

## Password Mask Analyzer

A simple tool to analize word list mask distribution.

### Password Mask Analyzer: usage

```bash
python Main.py --top=length_of_top_list wordlist_file
```

---

## Hash dumper

This tool takes raw password dumps and retrieves only the hashes for use in programs like hashcat, it works on the following type of line:

```shell
fanp:xOBJK020QFPMo:53201:532:Cpr E 532 Student:/home/issl/532/fanp:/bin/tcsh
```

### Hash dumper: usage

```bash
python Main.py --output=output_file dump_file
```
