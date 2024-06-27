import json

with open('./melo_piante.geojson', 'r') as f:
    # Load the input JSON document
    data = json.loads(f.read())

    # Process each feature and generate the required document
    output_documents = []
    i = 0
    for feature in data['features']:
        i += 1
        output_document = {
            "id": f"urn:ngsi-ld:AgriTree:unibo:tree-{i}",
            "type": "AgriTree",
            "name": feature['properties']['Field_Row_Tree'],
            "description": feature['properties']['Description'],
            "location": feature['geometry']
        }
        output_documents.append(output_document)

# Print or use the generated documents
i = 0
for doc in output_documents:
    i += 1
    with open(f'melo-tree-{i}.json', 'w') as f:
        f.write(json.dumps(doc, indent=4))
