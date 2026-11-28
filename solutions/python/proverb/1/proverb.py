def proverb(*args, **kwargs):
    # Return proverbs as an array
    proverbs = []
    for index in range(len(args) - 1):
        proverbs.append(f"For want of a {args[index]} the {args[index + 1]} was lost.")
    if kwargs["qualifier"] and args:
        proverbs.append(f"And all for the want of a {kwargs["qualifier"]} {args[0]}.")
    if kwargs["qualifier"] is None and args:
        proverbs.append(f"And all for the want of a {args[0]}.")
    return proverbs
    