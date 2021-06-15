import pikepdf
from tqdm import tqdm
pw=[line.strip() for line in open("WordList.txt")]
for pass in tqdm(pw,"Decrypting PDF"):
    try:
        with pikepdf.open("sample.pdf",pass=pass) as pdf:
            print("\n[+] Password found:", pass)
            break
    except pikepdf._qpdf.pwerror as e:
        continue