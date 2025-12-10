def can_vote(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not eligible"

print(can_vote(12))
print(can_vote(20))
