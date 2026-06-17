import re
import sys
from pathlib import Path


def split_blocks(full_text):
    return re.split(r"\n\s*\n", full_text.strip())


def expand_citation(block):
    def expand(m):
        nums = []
        for part in m.group(1).split(","):
            part = part.strip()
            if "-" in part:
                a, b = map(int, re.split(r"\s*-\s*", part, maxsplit=1))
                nums.extend(range(a, b + 1))
            else:
                nums.append(int(part))
        return ", ".join(f"[{n}]" for n in nums)

    return re.sub(r"(?<!\[)\[(\d+(?:\s*(?:,|-)\s*\d+)*)\](?!\])", expand, block)


def add_old_label(block):
    block = re.sub(r"\[\[(\d+)(?=\()", lambda m: f"[[OLD_{m.group(1)}_OLD", block)
    block = re.sub(r"#ref(\d+)\b", lambda m: f"#OLD_ref{m.group(1)}_OLD", block)
    block = re.sub(r'"ref(\d+)"', lambda m: f'"OLD_ref{m.group(1)}_OLD"', block)
    return re.sub(r"(?<!\[)\[(\d+)\](?!\])", lambda m: f"[OLD_{m.group(1)}_OLD]", block)


def get_citation_list(old_block):
    return [int(x) for x in re.findall(r"\[OLD_(\d+)_OLD\]", old_block)]


def store_citation_list(full_citation_list, block_citation_list):
    for cite_num in block_citation_list:
        if cite_num not in full_citation_list:
            full_citation_list.append(cite_num)
    return full_citation_list


def replace_citations(old_block, full_citation_list):
    def new_num(m):
        old = int(m.group(1))
        return str(full_citation_list.index(old) + 1) if old in full_citation_list else str(old)

    old_block = re.sub(r"#OLD_ref(\d+)_OLD\b", lambda m: "#ref" + new_num(m), old_block)
    old_block = re.sub(r'"OLD_ref(\d+)_OLD"', lambda m: '"ref' + new_num(m) + '"', old_block)
    return re.sub(r"OLD_(\d+)_OLD", new_num, old_block)


def sort_ref_blocks(blocks):
    ref_blocks = []
    other_blocks = []

    for block in blocks:
        if re.match(r'<a id="ref(\d+)"></a>\[\d+\]', block):
            ref_blocks.append(block)
        else:
            other_blocks.append(block)

    ref_blocks.sort(key=lambda block: int(re.match(r'<a id="ref(\d+)"></a>\[\d+\]', block).group(1)))
    return other_blocks + ref_blocks


def main(file_path):
    src = Path(file_path)
    dst = src.with_name(src.stem + "_reordered" + src.suffix)

    blocks = split_blocks(src.read_text(encoding="utf-8"))
    full_citation_list = []
    old_blocks = []

    for block in blocks:
        expanded_block = expand_citation(block)
        old_block = add_old_label(expanded_block)
        block_citation_list = get_citation_list(old_block)
        full_citation_list = store_citation_list(full_citation_list, block_citation_list)
        old_blocks.append(old_block)

    new_blocks = []
    for old_block in old_blocks:
        new_blocks.append(replace_citations(old_block, full_citation_list))

    new_blocks = sort_ref_blocks(new_blocks)
    dst.write_text("\n\n".join(new_blocks) + "\n", encoding="utf-8")
    print(dst)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python reorder_refs.py input.md")
    else:
        main(sys.argv[1])
