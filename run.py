import string
import itertools

def unique_comb(length, alphabet=string.ascii_lowercase):
    return itertools.permutations(alphabet, length)

def gen_wri(combinations, output_file):
    with open(output_file, 'w') as f:
        for combo in combinations:
            f.write(''.join(combo) + '\n')
    print(f"Unique combinations saved to {output_file}")

if __name__ == "__main__":
    length = 2 #Specify here
    alphabet = string.ascii_lowercase
    output_filename = "unique_2_letter_comb.txt" #You can change it to whatever you want it to save it as
    
    combinations = unique_comb(length, alphabet)
    gen_wri(combinations, output_filename)