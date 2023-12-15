Run python .github/workflows/autoassign.py
Traceback (most recent call last):
  File "/home/runner/work/.github/.github/.github/workflows/autoassign.py", line 43, in <module>
    main()
  File "/home/runner/work/.github/.github/.github/workflows/autoassign.py", line 37, in main
    assignee = random.choice(members)
  File "/usr/lib/python3.10/random.py", line 378, in choice
    return seq[self._randbelow(len(seq))]
IndexError: list index out of range
