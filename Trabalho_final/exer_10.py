#Function that reads a list of reasons and counts the number of occurrences of each in the genome

def counts_reasons(genome, list_reasons):
    list_count_reasons =[]
    for reason in list_reasons:
        count = genome.count(reason.strip())
        list_count_reasons.append(count)
    return list_count_reasons

def process_genome_file(file_path_genome):
    file_genome = open(file_path_genome, "r")
    genome_lines = file_genome.readlines()
    genome = ''.join(genome_lines[1:])
    return genome


def process_reasons(reasons):
    list_reasons = reasons.split(",")
    return list_reasons

reasons = input("Enter a list of reasons: ")
file_path_genome = input("Enter the path to the genome file: ")
list_reasons = process_reasons(reasons)
genome = process_genome_file(file_path_genome)

if list_reasons and genome:
    number_reasons = counts_reasons(genome, list_reasons)
    for reason, count in zip(list_reasons, number_reasons):
        print(f"The number of {reason} is {count}")