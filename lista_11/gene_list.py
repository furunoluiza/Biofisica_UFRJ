#Function that searches for a gene in a list
def gene_search(gene_list, search_gene):
    #Remove whitespace and convert to lowercase
    clean_gene_list = [gene.strip().lower() for gene in gene_list]
    search_gene = search_gene.strip().lower()
    return search_gene in clean_gene_list 
gene_list = ['rpoA', 'gyrB', 'topA', 'pyrH', 'recA', 'topB', 'apoA', 'dhaB', 'oleA']
search_gene = input("Enter a gene and I will search if its on the list: ")
if (gene_search(gene_list, search_gene)):
    print (f'The gene {search_gene} is on the list')
else:
    print (f'The gene {search_gene} isn\'t on the list')