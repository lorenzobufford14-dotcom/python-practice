# interactive security access auditor

def audit_access(username, role, is_active):
    username = username.strip()
    role = role.strip().lower()

    if not is_active:
        return f"{username.upper()}: access denied - account is inactive."
    if role == "admin":
        return f"{username.upper()}: access granted - full administrative privileges."
    if role == "user":
        return f"{username.upper()}: access granted - standard user privileges."
    return f"{username.upper()}: access denied - unrecognized role '{role}'."


# get interactive input from terminal
print("--- security audit terminal ---")
user_input = input("enter username: ").strip()
role_input = input("enter role (admin/user/guest): ").strip()
status_input = input("is account active? (yes/no): ").strip().lower()
active_flag = status_input == "yes"

# run the function and print the results
result = audit_access(user_input, role_input, active_flag)
print("\naudit result:")
print(result)