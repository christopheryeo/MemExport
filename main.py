import json


def filter_and_save_quotes(input_file, output_file):
  """Filters JSON records with tag 'quote' and saves them to a new file,
  adding 'shared' to tags, removing '#shared' or '#share' from 'markdown',
  and displaying modification count.

  Args:
      input_file (str): Path to the input JSON file.
      output_file (str): Path to the output JSON file.
  """

  # Read the JSON file
  try:
    with open(input_file, "r") as f:
      data = json.load(f)
  except FileNotFoundError:
    print(f"Error: '{input_file}' file not found!")
    return

  # Filter records with only 'quote' tag
  quoted_data = [record for record in data if record.get('tags', []) == ['quote']]

  # Track modifications
  modified_count = 0

  # Check if any quotes found
  if not quoted_data:
    print("No records found with only 'quote' tag")
  else:
    # Modify records and save filtered data
    for record in quoted_data:
      # Add 'shared' to tags (if not already present)
      if "shared" not in record.get("tags", []):
        record["tags"].append("shared")
        modified_count += 1

      # Remove "#shared" or "#share" from markdown
      markdown = record.get("markdown", "")
      for term in ("#shared", "#share"):
        markdown = markdown.replace(term, "", 1)
      record["markdown"] = markdown

    # Save filtered data to output file
    try:
      with open(output_file, "w") as f:
        json.dump(quoted_data, f, indent=2)
      print(f"Filtered records saved to '{output_file}'.")
    except OSError as e:
      print(f"Error saving data: {e}")

    # Display modification count
    print(f"\nTotal records modified: {modified_count}")


# Set input and output file paths (modify as needed)
input_file = "inputs.json"
output_file = "output.json"

# Call the filter and save function
if __name__ == "__main__":
  filter_and_save_quotes(input_file, output_file)
