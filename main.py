import argparse
from manager import create_resource, list_resources, delete_resource


parser = argparse.ArgumentParser(description="Cloud Resource Tracker")

subparsers = parser.add_subparsers(dest="command")

# Create
create_parser = subparsers.add_parser("create")
create_parser.add_argument("name")
create_parser.add_argument("type")

# List
subparsers.add_parser('list')

# Delete
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id")

args = parser.parse_args()

# Detect user inputs ("Create", "List", or "Delete")
if args.command == "create":
    res = create_resource(args.name, args.type)
    print(f"Created {res}")

elif args.command == "list":
    for r in list_resources():
        print(r)

elif args.command == "delete":
    delete_resource(args.id)
    print(f"Deleted resource {args.id}")

else:
    parser.print_help()