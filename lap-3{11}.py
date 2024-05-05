# Initialize an empty dictionary to store the votes
votes = {}

# List of candidate names
candidates = ['Candidate A', 'Candidate B', 'Candidate C']

# Simulated votes (you can replace this with actual voting data)
votes_casted = ['Candidate A', 'Candidate B', 'Candidate A', 'Candidate C', 'Candidate A', 'Candidate B', 'Candidate B']

# Count the votes for each candidate
for candidate in candidates:
    votes[candidate] = votes_casted.count(candidate)

# Print the vote counts for each candidate
for candidate, count in votes.items():
    print(f"{candidate}: {count} votes")

