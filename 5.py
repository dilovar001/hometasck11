recovers=int(input())
new_cases=int(input())
active_cases = int(input())
days = 0
while active_cases > 0:
    days += 1
    active_cases = active_cases-recovers+new_cases
print(days)