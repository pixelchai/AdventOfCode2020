from utils import *

with open("input.txt", "r") as f:
    raw = f.read()

def get_bin(x, n=0):
    # https://stackoverflow.com/a/21732313/5013267
    return format(x, 'b').zfill(n)

def eval_floating(s):
    ret = ""
    if "X" not in s:
        yield s
        return
    for i, c in enumerate(s):
        if c != "X":
            ret += c
        else:
            eee = s[i+1:]
            if len(eee) > 0:
                for ending in eval_floating(eee):
                    yield ret + "0" + ending
                    yield ret + "1" + ending
            else:
                yield ret + "0"
                yield ret + "1"
            break

def apply_mask(val_str, mask_str):
    ret = ""
    for i, c in enumerate(val_str):
        if mask_str[i] == "0":
            ret += c
        elif mask_str[i] == "1":
            ret += "1"
        elif mask_str[i] == "X":
            ret += "X"
    yield from eval_floating(ret)

mask = ""
mem = defaultdict(int)
for line in raw.splitlines():
    if line.startswith("mask"):
        mask, = re.match("mask = (.+)", line).groups()
        mask = mask.strip()
    else:
        adr, raw_val = re.match(r"mem\[(\d+)\]\s*=\s*(\d+)", line).groups()
        adr_bin = get_bin(int(adr), len(mask))

        for new_adr_bin in apply_mask(adr_bin, mask):
            aa = int(new_adr_bin, 2)
            print(aa>2**36)
            mem[aa] = int(raw_val)

print(sum(mem.values()))

# for lol in eval_floating("0X1101X"):
#     print(lol)