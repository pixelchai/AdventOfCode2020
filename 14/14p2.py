from utils import *

with open("input.txt", "r") as f:
    raw = f.read()

def get_bin(x, n=0):
    # https://stackoverflow.com/a/21732313/5013267
    return format(x, 'b').zfill(n)

def eval_floating(s):
    if "X" not in s:
        yield s
    else:
        i = s.index("X")
        for ending in eval_floating(s[i+1:]):
            yield s[:i] + "0" + ending
            yield s[:i] + "1" + ending

def apply_mask(val_str, mask_str):
    ret = "".join(("1" if mask_str[i] == "1" else
                   ("X" if mask_str[i] == "X" else c)
                    for i, c in enumerate(val_str)))
    yield from eval_floating(ret)

mask = ""
mem = defaultdict(int)
for line in raw.splitlines():
    if line.startswith("mask"):
        mask = line[len('mask = '):]
    else:
        adr, raw_val = re.match(r"mem\[(\d+)\]\s*=\s*(\d+)", line).groups()
        raw_val = int(raw_val)
        adr_bin = get_bin(int(adr), len(mask))

        for new_adr_bin in apply_mask(adr_bin, mask):
            mem[int(new_adr_bin, 2)] = raw_val

print(sum(mem.values()))
