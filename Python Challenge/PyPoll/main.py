import os
import csv

input_file = "Resources/election_data.csv"

print(f"     Election Results    ")
print(f"----------------------------")

total_votes = 0 
vote_khan = 0
vote_correy = 0
vote_li = 0
vote_otooley = 0

with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        
        if row[2] == "Khan": 
            vote_khan +=1
        elif row[2] == "Correy":
            vote_correy +=1
        elif row[2] == "Li": 
            vote_li +=1
        elif row[2] == "O'Tooley":
            vote_otooley +=1


print(f"   Total Votes: {total_votes} ")
print(f"---------------------------------")

candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [vote_khan, vote_correy, vote_li, vote_otooley]


dict_candidates = dict(zip(candidates,votes))
key = max(dict_candidates, key=dict_candidates.get)

percent_khan = (vote_khan/total_votes) *100
print(f"Khan: {percent_khan:.3f}% ({vote_khan})")

percent_correy = (vote_correy/total_votes) * 100
print(f"Correy: {percent_correy:.3f}% ({vote_correy})")

percent_li = (vote_li/total_votes)* 100
print(f"Li: {percent_li:.3f}% ({vote_li})")

percent_otooley = (vote_otooley/total_votes) * 100
print(f"O'Tooley: {percent_otooley:.3f}% ({vote_otooley})")

print(f"----------------------------")
print(f"  Winner: {key}  ")
print(f"----------------------------")

# to write in output file
output_file = "Resources/election_analysis.txt"

with open(output_file,"w") as file:

    file.write(f"Election Results")

    file.write("\n")

    file.write(f"----------------------------")

    file.write("\n")

    file.write(f"Total Votes: {total_votes}")

    file.write("\n")

    file.write(f"----------------------------")

    file.write("\n")

    file.write(f"Khan: {percent_khan:.3f}% ({vote_khan})")

    file.write("\n")

    file.write(f"Correy: {percent_correy:.3f}% ({vote_correy})")

    file.write("\n")

    file.write(f"Li: {percent_li:.3f}% ({vote_li})")

    file.write("\n")

    file.write(f"O'Tooley: {percent_otooley:.3f}% ({vote_otooley})")

    file.write("\n")

    file.write(f"----------------------------")

    file.write("\n")

    file.write(f"Winner: {key}")

    file.write("\n")
    
    file.write(f"----------------------------")