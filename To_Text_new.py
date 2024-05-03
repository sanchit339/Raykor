import os
import json

def extract_all_text(data, parent_key='', result=None):
    """
    Recursively extract all string values from nested JSON data, formatted with parent keys followed by their properties, 
    separated by commas.
    """
    if result is None:
        result = []

    if isinstance(data, dict):
        if parent_key:  # Add the parent key at the beginning of each new dictionary
            result.append(f"{parent_key}")
        for key, value in data.items():
            # Proceed to extract from the next level while appending results to the same list
            extract_all_text(value, key, result)
            if key != list(data.keys())[-1]:  # Add a comma except for the last key in the dictionary
                result.append(',')
    elif isinstance(data, list):
        for index, item in enumerate(data):
            extract_all_text(item, parent_key, result)  # Apply the same parent key to all items in the list
            if index != len(data) - 1:  # Add a comma except for the last item in the list
                result.append(',')
    elif isinstance(data, str):
        result.append(f"{parent_key}: {data}")  # Append key-value as a string
    else:
        result.append(f"{parent_key}: {str(data)}")  # Handle non-string data types by converting them to strings

    return result

def process_json_file(json_file, output_file):
    """
    Process a single JSON file to extract all text, formatted and save it to a single output file.
    Each new document starts on a new line with all related entries on the same line.
    """
    try:
        with open(json_file, 'r') as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print(f"File not found: {json_file}")
        return
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Initialize a list to hold each document's formatted text
    documents = []

    # Check if json_data is a list and iterate accordingly
    if isinstance(json_data, list):
        # Iterate over each entry in the list, each entry is assumed to be a separate document
        for item in json_data:
            extracted_texts = extract_all_text(item)
            document_text = ' '.join(extracted_texts)  # Combine all elements into a single line
            documents.append(document_text)
    else:
        print("Expected a list of JSON objects at the root level. Please check the JSON file format.")

    # Write the extracted text to a text file, each document on a new line
    processed_data = '\n'.join(documents)
    with open(output_file, 'w', encoding='utf-8') as text_file:
        text_file.write(processed_data)

    print("Text extraction completed.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python3 to_text.py <input_json_file> <output_text_file>")
    else:
        json_file = sys.argv[1]
        output_file = sys.argv[2]
        process_json_file(json_file, output_file)
