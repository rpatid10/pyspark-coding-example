def calculate_subdomain_counts(domains):
    from collections import defaultdict

    # Dictionary to store the visit counts for each domain
    counts = defaultdict(int)

    # Parse the input and build the counts dictionary
    for count, domain in domains:
        parts = domain.split('.')
        # Add the count to the full domain and its subdomains
        for i in range(len(parts)):
            subdomain = '.'.join(parts[i:])
            counts[subdomain] += count

    # Prepare the result list
    result = [(count, domain) for domain, count in counts.items()]

    # Sort the result by domain
    result.sort(key=lambda x: (len(x[1]), x[1]))

    return result


# Input list of tuples (visit count, domain)
input_domains = [
    (900, "google.mail.com"),
    (50, "yahoo.com"),
    (1, "intel.mail.com"),
    (5, "wiki.org")
]

# Calculate the subdomain counts
result = calculate_subdomain_counts(input_domains)

# Print the results
for count, domain in result:
    print(f"{count}, {domain}")
