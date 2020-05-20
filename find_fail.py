import subprocess
import sys

object_dir = sys.argv[1]

out_bytes = subprocess.check_output(['find', object_dir, '-type', 'f', '-size', '-1k'])

# out_text = out_bytes.decode('utf-8')

out_lines = out_bytes.splitlines()

items = [int(p.split(str.encode('/'))[-1].split(str.encode('-'))[1]) for p in out_lines]

final = []
for i in items:
    final.append(i - 1)
    final.append(i)

final = sorted(set(final))
# print(type(out_lines))
# print(out_lines)

print(type(final))
print(final)