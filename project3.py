# Account Signup Program

# Validate email using realistic criteria
def validate_email(email):

    exactly_one_at = email.count("@") == 1

    at_not_first_last = ("@" in email and not email.startswith("@") and
        not email.endswith("@"))

    no_spaces = " " not in email
    no_consecutive_dots = ".." not in email

    local = ""
    domain = ""

    if exactly_one_at:
        local, domain = email.split("@")

    domain_contains_dot = "." in domain

    domain_start_end = ( domain != "" and not domain.startswith(".") and
        not domain.endswith("."))

    # Check local part
    local_valid = True
    for ch in local:
        if not (ch.isalnum() or ch in "._-"):
            local_valid = False

    # Check domain part
    domain_valid = True
    for ch in domain:
        if not (ch.isalnum() or ch in ".-"):
            domain_valid = False

    banned_domains = ["test.com", "fake.com", "example.com"]
    domain_not_banned = domain.lower() not in banned_domains

    tld_valid = False
    if "." in domain:
        tld = domain.split(".")[-1]
        if 2 <= len(tld) <= 6:
            tld_valid = True

    email_valid = (exactly_one_at and at_not_first_last and no_spaces and
        no_consecutive_dots and domain_contains_dot and domain_start_end and
        local_valid and domain_valid and domain_not_banned and
        tld_valid)

    return (email_valid,exactly_one_at, at_not_first_last,no_spaces,no_consecutive_dots,
        domain_contains_dot,domain_start_end,local_valid,domain_valid,domain_not_banned,
        tld_valid)
# Generate username suggestion
def generate_username(first_name, last_name, student_id):

    username = ( first_name[0] + last_name + student_id[-2:])

    username = username.lower()

    # Keep only letters and digits
    username = "".join(ch for ch in username if ch.isalnum())

    return username


def main():

    print("===== Account Signup =====")

    while True:

        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        email = input("Enter email address: ").strip()
        confirm_email = input("Confirm email address: ").strip()
        student_id = input("Enter 5-digit student ID: ").strip()

        name_valid = first_name != "" and last_name != ""

        (email_valid,exactly_one_at,at_not_first_last,no_spaces,
         no_consecutive_dots,domain_contains_dot,domain_start_end,
        local_valid,domain_valid, domain_not_banned,tld_valid) = validate_email(email)

        confirm_valid = email.lower() == confirm_email.lower()

        student_valid = (student_id.isdigit() and
            len(student_id) == 5)

        print("\nAccount Signup Validation Report")
        print("--------------------------------")
        print("Name provided:",
              "PASS" if name_valid else "FAIL")
        print("Email contains exactly one @:",
              "PASS" if exactly_one_at else "FAIL")
        print("Email @ is not first or last:",
              "PASS" if at_not_first_last else "FAIL")
        print("Email has no spaces:",
              "PASS" if no_spaces else "FAIL")
        print("Email has no consecutive dots:",
              "PASS" if no_consecutive_dots else "FAIL")
        print("Domain contains a dot:",
              "PASS" if domain_contains_dot else "FAIL")
        print("Domain does not start or end with dot:",
              "PASS" if domain_start_end else "FAIL")
        print("Local part has valid characters:",
              "PASS" if local_valid else "FAIL")
        print("Domain part has valid characters:",
              "PASS" if domain_valid else "FAIL")
        print("Domain is not banned:",
              "PASS" if domain_not_banned else "FAIL")
        print("Top-level domain length is 2-6 characters:",
              "PASS" if tld_valid else "FAIL")
        print("Confirm email matches:",
              "PASS" if confirm_valid else "FAIL")
        print("Student ID is exactly 5 digits:",
              "PASS" if student_valid else "FAIL")

        all_valid = (
            name_valid and email_valid and confirm_valid and student_valid )
        if all_valid:
            username = generate_username(first_name, last_name, student_id)
            print("\nAccount created successfully!")
            print("Suggested Username:", username)
            break
        else:
            print("\nSignup failed. Please try again.\n")


if __name__ == "__main__":
    main()






        
