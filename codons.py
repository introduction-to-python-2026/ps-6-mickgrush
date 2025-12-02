def create_codon_dict(file_path):
    codon_dict = {}
    for i in (rows):
      parts = i.split('\t')
      codon = parts [0]
      amino = parts [2]

      codon_dict[codon] = amino
    return (codon_dict)
