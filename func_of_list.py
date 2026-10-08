def greet_users(names):
     """A simple greeting to each user in the list."""
     for name in names:
        msg = f"Hello , {name.title()}"
        print(msg)
usernames = ['ashu', 'ashutosh', 'a']
greet_users(usernames)

