# ☁️ Cloud Resource Tracker

A simple Python command line tool that simulates creating, listing, and deleting cloud resources.

## 🚀 Features

- Create cloud-like resources (EC2, S3, RDS, etc.)
- Assigns a unique ID to each resource using uuid4
- View a list of all active resources
- Delete resources by ID
- All data saved locally in `storage.json`

## 🧱 Example Usage

```bash
# Create a new EC2 instance
python main.py create web-server EC2

# List all resources
python main.py list

# Delete a resource by ID
python main.py delete <resource-id>
