import os
import json

def extract_all_text(data, parent_key='', result=None):
    if result is None:
        result = []

    if isinstance(data, dict):
        if parent_key:  
            result.append(f"{parent_key}")
        for key, value in data.items():
            extract_all_text(value, key, result)
            if key != list(data.keys())[-1]:
                result.append(',')
    elif isinstance(data, list):
        for index, item in enumerate(data):
            extract_all_text(item, parent_key, result) 
            if index != len(data) - 1:  
                result.append(',')
    elif isinstance(data, str):
        result.append(f"{parent_key}: {data}") 
    else:
        result.append(f"{parent_key}: {str(data)}") 
    return result

def process_json_file(json_file, output_file):
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

    documents = []

    if isinstance(json_data, list):
        for item in json_data:
            extracted_texts = extract_all_text(item)
            document_text = ' '.join(extracted_texts) 
            documents.append(document_text)
    else:
        print("Expected a list of JSON objects at the root level. Please check the JSON file format.")

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
