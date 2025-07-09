# pygerm

a terminal-based germ sim that spreads, clones, and eventually infects the whole screen. just run it and watch the infection take over. nothing fancy — just pure terminal chaos.

---

## how it works

- starts with one germ in the middle
- moves randomly and leaves a trail behind
- if it touches a marked trail, it might spawn another germ
- each germ lives for 1 second, then dies and leaves an `X`
- dead cells can't be touched again
- when all germs are gone, it restarts
- when the whole terminal fills up, it ends.

---

## how to run it

```bash
python3 pygerm.py


```or make it executable:

chmod +x pygerm.py
./pygerm.py

