import collections

# user = ('Siarhei', 'coder')
User = collections.namedtuple('User', 'name role')
user = User(name='Siarhei', role='coder')
print(f'{user.name} is {user.role}')

users = {'Siarhei': 'coder'}
print(f'Who?: {users["Siarhei"]}')
print(f'Who?: {users.get("Max") is None}')

challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]
print(challenges_done)
challenges = collections.defaultdict(list)

for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)

words = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum".split()
print(collections.Counter(words).most_common(5))