API documentation - https://qwality-prod.onrender.com/swagger

pip install requests, faker

Main test scenario:
1. Register non-admin user -> Post
2. Login with registered non-admin user -> Post
3. Add account balance -> Post
4. Check that account balance is correct -> Get

- data.py: keep test data
- endpoints.py: keep all endpoints

test cases:
register_user.py      - register non-admin user
login.py              - login with non-admin user
add_balance.py        - add account balance
check_balance.py      - check account balance


