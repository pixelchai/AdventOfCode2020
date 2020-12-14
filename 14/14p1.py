from utils import *

with open("input.txt", "r") as f:
    raw = f.read()

def get_bin(x, n=0):
    # https://stackoverflow.com/a/21732313/5013267
    return format(x, 'b').zfill(n)

def apply_mask(val_str, mask_str):
    ret = ""
    for i, c in enumerate(val_str):
        ret += c if mask_str[i] == "X" else mask_str[i]
    return ret

mask = ""
mem = defaultdict(int)
for line in raw.splitlines():
    if line.startswith("mask"):
        mask, = re.match("mask = (.+)", line).groups()
    else:
        adr, raw_val = re.match(r"mem\[(\d+)\]\s*=\s*(\d+)", line).groups()
        val_bin = get_bin(int(raw_val), len(mask))

        new_val_bin = apply_mask(val_bin, mask)
        mem[int(adr)] = int(new_val_bin, 2)

print(sum(mem.values()))