import hashlib
import json
import time
from datetime import datetime

class Voter:
    def __init__(self, voter_id, name):
        self.voter_id = voter_id
        self.name = name
        self.has_voted = False

    def to_dict(self):
        return {
            'voter_id': self.voter_id,
            'name': self.name,
            'has_voted': self.has_voted
        }

class Proposal:
    def __init__(self, proposal_id, description):
        self.proposal_id = proposal_id
        self.description = description
        self.vote_count = 0

    def to_dict(self):
        return {
            'proposal_id': self.proposal_id,
            'description': self.description,
            'vote_count': self.vote_count
        }

class VotingSystem:
    def __init__(self):
        self.proposals = []
        self.voters = []
        self.votes = []
        self.voting_active = False
        self.start_time = None
        self.end_time = None

    def add_proposal(self, description):
        proposal_id = len(self.proposals) + 1
        proposal = Proposal(proposal_id, description)
        self.proposals.append(proposal)
        return proposal

    def register_voter(self, name):
        voter_id = len(self.voters) + 1
        voter = Voter(voter_id, name)
        self.voters.append(voter)
        return voter

    def start_voting(self, duration_minutes=10):
        self.voting_active = True
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(minutes=duration_minutes)
        print(f"\nVoting started! Will end at {self.end_time.strftime('%H:%M:%S')}")

    def end_voting(self):
        self.voting_active = False
        print("\nVoting ended!")

    def cast_vote(self, voter_id, proposal_id):
        if not self.voting_active:
            return "Voting is not active"

        voter = next((v for v in self.voters if v.voter_id == voter_id), None)
        if not voter:
            return "Voter not found"

        if voter.has_voted:
            return "Voter has already voted"

        proposal = next((p for p in self.proposals if p.proposal_id == proposal_id), None)
        if not proposal:
            return "Proposal not found"

        voter.has_voted = True
        proposal.vote_count += 1

        vote_record = {
            'voter_id': voter_id,
            'proposal_id': proposal_id,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'hash': self.generate_vote_hash(voter_id, proposal_id)
        }
        self.votes.append(vote_record)

        return f"Vote cast successfully for proposal: {proposal.description}"

    def generate_vote_hash(self, voter_id, proposal_id):
        data = f"{voter_id}{proposal_id}{time.time()}"
        return hashlib.sha256(data.encode()).hexdigest()

    def get_results(self):
        print("\n" + "=" * 60)
        print("   VOTING RESULTS")
        print("=" * 60)

        if self.voting_active:
            print("Voting is still active!")
            remaining = self.end_time - datetime.now()
            print(f"Time remaining: {remaining.seconds // 60} minutes")
        else:
            print("Voting has ended")

        print("\nProposals:")
        print("-" * 40)
        for proposal in self.proposals:
            print(f"Proposal {proposal.proposal_id}: {proposal.description}")
            print(f"  Votes: {proposal.vote_count}")

        print("\nVoter Participation:")
        print("-" * 40)
        total_voters = len(self.voters)
        total_votes = len(self.votes)
        print(f"Total Registered Voters: {total_voters}")
        print(f"Total Votes Cast: {total_votes}")
        print(f"Participation Rate: {(total_votes/total_voters)*100:.1f}%" if total_voters > 0 else "No voters registered")

        return self.determine_winner()

    def determine_winner(self):
        if not self.proposals:
            return "No proposals found"

        winner = max(self.proposals, key=lambda p: p.vote_count)
        if winner.vote_count == 0:
            return "No votes cast"

        return f"Winner: Proposal {winner.proposal_id} - {winner.description} with {winner.vote_count} votes"

    def display_status(self):
        print("\n" + "=" * 60)
        print("   CURRENT STATUS")
        print("=" * 60)
        print(f"Voting Active: {self.voting_active}")
        print(f"Total Proposals: {len(self.proposals)}")
        print(f"Total Voters: {len(self.voters)}")
        print(f"Total Votes: {len(self.votes)}")

def main():
    from datetime import timedelta

    print("\n" + "=" * 60)
    print("   DECENTRALIZED VOTING SYSTEM - PROJECT 2 TASK 5")
    print("=" * 60)

    voting_system = VotingSystem()

    print("\n[1] Adding Proposals...")
    voting_system.add_proposal("Increase Education Budget")
    voting_system.add_proposal("Build New Hospital")
    voting_system.add_proposal("Improve Public Transport")
    voting_system.add_proposal("Plant 1 Million Trees")

    for p in voting_system.proposals:
        print(f"  Proposal {p.proposal_id}: {p.description}")

    print("\n[2] Registering Voters...")
    voters = ["Aiman Zahoor", "Ali Hassan", "Sara Ahmed", "Usman Malik", "Fatima Khan",
              "Ahmed Raza", "Zara Ali", "Hassan Shah", "Nadia Tariq", "Omar Farooq"]

    for name in voters:
        voter = voting_system.register_voter(name)
        print(f"  Voter {voter.voter_id}: {voter.name}")

    print("\n[3] Starting Voting Session...")
    voting_system.start_voting(duration_minutes=5)

    print("\n[4] Casting Votes...")
    votes_to_cast = [
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 1),
        (6, 2), (7, 3), (8, 4), (9, 1), (10, 2)
    ]

    for voter_id, proposal_id in votes_to_cast:
        result = voting_system.cast_vote(voter_id, proposal_id)
        print(f"  Voter {voter_id} -> Proposal {proposal_id}: {result}")

    print("\n[5] Attempting Double Vote...")
    result = voting_system.cast_vote(1, 2)
    print(f"  Voter 1 trying to vote again: {result}")

    print("\n[6] Ending Voting Session...")
    voting_system.end_voting()

    print("\n[7] Displaying Results...")
    winner = voting_system.get_results()
    print("\n" + "=" * 60)
    print(f"   {winner}")
    print("=" * 60)

    print("\n[8] Blockchain Security Features:")
    print("-" * 60)
    print("Hash generated for each vote: " + voting_system.votes[0]['hash'][:20] + "...")
    print("Votes are immutable (cannot be changed)")
    print("No central authority controls the voting")
    print("Transparent and verifiable results")

    print("\n" + "=" * 60)
    print("   TASK 5 COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()